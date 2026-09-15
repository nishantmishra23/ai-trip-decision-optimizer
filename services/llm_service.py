"""
LLM Service for AI Trip Decision Optimizer.
Powered by Google Gemini (gemini-3.6-flash via REST API) with automatic fallback.
"""
import os
import json
import re
import logging
from typing import Dict, Any, List, Optional
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY", "")


class RestGeminiModel:
    """Lightweight REST-based Gemini client that requires no external heavy dependencies."""
    def __init__(self, api_key: str, model_name: str = "gemini-3.6-flash"):
        self.api_key = api_key
        self.model_name = model_name

    def generate_content(self, prompt: str, **kwargs):
        models = [self.model_name, "gemini-flash-latest", "gemini-2.5-flash", "gemini-pro-latest"]
        last_err = None
        for m in models:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{m}:generateContent?key={self.api_key}"
            payload = {
                "contents": [{"parts": [{"text": prompt}]}],
                "generationConfig": {"temperature": 0.4, "maxOutputTokens": 2048}
            }
            try:
                resp = requests.post(url, json=payload, timeout=20)
                if resp.status_code == 200:
                    data = resp.json()
                    candidates = data.get("candidates", [])
                    if candidates:
                        parts = candidates[0].get("content", {}).get("parts", [])
                        text = "".join(p.get("text", "") for p in parts if "text" in p)
                        class ResponseObj:
                            def __init__(self, t):
                                self.text = t
                        return ResponseObj(text)
                elif resp.status_code != 404:
                    last_err = Exception(f"HTTP {resp.status_code}: {resp.text}")
            except Exception as e:
                last_err = e
                continue
        raise last_err or Exception("Failed to generate content from Gemini API")


def _init_gemini_model():
    """Attempt to configure and return a working Gemini GenerativeModel instance."""
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY", "")
    if not api_key:
        return None
    return RestGeminiModel(api_key=api_key, model_name="gemini-3.6-flash")


def generate_itinerary(
    destination: str,
    duration: int,
    travel_style: str,
    travelers: int,
    budget: float,
    activities: List[str]
) -> Dict[str, Any]:
    """
    Generate a day-by-day itinerary using Google Gemini.
    Returns a dictionary structured by day, or a fallback if the API fails.
    """
    model = _init_gemini_model()
    
    if model:
        prompt = f"""
        You are an expert travel planner. Create a {duration}-day itinerary for a trip to {destination}.
        The trip is for {travelers} traveler(s) with a travel style of '{travel_style}'.
        Their total budget is roughly INR {budget}.
        Their main interests are: {', '.join(activities) if activities else 'General sightseeing, local food, and student-friendly hotspots'}.
        
        Please provide the output STRICTLY as a JSON array where each element represents one day.
        Each day object MUST have the following structure:
        [
            {{
                "day": "Day 1",
                "title": "Short title for the day's theme",
                "slots": [
                    {{
                        "time": "Morning (09:00 - 12:30)",
                        "title": "Activity name",
                        "cost": 500,
                        "tip": "Short travel tip for this activity"
                    }},
                    {{
                        "time": "Afternoon (13:30 - 17:00)",
                        "title": "Activity name",
                        "cost": 800,
                        "tip": "Short travel tip"
                    }},
                    {{
                        "time": "Evening (18:00 - 21:00)",
                        "title": "Activity name",
                        "cost": 1200,
                        "tip": "Short travel tip"
                    }}
                ]
            }}
        ]
        
        Ensure costs are numbers in INR (per person).
        Generate exactly {duration} days.
        Return ONLY the raw JSON array string without any surrounding commentary or markdown codeblocks.
        """
        
        try:
            response = model.generate_content(prompt)
            raw_text = response.text.strip()
            
            # Clean up possible markdown wrappers like ```json ... ```
            clean_text = re.sub(r"^```(?:json)?\s*", "", raw_text, flags=re.MULTILINE)
            clean_text = re.sub(r"\s*```$", "", clean_text, flags=re.MULTILINE).strip()
            
            # Extract array if there is extra text
            match = re.search(r"\[\s*\{.*\}\s*\]", clean_text, re.DOTALL)
            if match:
                clean_text = match.group(0)
                
            itinerary_data = json.loads(clean_text)
            
            if isinstance(itinerary_data, list) and len(itinerary_data) > 0:
                return {"status": "success", "source": "gemini", "itinerary": itinerary_data}
                
        except Exception as e:
            logger.error(f"Gemini generation error: {e}")

    # Fallback to static logic
    return _generate_fallback_itinerary(destination, duration, travel_style)


def generate_packing_and_weather_tips(destination: str, weather: dict) -> List[str]:
    """Generate smart weather-aware packing suggestions using Gemini or intelligent heuristics."""
    model = _init_gemini_model()
    temp = weather.get("temp", 25)
    condition = weather.get("condition", "Clear")
    
    if model:
        prompt = f"""
        Give exactly 4 concise, high-value packing and travel tips for a student traveling to {destination}.
        Current weather: {temp}°C, condition: {condition}, humidity: {weather.get('humidity', 60)}%.
        Format strictly as 4 bullet points starting with an emoji. Keep each tip under 15 words.
        """
        try:
            resp = model.generate_content(prompt)
            lines = [line.strip("- *•").strip() for line in resp.text.strip().split("\n") if line.strip()]
            if len(lines) >= 3:
                return lines[:4]
        except Exception:
            pass

    # Heuristic tips
    tips = []
    if temp < 15:
        tips.append("🧥 Thermal innerwear and fleece jackets are essential for cool mountain winds.")
    elif temp > 30:
        tips.append("🧢 Breathable cottons, UV-protection sunglasses, and high-SPF sunscreen.")
    else:
        tips.append("👕 Layered casual clothing, light jacket for evening breezes.")
    
    if "rain" in condition.lower() or weather.get("rain_chance", 0) > 40:
        tips.append("☔ Compact umbrella and waterproof phone pouches for sudden downpours.")
    else:
        tips.append("👟 Comfortable walking or trekking shoes for exploring local streets and monuments.")
        
    tips.append("💳 Student ID card to claim major heritage monument and museum discounts.")
    tips.append("💧 Reusable water bottle and power bank for all-day sightseeing.")
    return tips


def ask_gemini_travel_advisor(destination: str, query: str) -> str:
    """Ask Gemini for quick student travel advice, hidden gems, or local food recommendations."""
    model = _init_gemini_model()
    if not model:
        return f"Explore {destination}'s bustling local markets, try street delicacies from renowned vendors, and take public transit or shared autos to keep costs student-friendly!"
        
    prompt = f"""
    You are a savvy student travel guide for India.
    Destination: {destination}
    User Query: {query}
    Provide an energetic, practical, and budget-friendly answer in 2-3 concise paragraphs with bullet points.
    Include estimated costs in INR where applicable.
    """
    try:
        resp = model.generate_content(prompt)
        return resp.text.strip()
    except Exception as e:
        logger.error(f"Gemini advisor error: {e}")
        return f"Explore {destination}'s vibrant street markets, connect with local students or hostel travelers, and discover off-beat spots for the best memories on a budget!"


def _generate_fallback_itinerary(destination: str, duration: int, travel_style: str) -> Dict[str, Any]:
    """Static fallback if Gemini is unavailable or fails."""
    days = []
    
    themes = [
        "Arrival & City Orientation",
        "Cultural Heritage & Landmarks",
        "Nature, Scenic Views & Adventure",
        "Local Markets & Street Food Exploration",
        "Hidden Gems & Student Hotspots",
        "Relaxation & Scenic Strolls",
        "Day Excursion & Outdoor Treks",
        "Arts, Museums & Local Crafts",
        "Sunset Viewpoint & Atmosphere Dining",
        "Farewell Tour & Souvenir Shopping"
    ]
    
    for i in range(1, duration + 1):
        theme = themes[(i - 1) % len(themes)]
        day_data = {
            "day": f"Day {i}",
            "title": f"{theme} in {destination}",
            "slots": [
                {
                    "time": "Morning (09:00 - 12:30)",
                    "title": f"Morning Exploration: Iconic Spots of {destination}",
                    "cost": 400 + (i * 50),
                    "tip": "Arrive early to beat the crowds and catch golden hour lighting."
                },
                {
                    "time": "Afternoon (13:30 - 17:00)",
                    "title": f"Local Food Trail & Culture in {destination}",
                    "cost": 600 + (i * 80),
                    "tip": "Ask locals for their favourite street food spots or student thali joints."
                },
                {
                    "time": "Evening (18:00 - 21:00)",
                    "title": f"Sunset Promenade & Night Vibes",
                    "cost": 800 + (i * 100),
                    "tip": "Great atmosphere for unwinding and mingling with fellow travelers."
                }
            ]
        }
        days.append(day_data)
        
    return {"status": "success", "source": "fallback", "itinerary": days}

import os
import json
import re
import logging
from typing import Dict, Any, List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)

# Safe import of google.generativeai
GENAI_AVAILABLE = False
try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
except ImportError:
    genai = None
    logger.warning("google.generativeai package is not installed. Using fallback itinerary generation.")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if GEMINI_API_KEY:
    os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY
    os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

def _init_gemini_model():
    """Attempt to configure and return a working Gemini GenerativeModel instance."""
    if not GENAI_AVAILABLE or not GEMINI_API_KEY:
        return None
        
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        models_to_try = [
            'gemini-1.5-flash',
            'gemini-2.0-flash',
            'gemini-pro',
            'models/gemini-1.5-flash',
            'models/gemini-pro',
            'gemini-1.5-pro'
        ]
        for m_name in models_to_try:
            try:
                model = genai.GenerativeModel(m_name)
                return model
            except Exception:
                continue
    except Exception as e:
        logger.error(f"Failed to initialize Gemini API: {e}")
        
    return None


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
        Their total budget is roughly ₹{budget}.
        Their main interests are: {', '.join(activities) if activities else 'General sightseeing'}.
        
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
        Return ONLY the raw JSON array string without markdown formatting or codeblocks.
        """
        
        try:
            try:
                response = model.generate_content(
                    prompt,
                    generation_config=genai.GenerationConfig(
                        response_mime_type="application/json",
                        temperature=0.4
                    )
                )
            except Exception:
                # Retry without generation_config if mime_type is unsupported
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


def _generate_fallback_itinerary(destination: str, duration: int, travel_style: str) -> Dict[str, Any]:
    """Static fallback if Gemini is unavailable or fails."""
    days = []
    
    themes = [
        "Arrival & City Orientation",
        "Cultural Heritage & Landmarks",
        "Nature, Scenic Views & Adventure",
        "Local Markets & Shopping Exploration",
        "Hidden Gems & Culinary Delights",
        "Relaxation & Scenic Strolls",
        "Day Excursion & Outdoor Activities",
        "Arts, Museums & Local Crafts",
        "Sunset Experience & Special Dining",
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
                    "title": f"Morning Tour: Highlights of {destination}",
                    "cost": 600 + (i * 50),
                    "tip": "Arrive early to capture great photos and beat the peak traffic."
                },
                {
                    "time": "Afternoon (13:30 - 17:00)",
                    "title": f"Culinary & Cultural Walk in {destination}",
                    "cost": 900 + (i * 100),
                    "tip": "Sample popular local snacks and drinks from recommended vendors."
                },
                {
                    "time": "Evening (18:00 - 21:00)",
                    "title": f"Sunset Viewpoint & Atmosphere Dinner",
                    "cost": 1200 + (i * 150),
                    "tip": "Reserve a window table for sunset views."
                }
            ]
        }
        days.append(day_data)
        
    return {"status": "success", "source": "fallback", "itinerary": days}

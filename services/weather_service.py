"""
Weather service for AI Trip Decision Optimizer.
Uses OpenWeatherMap API if key is available, otherwise returns curated static data.
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Comprehensive static weather data covering destinations & state capitals (fallback)
STATIC_WEATHER = {
    "Goa": {"temp": 30, "feels_like": 34, "humidity": 75, "description": "Clear sky", "wind_speed": 15, "condition": "Sunny", "rain_chance": 10, "best_months": "Oct–Mar"},
    "Panaji": {"temp": 30, "feels_like": 34, "humidity": 75, "description": "Clear sky", "wind_speed": 15, "condition": "Sunny", "rain_chance": 10, "best_months": "Oct–Mar"},
    "Manali": {"temp": 12, "feels_like": 10, "humidity": 55, "description": "Partly cloudy", "wind_speed": 18, "condition": "Clouds", "rain_chance": 20, "best_months": "Oct–Jun"},
    "Shimla": {"temp": 16, "feels_like": 15, "humidity": 50, "description": "Crisp mountain breeze", "wind_speed": 14, "condition": "Clear", "rain_chance": 15, "best_months": "Year-round"},
    "Jaipur": {"temp": 28, "feels_like": 30, "humidity": 45, "description": "Sunny & warm", "wind_speed": 12, "condition": "Clear", "rain_chance": 5, "best_months": "Oct–Mar"},
    "Udaipur": {"temp": 27, "feels_like": 29, "humidity": 48, "description": "Clear skies over lake", "wind_speed": 10, "condition": "Clear", "rain_chance": 5, "best_months": "Oct–Mar"},
    "Munnar": {"temp": 19, "feels_like": 18, "humidity": 82, "description": "Misty tea hills", "wind_speed": 8, "condition": "Mist", "rain_chance": 35, "best_months": "Oct–May"},
    "Kochi": {"temp": 29, "feels_like": 33, "humidity": 78, "description": "Tropical coastal breeze", "wind_speed": 14, "condition": "Clouds", "rain_chance": 25, "best_months": "Sep–Mar"},
    "Agra": {"temp": 26, "feels_like": 28, "humidity": 52, "description": "Clear morning", "wind_speed": 10, "condition": "Clear", "rain_chance": 5, "best_months": "Oct–Mar"},
    "Varanasi": {"temp": 27, "feels_like": 29, "humidity": 65, "description": "Pleasant river breeze", "wind_speed": 8, "condition": "Clear", "rain_chance": 10, "best_months": "Oct–Mar"},
    "Rishikesh": {"temp": 23, "feels_like": 22, "humidity": 55, "description": "Pleasant river breeze", "wind_speed": 10, "condition": "Clear", "rain_chance": 15, "best_months": "Sep–Jun"},
    "Dehradun": {"temp": 22, "feels_like": 21, "humidity": 58, "description": "Valley breeze", "wind_speed": 11, "condition": "Clouds", "rain_chance": 20, "best_months": "Year-round"},
    "Bengaluru": {"temp": 24, "feels_like": 24, "humidity": 60, "description": "Pleasant garden climate", "wind_speed": 13, "condition": "Clear", "rain_chance": 20, "best_months": "Year-round"},
    "Mumbai": {"temp": 31, "feels_like": 36, "humidity": 78, "description": "Warm sea breeze", "wind_speed": 16, "condition": "Haze", "rain_chance": 15, "best_months": "Oct–Mar"},
    "Kolkata": {"temp": 29, "feels_like": 33, "humidity": 72, "description": "Warm & humid", "wind_speed": 10, "condition": "Clouds", "rain_chance": 20, "best_months": "Oct–Mar"},
    "Chennai": {"temp": 31, "feels_like": 36, "humidity": 74, "description": "Sunny coastal", "wind_speed": 15, "condition": "Clear", "rain_chance": 15, "best_months": "Nov–Feb"},
    "Hyderabad": {"temp": 28, "feels_like": 29, "humidity": 55, "description": "Clear & breezy", "wind_speed": 12, "condition": "Clear", "rain_chance": 10, "best_months": "Oct–Mar"},
    "Bhopal": {"temp": 27, "feels_like": 28, "humidity": 50, "description": "Clear skies", "wind_speed": 10, "condition": "Clear", "rain_chance": 10, "best_months": "Oct–Mar"},
    "Patna": {"temp": 28, "feels_like": 30, "humidity": 62, "description": "Hazy sunshine", "wind_speed": 9, "condition": "Clear", "rain_chance": 10, "best_months": "Oct–Mar"},
    "Ranchi": {"temp": 25, "feels_like": 25, "humidity": 58, "description": "Pleasant plateau climate", "wind_speed": 11, "condition": "Clear", "rain_chance": 15, "best_months": "Oct–Mar"},
    "Guwahati": {"temp": 27, "feels_like": 29, "humidity": 70, "description": "River breeze", "wind_speed": 8, "condition": "Clouds", "rain_chance": 25, "best_months": "Nov–Apr"},
    "Shillong": {"temp": 17, "feels_like": 16, "humidity": 75, "description": "Cool cloud mist", "wind_speed": 10, "condition": "Clouds", "rain_chance": 35, "best_months": "Oct–Apr"},
    "Gangtok": {"temp": 15, "feels_like": 14, "humidity": 72, "description": "Mountain cool", "wind_speed": 12, "condition": "Clouds", "rain_chance": 30, "best_months": "Mar–Jun, Oct–Dec"},
    "Amritsar": {"temp": 26, "feels_like": 27, "humidity": 45, "description": "Sunny & dry", "wind_speed": 11, "condition": "Clear", "rain_chance": 5, "best_months": "Oct–Mar"},
    "Andaman Islands": {"temp": 29, "feels_like": 33, "humidity": 80, "description": "Sunny island breeze", "wind_speed": 16, "condition": "Sunny", "rain_chance": 15, "best_months": "Oct–May"},
    "Leh-Ladakh": {"temp": 14, "feels_like": 10, "humidity": 28, "description": "Clear and dry", "wind_speed": 22, "condition": "Clear", "rain_chance": 2, "best_months": "Jun–Sep"},
    "Bali": {"temp": 28, "feels_like": 32, "humidity": 78, "description": "Tropical", "wind_speed": 14, "condition": "Tropical Sunny", "rain_chance": 20, "best_months": "Apr–Oct"},
    "Paris": {"temp": 18, "feels_like": 16, "humidity": 65, "description": "Overcast", "wind_speed": 18, "condition": "Overcast", "rain_chance": 35, "best_months": "Apr–Jun, Sep–Oct"},
}


def _get_static(city: str, source_label: str = "sample") -> dict:
    """Return static fallback weather for a city, or generic data if city not found."""
    for key in STATIC_WEATHER:
        if key.lower() in city.lower() or city.lower() in key.lower():
            data = STATIC_WEATHER[key].copy()
            data["source"] = source_label
            return data
    # Generic fallback — unknown city
    return {
        "temp": 25, "feels_like": 27, "humidity": 60,
        "description": "Partly cloudy", "wind_speed": 12,
        "condition": "Partly Cloudy", "rain_chance": 20,
        "best_months": "Varies by season", "source": source_label,
    }


def get_weather(city: str) -> dict:
    """
    Fetch current weather for a city.
    Uses OpenWeatherMap if WEATHER_API_KEY is configured.
    Falls back reliably to curated static data.
    """
    api_key = os.getenv("WEATHER_API_KEY", "").strip()

    if api_key:
        try:
            # Query city directly or with India country code if appropriate
            query_city = city.split("(")[0].strip()
            resp = requests.get(
                BASE_URL,
                params={"q": query_city, "appid": api_key, "units": "metric"},
                timeout=5,
            )

            if resp.status_code == 200:
                data = resp.json()
                main_condition = data["weather"][0]["main"]
                desc = data["weather"][0]["description"].title()
                temp = round(data["main"]["temp"])
                feels_like = round(data["main"]["feels_like"])
                humidity = data["main"]["humidity"]
                wind_speed = round(data["wind"]["speed"] * 3.6) # m/s -> km/h
                clouds = data.get("clouds", {}).get("all", 0)
                
                return {
                    "temp": temp,
                    "feels_like": feels_like,
                    "humidity": humidity,
                    "description": desc,
                    "wind_speed": wind_speed,
                    "condition": main_condition,
                    "rain_chance": clouds,
                    "best_months": STATIC_WEATHER.get(city, {}).get("best_months", "Oct–Mar"),
                    "source": "live",
                }

            if resp.status_code in (401, 404):
                return _get_static(city, source_label="sample (api fallback)")

            return _get_static(city, source_label="sample")

        except Exception:
            return _get_static(city, source_label="sample (offline)")

    return _get_static(city, source_label="sample")

"""
Weather service for AI Trip Decision Optimizer.
Uses OpenWeatherMap API if key is available, otherwise returns curated static data.
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Static weather data per destination (fallback)
STATIC_WEATHER = {
    "Goa": {"temp": 30, "feels_like": 34, "humidity": 75, "description": "Clear sky",
             "wind_speed": 15, "condition": "Sunny", "rain_chance": 10, "best_months": "Oct–Mar"},
    "Manali": {"temp": 10, "feels_like": 7, "humidity": 60, "description": "Partly cloudy",
                "wind_speed": 20, "condition": "Partly Cloudy", "rain_chance": 25, "best_months": "Oct–Jun"},
    "Jaipur": {"temp": 26, "feels_like": 28, "humidity": 40, "description": "Clear sky",
                "wind_speed": 12, "condition": "Clear", "rain_chance": 5, "best_months": "Oct–Mar"},
    "Munnar": {"temp": 20, "feels_like": 18, "humidity": 80, "description": "Mist",
                "wind_speed": 8, "condition": "Misty", "rain_chance": 40, "best_months": "Oct–May"},
    "Agra": {"temp": 25, "feels_like": 27, "humidity": 50, "description": "Hazy",
              "wind_speed": 10, "condition": "Hazy", "rain_chance": 8, "best_months": "Oct–Mar"},
    "Bali": {"temp": 28, "feels_like": 32, "humidity": 78, "description": "Tropical",
              "wind_speed": 14, "condition": "Tropical Sunny", "rain_chance": 20, "best_months": "Apr–Oct"},
    "Paris": {"temp": 18, "feels_like": 16, "humidity": 65, "description": "Overcast",
               "wind_speed": 18, "condition": "Overcast", "rain_chance": 35, "best_months": "Apr–Jun, Sep–Oct"},
    "Rishikesh": {"temp": 22, "feels_like": 21, "humidity": 55, "description": "Partly cloudy",
                   "wind_speed": 10, "condition": "Partly Cloudy", "rain_chance": 20, "best_months": "Sep–Jun"},
    "Andaman Islands": {"temp": 29, "feels_like": 33, "humidity": 80, "description": "Sunny",
                         "wind_speed": 16, "condition": "Sunny", "rain_chance": 15, "best_months": "Oct–May"},
    "Leh-Ladakh": {"temp": 15, "feels_like": 11, "humidity": 30, "description": "Clear and dry",
                    "wind_speed": 22, "condition": "Clear & Dry", "rain_chance": 3, "best_months": "Jun–Sep"},
    "Rajasthan (Jaipur)": {"temp": 26, "feels_like": 28, "humidity": 40, "description": "Clear sky",
                "wind_speed": 12, "condition": "Clear", "rain_chance": 5, "best_months": "Oct–Mar"},
    "Kerala (Munnar)": {"temp": 20, "feels_like": 18, "humidity": 80, "description": "Mist",
                "wind_speed": 8, "condition": "Misty", "rain_chance": 40, "best_months": "Oct–May"},
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

    Priority:
      1. Live data from OpenWeatherMap (if WEATHER_API_KEY is set and reachable).
      2. Curated static data for known destinations.
      3. Generic fallback data.

    Never raises — always returns a dict. Never exposes the API key.
    """
    # Read key fresh each call so that late .env loading is handled correctly
    api_key = os.getenv("WEATHER_API_KEY", "").strip()

    if api_key:
        try:
            resp = requests.get(
                BASE_URL,
                params={"q": city, "appid": api_key, "units": "metric"},
                timeout=5,
            )

            if resp.status_code == 200:
                data = resp.json()
                return {
                    "temp": round(data["main"]["temp"]),
                    "feels_like": round(data["main"]["feels_like"]),
                    "humidity": data["main"]["humidity"],
                    "description": data["weather"][0]["description"].title(),
                    "wind_speed": round(data["wind"]["speed"] * 3.6),  # m/s → km/h
                    "condition": data["weather"][0]["main"],
                    "rain_chance": data.get("clouds", {}).get("all", 0),
                    "best_months": STATIC_WEATHER.get(city, {}).get("best_months", "Varies"),
                    "source": "live",
                }

            if resp.status_code == 401:
                # Key exists but not yet activated (takes up to 2 hours after signup)
                return _get_static(city, source_label="sample (key activating)")

            if resp.status_code == 404:
                # City name not recognised by OWM — use our static data
                return _get_static(city, source_label="sample (city not found)")

            # Any other HTTP error (429 rate limit, 5xx server error, etc.)
            return _get_static(city, source_label="sample (api error)")

        except requests.exceptions.Timeout:
            return _get_static(city, source_label="sample (timeout)")
        except requests.exceptions.ConnectionError:
            return _get_static(city, source_label="sample (offline)")
        except Exception:
            return _get_static(city, source_label="sample (error)")

    # No key configured — use static data silently
    return _get_static(city, source_label="sample")

"""
Common helper functions for the India Tourism Dataset.
"""
import urllib.parse

def gmaps_url(query: str) -> str:
    """Generate a clean, direct Google Maps search link."""
    return f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote_plus(query)}"

def make_destination(
    name, tagline, overview, budget_daily, best_time, duration, rating, popularity,
    travel_style, suitability, weather_city, neighborhoods, places, activities, hotels, restaurants
):
    """Factory function for structured destination records."""
    for h in hotels:
        if "gmaps_url" not in h:
            h["gmaps_url"] = gmaps_url(f"{h['name']}, {name}")
    for r in restaurants:
        if "gmaps_url" not in r:
            r["gmaps_url"] = gmaps_url(f"{r['name']}, {name}")
    for p in places:
        if "gmaps_url" not in p:
            p["gmaps_url"] = gmaps_url(f"{p['name']}, {name}")
    return {
        "name": name,
        "tagline": tagline,
        "overview": overview,
        "budget_daily": budget_daily,
        "best_time": best_time,
        "recommended_duration": duration,
        "rating": rating,
        "popularity": popularity,
        "travel_style": travel_style,
        "suitability": suitability,
        "weather_city": weather_city,
        "neighborhoods": neighborhoods,
        "places_to_visit": places,
        "things_to_do": activities,
        "hotels": hotels,
        "restaurants": restaurants
    }

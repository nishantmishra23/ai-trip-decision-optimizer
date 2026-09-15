"""
Generates the comprehensive data/india_tourism_data.py containing all 28 states of India
with 4-8 destinations per state, complete with neighborhoods, places, activities, hotels, and dining.
"""
import os
import sys
import json
import urllib.parse

def gmaps(q):
    return f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote_plus(q)}"

def d(name, tagline, overview, budget_daily, best_time, duration, rating, popularity, travel_style, suitability, weather_city, neighborhoods, places, activities, hotels, restaurants):
    for h in hotels:
        if "gmaps_url" not in h:
            h["gmaps_url"] = gmaps(f"{h['name']}, {name}")
    for r in restaurants:
        if "gmaps_url" not in r:
            r["gmaps_url"] = gmaps(f"{r['name']}, {name}")
    for p in places:
        if "gmaps_url" not in p:
            p["gmaps_url"] = gmaps(f"{p['name']}, {name}")
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

print("Generator functions prepared.")

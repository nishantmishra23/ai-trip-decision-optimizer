"""
Activity Recommendations page for AI Trip Decision Optimizer.
"""
import os
import sys

# Ensure project root is in sys.path
_current_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
ROOT_DIR = os.path.dirname(_current_dir) if "app_pages" in _current_dir else _current_dir
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import plotly_theme
from utils.components import render_activity_card


# ── Hero ───────────────────────────────────────────────────────────────────────
st.title("Activities & tours", icon=":material/hiking:")
st.caption("Discover thrilling adventure sports, cultural tours, water sports, and wellness retreats")

SAMPLE_ACTIVITIES = {
    "Goa": [
        {"name": "Scuba Diving at Grande Island", "category": "Water Sports", "price": 3500, "duration_hrs": 4, "rating": 4.8, "destination_name": "Goa"},
        {"name": "Dudhsagar Waterfalls Trek", "category": "Trekking", "price": 2000, "duration_hrs": 6, "rating": 4.7, "destination_name": "Goa"},
        {"name": "Sunset Cruise on Mandovi River", "category": "Sightseeing", "price": 800, "duration_hrs": 2, "rating": 4.5, "destination_name": "Goa"},
        {"name": "Old Goa Heritage Church Tour", "category": "Heritage", "price": 500, "duration_hrs": 3, "rating": 4.4, "destination_name": "Goa"},
    ],
    "Manali": [
        {"name": "Solang Valley Paragliding", "category": "Adventure", "price": 3000, "duration_hrs": 2, "rating": 4.7, "destination_name": "Manali"},
        {"name": "Beas River White Water Rafting", "category": "Adventure", "price": 1800, "duration_hrs": 3, "rating": 4.6, "destination_name": "Manali"},
        {"name": "Rohtang Pass Snow Scooter", "category": "Adventure", "price": 2500, "duration_hrs": 4, "rating": 4.8, "destination_name": "Manali"},
        {"name": "Hadimba Temple & Cedar Forest Walk", "category": "Heritage", "price": 300, "duration_hrs": 2, "rating": 4.5, "destination_name": "Manali"},
    ],
    "Jaipur": [
        {"name": "Amber Fort Elephant / Jeep Safari", "category": "Heritage", "price": 1200, "duration_hrs": 3, "rating": 4.7, "destination_name": "Jaipur"},
        {"name": "Hot Air Balloon Ride", "category": "Adventure", "price": 12000, "duration_hrs": 3, "rating": 4.9, "destination_name": "Jaipur"},
        {"name": "City Palace & Jantar Mantar Tour", "category": "Heritage", "price": 700, "duration_hrs": 3, "rating": 4.6, "destination_name": "Jaipur"},
        {"name": "Hawa Mahal Photography & Street Walk", "category": "Sightseeing", "price": 200, "duration_hrs": 2, "rating": 4.5, "destination_name": "Jaipur"},
    ],
    "Munnar": [
        {"name": "Tea Plantation & Processing Walk", "category": "Nature", "price": 400, "duration_hrs": 3, "rating": 4.7, "destination_name": "Munnar"},
        {"name": "Eravikulam National Park Nilgiri Tahr Safari", "category": "Wildlife", "price": 650, "duration_hrs": 4, "rating": 4.6, "destination_name": "Munnar"},
        {"name": "Traditional Ayurvedic Spa & Wellness", "category": "Yoga & Wellness", "price": 2500, "duration_hrs": 2, "rating": 4.8, "destination_name": "Munnar"},
        {"name": "Top Station Panoramic Trek", "category": "Trekking", "price": 800, "duration_hrs": 5, "rating": 4.6, "destination_name": "Munnar"},
    ],
    "Agra": [
        {"name": "Taj Mahal Sunrise Guided Tour", "category": "Heritage", "price": 1100, "duration_hrs": 3, "rating": 4.9, "destination_name": "Agra"},
        {"name": "Agra Fort Mughal Citadel Walk", "category": "Heritage", "price": 600, "duration_hrs": 2, "rating": 4.6, "destination_name": "Agra"},
        {"name": "Fatehpur Sikri Royal Complex Excursion", "category": "Heritage", "price": 850, "duration_hrs": 4, "rating": 4.5, "destination_name": "Agra"},
        {"name": "Mehtab Bagh River Sunset View", "category": "Sightseeing", "price": 350, "duration_hrs": 2, "rating": 4.7, "destination_name": "Agra"},
    ],
    "Bali": [
        {"name": "Tanah Lot Sea Temple Sunset", "category": "Heritage", "price": 800, "duration_hrs": 3, "rating": 4.8, "destination_name": "Bali"},
        {"name": "Tegallalang Rice Terrace Trek", "category": "Nature", "price": 500, "duration_hrs": 2, "rating": 4.7, "destination_name": "Bali"},
        {"name": "Kuta Beach Surfing Lessons", "category": "Water Sports", "price": 1800, "duration_hrs": 3, "rating": 4.6, "destination_name": "Bali"},
        {"name": "Balinese Traditional Massage & Wellness", "category": "Yoga & Wellness", "price": 2600, "duration_hrs": 2, "rating": 4.8, "destination_name": "Bali"},
    ],
    "Paris": [
        {"name": "Eiffel Tower Summit Access & Tour", "category": "Sightseeing", "price": 3200, "duration_hrs": 3, "rating": 4.8, "destination_name": "Paris"},
        {"name": "Louvre Museum Masterpieces Guided Visit", "category": "Heritage", "price": 2400, "duration_hrs": 3, "rating": 4.9, "destination_name": "Paris"},
        {"name": "Seine River Evening Dinner Cruise", "category": "Sightseeing", "price": 4500, "duration_hrs": 3, "rating": 4.7, "destination_name": "Paris"},
        {"name": "Versailles Palace & Royal Gardens", "category": "Heritage", "price": 3800, "duration_hrs": 5, "rating": 4.8, "destination_name": "Paris"},
    ],
    "Rishikesh": [
        {"name": "Ganges River Rafting (16km)", "category": "Adventure", "price": 1500, "duration_hrs": 4, "rating": 4.8, "destination_name": "Rishikesh"},
        {"name": "Bungee Jumping at Jumpin Heights", "category": "Adventure", "price": 3800, "duration_hrs": 2, "rating": 4.9, "destination_name": "Rishikesh"},
        {"name": "Sunrise Yoga & Ashram Meditation", "category": "Yoga & Wellness", "price": 500, "duration_hrs": 2, "rating": 4.7, "destination_name": "Rishikesh"},
        {"name": "Beatles Ashram Cultural Walk", "category": "Heritage", "price": 300, "duration_hrs": 2, "rating": 4.5, "destination_name": "Rishikesh"},
    ],
    "Andaman Islands": [
        {"name": "Scuba Diving at Elephant Beach", "category": "Water Sports", "price": 4200, "duration_hrs": 4, "rating": 4.8, "destination_name": "Andaman Islands"},
        {"name": "Radhanagar Beach White Sands Sunset", "category": "Sightseeing", "price": 500, "duration_hrs": 2, "rating": 4.9, "destination_name": "Andaman Islands"},
        {"name": "Cellular Jail National Memorial & Light Show", "category": "Heritage", "price": 400, "duration_hrs": 3, "rating": 4.6, "destination_name": "Andaman Islands"},
        {"name": "Mangrove Forest Kayaking Expedition", "category": "Nature", "price": 1800, "duration_hrs": 3, "rating": 4.7, "destination_name": "Andaman Islands"},
    ],
    "Leh-Ladakh": [
        {"name": "Pangong Tso High-Altitude Lake Excursion", "category": "Nature", "price": 3500, "duration_hrs": 8, "rating": 4.9, "destination_name": "Leh-Ladakh"},
        {"name": "Khardung La Pass Motorbike Experience", "category": "Adventure", "price": 2200, "duration_hrs": 4, "rating": 4.8, "destination_name": "Leh-Ladakh"},
        {"name": "Nubra Valley Sand Dunes & Camel Safari", "category": "Adventure", "price": 2800, "duration_hrs": 6, "rating": 4.7, "destination_name": "Leh-Ladakh"},
        {"name": "Thiksey & Hemis Monasteries Tour", "category": "Heritage", "price": 700, "duration_hrs": 4, "rating": 4.6, "destination_name": "Leh-Ladakh"},
    ],
}

def load_activities():
    try:
        from database.queries import get_all_activities
        act = get_all_activities()
        if act:
            return act
    except Exception:
        pass
    all_act = []
    for dest, a_list in SAMPLE_ACTIVITIES.items():
        all_act.extend(a_list)
    return all_act

activities = load_activities()

with st.container(border=True):
    st.subheader(":material/filter_list: Filter Activities", anchor=False)
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        dests = ["All Destinations"] + sorted(list(set(a.get("destination_name", "General") for a in activities)))
        selected_dest = st.selectbox("Destination", dests)
    with c2:
        cats = ["All Categories"] + sorted(list(set(a.get("category", "General") for a in activities)))
        selected_cat = st.selectbox("Activity Category", cats)
    with c3:
        max_price = st.slider("Max Activity Price (₹)", min_value=500, max_value=15000, value=10000, step=500)

filtered = activities
if selected_dest != "All Destinations":
    filtered = [a for a in filtered if a.get("destination_name") == selected_dest]
if selected_cat != "All Categories":
    filtered = [a for a in filtered if a.get("category") == selected_cat]
filtered = [a for a in filtered if a.get("price", 0) <= max_price]

st.markdown(f"Showing **{len(filtered)}** activity options")

if not filtered:
    st.info("No activities match your criteria.", icon=":material/search_off:")
else:
    cols = st.columns(3)
    for idx, a in enumerate(filtered):
        with cols[idx % 3]:
            render_activity_card(a)

if filtered:
    st.subheader(":material/bar_chart: Activities Breakdown by Category", anchor=False)
    df_act = pd.DataFrame(filtered)
    fig = px.bar(df_act, x="category", y="price", color="category", text_auto=True)
    plotly_theme(fig)
    st.plotly_chart(fig, key="act_price_chart")

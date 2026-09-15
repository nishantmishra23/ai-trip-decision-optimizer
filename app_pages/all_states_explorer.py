"""
All 28 Indian States & Destinations Explorer.
Interactive discovery of every state in India with live OpenWeatherMap queries,
Google Maps / Search links, and direct Gemini AI trip planning.
"""
import os
import sys

# Ensure project root is in sys.path
_current_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
ROOT_DIR = os.path.dirname(_current_dir) if "app_pages" in _current_dir else _current_dir
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st
from data.india_states_places import (
    get_all_states,
    get_states_by_region,
    get_google_maps_url,
    get_google_search_url,
)
from services.weather_service import get_weather

# Page Title & Header
st.title("🇮🇳 Explore All 28 States of India", icon=":material/explore:")
st.caption("Comprehensive student & traveler guide across India — featuring live weather, Google Maps integration, and AI trip planning.")

# ── Metrics Row ─────────────────────────────────────────────────────────────────
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("Total States", "28 States", delta="100% India Covered", delta_color="normal")
with m2:
    st.metric("Student Budget", "₹1,200 – ₹2,500", delta="Per Day Est.", delta_color="normal")
with m3:
    st.metric("Live Weather", "OpenWeather API", delta="Real-Time", delta_color="normal")
with m4:
    st.metric("AI Engine", "Gemini 3.6 Flash", delta="Personalized", delta_color="normal")

st.divider()

# ── Filter Controls ─────────────────────────────────────────────────────────────
col_search, col_region, col_cat = st.columns([2, 1, 1], gap="small")

with col_search:
    search_query = st.text_input(
        "Search State or Destination",
        placeholder="e.g. Goa, Himachal, Kerala, Varanasi, Tawang...",
        key="state_search_input"
    )

with col_region:
    region_options = ["All Regions", "North", "South", "East", "West", "North-East", "Central"]
    selected_region = st.selectbox("Filter by Region", region_options)

with col_cat:
    cat_filter = st.selectbox(
        "Filter by Vibe",
        ["All Vibes", "Mountains & Snow", "Beach", "Heritage", "Nature & Wildlife", "Spiritual", "Adventure"]
    )

# Filter logic
states = get_all_states()
if selected_region != "All Regions":
    states = [s for s in states if s["region"].lower() == selected_region.lower()]

if cat_filter != "All Vibes":
    states = [s for s in states if cat_filter.lower().split()[0] in s["category"].lower()]

if search_query.strip():
    q = search_query.strip().lower()
    states = [
        s for s in states
        if q in s["name"].lower()
        or q in s["capital"].lower()
        or any(q in p["name"].lower() or q in p["highlight"].lower() for p in s["top_places"])
    ]

st.markdown(f"**Showing {len(states)} States**")

# ── Render State Cards ──────────────────────────────────────────────────────────
REGION_COLORS = {
    "North": "blue",
    "South": "green",
    "East": "orange",
    "West": "violet",
    "North-East": "teal",
    "Central": "red",
}

for state in states:
    with st.container(border=True):
        col_header, col_badges = st.columns([3, 2])
        with col_header:
            st.subheader(f"{state['name']}", anchor=False)
            st.caption(f"**Capital:** {state['capital']} • *{state['tagline']}*")
        with col_badges:
            st.badge(f"Region: {state['region']}", color="blue")
            st.badge(f"Category: {state['category']}", color="violet")
            st.badge(f"Best: {state['best_season']}", color="green")
            st.badge(f"₹{state['student_daily_cost']:,}/day (Student)", color="orange")

        st.markdown(f"_{state['description']}_")

        # Top Places Section
        st.markdown("##### 📍 Top Places to Explore")
        cols_places = st.columns(len(state["top_places"]))
        for idx, place in enumerate(state["top_places"]):
            with cols_places[idx]:
                with st.container(border=True):
                    st.markdown(f"**{place['name']}**")
                    st.caption(f"🏷️ {place['type']}")
                    st.markdown(f"<small>{place['highlight']}</small>", unsafe_allow_html=True)
                    
                    # Direct Google Maps & Search Buttons
                    gmaps_url = get_google_maps_url(place["name"], state["name"])
                    gsearch_url = get_google_search_url(place["name"], state["name"])
                    
                    st.link_button("📍 Google Maps", gmaps_url, use_container_width=True)
                    st.link_button("🔍 Top Things to Do", gsearch_url, use_container_width=True)

        st.divider()

        # Action bar: Live Weather & Gemini Planner
        col_w_btn, col_w_disp = st.columns([1, 3], gap="medium")
        weather_key = f"show_weather_{state['id']}"

        with col_w_btn:
            if st.button(
                f"🌤️ Live Weather in {state['weather_city']}",
                key=f"btn_weather_{state['id']}",
                type="secondary",
                use_container_width=True,
            ):
                st.session_state[weather_key] = True

        with col_w_disp:
            if st.session_state.get(weather_key, False):
                with st.spinner(f"Fetching live weather for {state['weather_city']}..."):
                    w = get_weather(state["weather_city"])
                    source_label = "🟢 Live (OpenWeather API)" if w.get("source") == "live" else "🟡 Curated Regional Climate"
                    st.info(
                        f"**{state['weather_city']} Current Weather:** {w.get('temp')}°C (Feels like {w.get('feels_like')}°C) • "
                        f"**{w.get('condition')}** ({w.get('description')}) • "
                        f"Humidity: {w.get('humidity')}% • Wind: {w.get('wind_speed')} km/h • "
                        f"{source_label}",
                        icon=":material/wb_sunny:"
                    )

"""
Restaurant & Dining Recommendations page for AI Trip Decision Optimizer.
Complete dining discovery across all 28 Indian States with authentic cuisines,
pure veg options, signature dish recommendations, and direct Google Maps navigation.
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
from utils.helpers import plotly_theme, format_currency
from data.india_tourism_data import (
    get_all_state_names,
    get_destinations_by_state,
    get_destination_data,
    filter_restaurants,
    gmaps_url,
    get_stats
)
from services.weather_service import get_weather

# ── Hero Section ───────────────────────────────────────────────────────────────
st.title("Dining & Restaurants across All 28 States", icon=":material/restaurant:")
st.caption(
    "Discover legendary street food, authentic state thalis, coastal seafood shacks, and fine dining across every state in India — "
    "with verified average costs, popular dishes, pure-veg filters, and direct Google Maps locations."
)

stats = get_stats()
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("States Covered", f"{stats['states_count']} States", delta="100% of India", delta_color="normal")
with m2:
    st.metric("Food Destinations", f"{stats['destinations_count']}+ Cities", delta="Curated Flavors", delta_color="normal")
with m3:
    st.metric("Verified Eateries", f"{stats['restaurants_count']}+ Spots", delta="Street to Fine Dining", delta_color="normal")
with m4:
    st.metric("Cost for Two", "₹120 – ₹4,500", delta="Budget to Royal", delta_color="normal")

st.divider()

# ── State & Destination Cascade Selectors ──────────────────────────────────────
all_states = get_all_state_names()

default_state_idx = 0
if "selected_state" in st.session_state and st.session_state["selected_state"] in all_states:
    default_state_idx = all_states.index(st.session_state["selected_state"])
elif "Maharashtra" in all_states:
    default_state_idx = all_states.index("Maharashtra")

sel_c1, sel_c2, sel_c3 = st.columns([1.5, 2, 1.5], gap="medium")

with sel_c1:
    selected_state = st.selectbox(
        "1. Select State (All 28 States)",
        all_states,
        index=default_state_idx,
        key="rest_page_state_select"
    )

destinations = get_destinations_by_state(selected_state)
dest_names = [d["name"] for d in destinations] if destinations else []

with sel_c2:
    selected_dest_name = st.selectbox(
        f"2. Select Destination in {selected_state}",
        dest_names,
        key="rest_page_dest_select"
    )

current_dest = get_destination_data(selected_state, selected_dest_name) if selected_dest_name else None

# Area / Neighborhood selector
areas = ["All Areas"]
if current_dest and "neighborhoods" in current_dest:
    areas += current_dest["neighborhoods"]

with sel_c3:
    selected_area = st.selectbox(
        "3. Neighborhood / Area",
        areas,
        key="rest_page_area_select"
    )

# ── Destination Food Overview Banner ──────────────────────────────────────────
if current_dest:
    with st.container(border=True):
        head_c1, head_c2 = st.columns([3, 1])
        with head_c1:
            st.subheader(f"{current_dest['name']} — Culinary Flavors & Dining", anchor=False)
            st.write(current_dest.get("overview", ""))
            
            # Badges row
            b_cols = st.columns(4)
            with b_cols[0]:
                st.badge(f"Style: {current_dest.get('travel_style', 'Culinary & Culture')}", color="blue")
            with b_cols[1]:
                st.badge(f"Avg Meal for Two: ₹{current_dest.get('budget_daily', 1500) // 2:,}", color="orange")
            with b_cols[2]:
                st.badge(f"Rating: {current_dest.get('rating', 4.5):.1f} ★", color="green")
            with b_cols[3]:
                st.badge(f"Best Time: {current_dest.get('best_time', 'All Year')}", color="violet")

        with head_c2:
            st.markdown("##### 📍 Dining Tools")
            maps_all_rests = gmaps_url(f"Top Restaurants & Food in {selected_dest_name}, {selected_state}")
            st.link_button("🗺️ View Food Map", maps_all_rests, use_container_width=True)
            
            weather_city = current_dest.get("weather_city", selected_dest_name.split()[0])
            if st.button(f"🌤️ Weather in {weather_city}", key=f"rest_weather_btn_{weather_city}", use_container_width=True):
                w = get_weather(weather_city)
                st.info(
                    f"**{weather_city}:** {w.get('temp')}°C, {w.get('condition')} ({w.get('description')})\n\n"
                    f"Humidity: {w.get('humidity')}% • Wind: {w.get('wind_speed')} km/h",
                    icon=":material/wb_sunny:"
                )

# ── Dining Filters ─────────────────────────────────────────────────────────────
with st.container(border=True):
    st.subheader(":material/tune: Filter Dining Options in " + (selected_dest_name or selected_state), anchor=False)
    f1, f2, f3, f4 = st.columns(4, gap="medium")
    
    with f1:
        max_cost = st.slider(
            "Max Average Cost for Two (₹)",
            min_value=200,
            max_value=5000,
            value=3000,
            step=100,
            key="rest_slider_max_cost"
        )
    with f2:
        cuisine_choices = ["All Cuisines", "Traditional", "Seafood", "Thali", "Street Food", "Cafe", "Mughlai", "Continental", "Bakery", "Tibetan"]
        selected_cuisine = st.selectbox("Cuisine Style", cuisine_choices, key="rest_cuisine_select")
    with f3:
        min_rating_choice = st.selectbox(
            "Minimum Rating",
            ["All Ratings", "4.2+ Stars", "4.5+ Stars", "4.7+ Stars"],
            key="rest_rating_select"
        )
    with f4:
        st.write("**Dietary Preference**")
        veg_only = st.toggle("Pure Veg Only 🌱", value=False, key="rest_veg_toggle")

# Apply filters
min_rat = None
if min_rating_choice == "4.2+ Stars":
    min_rat = 4.2
elif min_rating_choice == "4.5+ Stars":
    min_rat = 4.5
elif min_rating_choice == "4.7+ Stars":
    min_rat = 4.7

filtered = filter_restaurants(
    current_dest,
    max_cost=max_cost,
    cuisine=selected_cuisine if selected_cuisine != "All Cuisines" else None,
    is_veg_only=veg_only,
    min_rating=min_rat
)

# Area filter
if selected_area != "All Areas":
    filtered = [r for r in filtered if selected_area.lower() in r.get("area", "").lower()]

st.markdown(f"#### Verified Dining in {selected_dest_name} ({len(filtered)} recommendations)")

if not filtered:
    st.info(
        f"No restaurants match your filters in {selected_dest_name}. Try disabling the Pure Veg toggle or expanding the budget.",
        icon=":material/search_off:"
    )
    st.link_button(
        f"🔍 Search All Dining in {selected_dest_name} on Google Maps",
        gmaps_url(f"Restaurants and Cafes in {selected_dest_name}, {selected_state}"),
        type="primary"
    )
else:
    # Render restaurant cards in 3 columns
    cols = st.columns(3, gap="medium")
    for idx, r in enumerate(filtered):
        with cols[idx % 3]:
            with st.container(border=True):
                # Title and Area
                st.markdown(f"#### 🍽️ {r.get('name')}")
                st.caption(f"📍 **{r.get('area', selected_dest_name)}**, {selected_dest_name}")
                
                # Badges: Cuisine and Veg/Non-Veg
                badge_cols = st.columns([2, 1])
                with badge_cols[0]:
                    st.badge(r.get("cuisine", "Local Cuisine"), color="blue")
                with badge_cols[1]:
                    if r.get("is_veg", False):
                        st.badge("Pure Veg 🌱", color="green")
                    else:
                        st.badge("Non-Veg 🍗", color="orange")
                
                # Pricing & Rating Metrics
                cost_col, rat_col = st.columns(2)
                with cost_col:
                    st.metric("Avg for Two", format_currency(r.get("average_cost_for_two", 0)))
                with rat_col:
                    st.metric("Rating", f"{r.get('rating', 4.5):.1f} ★")
                
                # Must-Try Dishes
                if "popular_dishes" in r and r["popular_dishes"]:
                    st.markdown(f"⭐ **Must-Try:** *{r['popular_dishes']}*")
                
                # Direct Google Maps Link
                rest_map_link = r.get("gmaps_url", gmaps_url(f"{r.get('name')}, {selected_dest_name}"))
                st.link_button("📍 View on Google Maps", rest_map_link, use_container_width=True)
                
                # Google Search Reviews / Menu button
                import urllib.parse
                search_url = f"https://www.google.com/search?q={urllib.parse.quote_plus(r.get('name') + ' ' + selected_dest_name + ' menu reviews')}"
                st.link_button("📖 Reviews & Menu", search_url, use_container_width=True)

# ── Google-Style "Explore Other Culinary Cities in State" ─────────────────────
st.divider()
st.subheader(f":material/restaurant_menu: Explore Other Food Hubs in {selected_state}", anchor=False)

other_dests = [d for d in destinations if d["name"] != selected_dest_name]
if other_dests:
    od_cols = st.columns(min(len(other_dests), 4))
    for o_idx, od in enumerate(other_dests[:4]):
        with od_cols[o_idx]:
            with st.container(border=True):
                st.markdown(f"**{od['name']}**")
                st.caption(od.get("tagline", ""))
                st.write(f"🍽️ {len(od.get('restaurants', []))} dining spots • 🏨 {len(od.get('hotels', []))} stays")
                if st.button("Explore Dining Here", key=f"switch_rest_dest_{o_idx}_{od['name']}", use_container_width=True):
                    st.session_state["rest_page_dest_select"] = od["name"]
                    st.rerun()

# ── Dining Cost Distribution Chart ─────────────────────────────────────────────
if filtered:
    st.divider()
    st.subheader(":material/bar_chart: Average Cost for Two by Restaurant", anchor=False)
    df_r = pd.DataFrame(filtered)
    if "name" in df_r.columns and "average_cost_for_two" in df_r.columns:
        fig = px.bar(
            df_r,
            x="name",
            y="average_cost_for_two",
            color="is_veg",
            color_discrete_map={True: "#22c55e", False: "#f97316"},
            text_auto="₹%{y:,.0f}",
            labels={"average_cost_for_two": "Average Cost for Two (₹)", "name": "Restaurant", "is_veg": "Pure Vegetarian"},
            title=f"Cost Comparison of Dining Options in {selected_dest_name}"
        )
        plotly_theme(fig)
        st.plotly_chart(fig, key="rest_cost_chart_v2", use_container_width=True)

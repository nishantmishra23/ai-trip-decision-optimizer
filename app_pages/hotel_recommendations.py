"""
Hotel & Resort Recommendations page for AI Trip Decision Optimizer.
Provides complete coverage of all 28 Indian States and 119+ authentic destinations
with Google-style exploration, rich filters, and direct Google Maps integration.
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
    get_state_data,
    get_destinations_by_state,
    get_destination_data,
    filter_hotels,
    gmaps_url,
    get_stats
)
from services.weather_service import get_weather

# ── Hero Section ───────────────────────────────────────────────────────────────
st.title("Hotels & Stays across All 28 States", icon=":material/hotel:")
st.caption(
    "Explore luxury resorts, boutique heritage stays, and budget backpacker hostels across every state of India — "
    "complete with verified amenities, ratings, and direct Google Maps navigation."
)

stats = get_stats()
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("States Covered", f"{stats['states_count']} States", delta="100% of India", delta_color="normal")
with m2:
    st.metric("Curated Destinations", f"{stats['destinations_count']}+ Cities", delta="4–8 per State", delta_color="normal")
with m3:
    st.metric("Verified Stays", f"{stats['hotels_count']}+ Stays", delta="Luxury to Hostels", delta_color="normal")
with m4:
    st.metric("Price Range", "₹750 – ₹48,000", delta="Student to Ultra-Luxury", delta_color="normal")

st.divider()

# ── State & Destination Cascade Selectors ──────────────────────────────────────
all_states = get_all_state_names()

# Check for pre-selected state or destination in session state
default_state_idx = 0
if "selected_state" in st.session_state and st.session_state["selected_state"] in all_states:
    default_state_idx = all_states.index(st.session_state["selected_state"])
elif "Goa" in all_states:
    default_state_idx = all_states.index("Goa")

sel_c1, sel_c2, sel_c3 = st.columns([1.5, 2, 1.5], gap="medium")

with sel_c1:
    selected_state = st.selectbox(
        "1. Select State (All 28 States)",
        all_states,
        index=default_state_idx,
        key="hotel_page_state_select"
    )

destinations = get_destinations_by_state(selected_state)
dest_names = [d["name"] for d in destinations] if destinations else []

with sel_c2:
    selected_dest_name = st.selectbox(
        f"2. Select Destination in {selected_state}",
        dest_names,
        key="hotel_page_dest_select"
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
        key="hotel_page_area_select"
    )

# ── Destination Overview Banner ────────────────────────────────────────────────
if current_dest:
    with st.container(border=True):
        head_c1, head_c2 = st.columns([3, 1])
        with head_c1:
            st.subheader(f"{current_dest['name']} — {current_dest.get('tagline', '')}", anchor=False)
            st.write(current_dest.get("overview", ""))
            
            # Badges row
            b_cols = st.columns(4)
            with b_cols[0]:
                st.badge(f"Best Season: {current_dest.get('best_time', 'All Year')}", color="blue")
            with b_cols[1]:
                st.badge(f"Duration: {current_dest.get('recommended_duration', '3 Days')}", color="green")
            with b_cols[2]:
                st.badge(f"Est. Daily: ₹{current_dest.get('budget_daily', 2000):,}", color="orange")
            with b_cols[3]:
                st.badge(f"Rating: {current_dest.get('rating', 4.5):.1f} ★ ({current_dest.get('popularity', 9.0)}/10)", color="violet")

        with head_c2:
            st.markdown("##### 📍 Location Tools")
            maps_all_hotels = gmaps_url(f"Hotels in {selected_dest_name}, {selected_state}")
            st.link_button("🗺️ View on Google Maps", maps_all_hotels, use_container_width=True)
            
            weather_city = current_dest.get("weather_city", selected_dest_name.split()[0])
            if st.button(f"🌤️ Weather in {weather_city}", key=f"hotel_weather_btn_{weather_city}", use_container_width=True):
                w = get_weather(weather_city)
                st.info(
                    f"**{weather_city}:** {w.get('temp')}°C, {w.get('condition')} ({w.get('description')})\n\n"
                    f"Humidity: {w.get('humidity')}% • Wind: {w.get('wind_speed')} km/h",
                    icon=":material/wb_sunny:"
                )

# ── Stay Filters ───────────────────────────────────────────────────────────────
with st.container(border=True):
    st.subheader(":material/tune: Filter Stays in " + (selected_dest_name or selected_state), anchor=False)
    f1, f2, f3, f4 = st.columns(4, gap="medium")
    
    with f1:
        max_price = st.slider(
            "Max Price / Night (₹)",
            min_value=700,
            max_value=50000,
            value=35000,
            step=500,
            key="hotel_slider_max_price"
        )
    with f2:
        cat_choices = ["All Categories", "Luxury", "Boutique", "Hostel", "Heritage", "Resort", "Comfort", "Eco"]
        selected_cat = st.selectbox("Property Category", cat_choices, key="hotel_cat_select")
    with f3:
        min_rating_choice = st.selectbox("Minimum Guest Rating", ["All Ratings", "4.0+ Stars", "4.5+ Stars", "4.8+ Stars"], key="hotel_rating_select")
    with f4:
        suit_choices = ["All", "Couples", "Family", "Solo", "Friends"]
        selected_suit = st.selectbox("Ideal For", suit_choices, key="hotel_suit_select")

# Apply filters
min_rat = None
if min_rating_choice == "4.0+ Stars":
    min_rat = 4.0
elif min_rating_choice == "4.5+ Stars":
    min_rat = 4.5
elif min_rating_choice == "4.8+ Stars":
    min_rat = 4.8

raw_hotels = current_dest.get("hotels", []) if current_dest else []

filtered = filter_hotels(
    current_dest,
    max_price=max_price,
    category=selected_cat if selected_cat != "All Categories" else None,
    min_rating=min_rat,
    suitability=selected_suit if selected_suit != "All" else None
)

# Filter by area if selected
if selected_area != "All Areas":
    filtered = [h for h in filtered if selected_area.lower() in h.get("area", "").lower()]

st.markdown(f"#### Available Stays in {selected_dest_name} ({len(filtered)} options)")

if not filtered:
    st.info(
        f"No stays match the exact filters in {selected_dest_name}. Try relaxing the price slider or category filter.",
        icon=":material/search_off:"
    )
    # Provide fallback button to search Google Maps directly
    st.link_button(
        f"🔍 Search All Stays in {selected_dest_name} on Google Maps",
        gmaps_url(f"Hotels in {selected_dest_name}, {selected_state}"),
        type="primary"
    )
else:
    # Render hotel cards in 3 columns
    cols = st.columns(3, gap="medium")
    for idx, h in enumerate(filtered):
        with cols[idx % 3]:
            with st.container(border=True):
                # Hotel title & area
                st.markdown(f"#### 🏨 {h.get('name')}")
                st.caption(f"📍 **{h.get('area', selected_dest_name)}**, {selected_dest_name}")
                
                # Badges
                st.badge(h.get("category", "Hotel"), color="blue")
                
                # Pricing & Rating Metrics
                price_col, rat_col = st.columns(2)
                with price_col:
                    st.metric("Per Night", format_currency(h.get("price_per_night", 0)))
                with rat_col:
                    st.metric("Rating", f"{h.get('rating', 4.5):.1f} ★")
                
                # Amenities chips
                if "amenities" in h and h["amenities"]:
                    amenities_str = " • ".join(h["amenities"][:4])
                    st.caption(f"✨ **Amenities:** {amenities_str}")
                
                # Suitability
                if "suitability" in h and h["suitability"]:
                    st.caption(f"👥 **Best for:** {', '.join(h['suitability'])}")
                
                # Direct Google Maps navigation link
                hotel_map_link = h.get("gmaps_url", gmaps_url(f"{h.get('name')}, {selected_dest_name}"))
                st.link_button("📍 View on Google Maps", hotel_map_link, use_container_width=True)
                
                # Trip planner select button
                if st.button("📌 Add to Trip Planner", key=f"btn_add_hotel_{idx}_{h.get('name')[:15]}", use_container_width=True):
                    st.session_state["planner_prefill"] = selected_dest_name
                    st.session_state["selected_hotel"] = h.get("name")
                    st.success(f"Selected {h.get('name')} for your trip! Redirecting to Planner...")
                    st.switch_page("app_pages/trip_planner.py")

# ── Google-Style "Explore More Destinations in State" ──────────────────────────
st.divider()
st.subheader(f":material/travel_explore: Explore Other Destinations in {selected_state}", anchor=False)

other_dests = [d for d in destinations if d["name"] != selected_dest_name]
if other_dests:
    od_cols = st.columns(min(len(other_dests), 4))
    for o_idx, od in enumerate(other_dests[:4]):
        with od_cols[o_idx]:
            with st.container(border=True):
                st.markdown(f"**{od['name']}**")
                st.caption(od.get("tagline", ""))
                st.write(f"🏨 {len(od.get('hotels', []))} stays • 🍽️ {len(od.get('restaurants', []))} restaurants")
                if st.button("Switch to Destination", key=f"switch_dest_{o_idx}_{od['name']}", use_container_width=True):
                    st.session_state["hotel_page_dest_select"] = od["name"]
                    st.rerun()

# ── Price Distribution Chart ───────────────────────────────────────────────────
if filtered:
    st.divider()
    st.subheader(":material/bar_chart: Price Comparison by Hotel Category", anchor=False)
    df_h = pd.DataFrame(filtered)
    if "category" in df_h.columns and "price_per_night" in df_h.columns:
        avg_df = df_h.groupby("category")["price_per_night"].mean().reset_index()
        fig = px.bar(
            avg_df,
            x="category",
            y="price_per_night",
            color="category",
            text_auto="₹%{y:,.0f}",
            labels={"price_per_night": "Average Price per Night (₹)", "category": "Stay Category"},
            title=f"Average Nightly Rates in {selected_dest_name}"
        )
        plotly_theme(fig)
        st.plotly_chart(fig, key="hotel_price_chart_v2", use_container_width=True)

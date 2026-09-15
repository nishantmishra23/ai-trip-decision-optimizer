"""
Activity & Things to Do Recommendations page for AI Trip Decision Optimizer.
Comprehensive activities, adventure tours, spiritual walks, and heritage sights
across all 28 Indian States with direct Google Maps navigation and trip planning.
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
    filter_activities,
    filter_places,
    gmaps_url,
    get_stats
)
from services.weather_service import get_weather

# ── Hero Section ───────────────────────────────────────────────────────────────
st.title("Activities, Tours & Sights across All 28 States", icon=":material/hiking:")
st.caption(
    "Explore thrilling Himalayan treks, river rafting, desert camel safaris, cultural temple walks, and wildlife safaris "
    "across every state of India — complete with costs, duration, and direct Google Maps locations."
)

stats = get_stats()
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.metric("States Covered", f"{stats['states_count']} States", delta="100% of India", delta_color="normal")
with m2:
    st.metric("Destinations", f"{stats['destinations_count']}+ Cities", delta="Curated Experiences", delta_color="normal")
with m3:
    st.metric("Curated Activities", f"{stats['activities_count']}+ Tours", delta="Adventure & Heritage", delta_color="normal")
with m4:
    st.metric("Activity Cost", "Free – ₹4,500", delta="Walks to Safaris", delta_color="normal")

st.divider()

# ── State & Destination Cascade Selectors ──────────────────────────────────────
all_states = get_all_state_names()

default_state_idx = 0
if "selected_state" in st.session_state and st.session_state["selected_state"] in all_states:
    default_state_idx = all_states.index(st.session_state["selected_state"])
elif "Himachal Pradesh" in all_states:
    default_state_idx = all_states.index("Himachal Pradesh")

sel_c1, sel_c2 = st.columns([1.5, 2], gap="medium")

with sel_c1:
    selected_state = st.selectbox(
        "1. Select State (All 28 States)",
        all_states,
        index=default_state_idx,
        key="act_page_state_select"
    )

destinations = get_destinations_by_state(selected_state)
dest_names = [d["name"] for d in destinations] if destinations else []

with sel_c2:
    selected_dest_name = st.selectbox(
        f"2. Select Destination in {selected_state}",
        dest_names,
        key="act_page_dest_select"
    )

current_dest = get_destination_data(selected_state, selected_dest_name) if selected_dest_name else None

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
                st.badge(f"Style: {current_dest.get('travel_style', 'Adventure & Sights')}", color="blue")
            with b_cols[1]:
                st.badge(f"Best Time: {current_dest.get('best_time', 'All Year')}", color="green")
            with b_cols[2]:
                st.badge(f"Recommended: {current_dest.get('recommended_duration', '3 Days')}", color="orange")
            with b_cols[3]:
                st.badge(f"Rating: {current_dest.get('rating', 4.5):.1f} ★", color="violet")

        with head_c2:
            st.markdown("##### 📍 Exploration Tools")
            maps_all_acts = gmaps_url(f"Things to do and tourist spots in {selected_dest_name}, {selected_state}")
            st.link_button("🗺️ View Sights on Maps", maps_all_acts, use_container_width=True)
            
            weather_city = current_dest.get("weather_city", selected_dest_name.split()[0])
            if st.button(f"🌤️ Weather in {weather_city}", key=f"act_weather_btn_{weather_city}", use_container_width=True):
                w = get_weather(weather_city)
                st.info(
                    f"**{weather_city}:** {w.get('temp')}°C, {w.get('condition')} ({w.get('description')})\n\n"
                    f"Humidity: {w.get('humidity')}% • Wind: {w.get('wind_speed')} km/h",
                    icon=":material/wb_sunny:"
                )

# ── Section 1: Places to Visit ─────────────────────────────────────────────────
places = current_dest.get("places_to_visit", []) if current_dest else []
st.subheader(f"📍 Top Places to Visit in {selected_dest_name} ({len(places)} landmarks)", anchor=False)

if places:
    p_cols = st.columns(min(len(places), 3), gap="medium")
    for p_idx, p in enumerate(places):
        with p_cols[p_idx % 3]:
            with st.container(border=True):
                st.markdown(f"#### 🏛️ {p.get('name')}")
                st.badge(p.get("category", "Sight"), color="blue")
                st.write(p.get("highlight", ""))
                
                c_fee, c_time = st.columns(2)
                with c_fee:
                    st.metric("Entry Fee", p.get("fee", "Free"))
                with c_time:
                    st.metric("Est. Time", p.get("time", "2 hrs"))
                
                p_map_link = p.get("gmaps_url", gmaps_url(f"{p.get('name')}, {selected_dest_name}"))
                st.link_button("📍 View Location on Google Maps", p_map_link, use_container_width=True)

st.divider()

# ── Section 2: Things to Do & Activities ───────────────────────────────────────
with st.container(border=True):
    st.subheader(":material/tune: Filter Things to Do in " + (selected_dest_name or selected_state), anchor=False)
    f1, f2 = st.columns(2, gap="medium")
    
    with f1:
        max_cost = st.slider(
            "Max Activity Cost (₹)",
            min_value=0,
            max_value=5000,
            value=3500,
            step=250,
            key="act_slider_max_cost"
        )
    with f2:
        cat_choices = ["All Categories", "Adventure", "Trek", "Safari", "Tour", "Cultural", "Water Sports", "Yoga"]
        selected_cat = st.selectbox("Activity Style", cat_choices, key="act_cat_select")

filtered_acts = filter_activities(
    current_dest,
    max_cost=max_cost,
    category=selected_cat if selected_cat != "All Categories" else None
)

st.markdown(f"#### Curated Things to Do in {selected_dest_name} ({len(filtered_acts)} experiences)")

if not filtered_acts:
    st.info(
        f"No activities match your cost or category filter in {selected_dest_name}. Try increasing the cost slider.",
        icon=":material/search_off:"
    )
    st.link_button(
        f"🔍 Discover All Activities in {selected_dest_name} on Google Maps",
        gmaps_url(f"Tours, activities and things to do in {selected_dest_name}, {selected_state}"),
        type="primary"
    )
else:
    act_cols = st.columns(min(len(filtered_acts), 3), gap="medium")
    for a_idx, a in enumerate(filtered_acts):
        with act_cols[a_idx % 3]:
            with st.container(border=True):
                st.markdown(f"#### 🎯 {a.get('name')}")
                st.badge(a.get("category", "Activity"), color="green")
                
                c_cost, c_dur = st.columns(2)
                with c_cost:
                    cost_val = a.get("cost", 0)
                    st.metric("Estimated Cost", "Free" if cost_val == 0 else format_currency(cost_val))
                with c_dur:
                    st.metric("Duration", a.get("duration", "2 hrs"))
                
                # Direct Google Maps Link
                act_map_link = gmaps_url(f"{a.get('name')}, {selected_dest_name}")
                st.link_button("📍 Open in Google Maps", act_map_link, use_container_width=True)
                
                # Add to Trip Planner
                if st.button("📌 Add Activity to Planner", key=f"btn_act_plan_{a_idx}_{a.get('name')[:15]}", use_container_width=True):
                    st.session_state["planner_prefill"] = selected_dest_name
                    st.session_state["selected_activity"] = a.get("name")
                    st.success(f"Added {a.get('name')} to your plan! Opening Planner...")
                    st.switch_page("app_pages/trip_planner.py")

# ── Google-Style "Explore Other Destinations in State" ──────────────────────────
st.divider()
st.subheader(f":material/hiking: Explore Activities in Other Destinations of {selected_state}", anchor=False)

other_dests = [d for d in destinations if d["name"] != selected_dest_name]
if other_dests:
    od_cols = st.columns(min(len(other_dests), 4))
    for o_idx, od in enumerate(other_dests[:4]):
        with od_cols[o_idx]:
            with st.container(border=True):
                st.markdown(f"**{od['name']}**")
                st.caption(od.get("tagline", ""))
                st.write(f"🎯 {len(od.get('things_to_do', []))} activities • 🏛️ {len(od.get('places_to_visit', []))} sights")
                if st.button("Explore Here", key=f"switch_act_dest_{o_idx}_{od['name']}", use_container_width=True):
                    st.session_state["act_page_dest_select"] = od["name"]
                    st.rerun()

# ── Activity Cost Chart ────────────────────────────────────────────────────────
if filtered_acts:
    st.divider()
    st.subheader(":material/bar_chart: Activity Cost Overview", anchor=False)
    df_a = pd.DataFrame(filtered_acts)
    if "name" in df_a.columns and "cost" in df_a.columns:
        fig = px.bar(
            df_a,
            x="name",
            y="cost",
            color="category",
            text_auto="₹%{y:,.0f}",
            labels={"cost": "Estimated Cost (₹)", "name": "Activity / Tour", "category": "Category"},
            title=f"Activity Costs in {selected_dest_name}"
        )
        plotly_theme(fig)
        st.plotly_chart(fig, key="act_cost_chart_v2", use_container_width=True)

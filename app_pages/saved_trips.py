"""
Saved Trips for AI Trip Decision Optimizer.
Displays saved trips from database and current active session.
"""
import os
import sys

# Ensure project root is in sys.path
_current_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
ROOT_DIR = os.path.dirname(_current_dir) if "app_pages" in _current_dir else _current_dir
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st
from auth.auth import init_session
from utils.helpers import format_currency

init_session()

# Page Header
st.title("💾 Saved Trip Itineraries", icon=":material/bookmark:")
st.caption("Access and review your planned journeys, AI itineraries, and expense estimates.")

# Collect trips from DB and session
user_id = st.session_state.get("user_id", 0)
trips = []

# DB trips
try:
    from database.queries import get_user_trips
    if user_id:
        db_trips = get_user_trips(user_id)
        if db_trips:
            trips.extend(db_trips)
except Exception:
    pass

# Session trips
session_trips = st.session_state.get("saved_trips_data", [])
for st_trip in session_trips:
    trips.append({
        "destination_name": st_trip["destination"],
        "start_date": st_trip.get("date", "Upcoming"),
        "end_date": f"{st_trip.get('days', 3)} Days Trip",
        "total_budget": st_trip.get("total_cost", 12000),
        "travelers": st_trip.get("travelers", 2),
        "source": "AI Gemini Generator",
        "itinerary": st_trip.get("itinerary", [])
    })

if not trips:
    with st.container(border=True):
        st.info("You haven't saved any trips yet! Generate a custom schedule with the AI Itinerary planner or explore all 28 states.", icon=":material/info:")
        c1, c2 = st.columns(2)
        with c1:
            st.page_link("app_pages/ai_itinerary.py", label="Generate AI Itinerary", icon=":material/auto_awesome:")
        with c2:
            st.page_link("app_pages/all_states_explorer.py", label="Explore All 28 States", icon=":material/explore:")
else:
    st.markdown(f"**Showing {len(trips)} Saved Itinerary{'ies' if len(trips) > 1 else ''}**")
    cols = st.columns(3)
    for idx, t in enumerate(trips):
        dest_name = t.get("destination_name", "Destination")
        start_date = t.get("start_date", "")
        end_date = t.get("end_date", "")
        budget = t.get("total_budget", 0)
        travelers = t.get("travelers", 1)

        with cols[idx % 3]:
            with st.container(border=True):
                st.markdown(f"### {dest_name}")
                st.caption(f"🗓️ {start_date} • {end_date}")
                st.metric("Total Budget", format_currency(budget))
                st.badge(f"👥 {travelers} Traveler(s)", color="blue")
                
                if t.get("source"):
                    st.badge(t["source"], color="violet")

                if t.get("itinerary"):
                    with st.expander("View Daily Details"):
                        for d in t["itinerary"]:
                            st.markdown(f"**{d.get('day')}:** {d.get('title')}")
                            for s in d.get("slots", []):
                                st.caption(f"- {s.get('time')}: {s.get('title')} (₹{s.get('cost')})")

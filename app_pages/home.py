"""
Home / Main Dashboard page for AI Trip Decision Optimizer.
"""
import streamlit as st
from auth.auth import init_session
from utils.helpers import get_destinations_with_fallback
from utils.components import render_destination_card

init_session()

user = st.session_state.get("user", {}) or {}
name = user.get("name", "Explorer")

# ── Hero ───────────────────────────────────────────────────────────────────────
st.title(f"Welcome, {name}!", icon=":material/waving_hand:")
st.caption("AI Trip Decision Optimizer — intelligent multi-factor engine for seamless travel planning & destination discovery")

# ── Key Statistics ─────────────────────────────────────────────────────────────
try:
    from database.queries import count_destinations, count_trips
    c_dests = count_destinations()
    c_trips = count_trips()
except Exception:
    c_dests = "10+"
    c_trips = "50+"

m1, m2, m3, m4 = st.columns(4)
with m1:
    with st.container(border=True):
        st.metric("Top destinations", str(c_dests), help="Curated travel locations available")
with m2:
    with st.container(border=True):
        st.metric("Avg daily budget", "₹3,500", help="Estimated average daily cost")
with m3:
    with st.container(border=True):
        st.metric("Satisfaction rating", "4.7 / 5.0", help="Average user satisfaction score")
with m4:
    with st.container(border=True):
        st.metric("Trips planned", str(c_trips), help="Total itineraries generated")

# ── Smart Search ───────────────────────────────────────────────────────────────
with st.container(border=True):
    st.caption(":material/auto_awesome: **Smart travel search**")
    c_search, c_btn = st.columns([4, 1])
    with c_search:
        st.text_input("What are you planning?", placeholder="Search destinations, styles, or countries…", label_visibility="collapsed", key="home_search")
    with c_btn:
        if st.button("Explore", type="primary", icon=":material/search:"):
            st.switch_page("app_pages/destination_discovery.py")

# ── Featured Destinations ──────────────────────────────────────────────────────
st.header("Featured destinations", icon=":material/explore:", anchor=False)

dests = get_destinations_with_fallback()[:6]
cols = st.columns(3)
for i, dest in enumerate(dests):
    with cols[i % 3]:
        render_destination_card(dest, show_details=False)

# ── Quick Access Shortcuts ─────────────────────────────────────────────────────
st.header("Quick access", icon=":material/bolt:", anchor=False)
c1, c2, c3, c4 = st.columns(4)
with c1:
    with st.container(border=True):
        st.markdown(":material/map: **Trip planner**")
        st.caption("Build custom plans with budget splits.")
        st.page_link("app_pages/trip_planner.py", label="Open planner", icon=":material/arrow_forward:")
with c2:
    with st.container(border=True):
        st.markdown(":material/psychology: **AI recommendations**")
        st.caption("Rank destinations using weighted AI scoring.")
        st.page_link("app_pages/ai_recommendations.py", label="Get recommendations", icon=":material/arrow_forward:")
with c3:
    with st.container(border=True):
        st.markdown(":material/calculate: **Budget optimizer**")
        st.caption("Optimise expenses by hotel, food, and activities.")
        st.page_link("app_pages/budget_optimizer.py", label="Optimise budget", icon=":material/arrow_forward:")
with c4:
    with st.container(border=True):
        st.markdown(":material/bookmark: **Saved trips**")
        st.caption("View your previously generated itineraries.")
        st.page_link("app_pages/saved_trips.py", label="View trips", icon=":material/arrow_forward:")

# ── Auth Banner ────────────────────────────────────────────────────────────────
if not st.session_state.get("logged_in"):
    with st.container(border=True):
        st.markdown(":material/lock: **Personalise your experience**")
        st.caption("Sign in to save trip itineraries, track history, and get custom AI recommendations.")
        st.page_link("app_pages/login.py", label="Sign in / Register", icon=":material/login:")
else:
    with st.container(border=True):
        st.markdown(f":material/verified_user: **Welcome back, {name}!**")
        st.caption("You have access to saved itineraries and personalised decision tools.")
        st.page_link("app_pages/saved_trips.py", label="View saved trips", icon=":material/bookmark:")

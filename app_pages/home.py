"""
Home / Main Dashboard page for AI Trip Decision Optimizer.
"""
import streamlit as st
from auth.auth import init_session
from utils.helpers import get_destinations_with_fallback
from utils.theme import inject_theme_css
from utils.components import render_destination_card

init_session()
inject_theme_css()

user = st.session_state.get("user", {}) or {}
name = user.get("name", "Explorer")

# Hero Banner
st.markdown(f"""
<div class="app-hero-banner">
    <div class="app-hero-title">👋 Welcome, {name}!</div>
    <div class="app-hero-subtitle">AI Trip Decision Optimizer — Intelligent multi-factor decision engine for seamless travel planning & destination discovery</div>
</div>
""", unsafe_allow_html=True)

with st.container(border=True):
    st.caption(":material/auto_awesome: **SMART TRAVEL SEARCH & COMMAND CENTER**")
    
    c_search, c_btn = st.columns([4, 1])
    with c_search:
        search_query = st.text_input("What are you planning?", placeholder="Search destinations, styles, or countries...", label_visibility="collapsed")
    with c_btn:
        if st.button("Explore", type="primary", icon=":material/search:"):
            st.switch_page("app_pages/destination_discovery.py")

# Key Statistics Metrics
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
        st.metric("Top Destinations", str(c_dests), help="Curated travel locations available")
with m2:
    with st.container(border=True):
        st.metric("Avg Daily Budget", "₹3,500", help="Estimated average daily cost")
with m3:
    with st.container(border=True):
        st.metric("Satisfaction Rating", "4.7 / 5.0", help="Average user satisfaction score")
with m4:
    with st.container(border=True):
        st.metric("Trips Planned", str(c_trips), help="Total itineraries generated")

st.markdown("### :material/explore: Featured Destinations")

dests = get_destinations_with_fallback()[:6]
cols = st.columns(3)

for i, dest in enumerate(dests):
    with cols[i % 3]:
        render_destination_card(dest, show_details=False)

st.markdown("### :material/history: Recent Activity & Shortcuts")
c1, c2, c3, c4 = st.columns(4)
with c1:
    with st.container(border=True):
        st.markdown("#### :material/map: Trip Planner")
        st.caption("Build custom trip plans with budget splits.")
        st.page_link("app_pages/trip_planner.py", label="Open Planner", icon=":material/arrow_forward:")
with c2:
    with st.container(border=True):
        st.markdown("#### :material/psychology: AI Recommendations")
        st.caption("Rank destinations using weighted AI scoring.")
        st.page_link("app_pages/ai_recommendations.py", label="Get Recommendations", icon=":material/arrow_forward:")
with c3:
    with st.container(border=True):
        st.markdown("#### :material/calculate: Budget Optimizer")
        st.caption("Optimize expenses by hotel, food, and activities.")
        st.page_link("app_pages/budget_optimizer.py", label="Optimize Budget", icon=":material/arrow_forward:")
with c4:
    with st.container(border=True):
        st.markdown("#### :material/history: Saved Trips")
        st.caption("View your previously generated itineraries.")
        st.page_link("app_pages/saved_trips.py", label="View Trips", icon=":material/arrow_forward:")

st.divider()

if not st.session_state.get("logged_in"):
    with st.container(border=True):
        st.markdown("#### :material/lock: Personalize Your Experience")
        st.caption("Sign in to save trip itineraries, track history, and get custom recommendations.")
        st.page_link("app_pages/login.py", label="Sign In / Register", icon=":material/login:")
else:
    with st.container(border=True):
        st.markdown(f"#### :material/waving_hand: Welcome Back, {name}!")
        st.caption("You have access to saved itineraries and personalized decision tools.")
        st.page_link("app_pages/saved_trips.py", label="View Saved Trips", icon=":material/bookmark:")

"""
AI Trip Decision Optimizer — Main Entry Point
"""
import streamlit as st
from auth.auth import init_session

st.set_page_config(
    page_title="AI Trip Decision Optimizer",
    page_icon=":material/flight:",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session()


def build_navigation():
    logged_in = st.session_state.get("logged_in", False)
    user = st.session_state.get("user", {}) or {}
    is_admin = user.get("role", "") == "ADMIN"

    pages = {
        "": [
            st.Page("app_pages/home.py", title="Home", icon=":material/home:"),
            st.Page("app_pages/login.py", title="Sign in", icon=":material/login:"),
        ],
        "Plan Your Trip": [
            st.Page("app_pages/trip_planner.py", title="Trip planner", icon=":material/map:"),
            st.Page("app_pages/budget_optimizer.py", title="Budget optimizer", icon=":material/calculate:"),
            st.Page("app_pages/ai_itinerary.py", title="AI itinerary", icon=":material/calendar_month:"),
        ],
        "Discover": [
            st.Page("app_pages/destination_discovery.py", title="Destination discovery", icon=":material/explore:"),
            st.Page("app_pages/ai_recommendations.py", title="AI recommendations", icon=":material/psychology:"),
            st.Page("app_pages/destination_comparison.py", title="Destination comparison", icon=":material/compare:"),
        ],
        "Hotels & Dining": [
            st.Page("app_pages/hotel_recommendations.py", title="Hotels", icon=":material/hotel:"),
            st.Page("app_pages/restaurant_recommendations.py", title="Restaurants", icon=":material/restaurant:"),
            st.Page("app_pages/activity_recommendations.py", title="Activities", icon=":material/hiking:"),
        ],
        "Travel Info": [
            st.Page("app_pages/weather_intelligence.py", title="Weather intelligence", icon=":material/wb_sunny:"),
            st.Page("app_pages/transportation_analysis.py", title="Transportation", icon=":material/train:"),
        ],
        "My Trips": [
            st.Page("app_pages/saved_trips.py", title="Saved trips", icon=":material/bookmark:"),
            st.Page("app_pages/trip_history.py", title="Trip history", icon=":material/history:"),
            st.Page("app_pages/trip_summary.py", title="Trip summary", icon=":material/summarize:"),
        ],
        "Insights": [
            st.Page("app_pages/analytics.py", title="Analytics", icon=":material/bar_chart:"),
        ],
    }

    if is_admin:
        pages["Insights"].append(
            st.Page("app_pages/admin_dashboard.py", title="Admin dashboard", icon=":material/admin_panel_settings:")
        )

    return pages


# Sidebar header
with st.sidebar:
    st.markdown("### ✈️ AI Trip Optimizer")
    if st.session_state.get("logged_in"):
        user = st.session_state.get("user", {}) or {}
        st.caption(f"Logged in as **{user.get('name', 'User')}**")
        if st.button("Log out", icon=":material/logout:", key="global_logout"):
            from auth.auth import logout
            logout()
            st.rerun()
    else:
        st.caption("Not logged in")

pages = build_navigation()
page = st.navigation(pages, position="sidebar")
page.run()
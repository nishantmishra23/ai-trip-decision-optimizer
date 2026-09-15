"""
AI Trip Decision Optimizer — Main Entry Point
Handles multi-page navigation, sidebar branding, DB status, and session state.
"""
import streamlit as st
from auth.auth import init_session

st.set_page_config(
    page_title="AI Trip Decision Optimizer",
    page_icon=":material/flight:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize Session State
init_session()


@st.cache_data(ttl=30)
def _check_db() -> bool:
    """Cached DB health check (refreshes every 30 s)."""
    try:
        from database.connection import db_available
        return db_available()
    except Exception:
        return False


def _sidebar_db_status():
    """Render a compact DB status indicator in the sidebar."""
    is_up = _check_db()
    if is_up:
        st.sidebar.success("MySQL connected", icon=":material/cloud_done:")
    else:
        st.sidebar.caption(":material/cloud_off: Running in sample-data mode")


def build_navigation():
    logged_in = st.session_state.get("logged_in", False)
    user = st.session_state.get("user", {}) or {}
    is_admin = user.get("role", "") == "ADMIN"

    pages = {
        "Main": [
            st.Page("app_pages/home.py", title="Home", icon=":material/home:"),
            st.Page("app_pages/login.py", title="Account", icon=":material/person:"),
        ],
        "Trip Planning": [
            st.Page("app_pages/trip_planner.py", title="Trip planner", icon=":material/map:"),
            st.Page("app_pages/budget_optimizer.py", title="Budget optimizer", icon=":material/calculate:"),
            st.Page("app_pages/ai_itinerary.py", title="AI itinerary", icon=":material/calendar_month:"),
            st.Page("app_pages/ai_trip_optimizer.py", title="Multi-factor optimizer", icon=":material/auto_awesome:"),
        ],
        "Discover & Compare": [
            st.Page("app_pages/destination_discovery.py", title="Destination discovery", icon=":material/explore:"),
            st.Page("app_pages/ai_recommendations.py", title="AI recommendations", icon=":material/psychology:"),
            st.Page("app_pages/destination_comparison.py", title="Compare destinations", icon=":material/compare:"),
        ],
        "Stays & Experiences": [
            st.Page("app_pages/hotel_recommendations.py", title="Hotels & resorts", icon=":material/hotel:"),
            st.Page("app_pages/restaurant_recommendations.py", title="Restaurants & dining", icon=":material/restaurant:"),
            st.Page("app_pages/activity_recommendations.py", title="Activities & tours", icon=":material/hiking:"),
        ],
        "Travel Intelligence": [
            st.Page("app_pages/weather_intelligence.py", title="Weather intelligence", icon=":material/wb_sunny:"),
            st.Page("app_pages/transportation_analysis.py", title="Transport & routes", icon=":material/train:"),
        ],
        "My Travels": [
            st.Page("app_pages/saved_trips.py", title="Saved itineraries", icon=":material/bookmark:"),
            st.Page("app_pages/trip_history.py", title="Travel history", icon=":material/history:"),
            st.Page("app_pages/trip_summary.py", title="Trip summary", icon=":material/summarize:"),
        ],
        "Analytics": [
            st.Page("app_pages/analytics.py", title="Platform analytics", icon=":material/bar_chart:"),
        ],
    }

    if is_admin:
        pages["Analytics"].append(
            st.Page(
                "app_pages/admin_dashboard.py",
                title="Admin dashboard",
                icon=":material/admin_panel_settings:",
            )
        )

    return pages


# ── Sidebar Branding & Controls ────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### :material/flight: AI Trip Optimizer")
    st.caption("Intelligent multi-factor travel planning platform")
    st.divider()

    # Auth status
    if st.session_state.get("logged_in"):
        user = st.session_state.get("user", {}) or {}
        st.caption(f":material/person: Signed in as **{user.get('name', 'User')}**")
        if st.button("Sign out", icon=":material/logout:", key="global_logout"):
            from auth.auth import logout
            logout()
            st.rerun()
    else:
        st.caption(":material/person_outline: Guest user")

    st.divider()
    _sidebar_db_status()

# ── Navigation Execution ───────────────────────────────────────────────────────
pages = build_navigation()
page = st.navigation(pages, position="sidebar")
page.run()
"""
AI Trip Decision Optimizer — Main Entry Point
Handles multi-page navigation, theme switching, sidebar branding, DB status indicator, and session state.
"""
import streamlit as st
from auth.auth import init_session
from utils.theme import init_theme, inject_theme_css, render_theme_switcher

st.set_page_config(
    page_title="AI Trip Decision Optimizer",
    page_icon=":material/flight:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize Session State & Theme
init_session()
init_theme()
inject_theme_css()


@st.cache_data(ttl=30)
def _check_db() -> bool:
    """Cached DB health check (refreshes every 30 s)."""
    try:
        from database.connection import db_available
        return db_available()
    except Exception:
        return False


def _sidebar_db_status():
    """Render a live DB status indicator in the sidebar."""
    is_up = _check_db()
    if is_up:
        st.sidebar.success(":material/cloud_done: MySQL Connected", icon=None)
    else:
        st.sidebar.info(":material/cloud_off: Sample Data Mode", icon=None)


def build_navigation():
    logged_in = st.session_state.get("logged_in", False)
    user = st.session_state.get("user", {}) or {}
    is_admin = user.get("role", "") == "ADMIN"

    pages = {
        "Main": [
            st.Page("app_pages/home.py", title="Home Dashboard", icon=":material/home:"),
            st.Page("app_pages/login.py", title="Account & Auth", icon=":material/login:"),
        ],
        "Trip Planning": [
            st.Page("app_pages/trip_planner.py", title="Trip Planner", icon=":material/map:"),
            st.Page("app_pages/budget_optimizer.py", title="Budget Optimizer", icon=":material/calculate:"),
            st.Page("app_pages/ai_itinerary.py", title="AI Itinerary", icon=":material/calendar_month:"),
            st.Page("app_pages/ai_trip_optimizer.py", title="Multi-Factor Optimizer", icon=":material/auto_awesome:"),
        ],
        "Discover & Compare": [
            st.Page("app_pages/destination_discovery.py", title="Destination Discovery", icon=":material/explore:"),
            st.Page("app_pages/ai_recommendations.py", title="AI Recommendations", icon=":material/psychology:"),
            st.Page("app_pages/destination_comparison.py", title="Destination Comparison", icon=":material/compare:"),
        ],
        "Stays & Experiences": [
            st.Page("app_pages/hotel_recommendations.py", title="Hotels & Resorts", icon=":material/hotel:"),
            st.Page("app_pages/restaurant_recommendations.py", title="Restaurants & Dining", icon=":material/restaurant:"),
            st.Page("app_pages/activity_recommendations.py", title="Activities & Tours", icon=":material/hiking:"),
        ],
        "Travel Intelligence": [
            st.Page("app_pages/weather_intelligence.py", title="Weather Intelligence", icon=":material/wb_sunny:"),
            st.Page("app_pages/transportation_analysis.py", title="Transportation & Routes", icon=":material/train:"),
        ],
        "My Travels": [
            st.Page("app_pages/saved_trips.py", title="Saved Itineraries", icon=":material/bookmark:"),
            st.Page("app_pages/trip_history.py", title="Travel History", icon=":material/history:"),
            st.Page("app_pages/trip_summary.py", title="Trip Summary", icon=":material/summarize:"),
        ],
        "Analytics": [
            st.Page("app_pages/analytics.py", title="Platform Analytics", icon=":material/bar_chart:"),
        ],
    }

    if is_admin:
        pages["Analytics"].append(
            st.Page(
                "app_pages/admin_dashboard.py",
                title="Admin Dashboard",
                icon=":material/admin_panel_settings:",
            )
        )

    return pages


# ── Sidebar Branding & Controls ───────────────────────────────────────────────
with st.sidebar:
    st.markdown("## :material/flight: AI Trip Optimizer")
    st.caption("Intelligent Multi-Factor Travel Planning Platform")
    st.divider()

    # Render Theme Switcher Toggle
    render_theme_switcher()
    st.divider()

    # Auth status
    if st.session_state.get("logged_in"):
        user = st.session_state.get("user", {}) or {}
        st.markdown(f"👤 Signed in as **{user.get('name', 'User')}**")
        if st.button("Sign out", icon=":material/logout:", key="global_logout"):
            from auth.auth import logout
            logout()
            st.rerun()
    else:
        st.caption("👤 Guest User")

    # DB status indicator
    _sidebar_db_status()

# ── Navigation Execution ──────────────────────────────────────────────────────
pages = build_navigation()
page = st.navigation(pages, position="sidebar")
page.run()
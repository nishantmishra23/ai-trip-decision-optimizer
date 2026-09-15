"""
AI Trip Decision Optimizer — Main Entry Point
Streamlined navigation, enhanced sidebar typography, and state-of-the-art AI features.
"""
import streamlit as st
from auth.auth import init_session

st.set_page_config(
    page_title="AI Trip Decision Optimizer",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize Session State
init_session()

# ── Sidebar Styling: Larger text, vibrant branding ─────────────────────────────
st.markdown(
    """
    <style>
    /* Make sidebar navigation text noticeably larger and bolder */
    [data-testid="stSidebarNav"] span {
        font-size: 1.08rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.2px;
    }
    [data-testid="stSidebarNav"] a {
        padding-top: 0.55rem !important;
        padding-bottom: 0.55rem !important;
        border-radius: 8px !important;
        transition: all 0.2s ease-in-out;
    }
    [data-testid="stSidebarNav"] a:hover {
        background-color: rgba(99, 102, 241, 0.08) !important;
        transform: translateX(3px);
    }
    [data-testid="stSidebarNavSeparator"] {
        font-weight: 800 !important;
        font-size: 0.92rem !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        color: #6366f1 !important;
        margin-top: 1rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def build_navigation():
    """Build clean, focused navigation for student & traveler planning."""
    pages = {
        "Explore India": [
            st.Page("app_pages/home.py", title="Home Hub", icon=":material/home:"),
            st.Page("app_pages/all_states_explorer.py", title="All 28 States & Places", icon=":material/explore:"),
        ],
        "AI Planner": [
            st.Page("app_pages/trip_planner.py", title="Smart Trip Planner", icon=":material/map:"),
            st.Page("app_pages/ai_itinerary.py", title="AI Itinerary (Gemini)", icon=":material/auto_awesome:"),
            st.Page("app_pages/budget_optimizer.py", title="Budget Optimizer", icon=":material/calculate:"),
        ],
        "Stays & Dining": [
            st.Page("app_pages/hotel_recommendations.py", title="Hotels & Stays", icon=":material/hotel:"),
            st.Page("app_pages/restaurant_recommendations.py", title="Food & Dining", icon=":material/restaurant:"),
            st.Page("app_pages/activity_recommendations.py", title="Activities & Tours", icon=":material/hiking:"),
        ],
        "Live Weather": [
            st.Page("app_pages/weather_intelligence.py", title="Weather Intelligence", icon=":material/wb_sunny:"),
        ],
        "My Account": [
            st.Page("app_pages/saved_trips.py", title="Saved Itineraries", icon=":material/bookmark:"),
            st.Page("app_pages/login.py", title="Account & Login", icon=":material/account_circle:"),
        ],
    }
    return pages


# ── Sidebar Branding ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        """
        <div style="padding: 10px 0 6px 0;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <span style="font-size: 32px;">✈️</span>
                <div>
                    <div style="font-size: 1.35rem; font-weight: 800; line-height: 1.2; background: linear-gradient(135deg, #6366f1, #ec4899); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                        Trip Optimizer
                    </div>
                    <div style="font-size: 0.78rem; font-weight: 600; color: #64748b; letter-spacing: 0.5px;">
                        AI • 28 STATES • WEATHER
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.divider()

    # User Profile / Auth Status
    if st.session_state.get("logged_in"):
        user = st.session_state.get("user", {}) or {}
        st.markdown(f"🎓 **{user.get('name', 'Student')}**")
        st.caption(f"`{user.get('email', '')}`")
        if st.button("Sign out", icon=":material/logout:", key="global_logout", use_container_width=True):
            from auth.auth import logout
            logout()
            st.rerun()
    else:
        st.markdown("👋 **Welcome, Guest!**")
        st.caption("Sign in to save itineraries & get AI perks.")

    st.divider()

# ── Navigation Execution ───────────────────────────────────────────────────────
pages = build_navigation()
page = st.navigation(pages, position="sidebar")
page.run()
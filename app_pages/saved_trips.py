"""
Saved Trips page for AI Trip Decision Optimizer.
"""
import streamlit as st
from auth.auth import init_session
from utils.helpers import format_currency
from utils.theme import inject_theme_css

init_session()
inject_theme_css()

# Hero Header Banner
st.markdown("""
<div class="app-hero-banner">
    <div class="app-hero-title">🔖 Saved Trip Itineraries</div>
    <div class="app-hero-subtitle">Access and manage your saved trip plans and customized travel itineraries</div>
</div>
""", unsafe_allow_html=True)

if not st.session_state.get("logged_in"):
    with st.container(border=True):
        st.info("Please sign in to access your saved trips.", icon=":material/lock:")
        st.page_link("app_pages/login.py", label="Sign In / Register", icon=":material/login:")
    st.stop()

user_id = st.session_state.user_id
trips = []
try:
    from database.queries import get_user_trips
    trips = get_user_trips(user_id)
except Exception:
    pass

if not trips:
    with st.container(border=True):
        st.info("You haven't saved any trips yet! Use the Trip Planner or AI Recommendations to create one.", icon=":material/info:")
        st.page_link("app_pages/trip_planner.py", label="Plan Your First Trip", icon=":material/map:")
else:
    st.markdown(f"### Saved Itineraries ({len(trips)})")
    cols = st.columns(3)
    for idx, t in enumerate(trips):
        dest_name = t.get("destination_name", "Destination")
        start_date = t.get("start_date", "")
        end_date = t.get("end_date", "")
        budget = t.get("total_budget", 0)
        travelers = t.get("travelers", 1)
        
        with cols[idx % 3]:
            with st.container(border=True):
                st.markdown(f"### 📍 {dest_name}")
                st.caption(f":material/calendar_month: {start_date} to {end_date}")
                
                st.metric("Total Budget", format_currency(budget))
                st.caption(f"Travellers: **{travelers}**")
                
                st.page_link("app_pages/trip_summary.py", label="View Full Summary", icon=":material/arrow_forward:")

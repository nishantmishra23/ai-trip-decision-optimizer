"""Home / Dashboard page."""
import streamlit as st
from auth.auth import init_session
from utils.helpers import get_destinations_with_fallback, format_currency, db_status_banner
from recommendation.engine import get_sample_destinations

init_session()
db_status_banner()

user = st.session_state.get("user", {}) or {}
name = user.get("name", "Traveller")

st.title("Welcome back, " + name + "! ✈️", anchor=False)
st.caption("Your AI-powered travel planning hub — find, plan, and optimize your next trip.")

# ── Quick stats ──────────────────────────────────────────────────────────────
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Destinations available", "10+", help="Sample destinations loaded")
with col2:
    st.metric("Average trip budget", "₹45,000", help="Based on 7-day trips")
with col3:
    st.metric("User rating", "4.7 / 5.0", help="Average destination rating")
with col4:
    st.metric("Countries", "3+", help="India, Indonesia, France & more")

st.divider()

# ── Featured destinations ─────────────────────────────────────────────────────
st.subheader(":material/explore: Featured destinations", anchor=False)

dests = get_destinations_with_fallback()[:6]
cols = st.columns(3)
for i, dest in enumerate(dests):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"**{dest['name']}**, {dest['country']}")
            cost = dest.get('average_daily_cost', 0)
            rating = dest.get('rating', 0)
            st.caption(f"₹{cost:,.0f}/day · ⭐ {rating}/5.0")
            desc = (dest.get('description') or '')[:100]
            st.write(desc + "..." if len(dest.get('description', '')) > 100 else desc)

st.divider()

# ── Quick actions ─────────────────────────────────────────────────────────────
st.subheader(":material/bolt: Quick actions", anchor=False)
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.page_link("app_pages/trip_planner.py", label="Plan a trip", icon=":material/map:")
with c2:
    st.page_link("app_pages/ai_recommendations.py", label="Get recommendations", icon=":material/psychology:")
with c3:
    st.page_link("app_pages/budget_optimizer.py", label="Optimize budget", icon=":material/calculate:")
with c4:
    st.page_link("app_pages/destination_comparison.py", label="Compare destinations", icon=":material/compare:")

st.divider()

# ── Auth prompt ───────────────────────────────────────────────────────────────
if not st.session_state.get("logged_in"):
    st.info(
        "**Sign in** to save trips, track history, and get personalized recommendations.",
        icon=":material/lock:",
    )
    c1, c2 = st.columns([1, 5])
    with c1:
        st.page_link("app_pages/login.py", label="Sign in / Register", icon=":material/login:")

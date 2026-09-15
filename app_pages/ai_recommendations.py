"""AI Recommendations page — weighted scoring engine."""
import streamlit as st
import pandas as pd
from recommendation.engine import get_recommendations, SAMPLE_DESTINATIONS
from utils.helpers import format_currency
from utils.theme import inject_theme_css
from auth.auth import init_session

init_session()
inject_theme_css()

# Hero Header Banner
st.markdown("""
<div class="app-hero-banner">
    <div class="app-hero-title">🧠 AI Recommendations Engine</div>
    <div class="app-hero-subtitle">Multi-factor weighted engine evaluating budget fit (30%), activities (25%), season (20%), popularity (15%), and efficiency (10%)</div>
</div>
""", unsafe_allow_html=True)

# ── Form ──────────────────────────────────────────────────────────────────────
with st.container(border=True):
    st.subheader(":material/tune: Recommendation Preferences", anchor=False)
    with st.form("rec_form"):
        col1, col2 = st.columns(2)
        with col1:
            total_budget = st.number_input("Total budget (₹)", min_value=1000, value=50000, step=1000)
            duration_days = st.number_input("Duration (days)", min_value=1, max_value=30, value=5, step=1)
            travel_style = st.selectbox("Travel style", ["Budget", "Mid-range", "Luxury", "Backpacker", "Family"])
        with col2:
            activities = st.multiselect(
                "Interests / activities",
                ["Beach & Water Sports", "Adventure", "Trekking", "Heritage", "Wildlife",
                 "Shopping", "Food & Cuisine", "Yoga & Wellness", "Nightlife", "Photography", "Culture"],
                default=["Heritage", "Food & Cuisine"]
            )
            season = st.selectbox(
                "Travel season",
                ["Summer (Apr-Jun)", "Monsoon (Jul-Sep)", "Winter (Oct-Dec)", "Spring (Jan-Mar)", "Any season"],
                index=4,
            )
            top_n = st.slider("Number of recommendations", min_value=3, max_value=10, value=5)

        submitted = st.form_submit_button("Get AI Recommendations", icon=":material/psychology:", type="primary")

# ── Results ───────────────────────────────────────────────────────────────────
if submitted:
    
    # Save preferences to session state
    st.session_state["rec_prefs"] = {
        "budget": total_budget,
        "duration": duration_days,
        "style": travel_style,
        "activities": activities,
        "season": season
    }
    
    destinations = []
    user_history = []
    try:
        from database.queries import get_all_destinations, get_user_trips, save_recommendation
        dests = get_all_destinations()
        if dests:
            sample_map = {d["name"]: d for d in SAMPLE_DESTINATIONS}
            for d in dests:
                if "category" not in d or not d.get("category"):
                    sample = sample_map.get(d.get("name"), {})
                    d["category"] = sample.get("category", "General")
                    d["season"] = sample.get("season", "Oct-Mar")
            destinations = dests
            
        if st.session_state.get("logged_in") and st.session_state.get("user_id"):
            user_history = get_user_trips(st.session_state["user_id"])
    except Exception:
        pass

    if not destinations:
        destinations = SAMPLE_DESTINATIONS

    with st.spinner("Analyzing multi-factor data..."):
        recs = get_recommendations(
            destinations=destinations,
            budget=total_budget,
            duration_days=int(duration_days),
            preferred_activities=activities,
            preferred_season=season,
            travel_style=travel_style,
            top_n=top_n,
            user_history=user_history
        )

    if not recs:
        st.warning("No recommendations found. Try adjusting your filters.", icon=":material/warning:")
        st.stop()

    st.subheader(f"Top {len(recs)} Recommended Destinations", anchor=False)

    for idx, rec in enumerate(recs):
        dest = rec["destination"]
        score = rec.get("score", 0)
        
        # Save recommendation to DB if logged in
        if st.session_state.get("logged_in") and st.session_state.get("user_id"):
            try:
                save_recommendation(0, dest.get("destination_id", 0), score, ", ".join(rec.get("reasons", [])))
            except:
                pass

        with st.container(border=True):
            col_a, col_b = st.columns([3, 1], gap="medium")
            with col_a:
                st.markdown(f"### #{idx + 1} {dest.get('name')}, {dest.get('country', '')}")
                st.caption(f"**{dest.get('category', '')}** · Best season: {dest.get('season', 'Varies')}")

                subcols = st.columns(4)
                with subcols[0]:
                    st.caption("Budget fit")
                    st.progress(int(rec.get("budget_score", 0)) / 100, text=f"{rec.get('budget_score', 0):.0f}")
                with subcols[1]:
                    st.caption("Activity match")
                    st.progress(int(rec.get("activity_score", 0)) / 100, text=f"{rec.get('activity_score', 0):.0f}")
                with subcols[2]:
                    st.caption("Season")
                    st.progress(int(rec.get("season_score", 0)) / 100, text=f"{rec.get('season_score', 0):.0f}")
                with subcols[3]:
                    st.caption("Popularity")
                    st.progress(int(rec.get("popularity_score", 0)) / 100, text=f"{rec.get('popularity_score', 0):.0f}")

                for reason in rec.get("reasons", []):
                    st.caption(f"• {reason}")

            with col_b:
                if idx == 0:
                    st.metric("BEST MATCH", f"{score:.0f} / 100")
                else:
                    st.metric("Score", f"{score:.0f} / 100")
                est = rec.get("estimated_total", 0)
                st.metric("Est. total", format_currency(est))
                
                if st.button("Plan this trip", key=f"plan_rec_{idx}_{dest.get('name')}", type="primary" if idx == 0 else "secondary"):
                    st.session_state["planner_prefill"] = dest.get("name")
                    st.switch_page("app_pages/trip_planner.py")

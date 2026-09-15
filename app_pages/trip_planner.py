"""
Trip Planner page for AI Trip Decision Optimizer.
"""
import os
import sys

# Ensure project root is in sys.path
_current_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
ROOT_DIR = os.path.dirname(_current_dir) if "app_pages" in _current_dir else _current_dir
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st
from datetime import date, timedelta
import pandas as pd
import plotly.express as px
from auth.auth import init_session
from utils.helpers import get_destinations_with_fallback, format_currency, plotly_theme

init_session()

# ── Hero ───────────────────────────────────────────────────────────────────────
st.title("Interactive trip planner", icon=":material/map:")
st.caption("Customise dates, budget, and travel preferences to generate a detailed itinerary breakdown")

dests = get_destinations_with_fallback()
dest_names = [d["name"] for d in dests]

# ── Parameters Form ────────────────────────────────────────────────────────────
with st.container(border=True):
    st.subheader("Trip parameters", icon=":material/tune:", anchor=False)
    with st.form("trip_planner_form"):
        c1, c2 = st.columns(2, gap="medium")
        with c1:
            origin = st.text_input("Starting location", value="Delhi", placeholder="e.g. Delhi, Mumbai, New York")

            prefill_idx = 0
            if "planner_prefill" in st.session_state and st.session_state["planner_prefill"] in dest_names:
                prefill_idx = dest_names.index(st.session_state["planner_prefill"])

            destination = st.selectbox("Destination", dest_names, index=prefill_idx)
            travelers = st.number_input("Number of travellers", min_value=1, max_value=20, value=2)
            budget = st.number_input("Total budget (₹)", min_value=1000, max_value=1000000, value=35000, step=1000)

        with c2:
            start_date = st.date_input("Departure date", value=date.today() + timedelta(days=7))
            end_date = st.date_input("Return date", value=date.today() + timedelta(days=14))
            travel_style = st.selectbox("Travel style", ["Mid-range", "Budget", "Luxury", "Backpacker", "Family"])
            accommodation = st.selectbox("Accommodation type", ["Mid-range Hotel", "Hostel", "Budget Hotel", "4-Star Resort", "5-Star / Luxury Palace"])

        st.subheader("Preferences & activities", icon=":material/interests:", anchor=False)
        c3, c4 = st.columns(2, gap="medium")
        with c3:
            transport_pref = st.selectbox("Preferred transport", ["Any", "Flight", "Train", "Bus", "Self-drive"])
            food_pref = st.selectbox("Dietary preference", ["Any", "Vegetarian", "Non-vegetarian", "Vegan", "Local cuisine"])
        with c4:
            activities = st.multiselect(
                "Interests & activities",
                ["Beach & Water Sports", "Adventure", "Trekking", "Heritage", "Wildlife", "Shopping",
                 "Food & Cuisine", "Yoga & Wellness", "Nightlife", "Photography", "Culture"],
                default=["Heritage", "Food & Cuisine"],
            )
            season = st.selectbox("Preferred season", ["Winter (Oct-Dec)", "Spring (Jan-Mar)", "Summer (Apr-Jun)", "Monsoon (Jul-Sep)", "Any season"])

        submitted = st.form_submit_button("Generate complete trip plan", icon=":material/rocket_launch:", type="primary")

if submitted:
    duration = max(1, (end_date - start_date).days)
    if end_date <= start_date:
        st.error("Return date must be after departure date.", icon=":material/error:")
        st.stop()

    selected_dest = next((d for d in dests if d["name"] == destination), dests[0])

    # ── Summary Metrics ────────────────────────────────────────────────────────
    st.subheader(f"Trip summary: {origin} → {destination}", icon=":material/flight_takeoff:", anchor=False)

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        with st.container(border=True):
            st.metric("Duration", f"{duration} days")
    with m2:
        with st.container(border=True):
            st.metric("Travellers", str(travelers))
    with m3:
        with st.container(border=True):
            st.metric("Total budget", format_currency(budget))
    with m4:
        with st.container(border=True):
            daily = selected_dest.get("average_daily_cost", selected_dest.get("avg_daily_cost", 2500))
            est_cost = daily * duration * travelers
            delta_val = budget - est_cost
            st.metric(
                "Estimated total cost",
                format_currency(est_cost),
                delta=f"{format_currency(abs(delta_val))} {'under' if delta_val >= 0 else 'over'} budget"
            )

    # ── Budget Breakdown ───────────────────────────────────────────────────────
    st.subheader("Estimated budget breakdown", icon=":material/pie_chart:", anchor=False)
    daily = selected_dest.get("average_daily_cost", selected_dest.get("avg_daily_cost", 2500))
    t_cost = daily * 0.25 * duration * travelers
    h_cost = daily * 0.35 * duration * travelers
    f_cost = daily * 0.20 * duration * travelers
    a_cost = daily * 0.15 * duration * travelers
    m_cost = daily * 0.05 * duration * travelers

    b_df = pd.DataFrame({
        "Category": ["Transport", "Accommodation", "Food & dining", "Activities & sightseeing", "Miscellaneous"],
        "Amount (₹)": [t_cost, h_cost, f_cost, a_cost, m_cost],
    })

    fig = px.pie(
        b_df, names="Category", values="Amount (₹)", hole=0.45,
        color_discrete_sequence=["#4F46E5", "#0EA5E9", "#10B981", "#F59E0B", "#64748B"]
    )
    plotly_theme(fig)
    st.plotly_chart(fig, key="trip_planner_pie_chart")

    # ── AI Alternatives ────────────────────────────────────────────────────────
    st.subheader("AI-recommended alternatives", icon=":material/auto_awesome:", anchor=False)
    try:
        from recommendation.engine import get_recommendations
        recs = get_recommendations(dests, budget, duration, activities, season, travel_style, top_n=3)
    except Exception:
        recs = []

    if recs:
        r_cols = st.columns(len(recs))
        for idx, r in enumerate(recs):
            d = r["destination"]
            with r_cols[idx]:
                with st.container(border=True):
                    st.markdown(f"**Rank #{idx+1}: {d['name']}**")
                    st.caption(f":material/location_on: {d['country']}  •  Match score: **{r['score']:.0f}/100**")
                    for reason in r["reasons"][:2]:
                        st.caption(f"• {reason}")

    # ── Save Trip ──────────────────────────────────────────────────────────────
    st.subheader("Save your trip plan", icon=":material/bookmark:", anchor=False)
    if st.session_state.get("logged_in"):
        if st.button("Save itinerary to My Trips", icon=":material/save:", type="primary"):
            try:
                from database.queries import save_trip, save_trip_preferences
                dest_id = selected_dest.get("destination_id")
                trip_id = save_trip(st.session_state.user_id, dest_id, start_date, end_date, travelers, budget)
                if trip_id:
                    save_trip_preferences(trip_id, travel_style, ", ".join(activities), accommodation, food_pref, season, transport_pref)
                    st.success("Trip successfully saved to your profile!", icon=":material/check_circle:")
                else:
                    st.info("Trip details retained in memory (DB in sample mode).", icon=":material/info:")
            except Exception:
                st.info("Trip details retained in memory (DB in sample mode).", icon=":material/info:")
    else:
        st.info("Sign in to save this itinerary to your user profile.", icon=":material/lock:")
        st.page_link("app_pages/login.py", label="Sign in now", icon=":material/login:")

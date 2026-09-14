"""
Trip Planner page for AI Trip Decision Optimizer.
"""
import streamlit as st
from datetime import date, timedelta
import pandas as pd
import plotly.express as px
from auth.auth import init_session
from utils.helpers import get_destinations_with_fallback, format_currency, plotly_theme
from utils.images import HERO_IMAGES, get_destination_image
from utils.theme import inject_theme_css
from recommendation.engine import get_recommendations

init_session()
inject_theme_css()

st.image(HERO_IMAGES["Planner"], caption=None)
st.title("Interactive Trip Planner", anchor=False)
st.caption("Customise your dates, budget, and travel preferences to generate a detailed itinerary breakdown.")

dests = get_destinations_with_fallback()
dest_names = [d["name"] for d in dests]

with st.container(border=True):
    st.subheader(":material/tune: Trip Parameters", anchor=False)
    with st.form("trip_planner_form"):
        c1, c2 = st.columns(2, gap="medium")
        with c1:
            origin = st.text_input("Starting location", value="Delhi", placeholder="e.g. Delhi, Mumbai, New York")
            destination = st.selectbox("Destination", dest_names)
            travelers = st.number_input("Number of travellers", min_value=1, max_value=20, value=2)
            budget = st.number_input("Total budget (₹)", min_value=1000, max_value=1000000, value=35000, step=1000)

        with c2:
            start_date = st.date_input("Departure date", value=date.today() + timedelta(days=7))
            end_date = st.date_input("Return date", value=date.today() + timedelta(days=14))
            travel_style = st.selectbox("Travel style", ["Mid-range", "Budget", "Luxury", "Backpacker", "Family"])
            accommodation = st.selectbox("Accommodation type", ["Mid-range Hotel", "Hostel", "Budget Hotel", "4-Star Resort", "5-Star / Luxury Palace"])

        st.subheader(":material/interests: Preferences & Activities", anchor=False)
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

        submitted = st.form_submit_button("Generate Complete Trip Plan", icon=":material/rocket_launch:", type="primary")

if submitted:
    duration = max(1, (end_date - start_date).days)
    if end_date <= start_date:
        st.error("Return date must be after departure date.", icon=":material/error:")
        st.stop()

    selected_dest = next((d for d in dests if d["name"] == destination), dests[0])
    img_url = get_destination_image(selected_dest["name"], selected_dest.get("category"))

    st.markdown("---")
    st.subheader(f":material/flight_takeoff: Trip Plan: {origin} ➔ {destination}", anchor=False)

    col_img, col_metrics = st.columns([1, 2], gap="medium")
    with col_img:
        st.image(img_url, caption=f"{selected_dest['name']}, {selected_dest['country']}")

    with col_metrics:
        m1, m2 = st.columns(2)
        with m1:
            with st.container(border=True):
                st.metric("Duration", f"{duration} days")
            with st.container(border=True):
                st.metric("Total Budget", format_currency(budget))
        with m2:
            with st.container(border=True):
                st.metric("Travellers", str(travelers))
            with st.container(border=True):
                daily = selected_dest.get("average_daily_cost", selected_dest.get("avg_daily_cost", 2500))
                est_cost = daily * duration * travelers
                delta_val = budget - est_cost
                st.metric(
                    "Estimated Total Cost", 
                    format_currency(est_cost),
                    delta=f"{format_currency(abs(delta_val))} {'under' if delta_val >= 0 else 'over'} budget"
                )

    # Financial Breakdown
    st.subheader(":material/pie_chart: Estimated Budget Breakdown", anchor=False)
    daily = selected_dest.get("average_daily_cost", selected_dest.get("avg_daily_cost", 2500))
    t_cost = daily * 0.25 * duration * travelers
    h_cost = daily * 0.35 * duration * travelers
    f_cost = daily * 0.20 * duration * travelers
    a_cost = daily * 0.15 * duration * travelers
    m_cost = daily * 0.05 * duration * travelers

    b_df = pd.DataFrame({
        "Category": ["Transport", "Accommodation", "Food & Dining", "Activities & Sightseeing", "Miscellaneous"],
        "Amount (₹)": [t_cost, h_cost, f_cost, a_cost, m_cost],
    })
    
    fig = px.pie(
        b_df, names="Category", values="Amount (₹)", hole=0.45,
        color_discrete_sequence=["#0EA5E9", "#10B981", "#F59E0B", "#8B5CF6", "#64748B"]
    )
    plotly_theme(fig)
    st.plotly_chart(fig)

    # AI Top Recommended Alternatives
    st.subheader(":material/auto_awesome: AI Recommended Alternatives", anchor=False)
    recs = get_recommendations(dests, budget, duration, activities, season, travel_style, top_n=3)
    
    r_cols = st.columns(3)
    for idx, r in enumerate(recs):
        d = r["destination"]
        with r_cols[idx]:
            with st.container(border=True):
                r_img = get_destination_image(d["name"], d.get("category"))
                st.image(r_img, caption=None)
                st.markdown(f"**Rank #{idx+1}: {d['name']}**")
                st.caption(f"{d['country']} • Score: {r['score']}/100")
                for reason in r["reasons"][:2]:
                    st.caption(f"• {reason}")

    # Save trip action
    st.markdown("### :material/bookmark: Save Your Trip Plan")
    if st.session_state.get("logged_in"):
        if st.button("Save this itinerary to My Trips", icon=":material/save:", type="primary"):
            from database.queries import save_trip, save_trip_preferences
            dest_id = selected_dest.get("destination_id")
            trip_id = save_trip(
                st.session_state.user_id, dest_id, start_date, end_date, travelers, budget
            )
            if trip_id:
                save_trip_preferences(trip_id, travel_style, ", ".join(activities),
                                      accommodation, food_pref, season, transport_pref)
                st.success("Trip successfully saved to your profile!", icon=":material/check_circle:")
            else:
                st.info("Trip details retained in memory (DB in sample mode).", icon=":material/info:")
    else:
        st.info("Sign in to save this itinerary to your user profile.", icon=":material/lock:")
        st.page_link("app_pages/login.py", label="Sign In Now", icon=":material/login:")

"""Trip Planner page."""
import streamlit as st
from datetime import date, timedelta
from auth.auth import init_session
from utils.helpers import get_destinations_with_fallback, db_status_banner
from recommendation.engine import get_recommendations

init_session()
db_status_banner()

st.title("Trip planner", icon=":material/map:", anchor=False)
st.caption("Fill in your trip details and get a customised plan instantly.")

dests = get_destinations_with_fallback()
dest_names = [d["name"] for d in dests]

with st.form("trip_planner_form"):
    st.subheader("Basic details", anchor=False)
    c1, c2 = st.columns(2)
    with c1:
        origin = st.text_input("Starting from", placeholder="e.g. Delhi, Mumbai")
        destination = st.selectbox("Destination", dest_names)
        travelers = st.number_input("Number of travellers", min_value=1, max_value=20, value=2)
    with c2:
        start_date = st.date_input("Departure date", value=date.today() + timedelta(days=7))
        end_date = st.date_input("Return date", value=date.today() + timedelta(days=14))
        budget = st.number_input("Total budget (₹)", min_value=1000, max_value=1000000, value=30000, step=1000)

    st.subheader("Preferences", anchor=False)
    c3, c4 = st.columns(2)
    with c3:
        travel_style = st.selectbox("Travel style", ["Budget", "Mid-range", "Luxury", "Backpacker", "Family"])
        accommodation = st.selectbox("Accommodation", ["Any", "Hostel", "Budget Hotel", "Mid-range Hotel", "4-Star", "5-Star / Luxury"])
        transport_pref = st.selectbox("Preferred transport", ["Any", "Flight", "Train", "Bus", "Self-drive"])
    with c4:
        food_pref = st.selectbox("Food preference", ["Any", "Vegetarian", "Non-vegetarian", "Vegan", "Local cuisine", "Continental"])
        activities = st.multiselect(
            "Interests / activities",
            ["Beach & Water Sports", "Adventure", "Trekking", "Heritage", "Wildlife", "Shopping",
             "Food & Cuisine", "Yoga & Wellness", "Nightlife", "Photography", "Culture"],
            default=["Heritage", "Food & Cuisine"],
        )
        season = st.selectbox("Travel season", ["Winter (Oct-Dec)", "Spring (Jan-Mar)", "Summer (Apr-Jun)", "Monsoon (Jul-Sep)", "Any season"])

    submitted = st.form_submit_button("Generate trip plan", icon=":material/send:")

if submitted:
    duration = max(1, (end_date - start_date).days)
    if end_date <= start_date:
        st.error("Return date must be after departure date.", icon=":material/error:")
        st.stop()

    st.divider()
    st.subheader(f"Your trip plan: {origin} → {destination}", anchor=False)

    # Find selected destination data
    selected_dest = next((d for d in dests if d["name"] == destination), dests[0])

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Duration", f"{duration} days")
    with col2:
        st.metric("Travellers", travelers)
    with col3:
        st.metric("Total budget", f"₹{budget:,.0f}")
    with col4:
        est_cost = selected_dest.get("average_daily_cost", 2500) * duration * travelers
        st.metric("Estimated cost", f"₹{est_cost:,.0f}", delta=f"₹{budget - est_cost:,.0f} remaining" if budget >= est_cost else f"₹{est_cost - budget:,.0f} over budget")

    # Budget breakdown
    st.subheader("Budget breakdown", anchor=False)
    daily = selected_dest.get("average_daily_cost", 2500)
    transport_cost = daily * 0.25 * duration * travelers
    hotel_cost = daily * 0.35 * duration * travelers
    food_cost = daily * 0.20 * duration * travelers
    activity_cost = daily * 0.15 * duration * travelers
    misc_cost = daily * 0.05 * duration * travelers

    import plotly.express as px
    import pandas as pd
    breakdown = pd.DataFrame({
        "Category": ["Transport", "Accommodation", "Food", "Activities", "Miscellaneous"],
        "Amount (₹)": [transport_cost, hotel_cost, food_cost, activity_cost, misc_cost],
    })
    fig = px.pie(breakdown, names="Category", values="Amount (₹)",
                 color_discrete_sequence=["#0EA5E9", "#10B981", "#F59E0B", "#8B5CF6", "#64748B"])
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig)

    # Recommendations
    st.subheader("AI recommendation", anchor=False)
    recs = get_recommendations(dests, budget, duration, activities, season, travel_style, top_n=3)
    for r in recs:
        d = r["destination"]
        with st.container(border=True):
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.markdown(f"**{d['name']}**, {d['country']}")
                for reason in r["reasons"]:
                    st.caption(f"• {reason}")
            with col_b:
                score_color = "green" if r["score"] >= 75 else "orange" if r["score"] >= 50 else "red"
                st.metric("Score", f"{r['score']}/100")

    # Save trip
    if st.session_state.get("logged_in"):
        if st.button("Save this trip", icon=":material/bookmark:"):
            from database.queries import save_trip, save_trip_preferences
            selected_d = next((d for d in dests if d["name"] == destination), None)
            dest_id = selected_d.get("destination_id") if selected_d else None
            trip_id = save_trip(
                st.session_state.user_id, dest_id, start_date, end_date, travelers, budget
            )
            if trip_id:
                save_trip_preferences(trip_id, travel_style, ", ".join(activities),
                                      accommodation, food_pref, season, transport_pref)
                st.success("Trip saved!", icon=":material/check_circle:")
            else:
                st.warning("Could not save — database unavailable.", icon=":material/cloud_off:")
    else:
        st.info("Log in to save this trip.", icon=":material/lock:")

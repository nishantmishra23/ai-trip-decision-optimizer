from datetime import date, timedelta

import streamlit as st

from auth.authentication import require_login
from database.destinations import list_destinations
from database.seed import seed_destinations_if_empty
from database.trips import create_trip
from utils.trip_session import set_current_trip
from utils.ui import error_message, page_header, section_title, success_message

require_login()
page_header("🧭 Trip Planner", "Capture dates, budget, destination, and travel preferences.")

inserted, seed_error = seed_destinations_if_empty()
if seed_error:
    error_message(seed_error)
    st.stop()
if inserted:
    st.info("Sample destinations were added so you can start planning immediately.")

destinations, dest_error = list_destinations()
if dest_error:
    error_message(dest_error)
    st.stop()
if not destinations:
    error_message("No destinations are available yet. Ask an administrator to add destinations.")
    st.stop()

destination_labels = {
    f"{row['name']}, {row['country']}": row["destination_id"]
    for row in destinations
}

section_title("Trip details")

with st.form("trip_planner_form"):
    destination_label = st.selectbox("Destination", list(destination_labels.keys()))
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start date", value=date.today())
    with col2:
        end_date = st.date_input("End date", value=date.today() + timedelta(days=4))

    col3, col4 = st.columns(2)
    with col3:
        travelers = st.number_input("Travelers", min_value=1, max_value=20, value=1, step=1)
    with col4:
        total_budget = st.number_input("Total budget (INR)", min_value=1000.0, value=50000.0, step=500.0)

    section_title("Preferences")
    travel_style = st.selectbox(
        "Travel style",
        ["Leisure", "Adventure", "Family", "Romantic", "Business", "Budget"],
    )
    interests = st.multiselect(
        "Interests",
        ["Beaches", "Mountains", "Culture", "Food", "Nightlife", "Shopping", "Nature", "History"],
        default=["Culture", "Food"],
    )
    col5, col6 = st.columns(2)
    with col5:
        accommodation_preference = st.selectbox(
            "Accommodation",
            ["Hotel", "Resort", "Homestay", "Hostel", "Apartment"],
        )
        weather_preference = st.selectbox(
            "Weather",
            ["Warm", "Mild", "Cool", "Any"],
        )
    with col6:
        food_preference = st.selectbox(
            "Food",
            ["Local cuisine", "Vegetarian", "Vegan", "Street food", "Fine dining"],
        )
        transport_preference = st.selectbox(
            "Transport",
            ["Flight", "Train", "Bus", "Self-drive", "Any"],
        )

    submitted = st.form_submit_button("Save trip", use_container_width=True)

if submitted:
    if end_date < start_date:
        error_message("End date must be on or after the start date.")
    elif not interests:
        error_message("Please choose at least one interest.")
    else:
        destination_id = destination_labels[destination_label]
        trip_id, save_error = create_trip(
            user_id=st.session_state.user_id,
            destination_id=destination_id,
            start_date=start_date,
            end_date=end_date,
            travelers=int(travelers),
            total_budget=float(total_budget),
            travel_style=travel_style,
            interests=", ".join(interests),
            accommodation_preference=accommodation_preference,
            food_preference=food_preference,
            weather_preference=weather_preference,
            transport_preference=transport_preference,
        )
        if save_error:
            error_message(save_error)
        else:
            set_current_trip(
                {
                    "trip_id": trip_id,
                    "user_id": st.session_state.user_id,
                    "destination_id": destination_id,
                    "destination_name": destination_label.split(",")[0],
                    "start_date": start_date,
                    "end_date": end_date,
                    "travelers": int(travelers),
                    "total_budget": float(total_budget),
                    "travel_style": travel_style,
                    "interests": ", ".join(interests),
                    "accommodation_preference": accommodation_preference,
                    "food_preference": food_preference,
                    "weather_preference": weather_preference,
                    "transport_preference": transport_preference,
                }
            )
            success_message("Trip saved. It is now your active trip for recommendations and summaries.")
            st.caption(f"Trip ID: {trip_id}")

current = st.session_state.get("current_trip")
if current:
    st.markdown("---")
    section_title("Active trip")
    c1, c2, c3 = st.columns(3)
    c1.metric("Destination", current.get("destination_name", "—"))
    c2.metric("Travelers", current.get("travelers", "—"))
    c3.metric("Budget", f"{current.get('total_budget', 0):,.0f}")

import streamlit as st
import datetime
import random
import plotly.express as px
from recommendation.engine import SAMPLE_DESTINATIONS
from utils.helpers import db_status_banner
from auth.auth import init_session

st.title('AI itinerary', anchor=False)
db_status_banner()
init_session()

ACTIVITIES_BY_DEST = {
    "default": [
        "Visit local museum",
        "City walking tour",
        "Try local cuisine at food market",
        "Relax at a central park",
        "Shopping at main street",
        "Evening boat ride",
        "Attend a cultural show",
        "Visit historical monument"
    ]
}

dest_names = [dest['name'] for dest in SAMPLE_DESTINATIONS] if SAMPLE_DESTINATIONS else ["Goa", "Bali", "Paris", "Tokyo"]

with st.form("itinerary_form"):
    destination = st.selectbox("Destination", dest_names)
    duration = st.number_input("Duration (Days)", min_value=1, max_value=14, value=5)
    travelers = st.number_input("Travelers", min_value=1, max_value=20, value=2)
    start_date = st.date_input("Start Date", datetime.date.today() + datetime.timedelta(days=7))
    travel_style = st.selectbox("Travel Style", ["Budget", "Comfort", "Luxury", "Adventure"])
    
    generate_btn = st.form_submit_button("Generate Itinerary")

if generate_btn:
    st.subheader(f"Your {duration}-day itinerary for {destination}")
    
    total_cost = 0
    daily_costs = []
    
    # Generate itinerary
    for day in range(1, duration + 1):
        st.subheader(f"Day {day} - {(start_date + datetime.timedelta(days=day-1)).strftime('%b %d, %Y')}")
        
        day_cost = 0
        with st.expander(f"Day {day} Schedule", expanded=(day == 1)):
            if day == 1:
                cost = random.randint(20, 100)
                st.write(f"**Morning (10:00 AM - 12:00 PM)**: Arrival & Hotel Check-in - Estimated Cost: ${cost}")
                day_cost += cost
                
                cost = random.randint(10, 50)
                st.write(f"**Afternoon (1:00 PM - 4:00 PM)**: Local Area Walk & Exploration - Estimated Cost: ${cost}")
                day_cost += cost
                
                cost = random.randint(30, 150)
                st.write(f"**Evening (7:00 PM - 9:00 PM)**: Welcome Dinner - Estimated Cost: ${cost}")
                day_cost += cost
            elif day == duration:
                cost = 0
                st.write(f"**Morning (9:00 AM - 11:00 AM)**: Hotel Checkout - Estimated Cost: ${cost}")
                day_cost += cost
                
                cost = random.randint(20, 80)
                st.write(f"**Afternoon (12:00 PM - 3:00 PM)**: Last Minute Shopping & Departure - Estimated Cost: ${cost}")
                day_cost += cost
            else:
                activities = ACTIVITIES_BY_DEST.get(destination, ACTIVITIES_BY_DEST["default"])
                
                cost = random.randint(20, 100)
                st.write(f"**Morning (9:00 AM - 12:00 PM)**: {random.choice(activities)} - Estimated Cost: ${cost}")
                day_cost += cost
                
                cost = random.randint(20, 100)
                st.write(f"**Afternoon (2:00 PM - 5:00 PM)**: {random.choice(activities)} - Estimated Cost: ${cost}")
                day_cost += cost
                
                cost = random.randint(30, 150)
                st.write(f"**Evening (7:00 PM - 10:00 PM)**: {random.choice(activities)} - Estimated Cost: ${cost}")
                day_cost += cost
                
        daily_costs.append(day_cost)
        total_cost += day_cost
        
    st.markdown("---")
    st.subheader("Cost Breakdown")
    st.metric("Total Estimated Cost", f"${total_cost}")
    
    fig = px.bar(
        x=[f"Day {i}" for i in range(1, duration + 1)],
        y=daily_costs,
        labels={"x": "Day", "y": "Cost ($)"},
        title="Daily Cost Distribution"
    )
    st.plotly_chart(fig)
    
    if st.session_state.get('logged_in'):
        if st.button("Save to My Trips"):
            try:
                # Mock call or real DB insert logic could go here
                st.success("Trip saved successfully!")
            except Exception as e:
                st.error("Error saving trip.")
    else:
        st.info("Log in to save this itinerary.")

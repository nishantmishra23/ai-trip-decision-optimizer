import streamlit as st
import pandas as pd
import plotly.express as px
from database.queries import get_user_trips
from auth.auth import init_session
from utils.helpers import db_status_banner, format_currency
from services.weather_service import get_weather
from recommendation.engine import SAMPLE_DESTINATIONS

st.title('Trip summary', anchor=False)
db_status_banner()
init_session()

trip = None

if st.session_state.get('logged_in'):
    try:
        user_trips = get_user_trips(st.session_state.get('user_id', 1))
        if user_trips:
            trip_names = [f"{t.get('destination', 'Unknown')} ({t.get('start_date', 'N/A')})" for t in user_trips]
            selected_trip = st.selectbox("Select a trip", trip_names)
            trip_idx = trip_names.index(selected_trip)
            trip = user_trips[trip_idx]
    except Exception as e:
        st.error("Could not load trips from database.")
        
if not trip:
    # Demo trip
    trip = {
        'destination': 'Goa',
        'country': 'India',
        'start_date': '2023-11-01',
        'end_date': '2023-11-07',
        'duration_days': 7,
        'travelers': 2,
        'budget': 35000,
        'avg_daily_cost': 2000
    }
    st.info("Showing demo trip summary (Goa) because no trips were found.")

# Key details
st.subheader("Key Details")
details_df = pd.DataFrame([{
    'Destination': trip.get('destination', 'N/A'),
    'Country': trip.get('country', 'N/A'),
    'Start': trip.get('start_date', 'N/A'),
    'End': trip.get('end_date', 'N/A'),
    'Duration': f"{trip.get('duration_days', 0)} days",
    'Travelers': trip.get('travelers', 1),
    'Budget': format_currency(trip.get('budget', 0))
}])
st.dataframe(details_df, hide_index=True)

# Budget analysis
st.subheader("Budget Analysis")
budget = trip.get('budget', 0)
est_cost = trip.get('avg_daily_cost', 0) * trip.get('duration_days', 0) * trip.get('travelers', 1)
delta = budget - est_cost

col1, col2, col3 = st.columns(3)
col1.metric("Budget", format_currency(budget))
col2.metric("Estimated Cost", format_currency(est_cost))
col3.metric("Delta", format_currency(delta), delta_color="normal")

# Cost breakdown
st.subheader("Cost Breakdown")
labels = ['Transport', 'Hotel', 'Food', 'Activities', 'Misc']
values = [0.20, 0.35, 0.20, 0.15, 0.10]
fig = px.pie(names=labels, values=values, hole=0.4, title="Estimated Cost Distribution")
st.plotly_chart(fig)

# Checklist
st.subheader("Travel Checklist")
with st.expander("Documents"):
    st.checkbox("Passport/ID")
    st.checkbox("Visa")
    st.checkbox("Travel Insurance")
with st.expander("Bookings"):
    st.checkbox("Flight/Train Tickets")
    st.checkbox("Hotel Confirmations")
    st.checkbox("Activity Vouchers")
with st.expander("Health"):
    st.checkbox("First Aid Kit")
    st.checkbox("Prescription Meds")
    st.checkbox("Sunscreen")
with st.expander("Tech"):
    st.checkbox("Phone & Charger")
    st.checkbox("Power Bank")
    st.checkbox("Universal Adapter")
with st.expander("Clothing"):
    st.checkbox("Comfortable Shoes")
    st.checkbox("Weather-appropriate Clothes")
    st.checkbox("Swimwear")

# Weather
st.subheader("Weather Summary")
try:
    weather = get_weather(trip.get('destination', 'Goa'))
    st.write(f"Current weather in {trip.get('destination', 'Goa')}: {weather}")
except Exception as e:
    st.write("Weather service is temporarily unavailable. Expect typical seasonal weather for this destination.")

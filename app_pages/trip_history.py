import streamlit as st
import pandas as pd
import plotly.express as px
from database.queries import get_user_trips
from auth.auth import init_session
from utils.helpers import db_status_banner, format_currency

st.title('Trip history', anchor=False)
db_status_banner()
init_session()

if not st.session_state.get('logged_in'):
    st.warning("🔒 You are not logged in.")
    st.info("Please log in to view your trip history.")
    st.stop()

try:
    user_trips = get_user_trips(st.session_state.get('user_id', 1))
except Exception as e:
    st.error("Error connecting to database.")
    user_trips = []

if not user_trips:
    st.info("No trip history found. Showing demo data.")
    user_trips = [
        {'destination': 'Paris', 'country': 'France', 'start_date': '2022-05-10', 'end_date': '2022-05-17', 'duration_days': 7, 'travelers': 2, 'budget': 5000},
        {'destination': 'Tokyo', 'country': 'Japan', 'start_date': '2023-10-01', 'end_date': '2023-10-10', 'duration_days': 10, 'travelers': 1, 'budget': 4000}
    ]

# Top stats
total_trips = len(user_trips)
countries_visited = len(set(t.get('country') for t in user_trips if t.get('country')))
total_spend = sum(t.get('budget', 0) for t in user_trips)

col1, col2, col3 = st.columns(3)
col1.metric("Total Trips", total_trips)
col2.metric("Countries Visited", countries_visited)
col3.metric("Total Budgeted Spend", format_currency(total_spend))

# Dataframe
df = pd.DataFrame(user_trips)
display_df = df[['destination', 'country', 'start_date', 'end_date', 'duration_days', 'travelers', 'budget']].rename(
    columns={
        'destination': 'Destination',
        'country': 'Country',
        'start_date': 'Start Date',
        'end_date': 'End Date',
        'duration_days': 'Days',
        'travelers': 'Travelers',
        'budget': 'Budget'
    }
)
st.dataframe(display_df, hide_index=True)

if len(user_trips) > 1:
    st.subheader("Budget by Trip")
    bar_fig = px.bar(display_df, x='Destination', y='Budget', title="Budget by Destination")
    st.plotly_chart(bar_fig)

    st.subheader("Trips by Destination")
    pie_fig = px.pie(display_df, names='Destination', title="Destination Distribution")
    st.plotly_chart(pie_fig)

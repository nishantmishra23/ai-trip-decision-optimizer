import streamlit as st
import datetime
from database.queries import get_user_trips
from auth.auth import init_session
from utils.helpers import db_status_banner, format_currency

st.title('Saved trips', anchor=False)
db_status_banner()
init_session()

if not st.session_state.get('logged_in'):
    st.warning("🔒 You are not logged in.")
    st.info("Please log in to view your saved trips.")
    st.page_link("app.py", label="Go to Home / Login")
    st.stop()

try:
    user_trips = get_user_trips(st.session_state.get('user_id', 1))
except Exception as e:
    st.error("Error connecting to database.")
    user_trips = []

if not user_trips:
    st.info("You haven't saved any trips yet.")
    st.page_link("app_pages/ai_itinerary.py", label="Plan a Trip")
else:
    st.metric("Total Saved Trips", len(user_trips))
    
    for trip in user_trips:
        with st.container(border=True):
            st.markdown(f"**{trip.get('destination')} ({trip.get('country', 'N/A')})**")
            
            start_date = trip.get('start_date')
            end_date = trip.get('end_date')
            duration = trip.get('duration_days', 0)
            travelers = trip.get('travelers', 1)
            budget = format_currency(trip.get('budget', 0))
            
            st.write(f"📅 **Dates:** {start_date} - {end_date}")
            st.write(f"⏱️ **Duration:** {duration} days")
            st.write(f"👥 **Travelers:** {travelers} | 💰 **Budget:** {budget}")
            
            try:
                if isinstance(start_date, str):
                    start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
                else:
                    start_date_obj = start_date
                
                if start_date_obj and start_date_obj > datetime.date.today():
                    st.markdown("🟡 **Status:** Upcoming")
                else:
                    st.markdown("🟢 **Status:** Past")
            except Exception:
                st.markdown("⚪ **Status:** Unknown")

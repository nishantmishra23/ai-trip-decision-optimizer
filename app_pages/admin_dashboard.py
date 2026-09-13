import streamlit as st
import pandas as pd
import os
from database.queries import get_all_users, get_all_destinations, count_users, count_destinations, count_trips, insert_destination
from auth.auth import init_session
from database.connection import db_available
from utils.helpers import db_status_banner

st.title('Admin dashboard', anchor=False)
db_status_banner()
init_session()

if not st.session_state.get('logged_in') or st.session_state.get('user_role') != 'ADMIN':
    st.error('Access denied. Administrator privileges required.')
    st.stop()

# Metrics
try:
    c_users = count_users()
except:
    c_users = 0

try:
    c_dests = count_destinations()
except:
    c_dests = 0
    
try:
    c_trips = count_trips()
except:
    c_trips = 0

db_status_text = 'Online' if db_available() else 'Offline'

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Users", c_users)
col2.metric("Total Destinations", c_dests)
col3.metric("Total Trips", c_trips)
col4.metric("DB Status", db_status_text)

tab1, tab2, tab3 = st.tabs(["Users", "Destinations", "System"])

with tab1:
    st.subheader("User Management")
    try:
        users = get_all_users()
        if users:
            users_df = pd.DataFrame(users)
            if 'id' in users_df.columns:
                users_df = users_df.rename(columns={'id': 'ID', 'name': 'Name', 'email': 'Email', 'role': 'Role', 'created_at': 'Joined'})
            st.dataframe(users_df, hide_index=True)
        else:
            st.info("No users found.")
    except Exception as e:
        st.error("Failed to load users.")

with tab2:
    st.subheader("Destinations Management")
    try:
        destinations = get_all_destinations()
        if destinations:
            dest_df = pd.DataFrame(destinations)
            st.dataframe(dest_df, hide_index=True)
        else:
            st.info("No destinations found.")
    except Exception as e:
        st.error("Failed to load destinations.")
        
    st.markdown("---")
    st.subheader("Add New Destination")
    with st.form("add_dest_form"):
        name = st.text_input("Name")
        country = st.text_input("Country")
        description = st.text_area("Description")
        avg_cost = st.number_input("Avg Daily Cost", min_value=0, value=100)
        popularity = st.slider("Popularity", 1, 10, 5)
        rating = st.slider("Rating", 1.0, 5.0, 4.0, 0.1)
        
        submit = st.form_submit_button("Add Destination")
        if submit:
            try:
                insert_destination(name, country, description, avg_cost, popularity, rating)
                st.success(f"Successfully added destination: {name}")
            except Exception as e:
                st.error(f"Error adding destination: {str(e)}")

with tab3:
    st.subheader("System Status")
    st.markdown("**Environment Variables**")
    env_vars = ['DB_HOST', 'DB_USER', 'DB_NAME', 'DB_PORT', 'WEATHER_API_KEY']
    env_status = []
    
    for var in env_vars:
        val = os.getenv(var)
        status = 'Set' if val else 'Not set'
        env_status.append({'Variable': var, 'Status': status})
        
    st.dataframe(pd.DataFrame(env_status), hide_index=True)
    
    st.markdown("**Python Environment**")
    import sys
    st.write(f"Python Version: {sys.version}")

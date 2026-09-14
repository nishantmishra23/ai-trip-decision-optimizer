"""
Admin Dashboard page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import os
from auth.auth import init_session
from database.connection import db_available
from database.queries import (
    get_all_users,
    get_all_destinations,
    count_users,
    count_destinations,
    count_trips,
    insert_destination,
)
from utils.theme import inject_theme_css

init_session()
inject_theme_css()

# Admin Security Gate
user = st.session_state.get("user", {}) or {}
if not st.session_state.get("logged_in") or user.get("role") != "ADMIN":
    st.error("Access denied. Admin privileges required to view this dashboard.", icon=":material/gpp_bad:")
    st.info("Log in with an Admin account or set user role to ADMIN.", icon=":material/info:")
    st.stop()

st.title(":material/admin_panel_settings: System Administration Dashboard", anchor=False)
st.caption("Control panel for managing database records, reviewing registered accounts, and system status.")

# Platform Metrics
m1, m2, m3, m4 = st.columns(4)

with m1:
    with st.container(border=True):
        st.metric("Total Registered Users", str(count_users()))
with m2:
    with st.container(border=True):
        st.metric("Total Destinations", str(count_destinations()))
with m3:
    with st.container(border=True):
        st.metric("Total Trips Planned", str(count_trips()))
with m4:
    with st.container(border=True):
        status_text = "Online" if db_available() else "Sample Mode"
        st.metric("Database Status", status_text)

tab1, tab2, tab3 = st.tabs(["User Management", "Destination Catalog", "System Health"])

with tab1:
    st.subheader("Registered Users", anchor=False)
    users = get_all_users()
    if users:
        st.dataframe(pd.DataFrame(users))
    else:
        st.info("No registered user records found.")

with tab2:
    st.subheader("Add New Destination Record", anchor=False)
    with st.form("add_dest_form"):
        c1, c2 = st.columns(2)
        with c1:
            d_name = st.text_input("Destination Name")
            d_country = st.text_input("Country")
            d_cost = st.number_input("Average Daily Cost (₹)", min_value=100, max_value=100000, value=3000)
        with c2:
            d_pop = st.slider("Popularity Score (1-10)", 1.0, 10.0, 8.5)
            d_rat = st.slider("Rating (1-5)", 1.0, 5.0, 4.5)
            d_desc = st.text_area("Description")
        
        submitted = st.form_submit_button("Add Destination to DB", icon=":material/add:")
        if submitted:
            if d_name and d_country:
                ok = insert_destination(d_name, d_country, d_desc, d_cost, d_pop, d_rat)
                if ok:
                    st.success(f"Successfully added {d_name}!", icon=":material/check_circle:")
                else:
                    st.error("Failed to add destination to MySQL database.", icon=":material/error:")
            else:
                st.warning("Destination Name and Country are required.", icon=":material/warning:")

    st.subheader("Existing Destination Records", anchor=False)
    dests = get_all_destinations()
    if dests:
        st.dataframe(pd.DataFrame(dests))

with tab3:
    st.subheader("Environment & System Diagnostics", anchor=False)
    env_keys = ["DB_HOST", "DB_USER", "DB_NAME", "DB_PORT", "WEATHER_API_KEY"]
    env_status = [{"Variable": k, "Status": "Configured" if os.getenv(k) else "Not set / Default"} for k in env_keys]
    st.dataframe(pd.DataFrame(env_status))

"""
Admin Dashboard page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import os
from auth.auth import init_session

init_session()

# ── Admin security gate ────────────────────────────────────────────────────────
user = st.session_state.get("user", {}) or {}
if not st.session_state.get("logged_in") or user.get("role") != "ADMIN":
    st.error("Access denied. Admin privileges required to view this dashboard.", icon=":material/gpp_bad:")
    st.info("Log in with an admin account or set user role to ADMIN.", icon=":material/info:")
    st.stop()

# ── Hero ───────────────────────────────────────────────────────────────────────
st.title("System administration dashboard", icon=":material/admin_panel_settings:")
st.caption("Control panel for managing database records, reviewing registered accounts, and system health")

# ── DB functions with graceful fallback ───────────────────────────────────────
def _safe_call(fn, default=None):
    try:
        return fn()
    except Exception:
        return default if default is not None else "N/A"


# ── Platform Metrics ───────────────────────────────────────────────────────────
m1, m2, m3, m4 = st.columns(4)

with m1:
    with st.container(border=True):
        from database.queries import count_users
        st.metric("Total registered users", str(_safe_call(count_users, 0)))
with m2:
    with st.container(border=True):
        from database.queries import count_destinations
        st.metric("Total destinations", str(_safe_call(count_destinations, 0)))
with m3:
    with st.container(border=True):
        from database.queries import count_trips
        st.metric("Total trips planned", str(_safe_call(count_trips, 0)))
with m4:
    with st.container(border=True):
        try:
            from database.connection import db_available
            status_text = "Online" if db_available() else "Sample mode"
        except Exception:
            status_text = "Unavailable"
        st.metric("Database status", status_text)

# ── Tabs ───────────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["User management", "Destination catalog", "System health"])

with tab1:
    st.subheader("Registered users", anchor=False)
    try:
        from database.queries import get_all_users
        users = get_all_users()
        if users:
            st.dataframe(pd.DataFrame(users))
        else:
            st.info("No registered user records found.")
    except Exception:
        st.warning("Could not load users (DB unavailable).", icon=":material/warning:")

with tab2:
    st.subheader("Add new destination record", anchor=False)
    with st.form("add_dest_form"):
        c1, c2 = st.columns(2)
        with c1:
            d_name = st.text_input("Destination name")
            d_country = st.text_input("Country")
            d_cost = st.number_input("Average daily cost (₹)", min_value=100, max_value=100000, value=3000)
        with c2:
            d_pop = st.slider("Popularity score (1–10)", 1.0, 10.0, 8.5)
            d_rat = st.slider("Rating (1–5)", 1.0, 5.0, 4.5)
            d_desc = st.text_area("Description")

        submitted = st.form_submit_button("Add destination to DB", icon=":material/add:")
        if submitted:
            if d_name and d_country:
                try:
                    from database.queries import insert_destination
                    ok = insert_destination(d_name, d_country, d_desc, d_cost, d_pop, d_rat)
                    if ok:
                        st.success(f"Successfully added {d_name}!", icon=":material/check_circle:")
                    else:
                        st.error("Failed to add destination to MySQL database.", icon=":material/error:")
                except Exception as e:
                    st.error(f"Database error: {e}", icon=":material/error:")
            else:
                st.warning("Destination name and country are required.", icon=":material/warning:")

    st.subheader("Existing destination records", anchor=False)
    try:
        from database.queries import get_all_destinations
        dests = get_all_destinations()
        if dests:
            st.dataframe(pd.DataFrame(dests))
    except Exception:
        st.warning("Could not load destinations (DB unavailable).", icon=":material/warning:")

with tab3:
    st.subheader("Environment & system diagnostics", anchor=False)
    env_keys = ["DB_HOST", "DB_USER", "DB_NAME", "DB_PORT", "WEATHER_API_KEY", "GEMINI_API_KEY"]
    env_status = [{"Variable": k, "Status": "Configured ✓" if os.getenv(k) else "Not set / Default"} for k in env_keys]
    st.dataframe(pd.DataFrame(env_status))

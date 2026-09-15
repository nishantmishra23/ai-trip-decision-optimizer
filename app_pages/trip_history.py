"""
Trip History page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from auth.auth import init_session
from utils.helpers import format_currency, plotly_theme

init_session()

# ── Hero ───────────────────────────────────────────────────────────────────────
st.title("Travel history & analytics", icon=":material/history:")
st.caption("Track your travel journey, total expenditure, visited destinations, and historical trip statistics")

if not st.session_state.get("logged_in"):
    with st.container(border=True):
        st.info("Please sign in to view your personal trip history.", icon=":material/lock:")
        st.page_link("app_pages/login.py", label="Sign in / Register", icon=":material/login:")
    st.stop()

user_id = st.session_state.user_id
trips = []
try:
    from database.queries import get_user_trips
    trips = get_user_trips(user_id)
except Exception:
    pass

if not trips:
    st.info("No recorded trip history found in your account.", icon=":material/history_toggle_off:")
else:
    df_trips = pd.DataFrame(trips)

    # ── Stats ──────────────────────────────────────────────────────────────────
    st.subheader("Personal travel statistics", icon=":material/monitoring:", anchor=False)
    m1, m2, m3 = st.columns(3)

    with m1:
        with st.container(border=True):
            st.metric("Total trips", str(len(trips)))
    with m2:
        with st.container(border=True):
            countries = df_trips["country"].nunique() if "country" in df_trips else 1
            st.metric("Countries visited", str(countries))
    with m3:
        with st.container(border=True):
            total_spend = df_trips["total_budget"].sum() if "total_budget" in df_trips else 0
            st.metric("Total travel spend", format_currency(total_spend))

    # ── Table ──────────────────────────────────────────────────────────────────
    st.subheader("Historical itineraries", icon=":material/table_chart:", anchor=False)
    st.dataframe(
        df_trips,
        column_config={
            "total_budget": st.column_config.NumberColumn(format="₹%d"),
        }
    )

    # ── Chart ──────────────────────────────────────────────────────────────────
    st.subheader("Travel spend per trip", icon=":material/bar_chart:", anchor=False)
    fig_spend = px.bar(df_trips, x="destination_name", y="total_budget", color="destination_name", text_auto=True)
    plotly_theme(fig_spend)
    st.plotly_chart(fig_spend, key="history_spend_chart")

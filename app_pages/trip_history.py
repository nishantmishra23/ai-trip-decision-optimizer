"""
Trip History page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from auth.auth import init_session
from utils.helpers import format_currency, plotly_theme
from utils.theme import inject_theme_css

init_session()
inject_theme_css()

st.title(":material/history: Travel History & Analytics", anchor=False)
st.caption("Track your travel journey, total expenditure, visited destinations, and historical trip statistics.")

if not st.session_state.get("logged_in"):
    with st.container(border=True):
        st.info("Please sign in to view your personal trip history.", icon=":material/lock:")
        st.page_link("app_pages/login.py", label="Sign In / Register", icon=":material/login:")
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
    
    # User Stats KPI Cards
    st.subheader(":material/monitoring: Personal Travel Statistics", anchor=False)
    m1, m2, m3 = st.columns(3)
    
    with m1:
        with st.container(border=True):
            st.metric("Total Trips", str(len(trips)))
    with m2:
        with st.container(border=True):
            countries = df_trips["country"].nunique() if "country" in df_trips else 1
            st.metric("Countries Visited", str(countries))
    with m3:
        with st.container(border=True):
            total_spend = df_trips["total_budget"].sum() if "total_budget" in df_trips else 0
            st.metric("Total Travel Spend", format_currency(total_spend))

    # Detailed Table
    st.subheader(":material/table_chart: Historical Itineraries", anchor=False)
    st.dataframe(
        df_trips,
        column_config={
            "total_budget": st.column_config.NumberColumn(format="₹%d"),
        }
    )

    # Charts
    st.subheader(":material/bar_chart: Historical Travel Spend per Trip", anchor=False)
    fig_spend = px.bar(df_trips, x="destination_name", y="total_budget", color="destination_name", text_auto="₹%.0f")
    plotly_theme(fig_spend)
    st.plotly_chart(fig_spend)

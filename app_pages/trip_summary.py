"""
Trip Summary page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from auth.auth import init_session
from utils.helpers import format_currency, plotly_theme
from utils.theme import inject_theme_css
from utils.images import get_destination_image
from services.weather_service import get_weather

init_session()
inject_theme_css()

st.title(":material/summarize: Comprehensive Trip Summary", anchor=False)
st.caption("Complete overview of your upcoming or past trip, including expense breakdown, weather forecast, and packing checklist.")

user = st.session_state.get("user", {}) or {}
user_id = user.get("user_id")

trips = []
if st.session_state.get("logged_in") and user_id:
    try:
        from database.queries import get_user_trips
        trips = get_user_trips(user_id)
    except Exception:
        pass

if trips:
    trip_names = [f"Trip to {t.get('destination_name', 'Destination')} ({t.get('start_date', '')})" for t in trips]
    selected_idx = st.selectbox("Select Trip", range(len(trips)), format_func=lambda x: trip_names[x])
    current_trip = trips[selected_idx]
    dest_name = current_trip.get("destination_name", "Goa")
    budget = float(current_trip.get("total_budget", 35000))
    travelers = current_trip.get("travelers", 2)
else:
    st.info("Showing Demo Trip Summary (Log in and create a trip to see your custom trip summary).", icon=":material/info:")
    dest_name = "Goa"
    budget = 35000
    travelers = 2
    current_trip = {
        "destination_name": "Goa",
        "country": "India",
        "start_date": "2026-10-15",
        "end_date": "2026-10-22",
        "travelers": 2,
        "total_budget": 35000
    }

# Destination Cover Banner
img_url = get_destination_image(dest_name)
st.image(img_url, caption=f"Trip Summary: {dest_name}")

st.subheader(f":material/flight_takeoff: Overview: {dest_name}", anchor=False)
m1, m2, m3, m4 = st.columns(4)

with m1:
    with st.container(border=True):
        st.metric("Destination", dest_name)
with m2:
    with st.container(border=True):
        st.metric("Travellers", str(travelers))
with m3:
    with st.container(border=True):
        st.metric("Total Budget", format_currency(budget))
with m4:
    with st.container(border=True):
        est_cost = 32000
        st.metric("Est. Total Expense", format_currency(est_cost), delta=format_currency(budget - est_cost))

# Financial Breakdown Donut
st.subheader(":material/pie_chart: Expense Distribution Breakdown", anchor=False)
categories = ["Transport", "Accommodation", "Food & Dining", "Activities", "Miscellaneous"]
amounts = [budget * 0.25, budget * 0.35, budget * 0.20, budget * 0.15, budget * 0.05]

df_b = pd.DataFrame({"Category": categories, "Amount (₹)": amounts})
fig_donut = px.pie(df_b, names="Category", values="Amount (₹)", hole=0.5,
                   color_discrete_sequence=["#0EA5E9", "#10B981", "#F59E0B", "#8B5CF6", "#64748B"])
plotly_theme(fig_donut)
st.plotly_chart(fig_donut)

# Weather Forecast & Packing Checklist
c_w, c_c = st.columns(2, gap="medium")

with c_w:
    st.subheader(":material/wb_sunny: Weather Outlook", anchor=False)
    weather = get_weather(dest_name)
    with st.container(border=True):
        st.write(f"• **Expected Temp:** {weather.get('temp', 28)}°C")
        st.write(f"• **Condition:** {weather.get('condition', 'Sunny')}")
        st.write(f"• **Humidity:** {weather.get('humidity', 65)}%")

with c_c:
    st.subheader(":material/checklist: Pre-Trip Checklist", anchor=False)
    with st.expander("📁 Travel Documents", expanded=True):
        st.checkbox("Government ID / Passport", value=True)
        st.checkbox("Flight & Hotel Tickets", value=True)
        st.checkbox("Travel Insurance Copy", value=False)
    with st.expander("🧳 Packing & Wearables"):
        st.checkbox("Weather Appropriate Clothing", value=True)
        st.checkbox("Footwear & Comfort Shoes", value=True)
        st.checkbox("Toiletries & Sunscreen", value=True)

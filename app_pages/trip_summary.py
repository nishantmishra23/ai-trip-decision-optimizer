"""
Trip Summary page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from auth.auth import init_session
from utils.helpers import format_currency, plotly_theme
from utils.theme import inject_theme_css
from services.weather_service import get_weather
from recommendation.engine import score_destination, SAMPLE_DESTINATIONS

init_session()
inject_theme_css()

# Hero Header Banner
st.markdown("""
<div class="app-hero-banner">
    <div class="app-hero-title">📋 Comprehensive Trip Summary</div>
    <div class="app-hero-subtitle">Complete overview of your trip plan, expense breakdown, AI Match Score, and dynamic packing checklist</div>
</div>
""", unsafe_allow_html=True)

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

# Find destination data
dest_dict = {d["name"]: d for d in SAMPLE_DESTINATIONS}
dest_data = dest_dict.get(dest_name, SAMPLE_DESTINATIONS[0])
category = dest_data.get("category", "General")

# Generate Match Score & Reasons
rec_prefs = st.session_state.get("rec_prefs", {
    "budget": budget,
    "duration": 7,
    "activities": ["Sightseeing", "Food"],
    "season": dest_data.get("season", "Any season"),
    "style": "Mid-range"
})

budget_per_day = rec_prefs.get("budget", budget) / max(rec_prefs.get("duration", 7), 1)

match_data = score_destination(
    dest_data, 
    budget_per_day, 
    rec_prefs.get("duration", 7), 
    rec_prefs.get("activities", []), 
    rec_prefs.get("season", "Any season"), 
    rec_prefs.get("style", "Mid-range")
)
match_score = match_data.get("score", 85.0)
reasons = match_data.get("reasons", [])

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
        st.metric("AI Match Score", f"{match_score:.0f}%", delta="Excellent Match" if match_score > 75 else None)

if reasons:
    with st.expander("✨ Why this trip works for you", expanded=True):
        for reason in reasons:
            st.markdown(f"- {reason}")

# Financial Breakdown Donut
st.subheader(":material/pie_chart: Expense Distribution Breakdown", anchor=False)
categories = ["Transport", "Accommodation", "Food & Dining", "Activities", "Miscellaneous"]
amounts = [budget * 0.25, budget * 0.35, budget * 0.20, budget * 0.15, budget * 0.05]

df_b = pd.DataFrame({"Category": categories, "Amount (₹)": amounts})
fig_donut = px.pie(df_b, names="Category", values="Amount (₹)", hole=0.5,
                   color_discrete_sequence=["#0EA5E9", "#10B981", "#F59E0B", "#8B5CF6", "#64748B"])
plotly_theme(fig_donut)
st.plotly_chart(fig_donut, key="summary_donut_chart")

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
    st.subheader(":material/checklist: Dynamic Packing Checklist", anchor=False)
    with st.expander("📁 Travel Documents", expanded=True):
        st.checkbox("Government ID / Passport", value=True)
        st.checkbox("Flight & Hotel Tickets", value=True)
        st.checkbox("Travel Insurance Copy", value=False)
        
    with st.expander(f"🧳 Packing for {category}", expanded=True):
        st.checkbox("Toiletries & Essentials", value=True)
        
        # Dynamic additions based on category
        if category == "Beach":
            st.checkbox("Swimwear & Beach Towel", value=True)
            st.checkbox("Sunscreen (SPF 50+) & Sunglasses", value=True)
            st.checkbox("Flip-flops & Hat", value=True)
        elif category == "Mountains" or "snow" in weather.get("condition", "").lower():
            st.checkbox("Heavy Jackets & Thermals", value=True)
            st.checkbox("Trekking/Hiking Shoes", value=True)
            st.checkbox("Gloves, Beanies & Woollen Socks", value=True)
        elif category == "City" or category == "Heritage":
            st.checkbox("Comfortable Walking Shoes", value=True)
            st.checkbox("Smart Casual Evening Wear", value=True)
            st.checkbox("Power Bank for Photography", value=True)
            
        # Dynamic additions based on weather
        if "rain" in weather.get("condition", "").lower():
            st.checkbox("Umbrella & Raincoat", value=True, key="rain_gear")
            st.checkbox("Waterproof Bag/Cover", value=True, key="wp_bag")

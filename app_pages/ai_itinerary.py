"""
AI Itinerary Generator page for AI Trip Decision Optimizer.
"""
import streamlit as st
from datetime import date, timedelta
import pandas as pd
import plotly.express as px
from recommendation.engine import SAMPLE_DESTINATIONS
from utils.helpers import format_currency, plotly_theme
from utils.theme import inject_theme_css
from utils.images import get_destination_image
from auth.auth import init_session

init_session()
inject_theme_css()

st.title(":material/calendar_month: AI Itinerary Generator", anchor=False)
st.caption("Generate a structured day-by-day travel schedule with morning, afternoon, and evening slots.")

dest_names = [d["name"] for d in SAMPLE_DESTINATIONS]
dest_dict = {d["name"]: d for d in SAMPLE_DESTINATIONS}

with st.container(border=True):
    st.subheader(":material/tune: Itinerary Parameters", anchor=False)
    with st.form("itinerary_form"):
        c1, c2 = st.columns(2, gap="medium")
        with c1:
            destination = st.selectbox("Destination", dest_names)
            duration = st.slider("Trip Duration (Days)", min_value=1, max_value=10, value=4)
            travelers = st.number_input("Number of Travellers", min_value=1, max_value=10, value=2)
        with c2:
            start_date = st.date_input("Start Date", value=date.today() + timedelta(days=7))
            travel_style = st.selectbox("Pace & Style", ["Balanced Explorer", "Action Packed", "Relaxed & Leisure"])
        
        submitted = st.form_submit_button("Generate Day-by-Day Itinerary", icon=":material/auto_awesome:", type="primary")

selected_dest = dest_dict.get(destination, SAMPLE_DESTINATIONS[0])

# Destination Cover Banner
img_url = get_destination_image(destination, selected_dest.get("category"))
st.image(img_url, caption=f"Custom Itinerary for {destination}, {selected_dest.get('country')}")

st.subheader(f":material/timeline: Day-by-Day Schedule: {destination}", anchor=False)

days_data = []
daily_costs = []

sample_activities_pool = [
    ("Morning (09:00 - 12:30)", "Guided City Tour & Heritage Walk", 800),
    ("Afternoon (13:30 - 17:00)", "Local Food Tasting & Market Exploration", 1200),
    ("Evening (18:00 - 21:00)", "Sunset Viewpoint & Fine Dining Dinner", 1500),
]

for day in range(1, duration + 1):
    day_date = start_date + timedelta(days=day-1)
    day_cost = 0
    with st.container(border=True):
        st.markdown(f"### 📍 Day {day}: {day_date.strftime('%A, %b %d')}")
        
        cols = st.columns(3)
        for idx, (slot, title, cost) in enumerate(sample_activities_pool):
            actual_cost = cost * travelers
            day_cost += actual_cost
            with cols[idx]:
                st.markdown(f"**{slot}**")
                st.write(f"• {title}")
                st.caption(f"Est. Cost: **{format_currency(actual_cost)}**")
                
        daily_costs.append({"Day": f"Day {day}", "Estimated Cost (₹)": day_cost})

# Total Cost Summary & Chart
total_trip_cost = sum(d["Estimated Cost (₹)"] for d in daily_costs)
st.markdown(f"### Total Estimated Itinerary Cost: **{format_currency(total_trip_cost)}**")

df_days = pd.DataFrame(daily_costs)
fig_daily = px.bar(df_days, x="Day", y="Estimated Cost (₹)", text_auto="₹%.0f", color="Day")
plotly_theme(fig_daily)
st.plotly_chart(fig_daily)

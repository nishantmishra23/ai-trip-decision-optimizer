"""
Activity Recommendations page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import plotly_theme
from utils.theme import inject_theme_css
from utils.components import render_activity_card

inject_theme_css()

SAMPLE_ACTIVITIES = {
    "Goa": [
        {"name": "Scuba Diving at Grande Island", "category": "Water Sports", "price": 3500, "duration_hrs": 4, "rating": 4.8, "destination_name": "Goa"},
        {"name": "Dudhsagar Waterfalls Trek", "category": "Trekking", "price": 2000, "duration_hrs": 6, "rating": 4.7, "destination_name": "Goa"},
        {"name": "Sunset Cruise on Mandovi River", "category": "Sightseeing", "price": 800, "duration_hrs": 2, "rating": 4.5, "destination_name": "Goa"},
    ],
    "Manali": [
        {"name": "Solang Valley Paragliding", "category": "Adventure", "price": 3000, "duration_hrs": 2, "rating": 4.7, "destination_name": "Manali"},
        {"name": "Beas River White Water Rafting", "category": "Adventure", "price": 1800, "duration_hrs": 3, "rating": 4.6, "destination_name": "Manali"},
        {"name": "Rohtang Pass Snow Scooter", "category": "Adventure", "price": 2500, "duration_hrs": 4, "rating": 4.8, "destination_name": "Manali"},
    ],
    "Jaipur": [
        {"name": "Amber Fort Elephant / Jeep Safari", "category": "Heritage", "price": 1200, "duration_hrs": 3, "rating": 4.7, "destination_name": "Jaipur"},
        {"name": "Hot Air Balloon Ride", "category": "Adventure", "price": 12000, "duration_hrs": 3, "rating": 4.9, "destination_name": "Jaipur"},
    ],
    "Rishikesh": [
        {"name": "Ganges River Rafting (16km)", "category": "Adventure", "price": 1500, "duration_hrs": 4, "rating": 4.8, "destination_name": "Rishikesh"},
        {"name": "Bungee Jumping at Jumpin Heights", "category": "Adventure", "price": 3800, "duration_hrs": 2, "rating": 4.9, "destination_name": "Rishikesh"},
        {"name": "Sunrise Yoga & Meditation", "category": "Yoga & Wellness", "price": 500, "duration_hrs": 2, "rating": 4.7, "destination_name": "Rishikesh"},
    ]
}

def load_activities():
    try:
        from database.queries import get_all_activities
        act = get_all_activities()
        if act:
            return act
    except Exception:
        pass
    all_act = []
    for dest, a_list in SAMPLE_ACTIVITIES.items():
        all_act.extend(a_list)
    return all_act

st.title(":material/hiking: Activities & Experiences", anchor=False)
st.caption("Discover thrilling adventure sports, cultural tours, water sports, and wellness retreats.")

activities = load_activities()

with st.container(border=True):
    st.subheader(":material/filter_list: Filter Activities", anchor=False)
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        dests = ["All Destinations"] + sorted(list(set(a.get("destination_name", "General") for a in activities)))
        selected_dest = st.selectbox("Destination", dests)
    with c2:
        cats = ["All Categories"] + sorted(list(set(a.get("category", "General") for a in activities)))
        selected_cat = st.selectbox("Activity Category", cats)
    with c3:
        max_price = st.slider("Max Activity Price (₹)", min_value=500, max_value=15000, value=10000, step=500)

filtered = activities
if selected_dest != "All Destinations":
    filtered = [a for a in filtered if a.get("destination_name") == selected_dest]
if selected_cat != "All Categories":
    filtered = [a for a in filtered if a.get("category") == selected_cat]
filtered = [a for a in filtered if a.get("price", 0) <= max_price]

st.markdown(f"Showing **{len(filtered)}** activity options")

if not filtered:
    st.info("No activities match your criteria.", icon=":material/search_off:")
else:
    cols = st.columns(3)
    for idx, a in enumerate(filtered):
        with cols[idx % 3]:
            render_activity_card(a)

if filtered:
    st.subheader(":material/bar_chart: Activities Breakdown by Category", anchor=False)
    df_act = pd.DataFrame(filtered)
    fig = px.bar(df_act, x="category", y="price", color="category", text_auto="₹%.0f")
    plotly_theme(fig)
    st.plotly_chart(fig)

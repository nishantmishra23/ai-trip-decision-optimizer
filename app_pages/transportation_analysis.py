"""
Transportation Analysis page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import format_currency, plotly_theme
from utils.theme import inject_theme_css
from utils.images import get_destination_image
from recommendation.engine import SAMPLE_DESTINATIONS

inject_theme_css()

SAMPLE_TRANSPORT = {
    "Goa": [
        {"mode": "Direct Flight", "icon": ":material/flight:", "cost": 5500, "duration_hours": 2.5, "comfort_rating": 4.8},
        {"mode": "Express Train", "icon": ":material/train:", "cost": 1800, "duration_hours": 11.0, "comfort_rating": 4.2},
        {"mode": "Overnight Volvo Bus", "icon": ":material/directions_bus:", "cost": 1400, "duration_hours": 14.0, "comfort_rating": 3.9},
    ],
    "Manali": [
        {"mode": "Flight + Taxi", "icon": ":material/flight:", "cost": 7500, "duration_hours": 4.0, "comfort_rating": 4.5},
        {"mode": "Overnight Sleeper Bus", "icon": ":material/directions_bus:", "cost": 1600, "duration_hours": 12.5, "comfort_rating": 4.1},
        {"mode": "Self-drive SUV", "icon": ":material/directions_car:", "cost": 6000, "duration_hours": 11.0, "comfort_rating": 4.6},
    ],
    "Jaipur": [
        {"mode": "Vande Bharat Express", "icon": ":material/train:", "cost": 1500, "duration_hours": 4.5, "comfort_rating": 4.7},
        {"mode": "Direct Flight", "icon": ":material/flight:", "cost": 3800, "duration_hours": 1.0, "comfort_rating": 4.8},
        {"mode": "Highway Bus", "icon": ":material/directions_bus:", "cost": 800, "duration_hours": 6.0, "comfort_rating": 4.0},
    ],
    "Paris": [
        {"mode": "International Flight", "icon": ":material/flight:", "cost": 45000, "duration_hours": 9.5, "comfort_rating": 4.8},
        {"mode": "TGV High-speed Train", "icon": ":material/train:", "cost": 8500, "duration_hours": 3.0, "comfort_rating": 4.9},
    ]
}

st.title(":material/train: Transportation & Route Analysis", anchor=False)
st.caption("Compare flights, express trains, intercity buses, and self-drive routes by cost, duration, and convenience.")

dest_names = [d["name"] for d in SAMPLE_DESTINATIONS]
selected_dest = st.selectbox("Select Target Destination", dest_names)

# Destination Cover Banner
img_url = get_destination_image(selected_dest)
st.image(img_url, caption=f"Transit Routes to {selected_dest}")

routes = SAMPLE_TRANSPORT.get(selected_dest, [
    {"mode": "Direct Flight", "icon": ":material/flight:", "cost": 6000, "duration_hours": 2.5, "comfort_rating": 4.7},
    {"mode": "Express Train", "icon": ":material/train:", "cost": 2000, "duration_hours": 10.0, "comfort_rating": 4.3},
    {"mode": "Intercity Bus", "icon": ":material/directions_bus:", "cost": 1200, "duration_hours": 12.0, "comfort_rating": 4.0},
])

st.subheader(f":material/alt_route: Transit Mode Options for {selected_dest}", anchor=False)
cols = st.columns(len(routes))

for idx, r in enumerate(routes):
    with cols[idx]:
        with st.container(border=True):
            st.markdown(f"### {r['icon']} {r['mode']}")
            st.metric("Estimated Cost", format_currency(r["cost"]))
            st.metric("Duration", f"{r['duration_hours']} hrs")
            st.caption(f"Comfort Score: **{r['comfort_rating']} / 5.0**")

# Visual Comparison Charts
st.subheader(":material/bar_chart: Transit Cost & Travel Time Comparison", anchor=False)
df_t = pd.DataFrame(routes)

c1, c2 = st.columns(2, gap="medium")
with c1:
    st.markdown("#### Travel Cost by Mode")
    fig_cost = px.bar(df_t, x="mode", y="cost", color="mode", text_auto="₹%.0f")
    plotly_theme(fig_cost)
    st.plotly_chart(fig_cost)

with c2:
    st.markdown("#### Duration by Mode (Hours)")
    fig_dur = px.bar(df_t, x="duration_hours", y="mode", orientation="h", color="mode")
    plotly_theme(fig_dur)
    st.plotly_chart(fig_dur)

with st.expander(":material/lightbulb: Essential Travel & Packing Tips"):
    st.write("• **Flight Bookings:** Book at least 3-4 weeks in advance for optimal fares.")
    st.write("• **Train Tickets:** Tatkal quota opens 24 hours prior to departure for Indian Railways.")
    st.write("• **Luggage:** Ensure baggage complies with airline limits (15kg check-in for domestic flights).")

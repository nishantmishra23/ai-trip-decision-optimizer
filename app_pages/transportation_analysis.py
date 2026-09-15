"""
Transportation Analysis page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import format_currency, plotly_theme
from recommendation.engine import SAMPLE_DESTINATIONS

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
    ],
    "Munnar": [
        {"mode": "Flight to Kochi + Taxi", "icon": ":material/flight:", "cost": 6500, "duration_hours": 4.5, "comfort_rating": 4.6},
        {"mode": "Train to Ernakulam + Scenic Bus", "icon": ":material/train:", "cost": 1600, "duration_hours": 12.0, "comfort_rating": 4.1},
        {"mode": "Intercity AC Sleeper Bus", "icon": ":material/directions_bus:", "cost": 1200, "duration_hours": 14.0, "comfort_rating": 3.9},
    ],
    "Agra": [
        {"mode": "Gatimaan Express (Fast Train)", "icon": ":material/train:", "cost": 900, "duration_hours": 1.7, "comfort_rating": 4.8},
        {"mode": "Yamuna Expressway Cab", "icon": ":material/directions_car:", "cost": 3200, "duration_hours": 3.0, "comfort_rating": 4.5},
        {"mode": "Express Bus", "icon": ":material/directions_bus:", "cost": 450, "duration_hours": 4.0, "comfort_rating": 4.0},
    ],
    "Bali": [
        {"mode": "Connecting Flight (DPS)", "icon": ":material/flight:", "cost": 28000, "duration_hours": 8.0, "comfort_rating": 4.7},
        {"mode": "Island Ferry / Fast Boat", "icon": ":material/directions_boat:", "cost": 1500, "duration_hours": 2.0, "comfort_rating": 4.2},
    ],
    "Rishikesh": [
        {"mode": "Vande Bharat / Jan Shatabdi Train", "icon": ":material/train:", "cost": 850, "duration_hours": 4.5, "comfort_rating": 4.7},
        {"mode": "Flight to Dehradun + Taxi", "icon": ":material/flight:", "cost": 4200, "duration_hours": 2.0, "comfort_rating": 4.6},
        {"mode": "Overnight Volvo Bus", "icon": ":material/directions_bus:", "cost": 750, "duration_hours": 6.0, "comfort_rating": 4.1},
    ],
    "Andaman Islands": [
        {"mode": "Direct Flight to Port Blair", "icon": ":material/flight:", "cost": 11000, "duration_hours": 2.5, "comfort_rating": 4.8},
        {"mode": "Inter-Island Catamaran / Ferry", "icon": ":material/directions_boat:", "cost": 1800, "duration_hours": 2.0, "comfort_rating": 4.5},
    ],
    "Leh-Ladakh": [
        {"mode": "Direct Mountain Flight (IXL)", "icon": ":material/flight:", "cost": 8500, "duration_hours": 1.5, "comfort_rating": 4.7},
        {"mode": "Manali-Leh Highway Expedition (SUV)", "icon": ":material/directions_car:", "cost": 7000, "duration_hours": 16.0, "comfort_rating": 4.5},
    ],
}

# ── Hero ───────────────────────────────────────────────────────────────────────
st.title("Transportation & route analysis", icon=":material/train:")
st.caption("Compare flights, express trains, intercity buses, and self-drive routes by cost, duration, and convenience")

dest_names = [d["name"] for d in SAMPLE_DESTINATIONS]

with st.container(border=True):
    st.subheader("Route selection", icon=":material/tune:", anchor=False)
    selected_dest = st.selectbox("Select target destination", dest_names)

routes = SAMPLE_TRANSPORT.get(selected_dest, [
    {"mode": "Direct Flight", "icon": ":material/flight:", "cost": 6000, "duration_hours": 2.5, "comfort_rating": 4.7},
    {"mode": "Express Train", "icon": ":material/train:", "cost": 2000, "duration_hours": 10.0, "comfort_rating": 4.3},
    {"mode": "Intercity Bus", "icon": ":material/directions_bus:", "cost": 1200, "duration_hours": 12.0, "comfort_rating": 4.0},
])

st.subheader(f"Transit mode options for {selected_dest}", icon=":material/alt_route:", anchor=False)
cols = st.columns(len(routes))

for idx, r in enumerate(routes):
    with cols[idx]:
        with st.container(border=True):
            st.markdown(f"{r['icon']} **{r['mode']}**")
            st.metric("Estimated cost", format_currency(r["cost"]))
            st.metric("Duration", f"{r['duration_hours']} hrs")
            st.caption(f"Comfort score: **{r['comfort_rating']} / 5.0**")

# ── Charts ────────────────────────────────────────────────────────────────────
st.subheader("Cost & duration comparison", icon=":material/bar_chart:", anchor=False)
df_t = pd.DataFrame(routes)

c1, c2 = st.columns(2, gap="medium")
with c1:
    st.markdown("##### Travel cost by mode")
    fig_cost = px.bar(df_t, x="mode", y="cost", color="mode", text_auto=True)
    plotly_theme(fig_cost)
    st.plotly_chart(fig_cost, key="trans_cost_chart")

with c2:
    st.markdown("##### Duration by mode (hours)")
    fig_dur = px.bar(df_t, x="duration_hours", y="mode", orientation="h", color="mode")
    plotly_theme(fig_dur)
    st.plotly_chart(fig_dur, key="trans_dur_chart")

with st.expander("Essential travel tips", icon=":material/lightbulb:"):
    st.write("• **Flight bookings:** Book at least 3–4 weeks in advance for optimal fares.")
    st.write("• **Train tickets:** Tatkal quota opens 24 hours prior to departure for Indian Railways.")
    st.write("• **Luggage:** Ensure baggage complies with airline limits (15 kg check-in for domestic flights).")

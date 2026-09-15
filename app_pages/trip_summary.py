"""
Trip Summary page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from auth.auth import init_session
from utils.helpers import format_currency, plotly_theme
from services.weather_service import get_weather
from recommendation.engine import score_destination, SAMPLE_DESTINATIONS

init_session()

# ── Hero ───────────────────────────────────────────────────────────────────────
st.title("Comprehensive trip summary", icon=":material/summarize:")
st.caption("Complete overview of your trip plan, expense breakdown, AI match score, and dynamic packing checklist")

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
    selected_idx = st.selectbox("Select trip", range(len(trips)), format_func=lambda x: trip_names[x])
    current_trip = trips[selected_idx]
    dest_name = current_trip.get("destination_name", "Goa")
    budget = float(current_trip.get("total_budget", 35000))
    travelers = current_trip.get("travelers", 2)
else:
    st.info("Showing demo trip summary (sign in and create a trip to see your custom summary).", icon=":material/info:")
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

# ── Destination data ───────────────────────────────────────────────────────────
dest_dict = {d["name"]: d for d in SAMPLE_DESTINATIONS}
dest_data = dest_dict.get(dest_name, SAMPLE_DESTINATIONS[0])
category = dest_data.get("category", "General")

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

# ── Overview Metrics ───────────────────────────────────────────────────────────
st.subheader(f"Overview: {dest_name}", icon=":material/flight_takeoff:", anchor=False)
m1, m2, m3, m4 = st.columns(4)

with m1:
    with st.container(border=True):
        st.metric("Destination", dest_name)
with m2:
    with st.container(border=True):
        st.metric("Travellers", str(travelers))
with m3:
    with st.container(border=True):
        st.metric("Total budget", format_currency(budget))
with m4:
    with st.container(border=True):
        st.metric("AI match score", f"{match_score:.0f}%", delta="Excellent match" if match_score > 75 else None)

if reasons:
    with st.expander("Why this trip works for you", icon=":material/auto_awesome:", expanded=True):
        for reason in reasons:
            st.markdown(f"- {reason}")

# ── Budget Breakdown ───────────────────────────────────────────────────────────
st.subheader("Expense distribution", icon=":material/pie_chart:", anchor=False)
categories = ["Transport", "Accommodation", "Food & dining", "Activities", "Miscellaneous"]
amounts = [budget * 0.25, budget * 0.35, budget * 0.20, budget * 0.15, budget * 0.05]

df_b = pd.DataFrame({"Category": categories, "Amount (₹)": amounts})
fig_donut = px.pie(df_b, names="Category", values="Amount (₹)", hole=0.5,
                   color_discrete_sequence=["#4F46E5", "#0EA5E9", "#10B981", "#F59E0B", "#64748B"])
plotly_theme(fig_donut)
st.plotly_chart(fig_donut, key="summary_donut_chart")

# ── Weather & Checklist ────────────────────────────────────────────────────────
c_w, c_c = st.columns(2, gap="medium")

with c_w:
    st.subheader("Weather outlook", icon=":material/wb_sunny:", anchor=False)
    weather = get_weather(dest_name)
    with st.container(border=True):
        st.write(f"• **Expected temp:** {weather.get('temp', 28)}°C")
        st.write(f"• **Condition:** {weather.get('condition', 'Sunny')}")
        st.write(f"• **Humidity:** {weather.get('humidity', 65)}%")

with c_c:
    st.subheader("Packing checklist", icon=":material/checklist:", anchor=False)
    with st.expander("Travel documents", icon=":material/folder:", expanded=True):
        st.checkbox("Government ID / Passport", value=True)
        st.checkbox("Flight & hotel tickets", value=True)
        st.checkbox("Travel insurance copy", value=False)

    with st.expander(f"Packing for {category}", icon=":material/luggage:", expanded=True):
        st.checkbox("Toiletries & essentials", value=True)

        if category == "Beach":
            st.checkbox("Swimwear & beach towel", value=True)
            st.checkbox("Sunscreen (SPF 50+) & sunglasses", value=True)
            st.checkbox("Flip-flops & hat", value=True)
        elif category in ("Mountains", "Adventure"):
            st.checkbox("Heavy jackets & thermals", value=True)
            st.checkbox("Trekking / hiking shoes", value=True)
            st.checkbox("Gloves, beanies & woollen socks", value=True)
        elif category in ("City", "Heritage"):
            st.checkbox("Comfortable walking shoes", value=True)
            st.checkbox("Smart casual evening wear", value=True)
            st.checkbox("Power bank for photography", value=True)

        if "rain" in weather.get("condition", "").lower():
            st.checkbox("Umbrella & raincoat", value=True, key="rain_gear")
            st.checkbox("Waterproof bag / cover", value=True, key="wp_bag")

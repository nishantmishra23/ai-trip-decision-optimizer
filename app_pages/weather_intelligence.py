"""
Weather Intelligence for AI Trip Decision Optimizer.
Real-time climate indicators across all 28 states, OpenWeather API live queries,
and Gemini 3.6 Flash weather-aware packing suggestions.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from services.weather_service import get_weather
from services.llm_service import generate_packing_and_weather_tips, ask_gemini_travel_advisor
from data.india_states_places import ALL_28_STATES
from utils.helpers import plotly_theme

# Page Header
st.title("🌤️ Weather & Climate Intelligence", icon=":material/wb_sunny:")
st.caption("Live climate monitoring, seasonal advice, and Gemini AI packing recommendations for every Indian state.")

# ── Destination / City Selector ────────────────────────────────────────────────
with st.container(border=True):
    col_sel, col_custom = st.columns([2, 1], gap="medium")
    with col_sel:
        state_names = [f"{s['name']} ({s['weather_city']})" for s in ALL_28_STATES]
        chosen = st.selectbox("Choose Indian State & Capital", state_names, index=5) # Goa default
        selected_city = chosen.split("(")[-1].strip(")")
        state_name = chosen.split("(")[0].strip()

    with col_custom:
        custom_city = st.text_input("Or Enter Any City", placeholder="e.g. Manali, Ooty, Varanasi...")
        if custom_city.strip():
            selected_city = custom_city.strip()
            state_name = custom_city.strip()

# Fetch Live Weather
with st.spinner(f"Querying OpenWeatherMap for {selected_city}..."):
    weather_data = get_weather(selected_city)

is_live = weather_data.get("source") == "live"
source_badge = "🟢 Live OpenWeather API" if is_live else "🟡 Curated Regional Climate"

# ── Live Weather Overview ──────────────────────────────────────────────────────
st.subheader(f"Current Climate in {selected_city}", anchor=False)
st.caption(f"Status: **{source_badge}** • Sky: **{weather_data.get('description', 'Clear')}**")

m1, m2, m3, m4 = st.columns(4)
with m1:
    with st.container(border=True):
        st.metric("Temperature", f"{weather_data.get('temp', 25)}°C", delta=f"Feels like {weather_data.get('feels_like', 27)}°C")
with m2:
    with st.container(border=True):
        st.metric("Humidity", f"{weather_data.get('humidity', 60)}%", delta="Moisture level")
with m3:
    with st.container(border=True):
        st.metric("Wind Speed", f"{weather_data.get('wind_speed', 12)} km/h", delta="Air flow")
with m4:
    with st.container(border=True):
        st.metric("Rain Probability", f"{weather_data.get('rain_chance', 10)}%", delta=weather_data.get("condition", "Clear"))

# ── Weather Condition Evaluation ───────────────────────────────────────────────
with st.container(border=True):
    col_status, col_btn = st.columns([3, 1])
    with col_status:
        cond_lower = weather_data.get("condition", "Clear").lower()
        if "rain" in cond_lower or "thunder" in cond_lower:
            st.badge("🌧️ Rain / Monsoon Condition", color="orange")
            st.caption("Carry rain covers, waterproof footwear, and plan indoor cultural activities.")
        elif "snow" in cond_lower:
            st.badge("❄️ Cold / Snow Condition", color="blue")
            st.caption("Thermal layers, woolens, and snow trekking boots are essential.")
        elif "clear" in cond_lower or "sun" in cond_lower:
            st.badge("☀️ Prime Sightseeing Skies", color="green")
            st.caption("Perfect conditions for outdoor walks, monument visits, and photography.")
        else:
            st.badge("🌤️ Pleasant Travel Weather", color="green")
            st.caption("Great conditions for wandering through local streets and scenic spots.")

    with col_btn:
        if st.button("🗺️ Plan AI Trip Here", type="primary", use_container_width=True, icon=":material/flight_takeoff:"):
            st.session_state["itinerary_dest"] = state_name
            st.switch_page("app_pages/ai_itinerary.py")

# ── Gemini AI Weather & Packing Advisor ─────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("🤖 Gemini 3.6 Flash Weather & Packing Advisor", anchor=False)

with st.container(border=True):
    tips = generate_packing_and_weather_tips(selected_city, weather_data)
    col_t1, col_t2 = st.columns(2)
    for idx, tip in enumerate(tips):
        target_col = col_t1 if idx % 2 == 0 else col_t2
        with target_col:
            st.markdown(f"- {tip}")

    st.divider()
    advisor_query = st.text_input(
        f"Ask Gemini about traveling to {selected_city} in current conditions:",
        placeholder="e.g. What are the best sunset viewpoints and student street food spots right now?"
    )
    if st.button("Ask Gemini Advisor", icon=":material/psychology:", type="secondary"):
        if advisor_query.strip():
            with st.spinner("Gemini 3.6 Flash is analyzing..."):
                advice = ask_gemini_travel_advisor(selected_city, advisor_query)
                st.markdown(f"**Gemini Travel Advisor:**\n\n{advice}")

# ── Climate Trends Chart ───────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
st.subheader("📈 Annual Seasonal Trends", anchor=False)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
base_temp = weather_data.get("temp", 25)
temps = [
    base_temp - 6, base_temp - 4, base_temp - 1, base_temp + 4,
    base_temp + 7, base_temp + 5, base_temp + 2, base_temp + 2,
    base_temp + 1, base_temp - 1, base_temp - 4, base_temp - 6
]
rainfall = [10, 8, 15, 30, 70, 190, 260, 220, 140, 50, 20, 10]

df_climate = pd.DataFrame({"Month": months, "Average Temp (°C)": temps, "Rainfall (mm)": rainfall})

c1, c2 = st.columns(2, gap="medium")
with c1:
    st.markdown("##### Temperature Trend (°C)")
    fig_temp = px.line(
        df_climate,
        x="Month",
        y="Average Temp (°C)",
        markers=True,
        line_shape="spline",
        color_discrete_sequence=["#f59e0b"]
    )
    plotly_theme(fig_temp)
    st.plotly_chart(fig_temp, key="w_temp_chart", use_container_width=True)

with c2:
    st.markdown("##### Estimated Monthly Rainfall (mm)")
    fig_rain = px.bar(
        df_climate,
        x="Month",
        y="Rainfall (mm)",
        color_discrete_sequence=["#0ea5e9"]
    )
    plotly_theme(fig_rain)
    st.plotly_chart(fig_rain, key="w_rain_chart", use_container_width=True)

"""
Weather Intelligence page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from services.weather_service import get_weather
from recommendation.engine import SAMPLE_DESTINATIONS
from utils.helpers import plotly_theme
from utils.theme import inject_theme_css

inject_theme_css()

# Hero Header Banner
st.markdown("""
<div class="app-hero-banner">
    <div class="app-hero-title">☀️ Weather Intelligence</div>
    <div class="app-hero-subtitle">Real-time climate indicators, seasonal temperature trends, and best travel times for your chosen destination</div>
</div>
""", unsafe_allow_html=True)

dest_names = [d["name"] for d in SAMPLE_DESTINATIONS]
dest_dict = {d["name"]: d for d in SAMPLE_DESTINATIONS}

with st.container(border=True):
    st.subheader(":material/location_on: Destination Selection", anchor=False)
    dest_name = st.selectbox("Select Destination for Climate Report", dest_names)

selected_dest = dest_dict.get(dest_name, SAMPLE_DESTINATIONS[0])
weather_data = get_weather(dest_name)

st.subheader(f":material/cloud: Live Weather Summary for {dest_name}", anchor=False)
m1, m2, m3, m4 = st.columns(4)

with m1:
    with st.container(border=True):
        st.metric("Temperature", f"{weather_data.get('temp', 28)}°C")
with m2:
    with st.container(border=True):
        st.metric("Feels Like", f"{weather_data.get('feels_like', 30)}°C")
with m3:
    with st.container(border=True):
        st.metric("Humidity", f"{weather_data.get('humidity', 65)}%")
with m4:
    with st.container(border=True):
        st.metric("Wind Speed", f"{weather_data.get('wind_speed', 12)} km/h")

with st.container(border=True):
    c_cond, c_best = st.columns(2)
    with c_cond:
        condition_str = weather_data.get('condition', 'Sunny').lower()
        if 'rain' in condition_str or 'thunder' in condition_str or 'shower' in condition_str:
            suit = ":orange[Fair (Rain expected - indoor activities recommended)]"
        elif 'snow' in condition_str:
            suit = ":blue[Good (Snow expected - pack winter gear)]"
        elif 'clear' in condition_str or 'sun' in condition_str:
            suit = ":green[Excellent (Clear skies)]"
        else:
            suit = ":green[Good]"
            
        st.markdown(f"**Current Condition:** `{weather_data.get('condition', 'Sunny / Clear')}`")
        st.markdown(f"**Travel Suitability:** {suit}")
        
    with c_best:
        st.markdown(f"**Recommended Best Season:** `{selected_dest.get('season', 'Oct-Mar')}`")
        st.caption("Ideal weather for sightseeing, outdoor activities, and pleasant temperatures.")
        
st.markdown("---")
if st.button(f"Plan Trip to {dest_name}", type="primary", icon=":material/flight_takeoff:"):
    st.session_state["planner_prefill"] = dest_name
    st.switch_page("app_pages/trip_planner.py")

# Seasonal Temperature & Rainfall Trends
st.subheader(":material/show_chart: Annual Climate & Precipitation Trends", anchor=False)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

base_temp = weather_data.get("temp", 25)
temps = [base_temp - 5, base_temp - 3, base_temp, base_temp + 4, base_temp + 6, base_temp + 5, base_temp + 3, base_temp + 2, base_temp + 2, base_temp, base_temp - 2, base_temp - 4]
rainfall = [15, 10, 20, 35, 60, 180, 240, 210, 130, 45, 20, 10]

df_climate = pd.DataFrame({"Month": months, "Average Temp (°C)": temps, "Rainfall (mm)": rainfall})

c1, c2 = st.columns(2, gap="medium")
with c1:
    st.markdown("#### Monthly Temperature Trends")
    fig_temp = px.line(df_climate, x="Month", y="Average Temp (°C)", markers=True, line_shape="spline")
    plotly_theme(fig_temp)
    st.plotly_chart(fig_temp, key="weather_temp_chart")

with c2:
    st.markdown("#### Estimated Monthly Rainfall")
    fig_rain = px.bar(df_climate, x="Month", y="Rainfall (mm)", color_discrete_sequence=["#0EA5E9"])
    plotly_theme(fig_rain)
    st.plotly_chart(fig_rain, key="weather_rain_chart")

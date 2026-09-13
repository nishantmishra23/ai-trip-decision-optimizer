import streamlit as st
import plotly.express as px
import pandas as pd
import random

try:
    from services.weather_service import get_weather, STATIC_WEATHER
except ImportError:
    STATIC_WEATHER = {}
    def get_weather(dest): return {"temperature": 25, "feels_like": 27, "humidity": 60, "wind_speed": 10, "condition": "Sunny", "source": "sample"}

try:
    from recommendation.engine import SAMPLE_DESTINATIONS
except ImportError:
    SAMPLE_DESTINATIONS = [
        {"name": "Goa", "avg_daily_cost": 3000},
        {"name": "Manali", "avg_daily_cost": 2500},
        {"name": "Jaipur", "avg_daily_cost": 2800},
        {"name": "Munnar", "avg_daily_cost": 2200},
        {"name": "Agra", "avg_daily_cost": 2000},
        {"name": "Bali", "avg_daily_cost": 4000},
        {"name": "Paris", "avg_daily_cost": 8000},
        {"name": "Rishikesh", "avg_daily_cost": 1500},
        {"name": "Andaman Islands", "avg_daily_cost": 4500},
        {"name": "Leh-Ladakh", "avg_daily_cost": 3500}
    ]

try:
    from utils.helpers import db_status_banner
except ImportError:
    def db_status_banner(): pass

st.title('Weather intelligence', anchor=False)
db_status_banner()

dest_names = [d["name"] for d in SAMPLE_DESTINATIONS]
selected_dest = st.selectbox("Select Destination", dest_names)

weather_data = None
try:
    weather_data = get_weather(selected_dest)
except Exception as e:
    st.error(f"Error fetching weather: {e}")
    weather_data = {"temperature": 25, "feels_like": 27, "humidity": 60, "wind_speed": 10, "condition": "Sunny", "source": "sample"}

if weather_data.get("source") == "sample":
    st.caption("Showing demo weather data. Live API might be down.")

col1, col2, col3, col4 = st.columns(4)
with col1:
    with st.container(border=True):
        st.metric("Temperature", f"{weather_data.get('temperature', '--')} °C")
with col2:
    with st.container(border=True):
        st.metric("Feels like", f"{weather_data.get('feels_like', '--')} °C")
with col3:
    with st.container(border=True):
        st.metric("Humidity", f"{weather_data.get('humidity', '--')} %")
with col4:
    with st.container(border=True):
        st.metric("Wind speed", f"{weather_data.get('wind_speed', '--')} km/h")

st.write("### Current Condition")
cond = weather_data.get('condition', 'Clear')
st.markdown(f"**{cond}**")

# Suitability badge
lower_cond = cond.lower()
if any(x in lower_cond for x in ['clear', 'sunny', 'tropical']):
    suitability = "Excellent"
    color = "green"
elif any(x in lower_cond for x in ['partly', 'overcast', 'hazy', 'cloudy']):
    suitability = "Good"
    color = "blue"
else:
    suitability = "Fair"
    color = "orange"

st.markdown(f"**Suitability:** :{color}[{suitability}]")

with st.container(border=True):
    st.write("### Best time to visit")
    st.write("Depending on your preferences, choose months with optimal weather to make the most of your trip.")

st.divider()
st.subheader("Annual Weather Patterns")
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
base_temp = weather_data.get('temperature', 25)
# Generate realistic seasonal pattern
monthly_temps = []
monthly_rain = []
for i, m in enumerate(months):
    if i in [4, 5, 6]: # May-Jul peak
        monthly_temps.append(base_temp + random.uniform(3, 8))
        monthly_rain.append(random.uniform(50, 200))
    elif i in [11, 0, 1]: # Dec-Feb low
        monthly_temps.append(base_temp - random.uniform(5, 12))
        monthly_rain.append(random.uniform(0, 30))
    else:
        monthly_temps.append(base_temp + random.uniform(-2, 3))
        monthly_rain.append(random.uniform(20, 100))

c1, c2 = st.columns(2)
with c1:
    df_temp = pd.DataFrame({'Month': months, 'Temperature (°C)': monthly_temps})
    fig_temp = px.line(df_temp, x='Month', y='Temperature (°C)', title='Monthly Average Temperature')
    st.plotly_chart(fig_temp)

with c2:
    df_rain = pd.DataFrame({'Month': months, 'Rainfall (mm)': monthly_rain})
    fig_rain = px.bar(df_rain, x='Month', y='Rainfall (mm)', title='Estimated Monthly Rainfall')
    st.plotly_chart(fig_rain)

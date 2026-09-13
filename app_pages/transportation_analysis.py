import streamlit as st
import plotly.express as px
import pandas as pd

try:
    from database.queries import get_transportation_by_destination, get_all_destinations
except ImportError:
    def get_transportation_by_destination(dest_id): return []
    def get_all_destinations(): return []

try:
    from recommendation.engine import SAMPLE_DESTINATIONS
except ImportError:
    SAMPLE_DESTINATIONS = [
        {"name": "Goa", "avg_daily_cost": 3000, "id": 1},
        {"name": "Manali", "avg_daily_cost": 2500, "id": 2},
        {"name": "Jaipur", "avg_daily_cost": 2800, "id": 3},
        {"name": "Munnar", "avg_daily_cost": 2200, "id": 4}
    ]

try:
    from utils.helpers import db_status_banner
except ImportError:
    def db_status_banner(): pass

st.title('Transportation', anchor=False)
db_status_banner()

SAMPLE_TRANSPORT = {
    'Goa': [
        {'transport_type': 'Flight', 'estimated_cost': 5000, 'duration_minutes': 120, 'rating': 4.5},
        {'transport_type': 'Train', 'estimated_cost': 1500, 'duration_minutes': 720, 'rating': 4.0},
        {'transport_type': 'Bus', 'estimated_cost': 1000, 'duration_minutes': 840, 'rating': 3.5}
    ],
    'Manali': [
        {'transport_type': 'Flight (to Kullu)', 'estimated_cost': 8000, 'duration_minutes': 90, 'rating': 4.2},
        {'transport_type': 'Volvo Bus', 'estimated_cost': 1500, 'duration_minutes': 840, 'rating': 4.3},
        {'transport_type': 'Private Taxi', 'estimated_cost': 12000, 'duration_minutes': 720, 'rating': 4.6}
    ],
    'Jaipur': [
        {'transport_type': 'Flight', 'estimated_cost': 3500, 'duration_minutes': 60, 'rating': 4.6},
        {'transport_type': 'Train (Shatabdi)', 'estimated_cost': 800, 'duration_minutes': 240, 'rating': 4.8},
        {'transport_type': 'Bus', 'estimated_cost': 600, 'duration_minutes': 300, 'rating': 4.1}
    ],
    'Munnar': [
        {'transport_type': 'Flight (to Kochi)', 'estimated_cost': 6000, 'duration_minutes': 180, 'rating': 4.4},
        {'transport_type': 'Bus (from Kochi)', 'estimated_cost': 300, 'duration_minutes': 240, 'rating': 3.9},
        {'transport_type': 'Taxi (from Kochi)', 'estimated_cost': 3000, 'duration_minutes': 210, 'rating': 4.7}
    ]
}

dest_names = [d["name"] for d in SAMPLE_DESTINATIONS]
selected_dest = st.selectbox("Select Destination", dest_names)

transport_data = []
try:
    dest_id = next((d.get("id", 1) for d in SAMPLE_DESTINATIONS if d["name"] == selected_dest), 1)
    transport_data = get_transportation_by_destination(dest_id)
except Exception as e:
    st.error(f"Error fetching transport data: {e}")

if not transport_data:
    transport_data = SAMPLE_TRANSPORT.get(selected_dest, SAMPLE_TRANSPORT['Goa'])

st.subheader("Transport Options")
cols = st.columns(3)
for idx, opt in enumerate(transport_data):
    with cols[idx % 3]:
        with st.container(border=True):
            st.write(f"### {opt['transport_type']}")
            st.write(f"**Cost:** ₹{opt['estimated_cost']}")
            h = opt['duration_minutes'] // 60
            m = opt['duration_minutes'] % 60
            st.write(f"**Duration:** {h}h {m}m")
            st.write(f"**Rating:** {opt['rating']} ⭐")

st.divider()
st.subheader("Transportation Analytics")
df = pd.DataFrame(transport_data)
df['duration_hours'] = df['duration_minutes'] / 60

c1, c2 = st.columns(2)
with c1:
    fig_cost = px.bar(df, x='transport_type', y='estimated_cost', title='Cost by Transport Type', labels={'estimated_cost': 'Cost (₹)', 'transport_type': 'Transport Type'})
    st.plotly_chart(fig_cost)
with c2:
    fig_dur = px.bar(df, y='transport_type', x='duration_hours', orientation='h', title='Duration by Transport Type', labels={'duration_hours': 'Duration (Hours)', 'transport_type': 'Transport Type'})
    st.plotly_chart(fig_dur)

with st.expander("Travel Tips"):
    st.write("- **Packing:** Pack light if you're taking flights to save on baggage fees.")
    st.write("- **Booking Advice:** Book trains at least 30 days in advance for confirmed seats.")
    st.write("- **Local Transport:** Use local ride-hailing apps or pre-paid taxis to avoid haggling.")

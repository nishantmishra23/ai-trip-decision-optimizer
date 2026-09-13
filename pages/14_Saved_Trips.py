import pandas as pd
import streamlit as st

from auth.authentication import require_login
from database.trips import list_user_trips
from utils.trip_session import set_current_trip
from utils.ui import error_message, page_header, section_title, success_message

require_login()
page_header("💾 Saved Trips", "Open a previously saved trip and make it the active plan.")

trips, error = list_user_trips(st.session_state.user_id)
if error:
    error_message(error)
    st.stop()

if not trips:
    st.info("You have not saved any trips yet. Create one in Trip Planner.")
    st.stop()

section_title("Your trips")
frame = pd.DataFrame(trips)
for column in ("start_date", "end_date", "created_at"):
    if column in frame.columns:
        frame[column] = frame[column].astype(str)

display_cols = [
    col
    for col in [
        "trip_id",
        "destination_name",
        "country",
        "start_date",
        "end_date",
        "travelers",
        "total_budget",
        "travel_style",
    ]
    if col in frame.columns
]
st.dataframe(frame[display_cols], use_container_width=True, hide_index=True)

labels = {
    f"#{row['trip_id']} · {row.get('destination_name') or 'Undecided'} ({row['start_date']} → {row['end_date']})": row
    for row in trips
}
choice = st.selectbox("Set active trip", list(labels.keys()))
if st.button("Use this trip", use_container_width=True):
    set_current_trip(labels[choice])
    success_message("This trip is now active for the rest of the application.")

current = st.session_state.get("current_trip")
if current:
    st.caption(f"Active trip ID: {current['trip_id']}")

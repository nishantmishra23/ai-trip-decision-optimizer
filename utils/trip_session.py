"""Keep the active trip in Streamlit session_state for later pages."""

import streamlit as st


def set_current_trip(trip):
    st.session_state.current_trip_id = trip["trip_id"]
    st.session_state.current_trip = trip


def get_current_trip():
    return st.session_state.get("current_trip")


def clear_current_trip():
    st.session_state.current_trip_id = None
    st.session_state.current_trip = None

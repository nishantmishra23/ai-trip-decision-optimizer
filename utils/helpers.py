"""
Shared utility functions for AI Trip Decision Optimizer.
"""
import streamlit as st
from recommendation.engine import SAMPLE_DESTINATIONS


def get_destinations_with_fallback():
    """Load destinations from DB; fall back to sample data."""
    try:
        from database.queries import get_all_destinations
        rows = get_all_destinations()
        if rows:
            return rows
    except Exception:
        pass
    return SAMPLE_DESTINATIONS


def format_currency(amount: float) -> str:
    """Format as Indian Rupees."""
    if amount >= 100000:
        return f"₹{amount / 100000:.1f}L"
    if amount >= 1000:
        return f"₹{amount / 1000:.1f}K"
    return f"₹{amount:,.0f}"


def rating_stars(rating: float) -> str:
    """Return star string for a rating out of 5."""
    full = int(rating)
    half = 1 if (rating - full) >= 0.5 else 0
    empty = 5 - full - half
    return "★" * full + "½" * half + "☆" * empty


def no_data_message(message: str = "No data available."):
    st.info(message, icon=":material/info:")


def db_status_banner():
    """Show a soft banner if DB is unavailable."""
    try:
        from database.connection import db_available
        if not db_available():
            st.caption(
                ":material/cloud_off: Running in demo mode — connect MySQL for full functionality."
            )
    except Exception:
        pass

"""
Shared utility functions for AI Trip Decision Optimizer.
"""
import streamlit as st
from recommendation.engine import SAMPLE_DESTINATIONS
from utils.theme import apply_plotly_theme


@st.cache_data(ttl=60)
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
    """Format as Indian Rupees with appropriate scale."""
    try:
        amount = float(amount)
    except (TypeError, ValueError):
        return "₹0"
    if amount >= 100_000:
        return f"₹{amount / 100_000:.1f}L"
    if amount >= 1_000:
        return f"₹{amount / 1_000:.1f}K"
    return f"₹{amount:,.0f}"


def rating_stars(rating: float) -> str:
    """Return star string for a rating out of 5."""
    try:
        rating = float(rating)
    except (TypeError, ValueError):
        return "☆☆☆☆☆"
    full = int(rating)
    half = 1 if (rating - full) >= 0.5 else 0
    empty = 5 - full - half
    return "★" * full + "½" * half + "☆" * empty + f"  {rating:.1f}"


def no_data_message(message: str = "No data available."):
    st.info(message, icon=":material/info:")


def plotly_theme(fig):
    """Apply active Light/Dark theme configuration to any Plotly chart."""
    return apply_plotly_theme(fig)

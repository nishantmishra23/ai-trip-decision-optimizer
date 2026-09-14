"""
Image utilities and mappings for AI Trip Decision Optimizer.
Provides high-resolution travel photography, local caching, and fallback handling.
"""
import os
import urllib.request
import streamlit as st
from typing import Optional

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "images")

# ---------------------------------------------------------------------------
# Unsplash High-Resolution Curated Travel Photography URLs
# ---------------------------------------------------------------------------
DESTINATION_IMAGES = {
    "Goa": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=800&q=80",
    "Manali": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?auto=format&fit=crop&w=800&q=80",
    "Jaipur": "https://images.unsplash.com/photo-1477587458883-47145ed94245?auto=format&fit=crop&w=800&q=80",
    "Munnar": "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?auto=format&fit=crop&w=800&q=80",
    "Agra": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=800&q=80",
    "Bali": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=800&q=80",
    "Paris": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=800&q=80",
    "Rishikesh": "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=800&q=80",
    "Andaman Islands": "https://images.unsplash.com/photo-1589394815804-964ed0be2eb5?auto=format&fit=crop&w=800&q=80",
    "Leh-Ladakh": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=800&q=80",
}

CATEGORY_IMAGES = {
    "Beach": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
    "Mountains": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=800&q=80",
    "Heritage": "https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=800&q=80",
    "Nature": "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=800&q=80",
    "City": "https://images.unsplash.com/photo-1477959858617-67f30ac72604?auto=format&fit=crop&w=800&q=80",
    "Adventure": "https://images.unsplash.com/photo-1522163182402-834f871fd851?auto=format&fit=crop&w=800&q=80",
}

HOTEL_IMAGES = {
    "Resort": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
    "Heritage": "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=800&q=80",
    "Lodge": "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=800&q=80",
    "Villa": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=800&q=80",
    "Default": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=800&q=80",
}

RESTAURANT_IMAGES = {
    "Seafood": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=800&q=80",
    "Indian": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=800&q=80",
    "French": "https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?auto=format&fit=crop&w=800&q=80",
    "Cafe": "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=800&q=80",
    "Default": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=800&q=80",
}

ACTIVITY_IMAGES = {
    "Water": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=800&q=80",
    "Trekking": "https://images.unsplash.com/photo-1551632811-561732d1e306?auto=format&fit=crop&w=800&q=80",
    "Sightseeing": "https://images.unsplash.com/photo-1599661046827-dacff0c0f09a?auto=format&fit=crop&w=800&q=80",
    "Yoga": "https://images.unsplash.com/photo-1545205597-3d9d02c29597?auto=format&fit=crop&w=800&q=80",
    "Default": "https://images.unsplash.com/photo-1522163182402-834f871fd851?auto=format&fit=crop&w=800&q=80",
}

HERO_IMAGES = {
    "Home": "https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=1200&q=80",
    "Login": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&w=1200&q=80",
    "Planner": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1200&q=80",
}

FALLBACK_IMAGE = "https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=800&q=80"


def get_destination_image(name: str, category: Optional[str] = None) -> str:
    """Return image URL for a given destination name or category."""
    if not name:
        return FALLBACK_IMAGE
    for k, url in DESTINATION_IMAGES.items():
        if k.lower() in name.lower() or name.lower() in k.lower():
            return url
    if category and category in CATEGORY_IMAGES:
        return CATEGORY_IMAGES[category]
    return FALLBACK_IMAGE


def get_hotel_image(hotel_name: str = "", hotel_type: str = "") -> str:
    """Return hotel image URL based on type or name."""
    text = (hotel_name + " " + hotel_type).lower()
    if "resort" in text or "villa" in text:
        return HOTEL_IMAGES["Resort"]
    elif "palace" in text or "heritage" in text:
        return HOTEL_IMAGES["Heritage"]
    elif "lodge" in text or "cottage" in text:
        return HOTEL_IMAGES["Lodge"]
    return HOTEL_IMAGES["Default"]


def get_restaurant_image(restaurant_name: str = "", cuisine: str = "") -> str:
    """Return restaurant image URL based on cuisine or name."""
    text = (restaurant_name + " " + cuisine).lower()
    if "sea" in text or "fish" in text:
        return RESTAURANT_IMAGES["Seafood"]
    elif "indian" in text or "thali" in text or "mughal" in text:
        return RESTAURANT_IMAGES["Indian"]
    elif "french" in text or "fine" in text:
        return RESTAURANT_IMAGES["French"]
    elif "cafe" in text or "coffee" in text or "bakery" in text:
        return RESTAURANT_IMAGES["Cafe"]
    return RESTAURANT_IMAGES["Default"]


def get_activity_image(activity_name: str = "", category: str = "") -> str:
    """Return activity image URL based on category or name."""
    text = (activity_name + " " + category).lower()
    if "water" in text or "scuba" in text or "surf" in text or "beach" in text:
        return ACTIVITY_IMAGES["Water"]
    elif "trek" in text or "hike" in text or "climb" in text:
        return ACTIVITY_IMAGES["Trekking"]
    elif "yoga" in text or "wellness" in text or "spa" in text:
        return ACTIVITY_IMAGES["Yoga"]
    elif "fort" in text or "tour" in text or "sight" in text or "temple" in text:
        return ACTIVITY_IMAGES["Sightseeing"]
    return ACTIVITY_IMAGES["Default"]


def render_card_image(url: str, caption: str = ""):
    """Render a clean image element inside Streamlit cards."""
    st.image(url, caption=caption if caption else None)

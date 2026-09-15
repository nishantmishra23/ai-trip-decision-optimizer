"""
Reusable UI Card Components for AI Trip Decision Optimizer.
Image-free: uses Material icons and structured text layouts for all cards.
"""
import streamlit as st
from utils.helpers import format_currency, rating_stars


# Category icon mapping
CATEGORY_ICONS = {
    "Beach": ":material/beach_access:",
    "Mountains": ":material/landscape:",
    "Heritage": ":material/account_balance:",
    "Nature": ":material/park:",
    "City": ":material/location_city:",
    "Adventure": ":material/hiking:",
    "Wildlife": ":material/nature:",
    "Default": ":material/explore:",
}

HOTEL_TYPE_ICONS = {
    "Resort": ":material/villa:",
    "Heritage": ":material/account_balance:",
    "Lodge": ":material/cabin:",
    "Hostel": ":material/weekend:",
    "Luxury": ":material/star:",
    "Default": ":material/hotel:",
}


def _category_icon(category: str) -> str:
    for k, v in CATEGORY_ICONS.items():
        if k.lower() in (category or "").lower():
            return v
    return CATEGORY_ICONS["Default"]


def render_hero_banner(title: str, subtitle: str, icon: str = ":material/flight_takeoff:"):
    """Render a native-styled hero section with title, icon, and subtitle."""
    st.title(title, icon=icon)
    st.caption(subtitle)


def render_destination_card(dest: dict, show_details: bool = True):
    """Render a standardized destination card with ratings, cost, and tags."""
    name = dest.get("name", "Destination")
    country = dest.get("country", "")
    category = dest.get("category", "Travel")
    cost = dest.get("average_daily_cost", dest.get("avg_daily_cost", 0))
    rating = dest.get("rating", 4.5)
    popularity = dest.get("popularity_score", 8.5)
    desc = dest.get("description", "")
    icon = _category_icon(category)

    with st.container(border=True):
        st.markdown(f"{icon} **{name}**")
        st.caption(f":material/location_on: {country}  •  **{category}**")

        col_cost, col_rate = st.columns(2)
        with col_cost:
            st.metric("Daily cost", format_currency(cost))
        with col_rate:
            st.metric("Rating", f"{rating:.1f} ★")

        if desc:
            short_desc = desc[:100] + "…" if len(desc) > 100 else desc
            st.caption(short_desc)

        if show_details:
            with st.expander("Destination details", icon=":material/info:"):
                st.write(f"**Popularity index:** {popularity} / 10")
                st.write(f"**Best season:** {dest.get('season', 'Oct–Mar')}")
                if desc:
                    st.write(f"**Overview:** {desc}")

        if st.button("Plan this trip", key=f"comp_plan_{name}", type="primary", icon=":material/map:"):
            st.session_state["planner_prefill"] = name
            st.switch_page("app_pages/trip_planner.py")


def render_hotel_card(hotel: dict):
    """Render a hotel accommodation card."""
    name = hotel.get("name", "Hotel Stay")
    dest_name = hotel.get("destination_name", "Destination")
    h_type = hotel.get("hotel_type", "Hotel")
    price = hotel.get("price_per_night", 0)
    rating = hotel.get("rating", 4.5)
    icon = HOTEL_TYPE_ICONS.get(h_type, HOTEL_TYPE_ICONS["Default"])

    with st.container(border=True):
        st.markdown(f"{icon} **{name}**")
        st.caption(f":material/location_on: {dest_name}  •  {h_type}")

        c_p, c_r = st.columns(2)
        with c_p:
            st.metric("Per night", format_currency(price))
        with c_r:
            st.metric("Rating", f"{rating:.1f} ★")

        st.page_link("app_pages/trip_planner.py", label="Select in planner", icon=":material/bookmark:")


def render_restaurant_card(restaurant: dict):
    """Render a restaurant dining card."""
    name = restaurant.get("name", "Restaurant")
    dest_name = restaurant.get("destination_name", "Destination")
    cuisine = restaurant.get("cuisine", "Local cuisine")
    cost = restaurant.get("average_cost", 0)
    rating = restaurant.get("rating", 4.5)

    with st.container(border=True):
        st.markdown(f":material/restaurant: **{name}**")
        st.caption(f":material/location_on: {dest_name}  •  {cuisine}")

        c_p, c_r = st.columns(2)
        with c_p:
            st.metric("Avg meal", format_currency(cost))
        with c_r:
            st.metric("Rating", f"{rating:.1f} ★")


def render_activity_card(activity: dict):
    """Render an activity / tour card."""
    name = activity.get("name", "Activity")
    dest_name = activity.get("destination_name", "Destination")
    category = activity.get("category", "Tour")
    price = activity.get("price", 0)
    duration = activity.get("duration_hrs", 2)
    rating = activity.get("rating", 4.5)

    with st.container(border=True):
        st.markdown(f":material/hiking: **{name}**")
        st.caption(f":material/location_on: {dest_name}  •  {category}  •  {duration} hrs")

        c_p, c_r = st.columns(2)
        with c_p:
            st.metric("Price", format_currency(price))
        with c_r:
            st.metric("Rating", f"{rating:.1f} ★")

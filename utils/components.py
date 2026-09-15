"""
Reusable Premium UI Card Components for AI Trip Decision Optimizer.
Provides structured destination, hotel, restaurant, activity, and KPI cards with hover transitions and theme integration.
"""
import streamlit as st
from utils.helpers import format_currency, rating_stars
from utils.images import get_destination_image, get_hotel_image, get_restaurant_image, get_activity_image


def render_hero_banner(title: str, subtitle: str, badge: str = "AI-POWERED PLATFORM"):
    """Render a gradient hero banner section."""
    st.markdown(f"""
    <div class="app-hero-banner">
        <div class="app-hero-title">{title}</div>
        <div class="app-hero-subtitle">{subtitle}</div>
    </div>
    """, unsafe_allow_html=True)


def render_destination_card(dest: dict, show_details: bool = True):
    """Render a standardized destination card with ratings, cost, and tags."""
    name = dest.get("name", "Destination")
    country = dest.get("country", "")
    category = dest.get("category", "Travel")
    cost = dest.get("average_daily_cost", dest.get("avg_daily_cost", 0))
    rating = dest.get("rating", 4.5)
    popularity = dest.get("popularity_score", 8.5)
    desc = dest.get("description", "")

    with st.container(border=True):
        st.markdown(f"### 📍 {name}")
        st.caption(f"{country} • **{category}**")

        col_cost, col_rate = st.columns(2)
        with col_cost:
            st.markdown(f"**Cost:** {format_currency(cost)}/day")
        with col_rate:
            st.markdown(f"**Rating:** {rating_stars(rating)}")

        if desc:
            short_desc = desc[:90] + "..." if len(desc) > 90 else desc
            st.write(short_desc)

        if show_details:
            with st.expander("Explore Destination Specs"):
                st.write(f"• **Popularity Index:** {popularity} / 10")
                st.write(f"• **Best Season:** {dest.get('season', 'Oct-Mar')}")
                st.write(f"• **Overview:** {desc}")
                
        # Connect Journey: Plan Trip Button
        if st.button("Plan this trip", key=f"comp_plan_{name}", type="primary"):
            st.session_state["planner_prefill"] = name
            st.switch_page("app_pages/trip_planner.py")


def render_hotel_card(hotel: dict):
    """Render a standardized hotel accommodation card."""
    name = hotel.get("name", "Hotel Stay")
    dest_name = hotel.get("destination_name", "Destination")
    h_type = hotel.get("hotel_type", "Hotel")
    price = hotel.get("price_per_night", 0)
    rating = hotel.get("rating", 4.5)

    with st.container(border=True):
        st.markdown(f"### 🏨 {name}")
        st.caption(f":material/location_on: {dest_name} • **{h_type}**")

        c_p, c_r = st.columns(2)
        with c_p:
            st.metric("Per Night", format_currency(price))
        with c_r:
            st.markdown(f"**Rating:**\n{rating_stars(rating)}")

        st.page_link("app_pages/trip_planner.py", label="Select in Planner", icon=":material/bookmark:")


def render_restaurant_card(restaurant: dict):
    """Render a standardized restaurant dining card."""
    name = restaurant.get("name", "Restaurant")
    dest_name = restaurant.get("destination_name", "Destination")
    cuisine = restaurant.get("cuisine", "Local Cuisine")
    cost = restaurant.get("average_cost", 0)
    rating = restaurant.get("rating", 4.5)

    with st.container(border=True):
        st.markdown(f"### 🍽️ {name}")
        st.caption(f":material/location_on: {dest_name} • **{cuisine}**")

        c_p, c_r = st.columns(2)
        with c_p:
            st.metric("Avg Meal", format_currency(cost))
        with c_r:
            st.markdown(f"**Rating:**\n{rating_stars(rating)}")


def render_activity_card(activity: dict):
    """Render a standardized activity tour card."""
    name = activity.get("name", "Activity")
    dest_name = activity.get("destination_name", "Destination")
    category = activity.get("category", "Tour")
    price = activity.get("price", 0)
    duration = activity.get("duration_hrs", 2)
    rating = activity.get("rating", 4.5)

    with st.container(border=True):
        st.markdown(f"### 🎯 {name}")
        st.caption(f":material/location_on: {dest_name} • **{category}**")

        c_p, c_r = st.columns(2)
        with c_p:
            st.metric("Price", format_currency(price))
            st.caption(f"Duration: {duration} hrs")
        with c_r:
            st.markdown(f"**Rating:**\n{rating_stars(rating)}")

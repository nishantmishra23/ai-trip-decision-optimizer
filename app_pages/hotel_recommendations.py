"""
Hotel Recommendations page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import format_currency, plotly_theme
from utils.theme import inject_theme_css
from utils.components import render_hotel_card

inject_theme_css()

SAMPLE_HOTELS = {
    "Goa": [
        {"name": "Taj Exotica Resort & Spa", "price_per_night": 14000, "rating": 4.8, "hotel_type": "Luxury Resort", "destination_name": "Goa"},
        {"name": "Hard Rock Hotel Goa", "price_per_night": 6500, "rating": 4.5, "hotel_type": "Boutique Hotel", "destination_name": "Goa"},
        {"name": "Goa Marriott Resort & Spa", "price_per_night": 11000, "rating": 4.7, "hotel_type": "Luxury Resort", "destination_name": "Goa"},
        {"name": "Zostel Goa", "price_per_night": 1200, "rating": 4.3, "hotel_type": "Hostel / Budget", "destination_name": "Goa"},
    ],
    "Manali": [
        {"name": "The Himalayan Resort", "price_per_night": 8500, "rating": 4.7, "hotel_type": "Luxury Resort", "destination_name": "Manali"},
        {"name": "Span Resort & Spa", "price_per_night": 12500, "rating": 4.8, "hotel_type": "Luxury Resort", "destination_name": "Manali"},
        {"name": "Snow Valley Resorts", "price_per_night": 3500, "rating": 4.4, "hotel_type": "Mid-range Hotel", "destination_name": "Manali"},
    ],
    "Jaipur": [
        {"name": "Rambagh Palace", "price_per_night": 28000, "rating": 4.9, "hotel_type": "Heritage Palace", "destination_name": "Jaipur"},
        {"name": "Fairmont Jaipur", "price_per_night": 15000, "rating": 4.7, "hotel_type": "Luxury Resort", "destination_name": "Jaipur"},
        {"name": "Umaid Bhawan Heritage Hotel", "price_per_night": 4500, "rating": 4.5, "hotel_type": "Heritage Hotel", "destination_name": "Jaipur"},
    ],
    "Bali": [
        {"name": "Mulung Sanctuary Resort", "price_per_night": 9500, "rating": 4.8, "hotel_type": "Eco Lodge", "destination_name": "Bali"},
        {"name": "Ubud Tropical Villa", "price_per_night": 6000, "rating": 4.6, "hotel_type": "Beach Villa", "destination_name": "Bali"},
        {"name": "Seminyak Beach Resort", "price_per_night": 12000, "rating": 4.7, "hotel_type": "Luxury Resort", "destination_name": "Bali"},
    ],
    "Paris": [
        {"name": "Le Meurice", "price_per_night": 35000, "rating": 4.9, "hotel_type": "Luxury Hotel", "destination_name": "Paris"},
        {"name": "Hotel Plaza Athénée", "price_per_night": 42000, "rating": 4.9, "hotel_type": "Luxury Hotel", "destination_name": "Paris"},
        {"name": "CitizenM Paris Gare de Lyon", "price_per_night": 12000, "rating": 4.5, "hotel_type": "Boutique Hotel", "destination_name": "Paris"},
    ]
}

def load_hotels():
    try:
        from database.queries import get_all_hotels
        h = get_all_hotels()
        if h:
            return h
    except Exception:
        pass
    all_h = []
    for dest, h_list in SAMPLE_HOTELS.items():
        all_h.extend(h_list)
    return all_h

st.title(":material/hotel: Hotel & Accommodations", anchor=False)
st.caption("Find verified resorts, luxury stays, boutique hotels, and budget stays tailored to your destination.")

hotels = load_hotels()

with st.container(border=True):
    st.subheader(":material/filter_list: Filter Stays", anchor=False)
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        dests = ["All Destinations"] + sorted(list(set(h.get("destination_name", "General") for h in hotels)))
        selected_dest = st.selectbox("Destination", dests)
    with c2:
        types = ["All Types"] + sorted(list(set(h.get("hotel_type", "Standard") for h in hotels)))
        selected_type = st.selectbox("Property Type", types)
    with c3:
        max_price = st.slider("Max Price / Night (₹)", min_value=1000, max_value=50000, value=30000, step=1000)

filtered = hotels
if selected_dest != "All Destinations":
    filtered = [h for h in filtered if h.get("destination_name") == selected_dest]
if selected_type != "All Types":
    filtered = [h for h in filtered if h.get("hotel_type") == selected_type]
filtered = [h for h in filtered if h.get("price_per_night", 0) <= max_price]

st.markdown(f"Showing **{len(filtered)}** property options")

if not filtered:
    st.info("No hotels match your filters.", icon=":material/search_off:")
else:
    cols = st.columns(3)
    for idx, h in enumerate(filtered):
        with cols[idx % 3]:
            render_hotel_card(h)

# Price Distribution Chart
if filtered:
    st.subheader(":material/bar_chart: Average Price by Property Type", anchor=False)
    df_h = pd.DataFrame(filtered)
    avg_df = df_h.groupby("hotel_type")["price_per_night"].mean().reset_index()
    fig = px.bar(avg_df, x="hotel_type", y="price_per_night", color="hotel_type", text_auto="₹%.0f")
    plotly_theme(fig)
    st.plotly_chart(fig)

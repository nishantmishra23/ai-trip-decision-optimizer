import streamlit as st
import plotly.express as px
from database.queries import get_all_hotels
from utils.helpers import rating_stars

st.title('Hotels', anchor=False)

SAMPLE_HOTELS = {
    "Goa": [
        {"name": "Taj Exotica", "price_per_night": 15000, "rating": 4.8, "hotel_type": "Luxury"},
        {"name": "Baga Beach Resort", "price_per_night": 5000, "rating": 4.2, "hotel_type": "Mid-range"},
        {"name": "Hostel Crowd", "price_per_night": 800, "rating": 4.0, "hotel_type": "Budget"}
    ],
    "Manali": [
        {"name": "Span Resort", "price_per_night": 12000, "rating": 4.7, "hotel_type": "Luxury"},
        {"name": "Snow Valley Resorts", "price_per_night": 4500, "rating": 4.3, "hotel_type": "Mid-range"},
        {"name": "Zostel Manali", "price_per_night": 600, "rating": 4.5, "hotel_type": "Budget"}
    ],
    "Jaipur": [
        {"name": "Rambagh Palace", "price_per_night": 25000, "rating": 4.9, "hotel_type": "Luxury"},
        {"name": "Trident Jaipur", "price_per_night": 8000, "rating": 4.6, "hotel_type": "Mid-range"},
        {"name": "Moustache Hostel", "price_per_night": 500, "rating": 4.4, "hotel_type": "Budget"}
    ]
}
# Fallback flat list
sample_hotels_flat = []
for dest, hotels in SAMPLE_HOTELS.items():
    for h in hotels:
        h_copy = h.copy()
        h_copy['destination_name'] = dest
        sample_hotels_flat.append(h_copy)

hotels_data = []
try:
    data = get_all_hotels()
    if data:
        hotels_data = data
    else:
        hotels_data = sample_hotels_flat
except Exception:
    hotels_data = sample_hotels_flat

destinations = sorted(list(set([h.get("destination_name", "") for h in hotels_data])))
destinations.insert(0, "All")

col1, col2, col3, col4 = st.columns(4)
with col1:
    selected_dest = st.selectbox("Destination", destinations)
with col2:
    max_price = st.slider("Max Price / Night", 500, 30000, 30000, 500)
with col3:
    min_rating = st.slider("Min Rating", 3.0, 5.0, 3.0, 0.1)
with col4:
    hotel_types = list(set([h.get("hotel_type", "Unknown") for h in hotels_data]))
    selected_types = st.multiselect("Hotel Type", hotel_types)

sort_by = st.selectbox("Sort by", ["Rating", "Price asc", "Price desc"])

filtered_hotels = []
for h in hotels_data:
    if selected_dest != "All" and h.get("destination_name") != selected_dest:
        continue
    if h.get("price_per_night", 0) > max_price:
        continue
    if h.get("rating", 0) < min_rating:
        continue
    if selected_types and h.get("hotel_type") not in selected_types:
        continue
    filtered_hotels.append(h)

if sort_by == "Rating":
    filtered_hotels.sort(key=lambda x: x.get("rating", 0), reverse=True)
elif sort_by == "Price asc":
    filtered_hotels.sort(key=lambda x: x.get("price_per_night", 0))
elif sort_by == "Price desc":
    filtered_hotels.sort(key=lambda x: x.get("price_per_night", 0), reverse=True)

st.write(f"Showing {len(filtered_hotels)} results")

cols = st.columns(3)
for i, h in enumerate(filtered_hotels):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"**{h.get('name')}**")
            st.caption(f"{h.get('destination_name')} | {h.get('hotel_type')}")
            
            # Use rating_stars if possible, fallback to simple text
            try:
                st.write(rating_stars(h.get('rating', 0)))
            except Exception:
                st.write(f"Rating: {h.get('rating', 0)}/5.0")
                
            st.write(f"₹{h.get('price_per_night', 0)} per night")

if filtered_hotels:
    import pandas as pd
    df = pd.DataFrame(filtered_hotels)
    avg_price = df.groupby('hotel_type')['price_per_night'].mean().reset_index()
    fig = px.bar(avg_price, x='hotel_type', y='price_per_night', title="Average Price per Hotel Type")
    st.plotly_chart(fig)

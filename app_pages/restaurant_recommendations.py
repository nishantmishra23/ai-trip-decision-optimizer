"""
Restaurant Recommendations page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import plotly_theme
from utils.theme import inject_theme_css
from utils.components import render_restaurant_card

inject_theme_css()

SAMPLE_RESTAURANTS = {
    "Goa": [
        {"name": "Thalassa", "cuisine": "Greek & Mediterranean", "average_cost": 2500, "rating": 4.7, "destination_name": "Goa"},
        {"name": "Fisherman's Wharf", "cuisine": "Seafood & Goan", "average_cost": 1800, "rating": 4.6, "destination_name": "Goa"},
        {"name": "Brittos Beach Shack", "cuisine": "Seafood & Drinks", "average_cost": 1200, "rating": 4.4, "destination_name": "Goa"},
    ],
    "Manali": [
        {"name": "Johnson's Cafe", "cuisine": "Trout & Italian", "average_cost": 1200, "rating": 4.6, "destination_name": "Manali"},
        {"name": "Cafe 1947", "cuisine": "Continental & Italian", "average_cost": 900, "rating": 4.5, "destination_name": "Manali"},
    ],
    "Jaipur": [
        {"name": "1135 AD", "cuisine": "Royal Mughlai & North Indian", "average_cost": 3500, "rating": 4.8, "destination_name": "Jaipur"},
        {"name": "Laxmi Mishthan Bhandar (LMB)", "cuisine": "Rajasthani Thali", "average_cost": 700, "rating": 4.5, "destination_name": "Jaipur"},
        {"name": "Chokhi Dhani Village", "cuisine": "Traditional Rajasthani", "average_cost": 1500, "rating": 4.6, "destination_name": "Jaipur"},
    ],
    "Paris": [
        {"name": "Le Jules Verne", "cuisine": "French Fine Dining", "average_cost": 18000, "rating": 4.9, "destination_name": "Paris"},
        {"name": "Bouillon Chartier", "cuisine": "Traditional French", "average_cost": 2500, "rating": 4.4, "destination_name": "Paris"},
    ]
}

def load_restaurants():
    try:
        from database.queries import get_all_restaurants
        r = get_all_restaurants()
        if r:
            return r
    except Exception:
        pass
    all_r = []
    for dest, r_list in SAMPLE_RESTAURANTS.items():
        all_r.extend(r_list)
    return all_r

st.title(":material/restaurant: Restaurants & Culinary Experiences", anchor=False)
st.caption("Explore fine dining, local food shacks, traditional thalis, and iconic cafes across travel destinations.")

restaurants = load_restaurants()

with st.container(border=True):
    st.subheader(":material/filter_list: Filter Restaurants", anchor=False)
    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        dests = ["All Destinations"] + sorted(list(set(r.get("destination_name", "General") for r in restaurants)))
        selected_dest = st.selectbox("Destination", dests)
    with c2:
        cuisines = ["All Cuisines"] + sorted(list(set(r.get("cuisine", "Local") for r in restaurants)))
        selected_cuisine = st.selectbox("Cuisine Type", cuisines)
    with c3:
        max_cost = st.slider("Max Avg Meal Cost (₹)", min_value=500, max_value=20000, value=10000, step=500)

filtered = restaurants
if selected_dest != "All Destinations":
    filtered = [r for r in filtered if r.get("destination_name") == selected_dest]
if selected_cuisine != "All Cuisines":
    filtered = [r for r in filtered if r.get("cuisine") == selected_cuisine]
filtered = [r for r in filtered if r.get("average_cost", 0) <= max_cost]

st.markdown(f"Showing **{len(filtered)}** restaurant options")

if not filtered:
    st.info("No restaurants match your filters.", icon=":material/search_off:")
else:
    cols = st.columns(3)
    for idx, r in enumerate(filtered):
        with cols[idx % 3]:
            render_restaurant_card(r)

if filtered:
    st.subheader(":material/pie_chart: Restaurants by Cuisine Type", anchor=False)
    df_r = pd.DataFrame(filtered)
    fig = px.pie(df_r, names="cuisine", hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel)
    plotly_theme(fig)
    st.plotly_chart(fig)

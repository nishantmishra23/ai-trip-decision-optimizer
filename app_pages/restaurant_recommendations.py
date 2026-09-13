import streamlit as st
import plotly.express as px
from database.queries import get_all_restaurants
from utils.helpers import rating_stars

st.title('Restaurants', anchor=False)

SAMPLE_RESTAURANTS = {
    "Goa": [
        {"name": "Britto's", "cuisine": "Seafood", "average_cost": 1200, "rating": 4.5},
        {"name": "Gunpowder", "cuisine": "South Indian", "average_cost": 1500, "rating": 4.6},
        {"name": "Cafe Alchemia", "cuisine": "Cafe", "average_cost": 800, "rating": 4.3}
    ],
    "Manali": [
        {"name": "Johnson's Cafe", "cuisine": "Continental", "average_cost": 1000, "rating": 4.4},
        {"name": "Renaissance", "cuisine": "Italian", "average_cost": 1200, "rating": 4.7},
        {"name": "The Corner House", "cuisine": "North Indian", "average_cost": 800, "rating": 4.2}
    ],
    "Jaipur": [
        {"name": "Chokhi Dhani", "cuisine": "Rajasthani", "average_cost": 1800, "rating": 4.8},
        {"name": "Laxmi Misthan Bhandar", "cuisine": "Desserts", "average_cost": 500, "rating": 4.5},
        {"name": "Tapri Central", "cuisine": "Cafe", "average_cost": 900, "rating": 4.6}
    ]
}

sample_restaurants_flat = []
for dest, rests in SAMPLE_RESTAURANTS.items():
    for r in rests:
        r_copy = r.copy()
        r_copy['destination_name'] = dest
        sample_restaurants_flat.append(r_copy)

rests_data = []
try:
    data = get_all_restaurants()
    if data:
        rests_data = data
    else:
        rests_data = sample_restaurants_flat
except Exception:
    rests_data = sample_restaurants_flat

destinations = sorted(list(set([r.get("destination_name", "") for r in rests_data])))
destinations.insert(0, "All")

col1, col2, col3, col4 = st.columns(4)
with col1:
    selected_dest = st.selectbox("Destination", destinations)
with col2:
    cuisines = list(set([r.get("cuisine", "Unknown") for r in rests_data]))
    selected_cuisines = st.multiselect("Cuisine", cuisines)
with col3:
    max_cost = st.slider("Max Average Cost", 200, 5000, 5000, 100)
with col4:
    min_rating = st.slider("Min Rating", 3.0, 5.0, 3.0, 0.1)

sort_by = st.selectbox("Sort by", ["Rating", "Price"])

filtered_rests = []
for r in rests_data:
    if selected_dest != "All" and r.get("destination_name") != selected_dest:
        continue
    if selected_cuisines and r.get("cuisine") not in selected_cuisines:
        continue
    if r.get("average_cost", 0) > max_cost:
        continue
    if r.get("rating", 0) < min_rating:
        continue
    filtered_rests.append(r)

if sort_by == "Rating":
    filtered_rests.sort(key=lambda x: x.get("rating", 0), reverse=True)
elif sort_by == "Price":
    filtered_rests.sort(key=lambda x: x.get("average_cost", 0))

st.write(f"Showing {len(filtered_rests)} results")

cols = st.columns(3)
for i, r in enumerate(filtered_rests):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"**{r.get('name')}**")
            st.caption(f"{r.get('destination_name')} | {r.get('cuisine')}")
            
            try:
                st.write(rating_stars(r.get('rating', 0)))
            except Exception:
                st.write(f"Rating: {r.get('rating', 0)}/5.0")
                
            st.write(f"₹{r.get('average_cost', 0)} avg cost")

if filtered_rests:
    import pandas as pd
    df = pd.DataFrame(filtered_rests)
    cuisine_counts = df['cuisine'].value_counts().reset_index()
    cuisine_counts.columns = ['cuisine', 'count']
    fig = px.bar(cuisine_counts, x='cuisine', y='count', title="Restaurants by Cuisine")
    st.plotly_chart(fig)

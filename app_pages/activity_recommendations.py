import streamlit as st
import plotly.express as px
import pandas as pd

try:
    from database.queries import get_all_activities
except ImportError:
    def get_all_activities(): return []

try:
    from utils.helpers import db_status_banner, rating_stars
except ImportError:
    def db_status_banner(): pass
    def rating_stars(rating): return "⭐" * int(round(rating))

st.title('Activities', anchor=False)
db_status_banner()

SAMPLE_ACTIVITIES = {
    'Goa': [
        {'name': 'Scuba Diving', 'category': 'Water Sports', 'price': 3000, 'duration_hrs': 4, 'rating': 4.8, 'destination_name': 'Goa'},
        {'name': 'Parasailing', 'category': 'Water Sports', 'price': 1500, 'duration_hrs': 1, 'rating': 4.5, 'destination_name': 'Goa'},
        {'name': 'Dudhsagar Trek', 'category': 'Adventure', 'price': 2000, 'duration_hrs': 8, 'rating': 4.6, 'destination_name': 'Goa'},
        {'name': 'Spice Plantation Tour', 'category': 'Heritage', 'price': 800, 'duration_hrs': 3, 'rating': 4.3, 'destination_name': 'Goa'}
    ],
    'Manali': [
        {'name': 'Rohtang Pass Tour', 'category': 'Nature', 'price': 2500, 'duration_hrs': 6, 'rating': 4.7, 'destination_name': 'Manali'},
        {'name': 'Solang Valley Paragliding', 'category': 'Adventure', 'price': 3000, 'duration_hrs': 2, 'rating': 4.9, 'destination_name': 'Manali'},
        {'name': 'River Rafting', 'category': 'Water Sports', 'price': 1500, 'duration_hrs': 3, 'rating': 4.6, 'destination_name': 'Manali'},
        {'name': 'Hadimba Temple Visit', 'category': 'Cultural', 'price': 0, 'duration_hrs': 1, 'rating': 4.4, 'destination_name': 'Manali'}
    ],
    'Jaipur': [
        {'name': 'Amber Fort Elephant Ride', 'category': 'Heritage', 'price': 1100, 'duration_hrs': 3, 'rating': 4.7, 'destination_name': 'Jaipur'},
        {'name': 'Hot Air Balloon Ride', 'category': 'Adventure', 'price': 12000, 'duration_hrs': 3, 'rating': 4.9, 'destination_name': 'Jaipur'},
        {'name': 'Chokhi Dhani Dinner', 'category': 'Cultural', 'price': 900, 'duration_hrs': 4, 'rating': 4.5, 'destination_name': 'Jaipur'},
        {'name': 'City Palace Tour', 'category': 'Heritage', 'price': 500, 'duration_hrs': 2, 'rating': 4.6, 'destination_name': 'Jaipur'}
    ],
    'Munnar': [
        {'name': 'Tea Estate Walk', 'category': 'Nature', 'price': 500, 'duration_hrs': 3, 'rating': 4.8, 'destination_name': 'Munnar'},
        {'name': 'Eravikulam Safari', 'category': 'Nature', 'price': 120, 'duration_hrs': 4, 'rating': 4.7, 'destination_name': 'Munnar'},
        {'name': 'Echo Point Boating', 'category': 'Water Sports', 'price': 300, 'duration_hrs': 1, 'rating': 4.2, 'destination_name': 'Munnar'},
        {'name': 'Ayurvedic Spa', 'category': 'Wellness', 'price': 2000, 'duration_hrs': 2, 'rating': 4.6, 'destination_name': 'Munnar'}
    ],
    'Agra': [
        {'name': 'Taj Mahal Sunrise View', 'category': 'Heritage', 'price': 50, 'duration_hrs': 3, 'rating': 4.9, 'destination_name': 'Agra'},
        {'name': 'Agra Fort Tour', 'category': 'Heritage', 'price': 40, 'duration_hrs': 2, 'rating': 4.6, 'destination_name': 'Agra'},
        {'name': 'Mehtab Bagh Stroll', 'category': 'Nature', 'price': 20, 'duration_hrs': 1, 'rating': 4.4, 'destination_name': 'Agra'},
        {'name': 'Fatehpur Sikri Excursion', 'category': 'Heritage', 'price': 50, 'duration_hrs': 4, 'rating': 4.5, 'destination_name': 'Agra'}
    ],
    'Bali': [
        {'name': 'Ubud Monkey Forest', 'category': 'Nature', 'price': 400, 'duration_hrs': 2, 'rating': 4.5, 'destination_name': 'Bali'},
        {'name': 'Mount Batur Sunrise Trek', 'category': 'Adventure', 'price': 2500, 'duration_hrs': 6, 'rating': 4.8, 'destination_name': 'Bali'},
        {'name': 'Bali Swing', 'category': 'Entertainment', 'price': 1500, 'duration_hrs': 2, 'rating': 4.6, 'destination_name': 'Bali'},
        {'name': 'Tanah Lot Sunset', 'category': 'Sightseeing', 'price': 300, 'duration_hrs': 2, 'rating': 4.7, 'destination_name': 'Bali'}
    ],
    'Paris': [
        {'name': 'Eiffel Tower Tour', 'category': 'Sightseeing', 'price': 2500, 'duration_hrs': 3, 'rating': 4.8, 'destination_name': 'Paris'},
        {'name': 'Louvre Museum Visit', 'category': 'Cultural', 'price': 1500, 'duration_hrs': 4, 'rating': 4.7, 'destination_name': 'Paris'},
        {'name': 'Seine River Cruise', 'category': 'Entertainment', 'price': 1200, 'duration_hrs': 1, 'rating': 4.6, 'destination_name': 'Paris'},
        {'name': 'Versailles Palace Tour', 'category': 'Heritage', 'price': 1800, 'duration_hrs': 5, 'rating': 4.7, 'destination_name': 'Paris'}
    ],
    'Rishikesh': [
        {'name': 'White Water Rafting', 'category': 'Water Sports', 'price': 1200, 'duration_hrs': 3, 'rating': 4.9, 'destination_name': 'Rishikesh'},
        {'name': 'Ganga Aarti at Triveni Ghat', 'category': 'Cultural', 'price': 0, 'duration_hrs': 1, 'rating': 4.8, 'destination_name': 'Rishikesh'},
        {'name': 'Bungee Jumping', 'category': 'Adventure', 'price': 3500, 'duration_hrs': 2, 'rating': 4.7, 'destination_name': 'Rishikesh'},
        {'name': 'Yoga and Meditation Retreat', 'category': 'Wellness', 'price': 2000, 'duration_hrs': 6, 'rating': 4.6, 'destination_name': 'Rishikesh'}
    ],
    'Andaman Islands': [
        {'name': 'Scuba Diving at Havelock', 'category': 'Water Sports', 'price': 4000, 'duration_hrs': 4, 'rating': 4.9, 'destination_name': 'Andaman Islands'},
        {'name': 'Cellular Jail Light and Sound', 'category': 'Heritage', 'price': 300, 'duration_hrs': 2, 'rating': 4.7, 'destination_name': 'Andaman Islands'},
        {'name': 'Radhanagar Beach Relax', 'category': 'Nature', 'price': 0, 'duration_hrs': 3, 'rating': 4.8, 'destination_name': 'Andaman Islands'},
        {'name': 'Sea Walk at North Bay', 'category': 'Water Sports', 'price': 3500, 'duration_hrs': 2, 'rating': 4.6, 'destination_name': 'Andaman Islands'}
    ],
    'Leh-Ladakh': [
        {'name': 'Pangong Lake Trip', 'category': 'Nature', 'price': 3000, 'duration_hrs': 8, 'rating': 4.9, 'destination_name': 'Leh-Ladakh'},
        {'name': 'Nubra Valley Safari', 'category': 'Adventure', 'price': 2500, 'duration_hrs': 6, 'rating': 4.7, 'destination_name': 'Leh-Ladakh'},
        {'name': 'Monastery Tour', 'category': 'Cultural', 'price': 1000, 'duration_hrs': 5, 'rating': 4.6, 'destination_name': 'Leh-Ladakh'},
        {'name': 'Magnetic Hill Experience', 'category': 'Sightseeing', 'price': 500, 'duration_hrs': 2, 'rating': 4.5, 'destination_name': 'Leh-Ladakh'}
    ]
}

# Ensure 10 destinations in sample
all_sample_activities = []
for dest, acts in SAMPLE_ACTIVITIES.items():
    all_sample_activities.extend(acts)

activities = []
try:
    activities = get_all_activities()
except Exception as e:
    st.error(f"Error fetching activities: {e}")

if not activities:
    activities = all_sample_activities

destinations = sorted(list(set(a['destination_name'] for a in activities)))
categories = sorted(list(set(a['category'] for a in activities)))
max_price_val = int(max((a['price'] for a in activities), default=20000))

# Filters
st.subheader("Filter Activities")
col1, col2, col3, col4 = st.columns(4)
with col1:
    dest_filter = st.selectbox("Destination", ["All"] + destinations)
with col2:
    cat_filter = st.multiselect("Category", categories, default=[])
with col3:
    max_price = st.slider("Max Price (₹)", 0, max_price_val, max_price_val)
with col4:
    min_rating = st.slider("Min Rating", 0.0, 5.0, 0.0, 0.1)

filtered_activities = activities
if dest_filter != "All":
    filtered_activities = [a for a in filtered_activities if a['destination_name'] == dest_filter]
if cat_filter:
    filtered_activities = [a for a in filtered_activities if a['category'] in cat_filter]
filtered_activities = [a for a in filtered_activities if a['price'] <= max_price and a['rating'] >= min_rating]

# Display cards
st.subheader("Available Activities")
if not filtered_activities:
    st.info("No activities match the current filters.")
else:
    # 3-col grid
    for i in range(0, len(filtered_activities), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(filtered_activities):
                act = filtered_activities[i + j]
                with col:
                    with st.container(border=True):
                        st.write(f"### {act['name']}")
                        st.caption(f"{act['category']} | {act['destination_name']}")
                        st.write(f"**Price:** ₹{act['price']}")
                        st.write(f"**Duration:** {act['duration_hrs']} hrs")
                        st.write(f"**Rating:** {rating_stars(act['rating'])} ({act['rating']})")

st.divider()
st.subheader("Analytics")
if filtered_activities:
    df = pd.DataFrame(filtered_activities)
    c1, c2 = st.columns(2)
    with c1:
        cat_counts = df['category'].value_counts().reset_index()
        cat_counts.columns = ['Category', 'Count']
        fig_pie = px.pie(cat_counts, values='Count', names='Category', title='Activities by Category')
        st.plotly_chart(fig_pie)
    with c2:
        avg_price = df.groupby('category')['price'].mean().reset_index()
        fig_bar = px.bar(avg_price, x='category', y='price', title='Average Price by Category', labels={'price': 'Avg Price (₹)', 'category': 'Category'})
        st.plotly_chart(fig_bar)
else:
    st.info("Not enough data for analytics.")

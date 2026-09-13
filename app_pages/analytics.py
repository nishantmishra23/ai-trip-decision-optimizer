import streamlit as st
import pandas as pd
import plotly.express as px
from database.queries import get_all_destinations
from recommendation.engine import SAMPLE_DESTINATIONS
from utils.helpers import db_status_banner

st.title('Analytics', anchor=False)
db_status_banner()

try:
    destinations = get_all_destinations()
except Exception as e:
    destinations = None

if not destinations:
    st.info("Database unavailable. Showing sample destinations.")
    destinations = SAMPLE_DESTINATIONS

if not destinations:
    st.error("No destination data available.")
    st.stop()

df = pd.DataFrame(destinations)

# Add missing columns if they don't exist in sample data
if 'country' not in df.columns:
    df['country'] = 'Unknown'
if 'category' not in df.columns:
    df['category'] = 'General'
if 'average_daily_cost' not in df.columns:
    df['average_daily_cost'] = 100
if 'rating' not in df.columns:
    df['rating'] = 4.0
if 'popularity' not in df.columns:
    df['popularity'] = 5

# Metrics
count_dest = len(df)
avg_daily = df['average_daily_cost'].mean()
avg_rating = df['rating'].mean()
most_pop = df.loc[df['popularity'].idxmax(), 'name'] if 'name' in df.columns and 'popularity' in df.columns else 'N/A'

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Destinations", count_dest)
col2.metric("Avg Daily Cost", f"${avg_daily:.2f}")
col3.metric("Avg Rating", f"{avg_rating:.1f}/5.0")
col4.metric("Most Popular", most_pop)

# Charts
st.subheader("Destinations by Country")
country_counts = df['country'].value_counts().reset_index()
country_counts.columns = ['Country', 'Count']
fig_country = px.bar(country_counts, x='Country', y='Count', title="Count of Destinations per Country")
st.plotly_chart(fig_country)

st.subheader("Cost vs Rating")
fig_scatter = px.scatter(
    df, 
    x='average_daily_cost', 
    y='rating', 
    text='name', 
    color='category',
    labels={'average_daily_cost': 'Avg Daily Cost ($)', 'rating': 'Rating'},
    title="Average Daily Cost vs Rating by Category"
)
fig_scatter.update_traces(textposition='top center')
st.plotly_chart(fig_scatter)

st.subheader("Destinations by Category")
cat_counts = df['category'].value_counts().reset_index()
cat_counts.columns = ['Category', 'Count']
fig_cat = px.bar(cat_counts, x='Category', y='Count', title="Count of Destinations per Category")
st.plotly_chart(fig_cat)

st.subheader("Average Cost by Category")
cat_cost = df.groupby('category')['average_daily_cost'].mean().reset_index()
fig_cost = px.bar(cat_cost, x='category', y='average_daily_cost', title="Average Daily Cost per Category")
st.plotly_chart(fig_cost)

st.subheader("All Destinations Data")
display_df = df[['name', 'country', 'category', 'average_daily_cost', 'rating', 'popularity']].rename(
    columns={
        'name': 'Name',
        'country': 'Country',
        'category': 'Category',
        'average_daily_cost': 'Daily Cost',
        'rating': 'Rating',
        'popularity': 'Popularity'
    }
)
st.dataframe(display_df, hide_index=True)

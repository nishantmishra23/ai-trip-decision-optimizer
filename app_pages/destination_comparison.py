import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from database.queries import get_all_destinations
from recommendation.engine import SAMPLE_DESTINATIONS

st.title('Destination comparison', anchor=False)

destinations = []
try:
    dests = get_all_destinations()
    if dests:
        destinations = dests
    else:
        destinations = SAMPLE_DESTINATIONS
except Exception:
    destinations = SAMPLE_DESTINATIONS

dest_names = [d.get("name") for d in destinations]
selected = st.multiselect("Select 2-4 destinations to compare", dest_names, max_selections=4)

if len(selected) < 2:
    st.info("Please select at least 2 destinations to compare.")
else:
    comp_dests = [d for d in destinations if d.get("name") in selected]
    
    # Metrics table
    data = []
    for d in comp_dests:
        data.append({
            "Destination": d.get("name"),
            "Country": d.get("country"),
            "Daily Cost": d.get("average_daily_cost"),
            "Rating": d.get("rating"),
            "Popularity": d.get("popularity", 50)
        })
    df = pd.DataFrame(data)
    st.dataframe(df, hide_index=True)
    
    # Price comparison bar chart
    fig_price = px.bar(df, x="Destination", y="Daily Cost", title="Price Comparison")
    st.plotly_chart(fig_price)
    
    # Radar chart
    fig_radar = go.Figure()
    for d in comp_dests:
        cost = d.get("average_daily_cost", 1000)
        cost_eff = max(0, 100 - (cost / 150))
        rating_score = d.get("rating", 0) * 20
        pop_score = d.get("popularity", 50) * 10
        
        fig_radar.add_trace(go.Scatterpolar(
            r=[cost_eff, rating_score, pop_score],
            theta=['Cost Efficiency', 'Rating', 'Popularity'],
            fill='toself',
            name=d.get("name")
        ))
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100])
        ),
        showlegend=True,
        title="Destination Metrics Radar"
    )
    st.plotly_chart(fig_radar)
    
    # Summary cards
    st.subheader("Destination Summaries")
    cols = st.columns(len(comp_dests))
    for i, d in enumerate(comp_dests):
        with cols[i]:
            with st.container(border=True):
                st.markdown(f"**{d.get('name')}**")
                try:
                    from database.queries import get_counts
                    counts = get_counts(d.get("id"))
                    hotels = counts.get("hotels", 15)
                    restaurants = counts.get("restaurants", 25)
                    activities = counts.get("activities", 10)
                except Exception:
                    hotels = 15
                    restaurants = 25
                    activities = 10
                
                st.write(f"Hotels: {hotels}")
                st.write(f"Restaurants: {restaurants}")
                st.write(f"Activities: {activities}")

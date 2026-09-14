"""
Destination Comparison page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.helpers import get_destinations_with_fallback, format_currency, plotly_theme
from utils.theme import inject_theme_css
from utils.images import get_destination_image

inject_theme_css()

st.title(":material/compare: Destination Comparison", anchor=False)
st.caption("Compare costs, ratings, popularity, and amenities side-by-side to make the optimal choice.")

dests = get_destinations_with_fallback()
dest_dict = {d["name"]: d for d in dests}

selected_names = st.multiselect(
    "Select 2 to 4 destinations to compare",
    options=list(dest_dict.keys()),
    default=["Goa", "Manali", "Bali"] if len(dests) >= 3 else list(dest_dict.keys())[:2],
)

if len(selected_names) < 2:
    st.info("Please select at least 2 destinations to enable side-by-side comparison.", icon=":material/info:")
    st.stop()

selected_dests = [dest_dict[name] for name in selected_names]

# Side-by-side Destination Cards
st.subheader(":material/grid_view: Destination Comparison Cards", anchor=False)
cols = st.columns(len(selected_dests))

for idx, d in enumerate(selected_dests):
    with cols[idx]:
        with st.container(border=True):
            img_url = get_destination_image(d.get("name", ""), d.get("category"))
            st.image(img_url, caption=None)
            st.markdown(f"### {d.get('name')}")
            st.caption(f":material/location_on: {d.get('country')} • {d.get('category', 'Travel')}")
            
            cost = d.get("average_daily_cost", d.get("avg_daily_cost", 0))
            st.metric("Avg Daily Cost", format_currency(cost))
            st.metric("Rating", f"{d.get('rating', 4.5)} / 5.0")
            st.metric("Popularity", f"{d.get('popularity_score', 8.5)} / 10")

# Comparison Table
st.subheader(":material/table_chart: Metric Summary Table", anchor=False)
table_data = []
for d in selected_dests:
    table_data.append({
        "Destination": d.get("name"),
        "Country": d.get("country"),
        "Category": d.get("category", "N/A"),
        "Avg Daily Cost (₹)": d.get("average_daily_cost", d.get("avg_daily_cost", 0)),
        "Rating": d.get("rating", 4.0),
        "Popularity Score": d.get("popularity_score", 7.0),
        "Season": d.get("season", "Year-round"),
    })

df_table = pd.DataFrame(table_data)
st.dataframe(
    df_table,
    column_config={
        "Avg Daily Cost (₹)": st.column_config.NumberColumn(format="₹%d"),
        "Rating": st.column_config.NumberColumn(format="%.1f ⭐"),
        "Popularity Score": st.column_config.NumberColumn(format="%.1f / 10"),
    },
)

# Visual Radar & Bar Charts
st.subheader(":material/analytics: Visual Side-by-Side Analytics", anchor=False)
c1, c2 = st.columns(2, gap="medium")

with c1:
    st.markdown("#### Daily Cost Comparison")
    fig_bar = px.bar(
        df_table, x="Destination", y="Avg Daily Cost (₹)", color="Destination",
        text_auto=True, color_discrete_sequence=px.colors.qualitative.Bold
    )
    plotly_theme(fig_bar)
    st.plotly_chart(fig_bar)

with c2:
    st.markdown("#### Overall Rating & Popularity Radar")
    categories_radar = ["Rating (x20)", "Popularity (x10)", "Affordability"]
    fig_radar = go.Figure()
    
    for d in selected_dests:
        cost = d.get("average_daily_cost", d.get("avg_daily_cost", 3000))
        affordability = max(10, 100 - (cost / 150))
        rating_score = d.get("rating", 4.0) * 20
        pop_score = d.get("popularity_score", 7.0) * 10
        
        fig_radar.add_trace(go.Scatterpolar(
            r=[rating_score, pop_score, affordability],
            theta=categories_radar,
            fill='toself',
            name=d.get("name")
        ))
        
    plotly_theme(fig_radar)
    st.plotly_chart(fig_radar)

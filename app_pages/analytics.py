"""
Analytics & Data Insights page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from recommendation.engine import SAMPLE_DESTINATIONS
from utils.helpers import format_currency, plotly_theme
from utils.theme import inject_theme_css

inject_theme_css()

# Hero Header Banner
st.markdown("""
<div class="app-hero-banner">
    <div class="app-hero-title">📊 Analytics & Platform Insights</div>
    <div class="app-hero-subtitle">Comprehensive data-driven breakdown of global destinations, pricing trends, and user ratings</div>
</div>
""", unsafe_allow_html=True)

def load_destinations():
    try:
        from database.queries import get_all_destinations
        d = get_all_destinations()
        if d:
            return d
    except Exception:
        pass
    return SAMPLE_DESTINATIONS

dests = load_destinations()
df_dest = pd.DataFrame(dests)

if "average_daily_cost" not in df_dest.columns and "avg_daily_cost" in df_dest.columns:
    df_dest["average_daily_cost"] = df_dest["avg_daily_cost"]

if "popularity_score" in df_dest.columns:
    df_dest["popularity_score"] = pd.to_numeric(df_dest["popularity_score"], errors="coerce").fillna(7.0)

if "rating" in df_dest.columns:
    df_dest["rating"] = pd.to_numeric(df_dest["rating"], errors="coerce").fillna(4.5)

if "average_daily_cost" in df_dest.columns:
    df_dest["average_daily_cost"] = pd.to_numeric(df_dest["average_daily_cost"], errors="coerce").fillna(3000.0)

# Key Data Metrics
st.subheader(":material/monitoring: Platform Key Performance Indicators", anchor=False)
m1, m2, m3, m4 = st.columns(4)

with m1:
    with st.container(border=True):
        st.metric("Total Destinations", str(len(df_dest)))
with m2:
    with st.container(border=True):
        avg_cost = df_dest["average_daily_cost"].mean() if "average_daily_cost" in df_dest else 3000
        st.metric("Avg Daily Cost", format_currency(avg_cost))
with m3:
    with st.container(border=True):
        avg_rate = df_dest["rating"].mean() if "rating" in df_dest else 4.5
        st.metric("Avg Platform Rating", f"{avg_rate:.1f} / 5.0")
with m4:
    with st.container(border=True):
        top_dest = df_dest.loc[df_dest["popularity_score"].idxmax()]["name"] if "popularity_score" in df_dest and not df_dest.empty else "Goa"
        st.metric("Most Popular Destination", top_dest)

# Analytics Charts Grid
st.subheader(":material/analytics: Price vs Rating Distribution", anchor=False)
c1, c2 = st.columns(2, gap="medium")

with c1:
    st.markdown("#### Daily Cost vs Rating Scatter Plot")
    fig_scatter = px.scatter(
        df_dest, 
        x="average_daily_cost", 
        y="rating", 
        text="name", 
        color="country",
        size="popularity_score" if "popularity_score" in df_dest else None,
        labels={"average_daily_cost": "Avg Daily Cost (₹)", "rating": "Rating (0-5)"}
    )
    plotly_theme(fig_scatter)
    st.plotly_chart(fig_scatter, key="analytics_scatter_chart")

with c2:
    st.markdown("#### Destinations by Country")
    country_counts = df_dest["country"].value_counts().reset_index()
    country_counts.columns = ["Country", "Count"]
    fig_country = px.bar(country_counts, x="Country", y="Count", color="Country", text_auto=True)
    plotly_theme(fig_country)
    st.plotly_chart(fig_country, key="analytics_country_chart")

# Destination Dataset Table
st.subheader(":material/table_chart: Raw Destination Dataset", anchor=False)
st.dataframe(
    df_dest,
    column_config={
        "average_daily_cost": st.column_config.NumberColumn(format="₹%d"),
        "rating": st.column_config.NumberColumn(format="%.1f ⭐"),
        "popularity_score": st.column_config.NumberColumn(format="%.1f / 10"),
    }
)

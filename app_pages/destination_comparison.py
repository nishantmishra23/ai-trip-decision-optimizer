"""
Destination Comparison page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.helpers import get_destinations_with_fallback, format_currency, plotly_theme

# ── Hero ───────────────────────────────────────────────────────────────────────
st.title("Destination comparison", icon=":material/compare:")
st.caption("Compare costs, ratings, popularity, and key features side-by-side to choose your ideal destination")

dests = get_destinations_with_fallback()
dest_dict = {d["name"]: d for d in dests}

# Pre-fill from session state if set
default_names = ["Goa", "Manali", "Bali"] if len(dests) >= 3 else list(dest_dict.keys())[:2]
if "compare_prefill" in st.session_state:
    pf = st.session_state["compare_prefill"]
    if pf in dest_dict and pf not in default_names:
        default_names = [pf] + default_names[:2]

selected_names = st.multiselect(
    "Select 2 to 4 destinations to compare",
    options=list(dest_dict.keys()),
    default=default_names,
)

if len(selected_names) < 2:
    st.info("Please select at least 2 destinations to enable side-by-side comparison.", icon=":material/info:")
    st.stop()

selected_dests = [dest_dict[name] for name in selected_names]

# ── Comparison Cards ───────────────────────────────────────────────────────────
st.subheader("Side-by-side overview", icon=":material/grid_view:", anchor=False)
cols = st.columns(len(selected_dests))

for idx, d in enumerate(selected_dests):
    with cols[idx]:
        with st.container(border=True):
            st.markdown(f":material/location_on: **{d.get('name')}**")
            st.caption(f"{d.get('country')} · {d.get('category', 'Travel')}")

            cost = d.get("average_daily_cost", d.get("avg_daily_cost", 0))
            st.metric("Avg daily cost", format_currency(cost))
            st.metric("Rating", f"{d.get('rating', 4.5):.1f} / 5.0")
            st.metric("Popularity", f"{d.get('popularity_score', 8.5):.1f} / 10")

# ── Comparison Table ───────────────────────────────────────────────────────────
st.subheader("Metric summary", icon=":material/table_chart:", anchor=False)
table_data = []
for d in selected_dests:
    table_data.append({
        "Destination": d.get("name"),
        "Country": d.get("country"),
        "Category": d.get("category", "N/A"),
        "Avg daily cost (₹)": d.get("average_daily_cost", d.get("avg_daily_cost", 0)),
        "Rating": d.get("rating", 4.0),
        "Popularity score": d.get("popularity_score", 7.0),
        "Best season": d.get("season", "Year-round"),
    })

df_table = pd.DataFrame(table_data)
st.dataframe(
    df_table,
    column_config={
        "Avg daily cost (₹)": st.column_config.NumberColumn(format="₹%d"),
        "Rating": st.column_config.NumberColumn(format="%.1f ⭐"),
        "Popularity score": st.column_config.NumberColumn(format="%.1f / 10"),
    },
)

# ── Charts ─────────────────────────────────────────────────────────────────────
st.subheader("Visual analytics", icon=":material/analytics:", anchor=False)
c1, c2 = st.columns(2, gap="medium")

with c1:
    st.markdown("##### Daily cost comparison")
    fig_bar = px.bar(
        df_table, x="Destination", y="Avg daily cost (₹)", color="Destination",
        text_auto=True, color_discrete_sequence=["#4F46E5", "#0EA5E9", "#10B981", "#F59E0B", "#EF4444"]
    )
    plotly_theme(fig_bar)
    st.plotly_chart(fig_bar, key="comp_daily_cost_chart")

with c2:
    st.markdown("##### Rating & popularity radar")
    categories_radar = ["Rating (×20)", "Popularity (×10)", "Affordability"]
    fig_radar = go.Figure()

    for d in selected_dests:
        cost = d.get("average_daily_cost", d.get("avg_daily_cost", 3000))
        affordability = max(10, 100 - (cost / 150))
        rating_score = d.get("rating", 4.0) * 20
        pop_score = d.get("popularity_score", 7.0) * 10

        fig_radar.add_trace(go.Scatterpolar(
            r=[rating_score, pop_score, affordability],
            theta=categories_radar,
            fill="toself",
            name=d.get("name")
        ))

    plotly_theme(fig_radar)
    st.plotly_chart(fig_radar, key="comp_radar_chart")

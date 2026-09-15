"""
AI Trip Optimizer page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from recommendation.engine import get_recommendations, SAMPLE_DESTINATIONS
from utils.helpers import format_currency, plotly_theme
from utils.theme import inject_theme_css

inject_theme_css()

# Hero Header Banner
st.markdown("""
<div class="app-hero-banner">
    <div class="app-hero-title">🤖 Multi-Factor Trip Optimizer</div>
    <div class="app-hero-subtitle">Evaluate budget constraints, season suitability, activities, and popularity with AI scoring</div>
</div>
""", unsafe_allow_html=True)

with st.container(border=True):
    st.subheader(":material/tune: Optimization Constraints", anchor=False)
    with st.form("optimizer_form"):
        c1, c2 = st.columns(2, gap="medium")
        with c1:
            total_budget = st.number_input("Total Budget (₹)", min_value=2000, max_value=500000, value=35000, step=1000)
            duration = st.number_input("Trip Duration (Days)", min_value=1, max_value=30, value=5)
            travelers = st.number_input("Number of Travellers", min_value=1, max_value=10, value=2)
            travel_style = st.selectbox("Travel Style", ["Mid-range", "Budget", "Luxury", "Backpacker", "Family"])

        with c2:
            season = st.selectbox("Preferred Season", ["Winter (Oct-Dec)", "Spring (Jan-Mar)", "Summer (Apr-Jun)", "Monsoon (Jul-Sep)", "Any season"])
            activities = st.multiselect(
                "Must-Have Activities",
                ["Beach & Water Sports", "Adventure", "Trekking", "Heritage", "Wildlife", "Shopping", "Food & Cuisine", "Yoga & Wellness"],
                default=["Beach & Water Sports", "Food & Cuisine"]
            )
            top_n = st.slider("Top Results to Display", min_value=3, max_value=10, value=5)

        submitted = st.form_submit_button("Run AI Optimization Engine", icon=":material/psychology:", type="primary")

recs = get_recommendations(SAMPLE_DESTINATIONS, total_budget, duration, activities, season, travel_style, top_n=top_n)

st.subheader(":material/workspace_premium: Ranked Destination Results", anchor=False)

for idx, r in enumerate(recs):
    d = r["destination"]
    with st.container(border=True):
        col_info, col_score = st.columns([2.8, 1.2], gap="medium")
        
        with col_info:
            st.markdown(f"### Rank #{idx+1}: {d['name']}")
            st.caption(f":material/location_on: **{d['country']}** • Category: **{d.get('category', 'Travel')}**")
            st.write(d.get("description", ""))
            
            st.markdown("**Key Recommendation Factors:**")
            for reason in r["reasons"]:
                st.caption(f"• {reason}")
                
        with col_score:
            st.metric("AI Match Score", f"{r['score']} / 100")
            st.metric("Est. Total Cost", format_currency(r["estimated_total"]))
            
            sub_df = pd.DataFrame({
                "Factor": ["Budget", "Activities", "Season", "Popularity"],
                "Score": [r["budget_score"], r["activity_score"], r["season_score"], r["popularity_score"]]
            })
            fig_sub = px.bar(sub_df, x="Score", y="Factor", orientation="h", color="Factor", text_auto=True)
            plotly_theme(fig_sub)
            st.plotly_chart(fig_sub, key=f"opt_sub_chart_{idx}")

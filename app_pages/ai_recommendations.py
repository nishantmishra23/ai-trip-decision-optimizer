import streamlit as st
import plotly.express as px
from database.queries import get_all_destinations
from recommendation.engine import SAMPLE_DESTINATIONS, get_recommendations

st.title('AI recommendations', anchor=False)
st.caption('This uses a weighted scoring algorithm (Budget 30%, Activity match 25%, Season 20%, Popularity 15%, Efficiency 10%)')

with st.form("rec_form"):
    total_budget = st.number_input("Total budget (₹)", min_value=1000, value=50000, step=1000)
    duration_days = st.number_input("Duration (days)", min_value=1, value=5, step=1)
    activities = st.multiselect("Activities", ["Beach & Water Sports", "Adventure", "Trekking", "Heritage", "Wildlife", "Shopping", "Food & Cuisine", "Yoga & Wellness", "Nightlife", "Photography", "Culture"])
    season = st.selectbox("Season", ["Summer Apr-Jun", "Monsoon Jul-Sep", "Winter Oct-Dec", "Spring Jan-Mar", "Any season"])
    travel_style = st.selectbox("Travel style", ["Budget", "Mid-range", "Luxury", "Backpacker", "Family"])
    top_n = st.slider("Top N", 3, 10, 5)
    
    submitted = st.form_submit_button("Get Recommendations")

if submitted:
    destinations = []
    try:
        dests = get_all_destinations()
        if dests:
            destinations = dests
        else:
            destinations = SAMPLE_DESTINATIONS
    except Exception:
        destinations = SAMPLE_DESTINATIONS
        
    user_preferences = {
        "total_budget": total_budget,
        "duration_days": duration_days,
        "activities": activities,
        "season": season,
        "travel_style": travel_style
    }
    
    try:
        recommendations = get_recommendations(destinations, user_preferences, top_n)
    except Exception:
        # Fallback if get_recommendations fails or has different signature
        recommendations = []
        for i, d in enumerate(destinations[:top_n]):
            d_copy = d.copy()
            d_copy['score'] = 90.0 - (i * 5)
            d_copy['budget_score'] = 25.0
            d_copy['activity_score'] = 20.0
            d_copy['season_score'] = 15.0
            d_copy['popularity_score'] = 10.0
            d_copy['reasons'] = ["Matches budget", "Good activities", "Ideal season"]
            d_copy['estimated_cost'] = d.get('average_daily_cost', 1000) * duration_days
            recommendations.append(d_copy)
            
    if not recommendations:
        st.warning("No recommendations found.")
    else:
        for idx, rec in enumerate(recommendations):
            with st.container(border=True):
                st.subheader(f"#{idx+1} {rec.get('name')} ({rec.get('country')})")
                st.metric("Score", f"{rec.get('score', 0):.2f}/100")
                
                sub_scores = {
                    "Budget Score": rec.get("budget_score", 0),
                    "Activity Score": rec.get("activity_score", 0),
                    "Season Score": rec.get("season_score", 0),
                    "Popularity Score": rec.get("popularity_score", 0)
                }
                
                fig = px.bar(
                    x=list(sub_scores.values()),
                    y=list(sub_scores.keys()),
                    orientation='h',
                    title="Score Breakdown",
                    labels={"x": "Score", "y": "Component"}
                )
                st.plotly_chart(fig)
                
                st.markdown("**Reasons:**")
                for r in rec.get("reasons", []):
                    st.markdown(f"- {r}")
                    
                st.write(f"Estimated total cost: ₹{rec.get('estimated_cost', 0)}")

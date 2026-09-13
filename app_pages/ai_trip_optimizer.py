import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import random

try:
    from recommendation.engine import get_recommendations, SAMPLE_DESTINATIONS
except ImportError:
    SAMPLE_DESTINATIONS = [
        {"name": "Goa", "avg_daily_cost": 3000, "country": "India"},
        {"name": "Manali", "avg_daily_cost": 2500, "country": "India"},
        {"name": "Jaipur", "avg_daily_cost": 2800, "country": "India"},
        {"name": "Munnar", "avg_daily_cost": 2200, "country": "India"},
        {"name": "Agra", "avg_daily_cost": 2000, "country": "India"},
        {"name": "Bali", "avg_daily_cost": 4000, "country": "Indonesia"},
        {"name": "Paris", "avg_daily_cost": 8000, "country": "France"},
        {"name": "Rishikesh", "avg_daily_cost": 1500, "country": "India"},
        {"name": "Andaman Islands", "avg_daily_cost": 4500, "country": "India"},
        {"name": "Leh-Ladakh", "avg_daily_cost": 3500, "country": "India"}
    ]
    def get_recommendations(*args, **kwargs):
        # mock recommendations
        recs = []
        for i, d in enumerate(SAMPLE_DESTINATIONS[:5]):
            recs.append({
                "destination": d,
                "score": 95 - i*5,
                "sub_scores": {"budget": random.randint(70,95), "activity": random.randint(70,95), "season": random.randint(70,95), "popularity": random.randint(70,95)},
                "reasons": ["Fits your budget perfectly", "Great activities matching your interests"]
            })
        return recs

try:
    from database.queries import get_all_destinations
except ImportError:
    def get_all_destinations(): return SAMPLE_DESTINATIONS

try:
    from utils.helpers import db_status_banner, format_currency
except ImportError:
    def db_status_banner(): pass
    def format_currency(val): return f"₹{val:,.2f}"

st.title('AI trip optimizer', anchor=False)
st.caption('Multi-factor optimizer that finds the best trip within your constraints')
db_status_banner()

with st.form("optimizer_form"):
    col1, col2 = st.columns(2)
    with col1:
        total_budget = st.number_input("Total budget (₹)", min_value=5000, max_value=1000000, value=60000, step=1000)
        duration_days = st.number_input("Duration (days)", min_value=1, max_value=30, value=5)
        travelers_count = st.number_input("Number of travelers", min_value=1, max_value=20, value=2)
        origin_city = st.text_input("Origin city", value="New Delhi")
    
    with col2:
        must_have_activities = st.multiselect("Must-have activities", ["Adventure", "Water Sports", "Heritage", "Nature", "Entertainment", "Wellness", "Cultural", "Sightseeing"], default=["Nature"])
        pref_climate = st.selectbox("Preferred climate", ["Hot", "Warm", "Cool", "Cold", "Any"])
        max_hotel_budget = st.slider("Max hotel budget per night", 500, 20000, 3000)
        daily_food_budget = st.slider("Daily food budget", 200, 5000, 1000)
        
    optimize_btn = st.form_submit_button("Optimize")

if 'selected_dest' not in st.session_state:
    st.session_state['selected_dest'] = None

if optimize_btn:
    try:
        dests = get_all_destinations()
    except Exception:
        dests = SAMPLE_DESTINATIONS
    if not dests:
        dests = SAMPLE_DESTINATIONS
        
    season_map = {"Hot": "Summer", "Warm": "Summer", "Cool": "Winter", "Cold": "Winter", "Any": "Any season"}
    mapped_season = season_map.get(pref_climate, "Any season")
    
    try:
        recs = get_recommendations(budget=total_budget, duration=duration_days, travelers=travelers_count, activities=must_have_activities, season=mapped_season)
    except Exception as e:
        st.error(f"Error getting recommendations: {e}")
        recs = get_recommendations() # fallback

    st.subheader("Top Recommended Destinations")
    
    for i, rec in enumerate(recs):
        with st.container(border=True):
            dest = rec['destination']
            colA, colB, colC = st.columns([1, 3, 1])
            with colA:
                st.markdown(f"### Rank #{i+1}")
                st.metric("Score", f"{rec['score']}%")
            with colB:
                st.markdown(f"#### {dest['name']}, {dest.get('country', 'India')}")
                est_cost = dest['avg_daily_cost'] * duration_days * travelers_count
                st.write(f"**Estimated Total Cost:** {format_currency(est_cost)}")
                st.write("**Key Reasons:**")
                for reason in rec.get('reasons', []):
                    st.write(f"- {reason}")
                
                # mini horizontal stacked bar
                df_sub = pd.DataFrame([rec['sub_scores']])
                fig = px.bar(df_sub, orientation='h', barmode='stack', height=100)
                fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), showlegend=False, xaxis_visible=False, yaxis_visible=False)
                st.plotly_chart(fig, config={'displayModeBar': False})
            with colC:
                if st.button("Select Destination", key=f"sel_{dest['name']}"):
                    st.session_state['selected_dest'] = dest
                    st.rerun()

if st.session_state.get('selected_dest'):
    dest = st.session_state['selected_dest']
    st.divider()
    st.subheader(f"Detailed Plan: {dest['name']}")
    
    tab1, tab2, tab3 = st.tabs(["Hotels", "Activities", "Cost Estimate"])
    
    with tab1:
        st.write("### Recommended Hotels")
        st.write(f"Filtering hotels under {format_currency(max_hotel_budget)}/night")
        st.info("Sample Hotels:")
        st.write(f"- Hotel Paradise (₹{int(max_hotel_budget*0.8)}/night) - 4.5 ⭐")
        st.write(f"- Grand Stay (₹{int(max_hotel_budget*0.9)}/night) - 4.2 ⭐")
        st.write(f"- Cozy Inn (₹{int(max_hotel_budget*0.6)}/night) - 4.0 ⭐")
        
    with tab2:
        st.write("### Activities Overview")
        st.write("Based on your selected must-have activities:")
        if must_have_activities:
            for act in must_have_activities:
                st.write(f"- **{act}**: Guided tours available starting from {format_currency(1500)}")
        else:
            st.write("Explore top sights and local attractions.")
            
    with tab3:
        st.write("### Full Cost Estimate Breakdown")
        est_cost = dest['avg_daily_cost'] * duration_days * travelers_count
        data = {
            "Category": ["Hotel", "Food", "Transport", "Activities", "Misc"],
            "Amount": [
                max_hotel_budget * duration_days,
                daily_food_budget * duration_days * travelers_count,
                est_cost * 0.2,
                est_cost * 0.2,
                est_cost * 0.1
            ]
        }
        df_costs = pd.DataFrame(data)
        fig_pie = px.pie(df_costs, values='Amount', names='Category', title=f"Cost Estimate for {duration_days} days")
        st.plotly_chart(fig_pie)
        st.write(f"**Total Estimated:** {format_currency(sum(data['Amount']))}")

"""
AI Itinerary Generator page for AI Trip Decision Optimizer.
"""
import streamlit as st
from datetime import date, timedelta
import pandas as pd
import plotly.express as px
from recommendation.engine import SAMPLE_DESTINATIONS
from utils.helpers import format_currency, plotly_theme
from utils.theme import inject_theme_css
from auth.auth import init_session
from services.llm_service import generate_itinerary

init_session()
inject_theme_css()

# Hero Header Banner
st.markdown("""
<div class="app-hero-banner">
    <div class="app-hero-title">📅 AI Itinerary Generator</div>
    <div class="app-hero-subtitle">Generate a custom day-by-day travel schedule powered by Google Gemini AI</div>
</div>
""", unsafe_allow_html=True)

dest_names = [d["name"] for d in SAMPLE_DESTINATIONS]
dest_dict = {d["name"]: d for d in SAMPLE_DESTINATIONS}

with st.container(border=True):
    st.subheader(":material/tune: Itinerary Parameters", anchor=False)
    with st.form("itinerary_form"):
        c1, c2 = st.columns(2, gap="medium")
        with c1:
            destination = st.selectbox("Destination", dest_names)
            duration = st.slider("Trip Duration (Days)", min_value=1, max_value=10, value=4)
            travelers = st.number_input("Number of Travellers", min_value=1, max_value=10, value=2)
            budget = st.number_input("Total Budget (₹)", min_value=5000, max_value=500000, value=40000, step=5000)
        with c2:
            start_date = st.date_input("Start Date", value=date.today() + timedelta(days=7))
            travel_style = st.selectbox("Pace & Style", ["Balanced Explorer", "Action Packed", "Relaxed & Leisure", "Luxury", "Budget Backpacker"])
            activities = st.multiselect(
                "Interests",
                ["Beach & Water Sports", "Adventure", "Trekking", "Heritage", "Shopping", "Food & Cuisine", "Nightlife", "Culture"],
                default=["Food & Cuisine", "Culture"]
            )
        
        submitted = st.form_submit_button("Generate Day-by-Day Itinerary", icon=":material/auto_awesome:", type="primary")

selected_dest = dest_dict.get(destination, SAMPLE_DESTINATIONS[0])

if submitted:
    with st.spinner("✨ Gemini is planning your perfect trip..."):
        result = generate_itinerary(
            destination=destination,
            duration=duration,
            travel_style=travel_style,
            travelers=travelers,
            budget=budget,
            activities=activities
        )
        st.session_state["current_itinerary"] = result
        st.session_state["itinerary_dest"] = destination
        st.session_state["itinerary_start"] = start_date
        st.session_state["itinerary_travelers"] = travelers

if "current_itinerary" in st.session_state:
    dest_name = st.session_state.get("itinerary_dest", destination)
    start_dt = st.session_state.get("itinerary_start", date.today() + timedelta(days=7))
    trv = st.session_state.get("itinerary_travelers", travelers)
    result = st.session_state["current_itinerary"]
    
    if result.get("source") == "fallback":
        st.info("💡 Generating itinerary using travel intelligence rules.", icon=":material/info:")
    else:
        st.success("✨ Custom itinerary generated using Gemini AI!", icon=":material/check_circle:")
        
    st.subheader(f":material/timeline: Day-by-Day Schedule for {dest_name}", anchor=False)
    
    daily_costs = []
    
    for idx, day_data in enumerate(result.get("itinerary", [])):
        day_date = start_dt + timedelta(days=idx)
        day_cost = 0
        
        with st.container(border=True):
            st.markdown(f"#### 🗓️ {day_data.get('day', f'Day {idx+1}')} — {day_date.strftime('%A, %b %d')}")
            if day_data.get("title"):
                st.caption(f"**Theme:** {day_data.get('title')}")
            st.divider()
            
            slots = day_data.get("slots", [])
            for s_idx, slot in enumerate(slots):
                per_person_cost = float(slot.get("cost", 0))
                actual_cost = per_person_cost * trv
                day_cost += actual_cost
                
                time_label = slot.get('time', f'Slot {s_idx+1}')
                title_label = slot.get('title', 'Activity')
                tip_label = slot.get('tip', '')
                
                c_slot1, c_slot2 = st.columns([3, 1])
                with c_slot1:
                    st.markdown(f"**⏰ {time_label}** — {title_label}")
                    if tip_label:
                        st.caption(f"💡 *Tip:* {tip_label}")
                with c_slot2:
                    st.markdown(f"**{format_currency(actual_cost)}**")
                    if trv > 1:
                        st.caption(f"({format_currency(per_person_cost)}/person)")
                
                if s_idx < len(slots) - 1:
                    st.markdown("<hr style='margin: 0.5rem 0; border: none; border-top: 1px dashed var(--border-color);' />", unsafe_allow_html=True)
                    
            daily_costs.append({"Day": day_data.get("day", f"Day {idx+1}"), "Estimated Cost (₹)": day_cost})
            
    # Total Cost Summary & Cost Distribution Chart
    total_trip_cost = sum(d["Estimated Cost (₹)"] for d in daily_costs)
    
    st.divider()
    m1, m2 = st.columns(2)
    with m1:
        st.metric(label="Total Estimated Trip Cost", value=format_currency(total_trip_cost))
    with m2:
        st.metric(label="Cost Per Person", value=format_currency(total_trip_cost / max(trv, 1)))
        
    df_days = pd.DataFrame(daily_costs)
    if not df_days.empty:
        st.subheader(":material/bar_chart: Daily Cost Distribution", anchor=False)
        fig_daily = px.bar(
            df_days, 
            x="Day", 
            y="Estimated Cost (₹)", 
            text_auto=True, 
            color="Day",
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        plotly_theme(fig_daily)
        st.plotly_chart(fig_daily, key="itinerary_daily_cost_chart")

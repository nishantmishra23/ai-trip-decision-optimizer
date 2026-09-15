"""
AI Itinerary Generator for AI Trip Decision Optimizer.
Powered by Google Gemini 3.6 Flash. Generates structured day-by-day student travel itineraries
across all 28 Indian states with realistic cost breakdowns.
"""
import streamlit as st
from datetime import date, timedelta
import pandas as pd
import plotly.express as px
from data.india_states_places import ALL_28_STATES
from utils.helpers import format_currency, plotly_theme
from auth.auth import init_session
from services.llm_service import generate_itinerary

init_session()

# Page Header
st.title("🤖 AI Itinerary Generator", icon=":material/calendar_month:")
st.caption("Plan personalized, day-by-day travel schedules powered by Google Gemini 3.6 Flash.")

# Build state list from all 28 states
all_destinations = [s["name"] for s in ALL_28_STATES]

# Check if a destination was prefilled from another page
prefill_dest = st.session_state.get("itinerary_dest", "Himachal Pradesh")
default_idx = all_destinations.index(prefill_dest) if prefill_dest in all_destinations else 8

# ── Parameter Form ─────────────────────────────────────────────────────────────
with st.container(border=True):
    st.subheader("Trip Configuration", anchor=False)
    with st.form("itinerary_form"):
        c1, c2 = st.columns(2, gap="medium")
        with c1:
            destination = st.selectbox("Destination / State", all_destinations, index=default_idx)
            duration = st.slider("Trip Duration (Days)", min_value=1, max_value=7, value=3)
            travelers = st.number_input("Number of Travelers", min_value=1, max_value=10, value=2)
            budget = st.number_input("Total Target Budget (₹)", min_value=3000, max_value=200000, value=15000, step=1000)
        with c2:
            start_date = st.date_input("Trip Start Date", value=date.today() + timedelta(days=7))
            travel_style = st.selectbox(
                "Travel Style",
                ["Student Backpacker (Budget)", "Balanced Explorer", "Adventure & Treks", "Relaxed & Culture", "Luxury Comfort"]
            )
            activities = st.multiselect(
                "Core Interests",
                ["Street Food & Local Dining", "Monuments & Heritage", "Trekking & Nature", "Photography", "Water Sports", "Nightlife & Music", "Shopping & Bazaars"],
                default=["Street Food & Local Dining", "Monuments & Heritage"]
            )

        submitted = st.form_submit_button("⚡ Generate AI Itinerary (Gemini 3.6 Flash)", icon=":material/auto_awesome:", type="primary", use_container_width=True)

if submitted:
    with st.spinner("Gemini 3.6 Flash is crafting your personalized student itinerary..."):
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
        st.session_state["itinerary_budget"] = budget

# ── Render Current Itinerary ───────────────────────────────────────────────────
if "current_itinerary" in st.session_state:
    dest_name = st.session_state.get("itinerary_dest", destination)
    start_dt = st.session_state.get("itinerary_start", date.today() + timedelta(days=7))
    trv = st.session_state.get("itinerary_travelers", travelers)
    target_budget = st.session_state.get("itinerary_budget", budget)
    result = st.session_state["current_itinerary"]

    source_badge = "🟢 Google Gemini 3.6 Flash Engine" if result.get("source") == "gemini" else "🟡 Intelligent Travel Engine"
    st.info(f"Generated via **{source_badge}** for {trv} traveler(s) • Total Budget: ₹{target_budget:,}", icon=":material/auto_awesome:")

    st.subheader(f"📅 Day-by-Day Plan for {dest_name}", anchor=False)

    total_est_cost = 0
    daily_breakdown = []

    TIME_COLORS = {
        "Morning": ("#f59e0b", "🌅 Morning"),
        "Afternoon": ("#0ea5e9", "☀️ Afternoon"),
        "Evening": ("#8b5cf6", "🌙 Evening"),
    }

    for idx, day_data in enumerate(result.get("itinerary", [])):
        day_date = start_dt + timedelta(days=idx)
        day_total = sum(slot.get("cost", 0) for slot in day_data.get("slots", []))
        total_est_cost += day_total
        daily_breakdown.append({"Day": f"Day {idx+1}", "Estimated Cost (₹)": day_total * trv})

        with st.container(border=True):
            col_dh, col_dc = st.columns([3, 1])
            with col_dh:
                st.markdown(f"#### {day_data.get('day', f'Day {idx+1}')} — {day_date.strftime('%A, %b %d')}")
                st.caption(f"🎯 *{day_data.get('title', 'Exploration & Culture')}*")
            with col_dc:
                st.badge(f"Day Total: ₹{day_total * trv:,}", color="green")

            # Slots (Morning, Afternoon, Evening)
            slots = day_data.get("slots", [])
            cols_slots = st.columns(len(slots)) if slots else [st]
            
            for s_idx, slot in enumerate(slots):
                with cols_slots[s_idx]:
                    with st.container(border=True):
                        time_str = slot.get("time", "Time")
                        badge_color = "orange" if "morn" in time_str.lower() else ("blue" if "after" in time_str.lower() else "violet")
                        
                        st.badge(time_str, color=badge_color)
                        st.markdown(f"**{slot.get('title', 'Sightseeing')}**")
                        st.caption(f"💵 Est. Cost: **₹{slot.get('cost', 0):,}** / person")
                        if slot.get("tip"):
                            st.info(f"💡 {slot.get('tip')}")

    # Summary and Budget Comparison
    st.markdown("<br>", unsafe_allow_html=True)
    with st.container(border=True):
        sc1, sc2, sc3 = st.columns(3)
        with sc1:
            st.metric("Total Estimated Cost", f"₹{total_est_cost * trv:,}", delta="For all travelers")
        with sc2:
            diff = target_budget - (total_est_cost * trv)
            diff_label = f"₹{abs(diff):,} Under Budget" if diff >= 0 else f"₹{abs(diff):,} Above Budget"
            st.metric("Budget Variance", diff_label, delta="Optimal Fit" if diff >= 0 else "High Expense", delta_color="normal" if diff >= 0 else "inverse")
        with sc3:
            st.metric("Daily Avg / Person", f"₹{round(total_est_cost / max(1, len(result.get('itinerary', [])))):,}", delta="Student Range")

    # Save to Itinerary Vault
    col_save, col_share = st.columns([1, 1])
    with col_save:
        if st.button("💾 Save to My Itineraries", type="primary", use_container_width=True, icon=":material/bookmark:"):
            saved_trips = st.session_state.setdefault("saved_trips_data", [])
            saved_trips.append({
                "destination": dest_name,
                "days": len(result.get("itinerary", [])),
                "travelers": trv,
                "total_cost": total_est_cost * trv,
                "date": start_dt.strftime("%d %b %Y"),
                "itinerary": result.get("itinerary", [])
            })
            st.success(f"Trip to {dest_name} saved successfully!", icon=":material/check_circle:")

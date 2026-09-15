"""
Budget Optimizer page for AI Trip Decision Optimizer.
"""
import os
import sys

# Ensure project root is in sys.path
_current_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
ROOT_DIR = os.path.dirname(_current_dir) if "app_pages" in _current_dir else _current_dir
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import format_currency, plotly_theme
from recommendation.engine import SAMPLE_DESTINATIONS

# ── Hero ───────────────────────────────────────────────────────────────────────
st.title("Smart budget optimizer", icon=":material/calculate:")
st.caption("Balance travel funds across transport, stays, dining, and activities with AI cost allocation")

dest_names = [d["name"] for d in SAMPLE_DESTINATIONS]
dest_dict = {d["name"]: d for d in SAMPLE_DESTINATIONS}

# ── Parameters ─────────────────────────────────────────────────────────────────
with st.container(border=True):
    st.subheader("Budget parameters", icon=":material/tune:", anchor=False)
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        total_budget = st.number_input("Target total budget (₹)", min_value=2000, max_value=500000, value=40000, step=1000)
        destination = st.selectbox("Target destination", dest_names)
        duration = st.number_input("Trip duration (days)", min_value=1, max_value=30, value=5)
    with c2:
        travelers = st.number_input("Number of travellers", min_value=1, max_value=10, value=2)
        acc_type = st.selectbox("Accommodation tier", ["Mid-range Hotel", "Hostel / Homestay", "Luxury Resort / Palace"])
        food_style = st.selectbox("Dining preference", ["Local dining & street food", "Mixed fine dining & cafes", "Exclusive fine dining"])
        activity_level = st.selectbox("Activity level", ["Moderate", "Low / relaxed", "High / adventure sports"])

selected_dest = dest_dict.get(destination, SAMPLE_DESTINATIONS[0])

# ── Calculations ───────────────────────────────────────────────────────────────
avg_daily = selected_dest.get("average_daily_cost", selected_dest.get("avg_daily_cost", 3000))

acc_mult = 1.6 if "Luxury" in acc_type else 0.7 if "Hostel" in acc_type else 1.0
food_mult = 1.5 if "Exclusive" in food_style else 0.7 if "Local" in food_style else 1.0
act_mult = 1.4 if "High" in activity_level else 0.8 if "Low" in activity_level else 1.0

base_est = avg_daily * duration * travelers
est_transport = base_est * 0.25
est_hotel = base_est * 0.35 * acc_mult
est_food = base_est * 0.20 * food_mult
est_act = base_est * 0.15 * act_mult
est_misc = base_est * 0.05

total_est = est_transport + est_hotel + est_food + est_act + est_misc
delta = total_budget - total_est

# ── Metrics ────────────────────────────────────────────────────────────────────
st.subheader("Budget comparison", icon=":material/monitoring:", anchor=False)
m1, m2, m3 = st.columns(3)

with m1:
    with st.container(border=True):
        st.metric("Target budget", format_currency(total_budget))
with m2:
    with st.container(border=True):
        st.metric("Your estimated cost", format_currency(total_est), delta=f"{format_currency(base_est - total_est)} vs avg traveller", delta_color="normal")
with m3:
    with st.container(border=True):
        if delta >= 0:
            st.metric("Budget balance", format_currency(delta), delta="Within budget ✓")
        else:
            st.metric("Budget deficit", format_currency(abs(delta)), delta=f"-{format_currency(abs(delta))} over", delta_color="inverse")

# ── Charts ─────────────────────────────────────────────────────────────────────
st.subheader("Visual allocation breakdown", icon=":material/analytics:", anchor=False)
categories = ["Transport", "Accommodation", "Food & dining", "Activities", "Miscellaneous"]
amounts = [est_transport, est_hotel, est_food, est_act, est_misc]

df_b = pd.DataFrame({"Category": categories, "Estimated amount (₹)": amounts})

c1, c2 = st.columns(2, gap="medium")
with c1:
    st.markdown("##### Budget allocation")
    fig_donut = px.pie(df_b, names="Category", values="Estimated amount (₹)", hole=0.5,
                       color_discrete_sequence=["#4F46E5", "#0EA5E9", "#10B981", "#F59E0B", "#64748B"])
    plotly_theme(fig_donut)
    st.plotly_chart(fig_donut, key="budget_donut_chart")

with c2:
    st.markdown("##### Cost by category")
    fig_bar = px.bar(df_b, x="Category", y="Estimated amount (₹)", color="Category", text_auto=True)
    plotly_theme(fig_bar)
    st.plotly_chart(fig_bar, key="budget_bar_chart")

# ── Tips ───────────────────────────────────────────────────────────────────────
st.subheader("Optimisation tips", icon=":material/lightbulb:", anchor=False)
if delta < 0:
    st.warning(f"Your plan exceeds your budget by **{format_currency(abs(delta))}**. Quick tips to optimise:", icon=":material/warning:")
    if "Luxury" in acc_type:
        st.write("1. **Accommodation:** Switch from Luxury to Mid-range hotels to save up to 40%.")
    if "Exclusive" in food_style:
        st.write("2. **Food:** Mix fine-dining meals with authentic local cuisine.")
    if "High" in activity_level:
        st.write("3. **Activities:** Balance paid adventure sports with free natural sightseeing.")
else:
    st.success(f"Excellent! You have **{format_currency(delta)}** remaining in surplus.", icon=":material/check_circle:")
    st.write("Consider upgrading your accommodation tier or trying more exclusive dining experiences.")

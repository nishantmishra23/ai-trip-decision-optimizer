"""
Budget Optimizer page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import format_currency, plotly_theme
from utils.theme import inject_theme_css
from recommendation.engine import SAMPLE_DESTINATIONS

inject_theme_css()

# Hero Header Banner
st.markdown("""
<div class="app-hero-banner">
    <div class="app-hero-title">🧮 Smart Budget Optimizer</div>
    <div class="app-hero-subtitle">Balance travel funds across transport, stays, dining, and activities with AI cost allocation</div>
</div>
""", unsafe_allow_html=True)

dest_names = [d["name"] for d in SAMPLE_DESTINATIONS]
dest_dict = {d["name"]: d for d in SAMPLE_DESTINATIONS}

with st.container(border=True):
    st.subheader(":material/tune: Budget Parameters", anchor=False)
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        total_budget = st.number_input("Target Total Budget (₹)", min_value=2000, max_value=500000, value=40000, step=1000)
        destination = st.selectbox("Target Destination", dest_names)
        duration = st.number_input("Trip Duration (Days)", min_value=1, max_value=30, value=5)
    with c2:
        travelers = st.number_input("Number of Travellers", min_value=1, max_value=10, value=2)
        acc_type = st.selectbox("Accommodation Tier", ["Mid-range Hotel", "Hostel / Homestay", "Luxury Resort / Palace"])
        food_style = st.selectbox("Dining Preference", ["Local Dining & Street Food", "Mixed Fine Dining & Cafes", "Exclusive Fine Dining"])
        activity_level = st.selectbox("Activity Level", ["Moderate", "Low / Relaxed", "High / Adventure Sports"])

selected_dest = dest_dict.get(destination, SAMPLE_DESTINATIONS[0])

# Cost Calculations
avg_daily = selected_dest.get("average_daily_cost", selected_dest.get("avg_daily_cost", 3000))

acc_mult = 1.6 if "Luxury" in acc_type else 0.7 if "Hostel" in acc_type else 1.0
food_mult = 1.5 if "Exclusive" in food_style else 0.7 if "Local" in food_style else 1.0
act_mult = 1.4 if "High" in activity_level else 0.8 if "Low" in activity_level else 1.0

# Base estimate is exactly what an average traveler spends
base_est = avg_daily * duration * travelers
est_transport = base_est * 0.25
est_hotel = base_est * 0.35 * acc_mult
est_food = base_est * 0.20 * food_mult
est_act = base_est * 0.15 * act_mult
est_misc = base_est * 0.05

total_est = est_transport + est_hotel + est_food + est_act + est_misc
delta = total_budget - total_est

# KPI Metrics Row
st.subheader(":material/monitoring: Budget Comparison Metrics", anchor=False)
m1, m2, m3 = st.columns(3)

with m1:
    with st.container(border=True):
        st.metric("Target Budget", format_currency(total_budget))
with m2:
    with st.container(border=True):
        st.metric("Your Estimated Cost", format_currency(total_est), delta=f"{format_currency(base_est - total_est)} vs Avg Traveller", delta_color="normal")
with m3:
    with st.container(border=True):
        if delta >= 0:
            st.metric("Budget Balance", format_currency(delta), delta="Within Budget 👍")
        else:
            st.metric("Budget Deficit", format_currency(abs(delta)), delta=f"-{format_currency(abs(delta))} Over", delta_color="inverse")

# Donut & Bar Charts
st.subheader(":material/analytics: Visual Breakdown & Allocation", anchor=False)
categories = ["Transport", "Accommodation", "Food & Dining", "Activities", "Miscellaneous"]
amounts = [est_transport, est_hotel, est_food, est_act, est_misc]

df_b = pd.DataFrame({"Category": categories, "Estimated Amount (₹)": amounts})

c1, c2 = st.columns(2, gap="medium")
with c1:
    st.markdown("#### Allocated Budget Donut Chart")
    fig_donut = px.pie(df_b, names="Category", values="Estimated Amount (₹)", hole=0.5,
                       color_discrete_sequence=["#0EA5E9", "#10B981", "#F59E0B", "#8B5CF6", "#64748B"])
    plotly_theme(fig_donut)
    st.plotly_chart(fig_donut, key="budget_donut_chart")

with c2:
    st.markdown("#### Cost Category Comparison")
    fig_bar = px.bar(df_b, x="Category", y="Estimated Amount (₹)", color="Category", text_auto=True)
    plotly_theme(fig_bar)
    st.plotly_chart(fig_bar, key="budget_bar_chart")

# Recommendations / Tips
st.subheader(":material/lightbulb: Where Your Money is Going & How to Save", anchor=False)
if delta < 0:
    st.warning(f"⚠️ Your plan exceeds your budget by **{format_currency(abs(delta))}**. Here are quick optimization tips:", icon=":material/warning:")
    if "Luxury" in acc_type:
        st.write("1. **Accommodation:** Consider switching from Luxury to Mid-range hotels to save up to 40%.")
    if "Exclusive" in food_style:
        st.write("2. **Food:** Mix fine-dining meals with authentic local cuisine shacks.")
    if "High" in activity_level:
        st.write("3. **Activities:** Balance paid adventure sports with free natural sightseeing.")
else:
    st.success(f"🎉 Excellent! You have **{format_currency(delta)}** remaining in surplus.", icon=":material/check_circle:")
    st.write("Since you are under budget, you might consider upgrading your accommodation tier or trying more exclusive dining experiences.")

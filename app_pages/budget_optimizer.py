"""
Budget Optimizer page for AI Trip Decision Optimizer.
"""
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import format_currency, plotly_theme
from utils.theme import inject_theme_css
from utils.images import get_destination_image
from recommendation.engine import SAMPLE_DESTINATIONS

inject_theme_css()

st.title(":material/calculate: Smart Budget Optimizer", anchor=False)
st.caption("Balance your travel funds across transport, luxury stays, fine dining, and activities with AI cost allocation.")

dest_names = [d["name"] for d in SAMPLE_DESTINATIONS]
dest_dict = {d["name"]: d for d in SAMPLE_DESTINATIONS}

with st.container(border=True):
    st.subheader(":material/tune: Budget Parameters", anchor=False)
    with st.form("budget_form"):
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

        submitted = st.form_submit_button("Calculate Optimized Budget", icon=":material/calculate:", type="primary")

selected_dest = dest_dict.get(destination, SAMPLE_DESTINATIONS[0])

# Destination Cover Banner
img_url = get_destination_image(destination, selected_dest.get("category"))
st.image(img_url, caption=f"Budget Optimization for {destination}")

# Cost Calculations
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

# KPI Metrics Row
st.subheader(":material/monitoring: Budget Comparison Metrics", anchor=False)
m1, m2, m3 = st.columns(3)

with m1:
    with st.container(border=True):
        st.metric("Target Budget", format_currency(total_budget))
with m2:
    with st.container(border=True):
        st.metric("Estimated Cost", format_currency(total_est))
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
    st.plotly_chart(fig_donut)

with c2:
    st.markdown("#### Cost Category Comparison")
    fig_bar = px.bar(df_b, x="Category", y="Estimated Amount (₹)", color="Category", text_auto="₹%.0f")
    plotly_theme(fig_bar)
    st.plotly_chart(fig_bar)

# Recommendations / Tips
if delta < 0:
    st.warning(f"⚠️ Your plan exceeds your budget by **{format_currency(abs(delta))}**. Here are quick optimization tips:", icon=":material/warning:")
    st.write("1. **Accommodation:** Consider switching from Luxury to Mid-range hotels to save up to 40%.")
    st.write("2. **Transport:** Check express trains instead of flight routes for nearby destinations.")
    st.write("3. **Food:** Mix fine-dining meals with authentic local cuisine shacks.")
else:
    st.success(f"🎉 Excellent! You have **{format_currency(delta)}** remaining in surplus.", icon=":material/check_circle:")

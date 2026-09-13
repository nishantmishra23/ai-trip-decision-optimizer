import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

try:
    from recommendation.engine import SAMPLE_DESTINATIONS
except ImportError:
    SAMPLE_DESTINATIONS = [
        {"name": "Goa", "avg_daily_cost": 3000},
        {"name": "Manali", "avg_daily_cost": 2500},
        {"name": "Jaipur", "avg_daily_cost": 2800},
        {"name": "Munnar", "avg_daily_cost": 2200}
    ]

try:
    from utils.helpers import db_status_banner, format_currency
except ImportError:
    def db_status_banner(): pass
    def format_currency(val): return f"₹{val:,.2f}"

st.title('Budget optimizer', anchor=False)
db_status_banner()

col1, col2 = st.columns(2)
with col1:
    total_budget = st.number_input("Total budget (₹)", min_value=1000, max_value=1000000, value=50000, step=1000)
    dest_names = [d["name"] for d in SAMPLE_DESTINATIONS]
    selected_dest = st.selectbox("Destination", dest_names)
    duration_days = st.number_input("Trip duration (days)", min_value=1, max_value=90, value=5)
    travelers_count = st.number_input("Travelers count", min_value=1, max_value=20, value=2)

with col2:
    acc_type = st.selectbox("Accommodation type", ["Budget", "Standard", "Luxury"])
    food_style = st.selectbox("Food style", ["Street Food", "Casual Dining", "Fine Dining"])
    activity_level = st.selectbox("Activity level", ["Low", "Medium", "High"])

# Base allocations
alloc = {"Transport": 0.20, "Hotel": 0.35, "Food": 0.20, "Activities": 0.15, "Misc": 0.10}

# Adjustments
if acc_type == "Luxury": alloc["Hotel"] += 0.10; alloc["Misc"] -= 0.05; alloc["Transport"] -= 0.05
elif acc_type == "Budget": alloc["Hotel"] -= 0.10; alloc["Misc"] += 0.05; alloc["Transport"] += 0.05

if food_style == "Fine Dining": alloc["Food"] += 0.10; alloc["Activities"] -= 0.05; alloc["Misc"] -= 0.05
elif food_style == "Street Food": alloc["Food"] -= 0.10; alloc["Activities"] += 0.05; alloc["Misc"] += 0.05

if activity_level == "High": alloc["Activities"] += 0.10; alloc["Hotel"] -= 0.05; alloc["Transport"] -= 0.05
elif activity_level == "Low": alloc["Activities"] -= 0.10; alloc["Hotel"] += 0.05; alloc["Transport"] += 0.05

# Normalize
total_alloc = sum(alloc.values())
for k in alloc: alloc[k] = alloc[k] / total_alloc

dest_obj = next((d for d in SAMPLE_DESTINATIONS if d["name"] == selected_dest), SAMPLE_DESTINATIONS[0])
avg_daily = dest_obj["avg_daily_cost"]

# Apply some multipliers based on selections to make estimated cost realistic
acc_mult = 1.5 if acc_type == "Luxury" else (0.7 if acc_type == "Budget" else 1.0)
food_mult = 1.3 if food_style == "Fine Dining" else (0.8 if food_style == "Street Food" else 1.0)
act_mult = 1.4 if activity_level == "High" else (0.7 if activity_level == "Low" else 1.0)

estimated_total = avg_daily * duration_days * travelers_count * ((acc_mult + food_mult + act_mult)/3)
difference = total_budget - estimated_total

st.divider()
st.subheader("Budget Analysis")
c1, c2, c3 = st.columns(3)
with c1:
    with st.container(border=True):
        st.metric("Total Budget", format_currency(total_budget))
with c2:
    with st.container(border=True):
        st.metric("Estimated Cost", format_currency(estimated_total))
with c3:
    with st.container(border=True):
        st.metric("Difference", format_currency(difference), delta=f"{difference:,.2f}")

if difference >= 0:
    if difference <= total_budget * 0.10:
        st.warning("You are within 10% of your budget. Monitor spending closely.")
    else:
        st.success("You are well under budget!")
else:
    st.error("You are over budget!")
    st.write("### Cost Saving Tips")
    st.write("1. Consider shifting to standard or budget accommodation.")
    st.write("2. Try local street food or casual dining.")
    st.write("3. Look for free or low-cost activities.")
    st.write("4. Use public transportation instead of private cabs.")
    st.write("5. Travel during off-peak seasons if possible.")

st.divider()
c1, c2 = st.columns(2)
with c1:
    budget_breakdown = {k: v * total_budget for k, v in alloc.items()}
    df_pie = pd.DataFrame(list(budget_breakdown.items()), columns=['Category', 'Amount'])
    fig_pie = px.pie(df_pie, values='Amount', names='Category', title='Budget Breakdown by Category', hole=0.4)
    st.plotly_chart(fig_pie)

with c2:
    est_breakdown = {k: v * estimated_total for k, v in alloc.items()}
    df_bar = pd.DataFrame({
        'Category': list(alloc.keys()) * 2,
        'Amount': list(budget_breakdown.values()) + list(est_breakdown.values()),
        'Type': ['Budgeted'] * 5 + ['Estimated'] * 5
    })
    fig_bar = px.bar(df_bar, x='Category', y='Amount', color='Type', barmode='group', title='Budgeted vs Estimated')
    st.plotly_chart(fig_bar)

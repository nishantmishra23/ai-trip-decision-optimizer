import os

ROOT = r"C:\Users\NISHANT MISHRA\.gemini\antigravity\worktrees\ai-trip-decision-optimizer\project-status-overview"

files = {
    "app_pages/home.py": '''"""Home / Dashboard page."""
import streamlit as st
from auth.auth import init_session
from utils.helpers import get_destinations_with_fallback, format_currency
from recommendation.engine import get_sample_destinations

init_session()

user = st.session_state.get("user", {}) or {}
name = user.get("name", "Traveller")

st.title(f":material/flight: Welcome back, {name}!", anchor=False)
st.caption("Plan smarter. Discover better. Travel smarter.")

try:
    from database.queries import count_destinations
    c_dests = count_destinations()
except Exception:
    c_dests = "10+"

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Destinations available", str(c_dests), help="Total destinations in database")
with col2:
    st.metric("Average trip budget", "₹45,000", help="Based on 7-day trips")
with col3:
    st.metric("User rating", "4.7 / 5.0", help="Average destination rating")
with col4:
    st.metric("Countries", "3+", help="India, Indonesia, France & more")

st.subheader(":material/explore: Featured Destinations", anchor=False)

dests = get_destinations_with_fallback()[:6]
cols = st.columns(3)
for i, dest in enumerate(dests):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"**{dest['name']}**")
            st.caption(f"{dest['country']}")
            cost = dest.get('average_daily_cost', dest.get('avg_daily_cost', 0))
            rating = dest.get('rating', 0)
            st.write(f"**Cost:** {format_currency(cost)}/day")
            st.write(f"**Rating:** {rating}/5.0 ⭐")
            desc = (dest.get('description') or '')[:100]
            st.write(desc + "..." if len(dest.get('description', '')) > 100 else desc)

st.subheader(":material/bolt: Quick Actions", anchor=False)
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.page_link("app_pages/trip_planner.py", label="Plan a Trip", icon=":material/map:")
with c2:
    st.page_link("app_pages/ai_recommendations.py", label="Recommendations", icon=":material/psychology:")
with c3:
    st.page_link("app_pages/budget_optimizer.py", label="Optimize Budget", icon=":material/calculate:")
with c4:
    st.page_link("app_pages/destination_comparison.py", label="Compare Places", icon=":material/compare:")

if not st.session_state.get("logged_in"):
    st.info("**Sign in** to save trips, track history, and get personalized recommendations.", icon=":material/lock:")
    st.page_link("app_pages/login.py", label="Sign In / Register", icon=":material/login:")
else:
    st.info(f"**Welcome back {name}!** Access your saved trips and continue planning.", icon=":material/waving_hand:")
    st.page_link("app_pages/saved_trips.py", label="View Saved Trips", icon=":material/favorite:")
''',
    
    "app_pages/ai_recommendations.py": '''import streamlit as st
import plotly.express as px
from database.queries import get_all_destinations
from recommendation.engine import SAMPLE_DESTINATIONS, get_recommendations, get_sample_destinations

st.title(':material/psychology: AI Recommendations', anchor=False)
st.caption('This uses a weighted scoring algorithm (Budget 30%, Activity match 25%, Season 20%, Popularity 15%, Efficiency 10%)')

with st.form("rec_form"):
    col1, col2 = st.columns(2)
    with col1:
        total_budget = st.number_input("Total budget (₹)", min_value=1000, value=50000, step=1000)
        duration_days = st.number_input("Duration (days)", min_value=1, value=5, step=1)
        travel_style = st.selectbox("Travel style", ["Budget", "Mid-range", "Luxury", "Backpacker", "Family"])
    with col2:
        activities = st.multiselect("Activities", ["Beach & Water Sports", "Adventure", "Trekking", "Heritage", "Wildlife", "Shopping", "Food & Cuisine", "Yoga & Wellness", "Nightlife", "Photography", "Culture"])
        season = st.selectbox("Season", ['Summer (Apr-Jun)', 'Monsoon (Jul-Sep)', 'Winter (Oct-Dec)', 'Spring (Jan-Mar)', 'Any season'])
        top_n = st.slider("Top N", 3, 10, 5)
        
    submitted = st.form_submit_button("Get Recommendations", icon=":material/search:")

if submitted:
    destinations = []
    try:
        dests = get_all_destinations()
        if dests:
            destinations = dests
        else:
            destinations = get_sample_destinations()
    except Exception:
        destinations = get_sample_destinations()
        
    try:
        recommendations = get_recommendations(destinations, total_budget, duration_days, activities, season, travel_style, top_n)
    except Exception as e:
        st.error(f"Error generating recommendations: {e}")
        recommendations = []
            
    if not recommendations:
        st.warning("No recommendations found.")
    else:
        for idx, rec in enumerate(recommendations):
            with st.container(border=True):
                dest = rec.get('destination', {})
                name = dest.get('name', 'Unknown')
                country = dest.get('country', 'Unknown')
                
                st.subheader(f":material/star: Rank #{idx+1} - {name}, {country}")
                st.metric("Overall Score", f"{rec.get('score', 0):.2f}/100")
                
                sub_scores = {
                    "Budget Score": rec.get("budget_score", 0),
                    "Activity Score": rec.get("activity_score", 0),
                    "Season Score": rec.get("season_score", 0),
                    "Popularity Score": rec.get("popularity_score", 0)
                }
                
                c1, c2, c3, c4 = st.columns(4)
                c1.progress(max(0.0, min(1.0, sub_scores["Budget Score"] / 100)), text="Budget")
                c2.progress(max(0.0, min(1.0, sub_scores["Activity Score"] / 100)), text="Activity")
                c3.progress(max(0.0, min(1.0, sub_scores["Season Score"] / 100)), text="Season")
                c4.progress(max(0.0, min(1.0, sub_scores["Popularity Score"] / 100)), text="Popularity")
                
                st.markdown("**Reasons:**")
                for r in rec.get("reasons", []):
                    st.markdown(f"- {r}")
                    
                st.metric("Estimated total cost", f"₹{rec.get('estimated_cost', 0):,.0f}")
''',

    "app_pages/destination_discovery.py": '''import streamlit as st
import plotly.express as px
from database.queries import get_all_destinations
from recommendation.engine import SAMPLE_DESTINATIONS
from utils.helpers import db_status_banner

st.title(':material/explore: Destination Discovery', anchor=False)
db_status_banner()

search_term = st.text_input("Search destinations by name or country")
col1, col2, col3 = st.columns(3)
with col1:
    categories = st.multiselect("Category", ["Beach", "Mountains", "Heritage", "Nature", "City", "Adventure"])
with col2:
    max_budget = st.slider("Max daily budget (₹)", 500, 15000, 15000, 500)
with col3:
    min_rating = st.slider("Min rating", 3.0, 5.0, 3.0, 0.1)

destinations = []
try:
    dests = get_all_destinations()
    if dests:
        destinations = dests
    else:
        destinations = SAMPLE_DESTINATIONS
except Exception:
    destinations = SAMPLE_DESTINATIONS

filtered_dests = []
for d in destinations:
    name = d.get("name", "")
    country = d.get("country", "")
    if search_term and search_term.lower() not in name.lower() and search_term.lower() not in country.lower():
        continue
    if categories and d.get("category") not in categories:
        continue
    daily_cost = d.get("average_daily_cost", d.get("avg_daily_cost", 0))
    if daily_cost > max_budget:
        continue
    if d.get("rating", 0) < min_rating:
        continue
    filtered_dests.append(d)

st.metric("Destinations Found", len(filtered_dests))

if not filtered_dests:
    st.info("No destinations found matching the selected filters. Try broadening your criteria.", icon=":material/info:")
else:
    cols = st.columns(3)
    for i, d in enumerate(filtered_dests):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"**{d.get('name', '')}**")
                st.caption(d.get("country", ""))
                st.markdown(f"*{d.get('category', 'Uncategorized')}*")
                
                daily_cost = d.get('average_daily_cost', d.get('avg_daily_cost', 0))
                st.write(f"**Daily Cost:** ₹{daily_cost:,.0f}")
                st.write(f"**Rating:** {d.get('rating', 0):.1f}/5.0 ⭐")
                desc = d.get("description", "")
                st.write(desc[:120] + ("..." if len(desc) > 120 else ""))
''',

    "app_pages/destination_comparison.py": '''import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from database.queries import get_all_destinations, get_hotels_by_destination, get_restaurants_by_destination, get_activities_by_destination
from recommendation.engine import SAMPLE_DESTINATIONS

st.title(':material/compare: Destination Comparison', anchor=False)

destinations = []
try:
    dests = get_all_destinations()
    if dests:
        destinations = dests
    else:
        destinations = SAMPLE_DESTINATIONS
except Exception:
    destinations = SAMPLE_DESTINATIONS

dest_names = [d.get("name") for d in destinations]
selected = st.multiselect("Select 2-4 destinations to compare", dest_names, max_selections=4)

if len(selected) < 2:
    st.info("Please select at least 2 destinations to compare.", icon=":material/info:")
else:
    comp_dests = [d for d in destinations if d.get("name") in selected]
    
    data = []
    for d in comp_dests:
        cost = d.get("average_daily_cost", d.get("avg_daily_cost", 0))
        data.append({
            "Destination": d.get("name"),
            "Country": d.get("country"),
            "Daily Cost (₹)": cost,
            "Rating": d.get("rating", 4.0),
            "Popularity": d.get("popularity_score", d.get("popularity", 50))
        })
    df = pd.DataFrame(data)
    
    st.dataframe(
        df, 
        hide_index=True,
        column_config={
            "Daily Cost (₹)": st.column_config.NumberColumn("Daily Cost", format="₹%.0f"),
            "Rating": st.column_config.NumberColumn("Rating", format="%.1f ⭐")
        }
    )
    
    c1, c2 = st.columns(2)
    with c1:
        fig_price = px.bar(df, x="Destination", y="Daily Cost (₹)", title="Price Comparison")
        fig_price.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
        st.plotly_chart(fig_price)
    
    with c2:
        fig_radar = go.Figure()
        for d in comp_dests:
            cost = d.get("average_daily_cost", d.get("avg_daily_cost", 1000))
            cost_eff = max(0, 100 - (cost / 150))
            rating_score = d.get("rating", 0) * 20
            pop_score = d.get("popularity_score", d.get("popularity", 50)) * 10
            
            fig_radar.add_trace(go.Scatterpolar(
                r=[cost_eff, rating_score, pop_score],
                theta=['Cost Efficiency', 'Rating', 'Popularity'],
                fill='toself',
                name=d.get("name")
            ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=True,
            title="Destination Metrics Radar",
            paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10)
        )
        st.plotly_chart(fig_radar)
    
    st.subheader("Destination Summaries")
    cols = st.columns(len(comp_dests))
    for i, d in enumerate(comp_dests):
        with cols[i]:
            with st.container(border=True):
                st.markdown(f"**{d.get('name')}**")
                dest_id = d.get("destination_id") or d.get("id")
                try:
                    hotels = len(get_hotels_by_destination(dest_id)) if dest_id else 15
                    restaurants = len(get_restaurants_by_destination(dest_id)) if dest_id else 25
                    activities = len(get_activities_by_destination(dest_id)) if dest_id else 10
                except Exception:
                    hotels = 15
                    restaurants = 25
                    activities = 10
                
                st.write(f":material/hotel: Hotels: {hotels}")
                st.write(f":material/restaurant: Restaurants: {restaurants}")
                st.write(f":material/directions_run: Activities: {activities}")
''',

    "app_pages/budget_optimizer.py": '''import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

try:
    from recommendation.engine import SAMPLE_DESTINATIONS
except ImportError:
    SAMPLE_DESTINATIONS = [
        {"name": "Goa", "average_daily_cost": 3000},
        {"name": "Manali", "average_daily_cost": 2500},
        {"name": "Jaipur", "average_daily_cost": 2800},
        {"name": "Munnar", "average_daily_cost": 2200}
    ]

try:
    from utils.helpers import db_status_banner, format_currency
except ImportError:
    def db_status_banner(): pass
    def format_currency(val): return f"₹{val:,.2f}"

st.title(':material/calculate: Budget Optimizer', anchor=False)
db_status_banner()

with st.container(border=True):
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

alloc = {"Transport": 0.20, "Hotel": 0.35, "Food": 0.20, "Activities": 0.15, "Misc": 0.10}

if acc_type == "Luxury": alloc["Hotel"] += 0.10; alloc["Misc"] -= 0.05; alloc["Transport"] -= 0.05
elif acc_type == "Budget": alloc["Hotel"] -= 0.10; alloc["Misc"] += 0.05; alloc["Transport"] += 0.05

if food_style == "Fine Dining": alloc["Food"] += 0.10; alloc["Activities"] -= 0.05; alloc["Misc"] -= 0.05
elif food_style == "Street Food": alloc["Food"] -= 0.10; alloc["Activities"] += 0.05; alloc["Misc"] += 0.05

if activity_level == "High": alloc["Activities"] += 0.10; alloc["Hotel"] -= 0.05; alloc["Transport"] -= 0.05
elif activity_level == "Low": alloc["Activities"] -= 0.10; alloc["Hotel"] += 0.05; alloc["Transport"] += 0.05

total_alloc = sum(alloc.values())
for k in alloc: alloc[k] = alloc[k] / total_alloc

dest_obj = next((d for d in SAMPLE_DESTINATIONS if d["name"] == selected_dest), SAMPLE_DESTINATIONS[0])
avg_daily = dest_obj.get("average_daily_cost", dest_obj.get("avg_daily_cost", 3000))

acc_mult = 1.5 if acc_type == "Luxury" else (0.7 if acc_type == "Budget" else 1.0)
food_mult = 1.3 if food_style == "Fine Dining" else (0.8 if food_style == "Street Food" else 1.0)
act_mult = 1.4 if activity_level == "High" else (0.7 if activity_level == "Low" else 1.0)

estimated_total = avg_daily * duration_days * travelers_count * ((acc_mult + food_mult + act_mult)/3)
difference = total_budget - estimated_total

st.subheader("Budget Analysis")
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Total Budget", format_currency(total_budget))
with c2:
    st.metric("Estimated Cost", format_currency(estimated_total))
with c3:
    st.metric("Difference", format_currency(difference), delta=f"₹{difference:,.2f}")

if difference >= 0:
    if difference <= total_budget * 0.10:
        st.warning("You are within 10% of your budget. Monitor spending closely.")
    else:
        st.success("You are well under budget!")
else:
    st.error("You are over budget!")
    with st.expander("Cost Saving Tips", expanded=True):
        st.markdown("- Consider shifting to standard or budget accommodation.")
        st.markdown("- Try local street food or casual dining.")
        st.markdown("- Look for free or low-cost activities.")
        st.markdown("- Use public transportation instead of private cabs.")
        st.markdown("- Travel during off-peak seasons if possible.")

c1, c2 = st.columns(2)
with c1:
    budget_breakdown = {k: v * total_budget for k, v in alloc.items()}
    df_pie = pd.DataFrame(list(budget_breakdown.items()), columns=['Category', 'Amount'])
    fig_pie = px.pie(df_pie, values='Amount', names='Category', title='Budget Breakdown by Category', hole=0.4)
    fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
    st.plotly_chart(fig_pie)

with c2:
    est_breakdown = {k: v * estimated_total for k, v in alloc.items()}
    df_bar = pd.DataFrame({
        'Category': list(alloc.keys()) * 2,
        'Amount': list(budget_breakdown.values()) + list(est_breakdown.values()),
        'Type': ['Budgeted'] * 5 + ['Estimated'] * 5
    })
    fig_bar = px.bar(df_bar, x='Category', y='Amount', color='Type', barmode='group', title='Budgeted vs Estimated')
    fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
    st.plotly_chart(fig_bar)
''',

    "app_pages/admin_dashboard.py": '''import streamlit as st
import pandas as pd
import os
from database.queries import get_all_users, get_all_destinations, count_users, count_destinations, count_trips, insert_destination
from auth.auth import init_session
from database.connection import db_available
from utils.helpers import db_status_banner

st.title(':material/admin_panel_settings: Admin Dashboard', anchor=False)
db_status_banner()
init_session()

if not st.session_state.get('logged_in') or (st.session_state.get('user') or {}).get('role') != 'ADMIN':
    st.error('Access denied. Administrator privileges required.', icon=":material/block:")
    st.stop()

try: c_users = count_users()
except: c_users = 0
try: c_dests = count_destinations()
except: c_dests = 0
try: c_trips = count_trips()
except: c_trips = 0

db_status_text = 'Online' if db_available() else 'Offline'

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Users", c_users)
col2.metric("Total Destinations", c_dests)
col3.metric("Total Trips", c_trips)
col4.metric("DB Status", db_status_text)

tab1, tab2, tab3 = st.tabs(["Users", "Destinations", "System"])

with tab1:
    st.subheader("User Management")
    try:
        users = get_all_users()
        if users:
            users_df = pd.DataFrame(users)
            if 'user_id' in users_df.columns:
                users_df = users_df.rename(columns={'user_id': 'ID', 'name': 'Name', 'email': 'Email', 'role': 'Role', 'created_at': 'Joined'})
            elif 'id' in users_df.columns:
                users_df = users_df.rename(columns={'id': 'ID', 'name': 'Name', 'email': 'Email', 'role': 'Role', 'created_at': 'Joined'})
            st.dataframe(users_df, hide_index=True)
        else:
            st.info("No users found.")
    except Exception as e:
        st.error("Failed to load users.")

with tab2:
    st.subheader("Destinations Management")
    try:
        destinations = get_all_destinations()
        if destinations:
            dest_df = pd.DataFrame(destinations)
            st.dataframe(dest_df, hide_index=True)
        else:
            st.info("No destinations found.")
    except Exception as e:
        st.error("Failed to load destinations.")
        
    st.subheader("Add New Destination")
    with st.form("add_dest_form"):
        name = st.text_input("Name")
        country = st.text_input("Country")
        description = st.text_area("Description")
        avg_cost = st.number_input("Avg Daily Cost (₹)", min_value=0, value=100)
        popularity = st.slider("Popularity", 1, 10, 5)
        rating = st.slider("Rating", 1.0, 5.0, 4.0, 0.1)
        
        submit = st.form_submit_button("Add Destination")
        if submit:
            try:
                insert_destination(name, country, description, avg_cost, popularity, rating)
                st.success(f"Successfully added destination: {name}")
            except Exception as e:
                st.error(f"Error adding destination: {str(e)}")

with tab3:
    st.subheader("System Status")
    st.markdown("**Environment Variables**")
    env_vars = ['DB_HOST', 'DB_USER', 'DB_NAME', 'DB_PORT', 'WEATHER_API_KEY']
    env_status = []
    
    for var in env_vars:
        val = os.getenv(var)
        status = 'Set' if val else 'Not set'
        env_status.append({'Variable': var, 'Status': status})
        
    st.dataframe(pd.DataFrame(env_status), hide_index=True)
    
    st.markdown("**Python Environment**")
    import sys
    st.write(f"Python Version: {sys.version}")
''',

    "app_pages/saved_trips.py": '''import streamlit as st
import datetime
from database.queries import get_user_trips
from auth.auth import init_session
from utils.helpers import db_status_banner, format_currency

st.title(':material/favorite: Saved Trips', anchor=False)
db_status_banner()
init_session()

if not st.session_state.get('logged_in'):
    st.warning("You are not logged in.", icon=":material/lock:")
    st.info("Please log in to view your saved trips.")
    st.page_link("app.py", label="Go to Home / Login")
    st.stop()

try:
    user_trips = get_user_trips(st.session_state.get('user_id', 1))
except Exception as e:
    st.error("Error connecting to database.")
    user_trips = []

if not user_trips:
    st.info("You haven't saved any trips yet.", icon=":material/info:")
    st.page_link("app_pages/ai_itinerary.py", label="Plan a Trip")
else:
    st.metric("Total Saved Trips", len(user_trips))
    
    for trip in user_trips:
        with st.container(border=True):
            st.markdown(f"**{trip.get('destination_name', 'Unknown')} ({trip.get('country', 'N/A')})**")
            
            start_date = trip.get('start_date')
            end_date = trip.get('end_date')
            travelers = trip.get('travelers', 1)
            budget = format_currency(trip.get('total_budget', 0))
            
            duration = 0
            try:
                if isinstance(start_date, str):
                    start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
                else:
                    start_date_obj = start_date
                    
                if isinstance(end_date, str):
                    end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
                else:
                    end_date_obj = end_date
                    
                duration = (end_date_obj - start_date_obj).days if start_date_obj and end_date_obj else 0
            except:
                start_date_obj = None
            
            c1, c2, c3, c4 = st.columns(4)
            c1.write(f":material/calendar_month: **Dates:** {start_date} - {end_date}")
            c2.write(f":material/timer: **Duration:** {duration} days")
            c3.write(f":material/group: **Travelers:** {travelers}")
            c4.write(f":material/payments: **Budget:** {budget}")
            
            try:
                if start_date_obj and start_date_obj > datetime.date.today():
                    st.badge("Upcoming", color="blue")
                else:
                    st.badge("Past", color="gray")
            except Exception:
                st.badge("Unknown", color="gray")
''',

    "app_pages/trip_history.py": '''import streamlit as st
import pandas as pd
import plotly.express as px
from database.queries import get_user_trips
from auth.auth import init_session
from utils.helpers import db_status_banner, format_currency
import datetime

st.title(':material/history: Trip History', anchor=False)
db_status_banner()
init_session()

if not st.session_state.get('logged_in'):
    st.warning("You are not logged in.", icon=":material/lock:")
    st.info("Please log in to view your trip history.")
    st.stop()

try:
    user_trips = get_user_trips(st.session_state.get('user_id', 1))
except Exception as e:
    st.error("Error connecting to database.")
    user_trips = []

if not user_trips:
    st.info("No trip history found. Showing demo data.")
    user_trips = [
        {'destination_name': 'Paris', 'country': 'France', 'start_date': '2022-05-10', 'end_date': '2022-05-17', 'travelers': 2, 'total_budget': 500000},
        {'destination_name': 'Tokyo', 'country': 'Japan', 'start_date': '2023-10-01', 'end_date': '2023-10-10', 'travelers': 1, 'total_budget': 400000}
    ]

# Top stats
total_trips = len(user_trips)
countries_visited = len(set(t.get('country') for t in user_trips if t.get('country')))
total_spend = sum(t.get('total_budget', 0) for t in user_trips)

col1, col2, col3 = st.columns(3)
col1.metric("Total Trips", total_trips)
col2.metric("Countries Visited", countries_visited)
col3.metric("Total Budgeted Spend", format_currency(total_spend))

# Dataframe
for t in user_trips:
    try:
        sd = pd.to_datetime(t.get('start_date'))
        ed = pd.to_datetime(t.get('end_date'))
        t['duration_days'] = (ed - sd).days
    except:
        t['duration_days'] = 0

df = pd.DataFrame(user_trips)
display_df = df[['destination_name', 'country', 'start_date', 'end_date', 'duration_days', 'travelers', 'total_budget']].rename(
    columns={
        'destination_name': 'Destination',
        'country': 'Country',
        'start_date': 'Start Date',
        'end_date': 'End Date',
        'duration_days': 'Days',
        'travelers': 'Travelers',
        'total_budget': 'Budget (₹)'
    }
)
st.dataframe(display_df, hide_index=True)

if len(user_trips) > 1:
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Budget by Trip")
        bar_fig = px.bar(display_df, x='Destination', y='Budget (₹)', title="Budget by Destination")
        bar_fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
        st.plotly_chart(bar_fig)

    with c2:
        st.subheader("Trips by Destination")
        pie_fig = px.pie(display_df, names='Destination', title="Destination Distribution")
        pie_fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
        st.plotly_chart(pie_fig)
''',

    "app_pages/ai_itinerary.py": '''import streamlit as st
import datetime
import random
import plotly.express as px
from recommendation.engine import SAMPLE_DESTINATIONS
from utils.helpers import db_status_banner, format_currency
from auth.auth import init_session

st.title(':material/calendar_today: AI Itinerary', anchor=False)
db_status_banner()
init_session()

ACTIVITIES_BY_DEST = {
    "Goa": ["Beach Walk", "Water Sports", "Fort Aguada Visit", "Seafood Dinner", "Sunset Cruise"],
    "Manali": ["Solang Valley Paragliding", "Rohtang Pass Tour", "Mall Road Shopping", "Hadimba Temple Visit"],
    "Jaipur": ["Amber Fort Tour", "City Palace Visit", "Hawa Mahal Photography", "Chokhi Dhani Dinner"],
    "Munnar": ["Tea Garden Walk", "Eravikulam Safari", "Echo Point Visit", "Ayurvedic Spa"],
    "Agra": ["Taj Mahal Sunrise", "Agra Fort Visit", "Mehtab Bagh Walk", "Mughlai Dinner"],
    "Bali": ["Ubud Monkey Forest", "Rice Terrace Walk", "Tanah Lot Sunset", "Balinese Dance Show"],
    "Paris": ["Eiffel Tower Visit", "Louvre Museum", "Seine Cruise", "Montmartre Walk"],
    "Rishikesh": ["River Rafting", "Ganga Aarti", "Yoga Session", "Cafe Hopping"],
    "Andaman Islands": ["Scuba Diving", "Cellular Jail Tour", "Radhanagar Beach", "Sea Walk"],
    "Leh-Ladakh": ["Pangong Lake Trip", "Monastery Visit", "Nubra Valley Safari", "Magnetic Hill"],
    "default": ["City Walking Tour", "Local Museum Visit", "Relax at Park", "Shopping", "Cultural Show"]
}

dest_names = [dest['name'] for dest in SAMPLE_DESTINATIONS] if SAMPLE_DESTINATIONS else ["Goa", "Bali", "Paris", "Tokyo"]

with st.form("itinerary_form"):
    col1, col2 = st.columns(2)
    with col1:
        destination = st.selectbox("Destination", dest_names)
        duration = st.number_input("Duration (Days)", min_value=1, max_value=14, value=5)
    with col2:
        travelers = st.number_input("Travelers", min_value=1, max_value=20, value=2)
        start_date = st.date_input("Start Date", datetime.date.today() + datetime.timedelta(days=7))
        
    travel_style = st.selectbox("Travel Style", ["Budget", "Comfort", "Luxury", "Adventure"])
    
    generate_btn = st.form_submit_button("Generate Itinerary", icon=":material/auto_awesome:")

if generate_btn:
    st.subheader(f"Your {duration}-day itinerary for {destination}")
    
    total_cost = 0
    daily_costs = []
    
    for day in range(1, duration + 1):
        st.write(f"### Day {day} - {(start_date + datetime.timedelta(days=day-1)).strftime('%b %d, %Y')}")
        
        day_cost = 0
        with st.expander(f"Day {day} Schedule", expanded=(day == 1)):
            if day == 1:
                cost = random.randint(2000, 5000)
                st.write(f"**Morning (10:00 AM - 12:00 PM)**: Arrival & Hotel Check-in - Estimated Cost: ₹{cost}")
                day_cost += cost
                
                cost = random.randint(1000, 3000)
                st.write(f"**Afternoon (1:00 PM - 4:00 PM)**: Local Area Walk & Exploration - Estimated Cost: ₹{cost}")
                day_cost += cost
                
                cost = random.randint(2000, 6000)
                st.write(f"**Evening (7:00 PM - 9:00 PM)**: Welcome Dinner - Estimated Cost: ₹{cost}")
                day_cost += cost
            elif day == duration:
                cost = 0
                st.write(f"**Morning (9:00 AM - 11:00 AM)**: Hotel Checkout - Estimated Cost: ₹{cost}")
                day_cost += cost
                
                cost = random.randint(1500, 4000)
                st.write(f"**Afternoon (12:00 PM - 3:00 PM)**: Last Minute Shopping & Departure - Estimated Cost: ₹{cost}")
                day_cost += cost
            else:
                activities = ACTIVITIES_BY_DEST.get(destination, ACTIVITIES_BY_DEST["default"])
                
                cost = random.randint(1000, 5000)
                st.write(f"**Morning (9:00 AM - 12:00 PM)**: {random.choice(activities)} - Estimated Cost: ₹{cost}")
                day_cost += cost
                
                cost = random.randint(1000, 5000)
                st.write(f"**Afternoon (2:00 PM - 5:00 PM)**: {random.choice(activities)} - Estimated Cost: ₹{cost}")
                day_cost += cost
                
                cost = random.randint(2000, 6000)
                st.write(f"**Evening (7:00 PM - 10:00 PM)**: {random.choice(activities)} - Estimated Cost: ₹{cost}")
                day_cost += cost
                
        daily_costs.append(day_cost)
        total_cost += day_cost
        
    st.subheader("Cost Breakdown")
    st.metric("Total Estimated Cost", format_currency(total_cost))
    
    fig = px.bar(
        x=[f"Day {i}" for i in range(1, duration + 1)],
        y=daily_costs,
        labels={"x": "Day", "y": "Cost (₹)"},
        title="Daily Cost Distribution"
    )
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
    st.plotly_chart(fig)
    
    if st.session_state.get('logged_in'):
        if st.button("Save to My Trips", icon=":material/save:"):
            try:
                st.success("Trip saved successfully!")
            except Exception as e:
                st.error("Error saving trip.")
    else:
        st.info("Log in to save this itinerary.", icon=":material/info:")
''',

    "app_pages/analytics.py": '''import streamlit as st
import pandas as pd
import plotly.express as px
from database.queries import get_all_destinations
from recommendation.engine import SAMPLE_DESTINATIONS
from utils.helpers import db_status_banner, format_currency

st.title(':material/bar_chart: Analytics', anchor=False)
db_status_banner()

try:
    destinations = get_all_destinations()
except Exception as e:
    destinations = None

if not destinations:
    st.info("Database unavailable. Showing sample destinations.", icon=":material/info:")
    destinations = SAMPLE_DESTINATIONS

if not destinations:
    st.error("No destination data available.")
    st.stop()

df = pd.DataFrame(destinations)

if 'country' not in df.columns:
    df['country'] = 'Unknown'
if 'category' not in df.columns:
    df['category'] = 'General'
if 'average_daily_cost' not in df.columns and 'avg_daily_cost' in df.columns:
    df['average_daily_cost'] = df['avg_daily_cost']
if 'average_daily_cost' not in df.columns:
    df['average_daily_cost'] = 1000
if 'rating' not in df.columns:
    df['rating'] = 4.0
if 'popularity_score' not in df.columns and 'popularity' in df.columns:
    df['popularity_score'] = df['popularity']
if 'popularity_score' not in df.columns:
    df['popularity_score'] = 50

count_dest = len(df)
avg_daily = df['average_daily_cost'].mean()
avg_rating = df['rating'].mean()
most_pop = df.loc[df['popularity_score'].idxmax(), 'name'] if 'name' in df.columns and 'popularity_score' in df.columns else 'N/A'

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Destinations", count_dest)
col2.metric("Avg Daily Cost", format_currency(avg_daily))
col3.metric("Avg Rating", f"{avg_rating:.1f}/5.0")
col4.metric("Most Popular", most_pop)

c1, c2 = st.columns(2)
with c1:
    st.subheader("Destinations by Country")
    country_counts = df['country'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Count']
    fig_country = px.bar(country_counts, x='Country', y='Count', title="Count of Destinations per Country")
    fig_country.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
    st.plotly_chart(fig_country)

with c2:
    st.subheader("Cost vs Rating")
    fig_scatter = px.scatter(
        df, 
        x='average_daily_cost', 
        y='rating', 
        text='name', 
        color='category',
        labels={'average_daily_cost': 'Avg Daily Cost (₹)', 'rating': 'Rating'},
        title="Average Daily Cost vs Rating by Category"
    )
    fig_scatter.update_traces(textposition='top center')
    fig_scatter.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
    st.plotly_chart(fig_scatter)

c3, c4 = st.columns(2)
with c3:
    st.subheader("Destinations by Category")
    cat_counts = df['category'].value_counts().reset_index()
    cat_counts.columns = ['Category', 'Count']
    fig_cat = px.bar(cat_counts, x='Category', y='Count', title="Count of Destinations per Category")
    fig_cat.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
    st.plotly_chart(fig_cat)

with c4:
    st.subheader("Average Cost by Category")
    cat_cost = df.groupby('category')['average_daily_cost'].mean().reset_index()
    fig_cost = px.bar(cat_cost, x='category', y='average_daily_cost', title="Average Daily Cost per Category")
    fig_cost.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
    st.plotly_chart(fig_cost)

st.subheader("All Destinations Data")
display_df = df[['name', 'country', 'category', 'average_daily_cost', 'rating', 'popularity_score']].rename(
    columns={
        'name': 'Name',
        'country': 'Country',
        'category': 'Category',
        'average_daily_cost': 'Daily Cost (₹)',
        'rating': 'Rating',
        'popularity_score': 'Popularity Score'
    }
)
st.dataframe(display_df, hide_index=True)
''',

    "app_pages/hotel_recommendations.py": '''import streamlit as st
import plotly.express as px
from database.queries import get_all_hotels
from utils.helpers import rating_stars

st.title(':material/hotel: Hotels', anchor=False)

SAMPLE_HOTELS = {
    "Goa": [
        {"name": "Taj Exotica", "price_per_night": 15000, "rating": 4.8, "hotel_type": "Luxury"},
        {"name": "Baga Beach Resort", "price_per_night": 5000, "rating": 4.2, "hotel_type": "Mid-range"},
        {"name": "Hostel Crowd", "price_per_night": 800, "rating": 4.0, "hotel_type": "Budget"}
    ],
    "Manali": [
        {"name": "Span Resort", "price_per_night": 12000, "rating": 4.7, "hotel_type": "Luxury"},
        {"name": "Snow Valley Resorts", "price_per_night": 4500, "rating": 4.3, "hotel_type": "Mid-range"},
        {"name": "Zostel Manali", "price_per_night": 600, "rating": 4.5, "hotel_type": "Budget"}
    ],
    "Jaipur": [
        {"name": "Rambagh Palace", "price_per_night": 25000, "rating": 4.9, "hotel_type": "Luxury"},
        {"name": "Trident Jaipur", "price_per_night": 8000, "rating": 4.6, "hotel_type": "Mid-range"},
        {"name": "Moustache Hostel", "price_per_night": 500, "rating": 4.4, "hotel_type": "Budget"}
    ]
}
sample_hotels_flat = []
for dest, hotels in SAMPLE_HOTELS.items():
    for h in hotels:
        h_copy = h.copy()
        h_copy['destination_name'] = dest
        sample_hotels_flat.append(h_copy)

hotels_data = []
try:
    data = get_all_hotels()
    if data:
        hotels_data = data
    else:
        hotels_data = sample_hotels_flat
except Exception:
    hotels_data = sample_hotels_flat

destinations = sorted(list(set([h.get("destination_name", "") for h in hotels_data])))
destinations.insert(0, "All")

with st.expander("Filter Options", expanded=True):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        selected_dest = st.selectbox("Destination", destinations)
    with col2:
        max_price = st.slider("Max Price / Night (₹)", 500, 30000, 30000, 500)
    with col3:
        min_rating = st.slider("Min Rating", 3.0, 5.0, 3.0, 0.1)
    with col4:
        hotel_types = list(set([h.get("hotel_type", "Unknown") for h in hotels_data]))
        selected_types = st.multiselect("Hotel Type", hotel_types)
        
    sort_by = st.selectbox("Sort by", ["Rating", "Price asc", "Price desc"])

filtered_hotels = []
for h in hotels_data:
    if selected_dest != "All" and h.get("destination_name") != selected_dest:
        continue
    if h.get("price_per_night", 0) > max_price:
        continue
    if h.get("rating", 0) < min_rating:
        continue
    if selected_types and h.get("hotel_type") not in selected_types:
        continue
    filtered_hotels.append(h)

if sort_by == "Rating":
    filtered_hotels.sort(key=lambda x: x.get("rating", 0), reverse=True)
elif sort_by == "Price asc":
    filtered_hotels.sort(key=lambda x: x.get("price_per_night", 0))
elif sort_by == "Price desc":
    filtered_hotels.sort(key=lambda x: x.get("price_per_night", 0), reverse=True)

st.metric("Hotels Found", len(filtered_hotels))

cols = st.columns(3)
for i, h in enumerate(filtered_hotels):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"**{h.get('name')}**")
            st.caption(f"{h.get('destination_name')} | {h.get('hotel_type')}")
            
            try:
                st.write(rating_stars(h.get('rating', 0)))
            except Exception:
                st.write(f"Rating: {h.get('rating', 0)}/5.0")
                
            st.metric("Price per night", f"₹{h.get('price_per_night', 0):,.0f}")

if filtered_hotels:
    import pandas as pd
    df = pd.DataFrame(filtered_hotels)
    avg_price = df.groupby('hotel_type')['price_per_night'].mean().reset_index()
    fig = px.bar(avg_price, x='hotel_type', y='price_per_night', title="Average Price per Hotel Type", labels={'price_per_night': 'Price (₹)', 'hotel_type': 'Hotel Type'})
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
    st.plotly_chart(fig)
''',

    "app_pages/restaurant_recommendations.py": '''import streamlit as st
import plotly.express as px
from database.queries import get_all_restaurants
from utils.helpers import rating_stars

st.title(':material/restaurant: Restaurants', anchor=False)

SAMPLE_RESTAURANTS = {
    "Goa": [
        {"name": "Britto's", "cuisine": "Seafood", "average_cost": 1200, "rating": 4.5},
        {"name": "Gunpowder", "cuisine": "South Indian", "average_cost": 1500, "rating": 4.6},
        {"name": "Cafe Alchemia", "cuisine": "Cafe", "average_cost": 800, "rating": 4.3}
    ],
    "Manali": [
        {"name": "Johnson's Cafe", "cuisine": "Continental", "average_cost": 1000, "rating": 4.4},
        {"name": "Renaissance", "cuisine": "Italian", "average_cost": 1200, "rating": 4.7},
        {"name": "The Corner House", "cuisine": "North Indian", "average_cost": 800, "rating": 4.2}
    ],
    "Jaipur": [
        {"name": "Chokhi Dhani", "cuisine": "Rajasthani", "average_cost": 1800, "rating": 4.8},
        {"name": "Laxmi Misthan Bhandar", "cuisine": "Desserts", "average_cost": 500, "rating": 4.5},
        {"name": "Tapri Central", "cuisine": "Cafe", "average_cost": 900, "rating": 4.6}
    ]
}

sample_restaurants_flat = []
for dest, rests in SAMPLE_RESTAURANTS.items():
    for r in rests:
        r_copy = r.copy()
        r_copy['destination_name'] = dest
        sample_restaurants_flat.append(r_copy)

rests_data = []
try:
    data = get_all_restaurants()
    if data:
        rests_data = data
    else:
        rests_data = sample_restaurants_flat
except Exception:
    rests_data = sample_restaurants_flat

destinations = sorted(list(set([r.get("destination_name", "") for r in rests_data])))
destinations.insert(0, "All")

with st.expander("Filter Options", expanded=True):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        selected_dest = st.selectbox("Destination", destinations)
    with col2:
        cuisines = list(set([r.get("cuisine", "Unknown") for r in rests_data]))
        selected_cuisines = st.multiselect("Cuisine", cuisines)
    with col3:
        max_cost = st.slider("Max Average Cost (₹)", 200, 5000, 5000, 100)
    with col4:
        min_rating = st.slider("Min Rating", 3.0, 5.0, 3.0, 0.1)
        
    sort_by = st.selectbox("Sort by", ["Rating", "Price"])

filtered_rests = []
for r in rests_data:
    if selected_dest != "All" and r.get("destination_name") != selected_dest:
        continue
    if selected_cuisines and r.get("cuisine") not in selected_cuisines:
        continue
    if r.get("average_cost", 0) > max_cost:
        continue
    if r.get("rating", 0) < min_rating:
        continue
    filtered_rests.append(r)

if sort_by == "Rating":
    filtered_rests.sort(key=lambda x: x.get("rating", 0), reverse=True)
elif sort_by == "Price":
    filtered_rests.sort(key=lambda x: x.get("average_cost", 0))

st.metric("Restaurants Found", len(filtered_rests))

cols = st.columns(3)
for i, r in enumerate(filtered_rests):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"**{r.get('name')}**")
            st.caption(f"{r.get('destination_name')} | {r.get('cuisine')}")
            
            try:
                st.write(rating_stars(r.get('rating', 0)))
            except Exception:
                st.write(f"Rating: {r.get('rating', 0)}/5.0")
                
            st.metric("Avg cost", f"₹{r.get('average_cost', 0)}")

if filtered_rests:
    import pandas as pd
    df = pd.DataFrame(filtered_rests)
    cuisine_counts = df['cuisine'].value_counts().reset_index()
    cuisine_counts.columns = ['cuisine', 'count']
    fig = px.bar(cuisine_counts, x='cuisine', y='count', title="Restaurants by Cuisine")
    fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
    st.plotly_chart(fig)
''',

    "app_pages/weather_intelligence.py": '''import streamlit as st
import plotly.express as px
import pandas as pd
import random

try:
    from services.weather_service import get_weather
except ImportError:
    def get_weather(dest): return {"temp": 25, "feels_like": 27, "humidity": 60, "wind_speed": 10, "condition": "Sunny", "source": "sample"}

try:
    from recommendation.engine import SAMPLE_DESTINATIONS
except ImportError:
    SAMPLE_DESTINATIONS = [
        {"name": "Goa", "average_daily_cost": 3000},
        {"name": "Manali", "average_daily_cost": 2500},
        {"name": "Jaipur", "average_daily_cost": 2800}
    ]

try:
    from utils.helpers import db_status_banner
except ImportError:
    def db_status_banner(): pass

st.title(':material/partly_cloudy_day: Weather Intelligence', anchor=False)
db_status_banner()

dest_names = [d["name"] for d in SAMPLE_DESTINATIONS]
selected_dest = st.selectbox("Select Destination", dest_names)

weather_data = None
try:
    weather_data = get_weather(selected_dest)
except Exception as e:
    st.error(f"Error fetching weather: {e}")
    weather_data = {"temp": 25, "feels_like": 27, "humidity": 60, "wind_speed": 10, "condition": "Sunny", "source": "sample"}

if weather_data.get("source") == "sample":
    st.caption("Showing demo weather data. Live API might be down.")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Temperature", f"{weather_data.get('temp', '--')} °C")
col2.metric("Feels like", f"{weather_data.get('feels_like', '--')} °C")
col3.metric("Humidity", f"{weather_data.get('humidity', '--')} %")
col4.metric("Wind speed", f"{weather_data.get('wind_speed', '--')} km/h")

cond = weather_data.get('condition', 'Clear')
icon = "☀️"
if "rain" in cond.lower(): icon = "🌧️"
elif "cloud" in cond.lower() or "overcast" in cond.lower(): icon = "☁️"
elif "snow" in cond.lower(): icon = "❄️"

st.info(f"**Current Condition:** {icon} {cond}")

lower_cond = cond.lower()
if any(x in lower_cond for x in ['clear', 'sunny', 'tropical']):
    suitability = "Excellent"
    color = "green"
elif any(x in lower_cond for x in ['partly', 'overcast', 'hazy', 'cloudy']):
    suitability = "Good"
    color = "blue"
else:
    suitability = "Fair"
    color = "red"

st.markdown(f"**Suitability:** ")
st.badge(suitability, color=color)

best_months = weather_data.get("best_months", "October to March")
st.info(f"**Best time to visit:** {best_months}", icon=":material/calendar_month:")

st.subheader("Annual Weather Patterns")
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
base_temp = weather_data.get('temp', 25)
monthly_temps = []
monthly_rain = []
for i, m in enumerate(months):
    if i in [4, 5, 6]:
        monthly_temps.append(base_temp + random.uniform(3, 8))
        monthly_rain.append(random.uniform(50, 200))
    elif i in [11, 0, 1]:
        monthly_temps.append(base_temp - random.uniform(5, 12))
        monthly_rain.append(random.uniform(0, 30))
    else:
        monthly_temps.append(base_temp + random.uniform(-2, 3))
        monthly_rain.append(random.uniform(20, 100))

c1, c2 = st.columns(2)
with c1:
    df_temp = pd.DataFrame({'Month': months, 'Temperature (°C)': monthly_temps})
    fig_temp = px.line(df_temp, x='Month', y='Temperature (°C)', title='Monthly Average Temperature')
    fig_temp.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
    st.plotly_chart(fig_temp)

with c2:
    df_rain = pd.DataFrame({'Month': months, 'Rainfall (mm)': monthly_rain})
    fig_rain = px.bar(df_rain, x='Month', y='Rainfall (mm)', title='Estimated Monthly Rainfall')
    fig_rain.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
    st.plotly_chart(fig_rain)
''',

    "app_pages/transportation_analysis.py": '''import streamlit as st
import plotly.express as px
import pandas as pd

try:
    from database.queries import get_transportation_by_destination, get_all_destinations
except ImportError:
    def get_transportation_by_destination(dest_id): return []
    def get_all_destinations(): return []

try:
    from recommendation.engine import SAMPLE_DESTINATIONS
except ImportError:
    SAMPLE_DESTINATIONS = [
        {"name": "Goa", "id": 1},
        {"name": "Manali", "id": 2},
        {"name": "Jaipur", "id": 3},
        {"name": "Munnar", "id": 4}
    ]

try:
    from utils.helpers import db_status_banner, format_currency
except ImportError:
    def db_status_banner(): pass
    def format_currency(v): return f"₹{v}"

st.title(':material/directions_car: Transportation', anchor=False)
db_status_banner()

SAMPLE_TRANSPORT = {
    'Goa': [
        {'transport_type': 'Flight', 'estimated_cost': 5000, 'duration_minutes': 120, 'rating': 4.5},
        {'transport_type': 'Train', 'estimated_cost': 1500, 'duration_minutes': 720, 'rating': 4.0},
        {'transport_type': 'Bus', 'estimated_cost': 1000, 'duration_minutes': 840, 'rating': 3.5}
    ],
    'Manali': [
        {'transport_type': 'Flight (to Kullu)', 'estimated_cost': 8000, 'duration_minutes': 90, 'rating': 4.2},
        {'transport_type': 'Volvo Bus', 'estimated_cost': 1500, 'duration_minutes': 840, 'rating': 4.3},
        {'transport_type': 'Private Taxi', 'estimated_cost': 12000, 'duration_minutes': 720, 'rating': 4.6}
    ],
    'Jaipur': [
        {'transport_type': 'Flight', 'estimated_cost': 3500, 'duration_minutes': 60, 'rating': 4.6},
        {'transport_type': 'Train (Shatabdi)', 'estimated_cost': 800, 'duration_minutes': 240, 'rating': 4.8},
        {'transport_type': 'Bus', 'estimated_cost': 600, 'duration_minutes': 300, 'rating': 4.1}
    ],
    'Munnar': [
        {'transport_type': 'Flight (to Kochi)', 'estimated_cost': 6000, 'duration_minutes': 180, 'rating': 4.4},
        {'transport_type': 'Bus (from Kochi)', 'estimated_cost': 300, 'duration_minutes': 240, 'rating': 3.9},
        {'transport_type': 'Taxi (from Kochi)', 'estimated_cost': 3000, 'duration_minutes': 210, 'rating': 4.7}
    ],
    'Agra': [
        {'transport_type': 'Train (Shatabdi)', 'estimated_cost': 700, 'duration_minutes': 120, 'rating': 4.7},
        {'transport_type': 'Bus', 'estimated_cost': 400, 'duration_minutes': 200, 'rating': 4.0}
    ],
    'Bali': [
        {'transport_type': 'Flight', 'estimated_cost': 25000, 'duration_minutes': 480, 'rating': 4.6}
    ],
    'Paris': [
        {'transport_type': 'Flight', 'estimated_cost': 45000, 'duration_minutes': 720, 'rating': 4.8}
    ],
    'Rishikesh': [
        {'transport_type': 'Flight (to Dehradun)', 'estimated_cost': 3500, 'duration_minutes': 60, 'rating': 4.5},
        {'transport_type': 'Bus', 'estimated_cost': 600, 'duration_minutes': 360, 'rating': 4.1}
    ],
    'Andaman Islands': [
        {'transport_type': 'Flight', 'estimated_cost': 12000, 'duration_minutes': 240, 'rating': 4.5},
        {'transport_type': 'Ship', 'estimated_cost': 4000, 'duration_minutes': 2880, 'rating': 3.5}
    ],
    'Leh-Ladakh': [
        {'transport_type': 'Flight', 'estimated_cost': 9000, 'duration_minutes': 90, 'rating': 4.4},
        {'transport_type': 'Bus (from Manali)', 'estimated_cost': 2000, 'duration_minutes': 1440, 'rating': 4.0}
    ]
}

dest_names = [d["name"] for d in SAMPLE_DESTINATIONS]
selected_dest = st.selectbox("Select Destination", dest_names)

transport_data = []
try:
    dest_id = next((d.get("id", 1) for d in SAMPLE_DESTINATIONS if d["name"] == selected_dest), 1)
    transport_data = get_transportation_by_destination(dest_id)
except Exception as e:
    pass

if not transport_data:
    transport_data = SAMPLE_TRANSPORT.get(selected_dest, SAMPLE_TRANSPORT['Goa'])

st.subheader("Transport Options")
cols = st.columns(3)
for idx, opt in enumerate(transport_data):
    with cols[idx % 3]:
        with st.container(border=True):
            ttype = opt['transport_type'].lower()
            icon = ":material/directions_car:"
            if "flight" in ttype: icon = ":material/flight:"
            elif "train" in ttype: icon = ":material/train:"
            elif "bus" in ttype: icon = ":material/directions_bus:"
            elif "ship" in ttype: icon = ":material/directions_boat:"
            
            st.markdown(f"**{icon} {opt['transport_type']}**")
            st.write(f"**Cost:** {format_currency(opt['estimated_cost'])}")
            h = opt['duration_minutes'] // 60
            m = opt['duration_minutes'] % 60
            st.write(f"**Duration:** {h}h {m}m")
            st.write(f"**Rating:** {opt['rating']} ⭐")

st.subheader("Transportation Analytics")
df = pd.DataFrame(transport_data)
df['duration_hours'] = df['duration_minutes'] / 60

c1, c2 = st.columns(2)
with c1:
    fig_cost = px.bar(df, x='transport_type', y='estimated_cost', title='Cost by Transport Type', labels={'estimated_cost': 'Cost (₹)', 'transport_type': 'Transport Type'})
    fig_cost.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
    st.plotly_chart(fig_cost)
with c2:
    fig_dur = px.bar(df, y='transport_type', x='duration_hours', orientation='h', title='Duration by Transport Type', labels={'duration_hours': 'Duration (Hours)', 'transport_type': 'Transport Type'})
    fig_dur.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
    st.plotly_chart(fig_dur)

with st.expander("Travel Tips", expanded=False):
    st.markdown("- **Packing:** Pack light if you're taking flights to save on baggage fees.")
    st.markdown("- **Booking Advice:** Book trains at least 30 days in advance for confirmed seats.")
    st.markdown("- **Local Transport:** Use local ride-hailing apps or pre-paid taxis to avoid haggling.")
''',

    "app_pages/trip_summary.py": '''import streamlit as st
import pandas as pd
import plotly.express as px
from database.queries import get_user_trips
from auth.auth import init_session
from utils.helpers import db_status_banner, format_currency
from services.weather_service import get_weather

st.title(':material/summarize: Trip Summary', anchor=False)
db_status_banner()
init_session()

trip = None
if st.session_state.get('logged_in'):
    try:
        user_trips = get_user_trips(st.session_state.get('user_id', 1))
        if user_trips:
            trip_names = [f"{t.get('destination_name', 'Unknown')} ({t.get('start_date', 'N/A')})" for t in user_trips]
            selected_trip = st.selectbox("Select a trip", trip_names)
            trip_idx = trip_names.index(selected_trip)
            trip = user_trips[trip_idx]
    except Exception as e:
        st.error("Could not load trips from database.")
        
if not trip:
    trip = {
        'destination_name': 'Goa',
        'country': 'India',
        'start_date': '2023-11-01',
        'end_date': '2023-11-07',
        'travelers': 2,
        'total_budget': 35000,
        'avg_daily_cost': 2000
    }
    st.info("Showing demo trip summary (Goa) because no trips were found.")

try:
    import datetime
    sd = pd.to_datetime(trip.get('start_date'))
    ed = pd.to_datetime(trip.get('end_date'))
    duration_days = (ed - sd).days
except:
    duration_days = 7

st.subheader("Key Details")
details_df = pd.DataFrame([{
    'Destination': trip.get('destination_name', 'N/A'),
    'Country': trip.get('country', 'N/A'),
    'Start': trip.get('start_date', 'N/A'),
    'End': trip.get('end_date', 'N/A'),
    'Duration': f"{duration_days} days",
    'Travelers': trip.get('travelers', 1),
    'Budget': format_currency(trip.get('total_budget', 0))
}])
st.dataframe(details_df, hide_index=True)

st.subheader("Budget Analysis")
budget = trip.get('total_budget', 0)
est_cost = trip.get('avg_daily_cost', 2000) * duration_days * trip.get('travelers', 1)
delta = budget - est_cost

col1, col2, col3 = st.columns(3)
with col1:
    with st.container(border=True):
        st.metric("Budget", format_currency(budget))
with col2:
    with st.container(border=True):
        st.metric("Estimated Cost", format_currency(est_cost))
with col3:
    with st.container(border=True):
        st.metric("Delta", format_currency(delta), delta_color="normal")

st.subheader("Cost Breakdown")
labels = ['Transport', 'Hotel', 'Food', 'Activities', 'Misc']
values = [0.20, 0.35, 0.20, 0.15, 0.10]
fig = px.pie(names=labels, values=values, hole=0.4, title="Estimated Cost Distribution")
fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
st.plotly_chart(fig)

st.subheader("Travel Checklist")
c1, c2, c3, c4, c5 = st.columns(5)
with c1:
    with st.expander("Documents"):
        st.checkbox("Passport/ID", key="chk_doc1")
        st.checkbox("Visa", key="chk_doc2")
        st.checkbox("Travel Insurance", key="chk_doc3")
with c2:
    with st.expander("Bookings"):
        st.checkbox("Flight/Train", key="chk_bk1")
        st.checkbox("Hotels", key="chk_bk2")
        st.checkbox("Activities", key="chk_bk3")
with c3:
    with st.expander("Health"):
        st.checkbox("First Aid Kit", key="chk_h1")
        st.checkbox("Meds", key="chk_h2")
        st.checkbox("Sunscreen", key="chk_h3")
with c4:
    with st.expander("Tech"):
        st.checkbox("Charger", key="chk_t1")
        st.checkbox("Power Bank", key="chk_t2")
        st.checkbox("Adapter", key="chk_t3")
with c5:
    with st.expander("Clothing"):
        st.checkbox("Shoes", key="chk_c1")
        st.checkbox("Weather-apt", key="chk_c2")
        st.checkbox("Swimwear", key="chk_c3")

st.subheader("Weather Summary")
try:
    dest_name = trip.get('destination_name', 'Goa')
    weather = get_weather(dest_name)
    temp = weather.get("temp", "--")
    cond = weather.get("condition", "Clear")
    best = weather.get("best_months", "N/A")
    
    st.info(f"**Current weather in {dest_name}:** {temp}°C, {cond}. Best time to visit: {best}", icon=":material/thermostat:")
except Exception as e:
    st.info("Weather service is temporarily unavailable. Expect typical seasonal weather.", icon=":material/info:")
''',
    
    "app_pages/activity_recommendations.py": '''import streamlit as st
import plotly.express as px
import pandas as pd

try:
    from database.queries import get_all_activities
except ImportError:
    def get_all_activities(): return []

try:
    from utils.helpers import db_status_banner, rating_stars, format_currency
except ImportError:
    def db_status_banner(): pass
    def rating_stars(rating): return "⭐" * int(round(rating))
    def format_currency(v): return f"₹{v}"

st.title(':material/sports_score: Activities', anchor=False)
db_status_banner()

SAMPLE_ACTIVITIES = {
    'Goa': [
        {'name': 'Scuba Diving', 'category': 'Water Sports', 'price': 3000, 'duration_hrs': 4, 'rating': 4.8, 'destination_name': 'Goa'},
        {'name': 'Parasailing', 'category': 'Water Sports', 'price': 1500, 'duration_hrs': 1, 'rating': 4.5, 'destination_name': 'Goa'},
        {'name': 'Dudhsagar Trek', 'category': 'Adventure', 'price': 2000, 'duration_hrs': 8, 'rating': 4.6, 'destination_name': 'Goa'},
        {'name': 'Spice Plantation Tour', 'category': 'Heritage', 'price': 800, 'duration_hrs': 3, 'rating': 4.3, 'destination_name': 'Goa'}
    ],
    'Manali': [
        {'name': 'Rohtang Pass Tour', 'category': 'Nature', 'price': 2500, 'duration_hrs': 6, 'rating': 4.7, 'destination_name': 'Manali'},
        {'name': 'Solang Valley Paragliding', 'category': 'Adventure', 'price': 3000, 'duration_hrs': 2, 'rating': 4.9, 'destination_name': 'Manali'}
    ]
}

all_sample_activities = []
for dest, acts in SAMPLE_ACTIVITIES.items():
    all_sample_activities.extend(acts)

activities = []
try:
    activities = get_all_activities()
except Exception as e:
    pass

if not activities:
    activities = all_sample_activities

destinations = sorted(list(set(a['destination_name'] for a in activities)))
categories = sorted(list(set(a['category'] for a in activities)))
max_price_val = int(max((a['price'] for a in activities), default=20000))

with st.expander("Filter Activities", expanded=True):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        dest_filter = st.selectbox("Destination", ["All"] + destinations)
    with col2:
        cat_filter = st.multiselect("Category", categories, default=[])
    with col3:
        max_price = st.slider("Max Price (₹)", 0, max_price_val, max_price_val)
    with col4:
        min_rating = st.slider("Min Rating", 0.0, 5.0, 0.0, 0.1)

filtered_activities = activities
if dest_filter != "All":
    filtered_activities = [a for a in filtered_activities if a['destination_name'] == dest_filter]
if cat_filter:
    filtered_activities = [a for a in filtered_activities if a['category'] in cat_filter]
filtered_activities = [a for a in filtered_activities if a['price'] <= max_price and a['rating'] >= min_rating]

st.metric("Available Activities", len(filtered_activities))
if not filtered_activities:
    st.info("No activities match the current filters.")
else:
    for i in range(0, len(filtered_activities), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(filtered_activities):
                act = filtered_activities[i + j]
                with col:
                    with st.container(border=True):
                        st.subheader(f"{act['name']}")
                        st.caption(f"{act['category']} | {act['destination_name']}")
                        st.metric("Price", format_currency(act['price']))
                        st.write(f"**Duration:** {act['duration_hrs']} hrs")
                        st.write(f"**Rating:** {rating_stars(act['rating'])} ({act['rating']})")

if filtered_activities:
    df = pd.DataFrame(filtered_activities)
    c1, c2 = st.columns(2)
    with c1:
        cat_counts = df['category'].value_counts().reset_index()
        cat_counts.columns = ['Category', 'Count']
        fig_pie = px.pie(cat_counts, values='Count', names='Category', title='Activities by Category')
        fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
        st.plotly_chart(fig_pie)
    with c2:
        avg_price = df.groupby('category')['price'].mean().reset_index()
        fig_bar = px.bar(avg_price, x='category', y='price', title='Average Price by Category', labels={'price': 'Avg Price (₹)', 'category': 'Category'})
        fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', margin=dict(t=40,b=10,l=10,r=10))
        st.plotly_chart(fig_bar)
'''
}

for path, content in files.items():
    full_path = os.path.join(ROOT, path)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Wrote {full_path}")

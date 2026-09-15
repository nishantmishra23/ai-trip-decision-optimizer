"""
Destination Discovery page for AI Trip Decision Optimizer.
"""
import streamlit as st
from utils.helpers import get_destinations_with_fallback, format_currency
from utils.theme import inject_theme_css
from utils.images import get_destination_image
from recommendation.engine import score_destination
from auth.auth import init_session

init_session()
inject_theme_css()

# Hero Header Banner
st.markdown("""
<div class="app-hero-banner">
    <div class="app-hero-title">🌍 Destination Discovery</div>
    <div class="app-hero-subtitle">Browse world-class travel destinations, filter by budget or category, and discover your next adventure</div>
</div>
""", unsafe_allow_html=True)

dests = get_destinations_with_fallback()

with st.container(border=True):
    st.subheader(":material/filter_list: Search & Filter Destinations", anchor=False)
    f1, f2, f3 = st.columns(3, gap="medium")
    with f1:
        query = st.text_input("Search by name or country", placeholder="e.g. Goa, Paris, India")
    with f2:
        categories = sorted(list(set(d.get("category", "General") for d in dests if d.get("category"))))
        selected_cat = st.multiselect("Category", categories)
    with f3:
        max_cost = st.slider("Max Daily Budget (₹)", min_value=1000, max_value=20000, value=15000, step=500)

filtered = dests
if query:
    q = query.lower()
    filtered = [d for d in filtered if q in d.get("name", "").lower() or q in d.get("country", "").lower()]
if selected_cat:
    filtered = [d for d in filtered if d.get("category") in selected_cat]
filtered = [d for d in filtered if d.get("average_daily_cost", d.get("avg_daily_cost", 0)) <= max_cost]

# Apply Match Scoring if preferences exist in session
rec_prefs = st.session_state.get("rec_prefs")
if rec_prefs:
    user_history = []
    if st.session_state.get("logged_in") and st.session_state.get("user_id"):
        try:
            from database.queries import get_user_trips
            user_history = get_user_trips(st.session_state["user_id"])
        except:
            pass
            
    budget_per_day = rec_prefs.get("budget", 50000) / max(rec_prefs.get("duration", 5), 1)
    
    scored_filtered = []
    for d in filtered:
        scored_data = score_destination(
            d, 
            budget_per_day, 
            rec_prefs.get("duration", 5), 
            rec_prefs.get("activities", []), 
            rec_prefs.get("season", "Any season"), 
            rec_prefs.get("style", "Mid-range"),
            user_history
        )
        scored_filtered.append(scored_data)
        
    scored_filtered.sort(key=lambda x: x["score"], reverse=True)
else:
    scored_filtered = [{"destination": d} for d in filtered]

st.markdown(f"Showing **{len(filtered)}** destination{'s' if len(filtered)!=1 else ''}")

if not filtered:
    st.info("No destinations match your filter criteria. Try relaxing your filters.", icon=":material/search_off:")
else:
    cols = st.columns(3)
    for idx, d_data in enumerate(scored_filtered):
        d = d_data["destination"]
        score = d_data.get("score")
        reasons = d_data.get("reasons", [])
        
        with cols[idx % 3]:
            with st.container(border=True):
                # Match Score Badge
                if score is not None:
                    if score >= 80:
                        st.success(f"**{score:.0f}% Match**", icon=":material/verified:")
                    elif score >= 60:
                        st.info(f"**{score:.0f}% Match**", icon=":material/thumb_up:")
                    else:
                        st.caption(f"{score:.0f}% Match")
                        
                st.markdown(f"### 📍 {d.get('name')}")
                st.caption(f"Country: **{d.get('country')}**")
                
                cost = d.get('average_daily_cost', d.get('avg_daily_cost', 0))
                st.caption(f"{d.get('category')} • ⭐ {d.get('rating')} • **{format_currency(cost)}/day**")
                
                # Show top 2 reasons if scored
                if score is not None and reasons:
                    for reason in reasons[:2]:
                        st.caption(f"✓ {reason.split('—')[0].split('at')[0].strip()}")
                        
                c1, c2 = st.columns(2)
                with c1:
                    if st.button("Compare", key=f"comp_{d.get('name')}_{idx}"):
                        st.session_state["compare_prefill"] = d.get("name")
                        st.switch_page("app_pages/destination_comparison.py")
                with c2:
                    if st.button("Plan Trip", key=f"plan_{d.get('name')}_{idx}", type="primary"):
                        st.session_state["planner_prefill"] = d.get("name")
                        st.switch_page("app_pages/trip_planner.py")

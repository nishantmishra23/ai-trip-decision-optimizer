"""
Destination Discovery page for AI Trip Decision Optimizer.
"""
import streamlit as st
from utils.helpers import get_destinations_with_fallback, format_currency
from recommendation.engine import score_destination
from auth.auth import init_session

init_session()

# ── Hero ───────────────────────────────────────────────────────────────────────
st.title("Destination discovery", icon=":material/explore:")
st.caption("Browse world-class travel destinations, filter by budget or category, and discover your next adventure")

dests = get_destinations_with_fallback()

# ── Filters ────────────────────────────────────────────────────────────────────
with st.container(border=True):
    st.subheader("Search & filter", icon=":material/filter_list:", anchor=False)
    f1, f2, f3 = st.columns(3, gap="medium")
    with f1:
        query = st.text_input("Search by name or country", placeholder="e.g. Goa, Paris, India")
    with f2:
        categories = sorted(list(set(d.get("category", "General") for d in dests if d.get("category"))))
        selected_cat = st.multiselect("Category", categories)
    with f3:
        max_cost = st.slider("Max daily budget (₹)", min_value=1000, max_value=20000, value=15000, step=500)

filtered = dests
if query:
    q = query.lower()
    filtered = [d for d in filtered if q in d.get("name", "").lower() or q in d.get("country", "").lower()]
if selected_cat:
    filtered = [d for d in filtered if d.get("category") in selected_cat]
filtered = [d for d in filtered if d.get("average_daily_cost", d.get("avg_daily_cost", 0)) <= max_cost]

# Apply match scoring if preferences exist in session
rec_prefs = st.session_state.get("rec_prefs")
if rec_prefs:
    user_history = []
    if st.session_state.get("logged_in") and st.session_state.get("user_id"):
        try:
            from database.queries import get_user_trips
            user_history = get_user_trips(st.session_state["user_id"])
        except Exception:
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

st.caption(f"Showing **{len(filtered)}** destination{'s' if len(filtered) != 1 else ''}")

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
                        st.markdown(f":green-badge[{score:.0f}% match]")
                    elif score >= 60:
                        st.markdown(f":blue-badge[{score:.0f}% match]")
                    else:
                        st.caption(f"{score:.0f}% match")

                st.markdown(f":material/location_on: **{d.get('name')}**")
                st.caption(f"{d.get('country')} · {d.get('category')} · ⭐ {d.get('rating')}")

                cost = d.get("average_daily_cost", d.get("avg_daily_cost", 0))
                st.caption(f"**{format_currency(cost)}/day**")

                if score is not None and reasons:
                    for reason in reasons[:2]:
                        st.caption(f"✓ {reason.split('—')[0].split('at')[0].strip()}")

                c1, c2 = st.columns(2)
                with c1:
                    if st.button("Compare", key=f"comp_{d.get('name')}_{idx}", icon=":material/compare:"):
                        st.session_state["compare_prefill"] = d.get("name")
                        st.switch_page("app_pages/destination_comparison.py")
                with c2:
                    if st.button("Plan trip", key=f"plan_{d.get('name')}_{idx}", type="primary", icon=":material/map:"):
                        st.session_state["planner_prefill"] = d.get("name")
                        st.switch_page("app_pages/trip_planner.py")

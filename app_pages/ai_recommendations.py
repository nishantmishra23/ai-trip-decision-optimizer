"""AI Recommendations page — weighted scoring engine."""
import streamlit as st
import plotly.express as px
import pandas as pd
from recommendation.engine import get_recommendations, SAMPLE_DESTINATIONS
from utils.helpers import format_currency
from utils.theme import inject_theme_css
from utils.images import get_destination_image

inject_theme_css()

st.title(":material/psychology: AI recommendations", anchor=False)
st.caption(
    "Weighted scoring algorithm: **Budget fit** 30% · "
    "**Activity match** 25% · **Season** 20% · **Popularity** 15% · **Efficiency** 10%"
)

# ── Form ──────────────────────────────────────────────────────────────────────
with st.form("rec_form"):
    col1, col2 = st.columns(2)
    with col1:
        total_budget = st.number_input("Total budget (₹)", min_value=1000, value=50000, step=1000)
        duration_days = st.number_input("Duration (days)", min_value=1, max_value=30, value=5, step=1)
        travel_style = st.selectbox("Travel style", ["Budget", "Mid-range", "Luxury", "Backpacker", "Family"])
    with col2:
        activities = st.multiselect(
            "Interests / activities",
            ["Beach & Water Sports", "Adventure", "Trekking", "Heritage", "Wildlife",
             "Shopping", "Food & Cuisine", "Yoga & Wellness", "Nightlife", "Photography", "Culture"],
        )
        season = st.selectbox(
            "Travel season",
            ["Summer (Apr-Jun)", "Monsoon (Jul-Sep)", "Winter (Oct-Dec)", "Spring (Jan-Mar)", "Any season"],
            index=4,
        )
        top_n = st.slider("Number of recommendations", min_value=3, max_value=10, value=5)

    submitted = st.form_submit_button(":material/send: Get recommendations", type="primary")

# ── Results ───────────────────────────────────────────────────────────────────
if submitted:
    destinations = []
    try:
        from database.queries import get_all_destinations
        dests = get_all_destinations()
        if dests:
            sample_map = {d["name"]: d for d in SAMPLE_DESTINATIONS}
            for d in dests:
                if "category" not in d or not d.get("category"):
                    sample = sample_map.get(d.get("name"), {})
                    d["category"] = sample.get("category", "General")
                    d["season"] = sample.get("season", "Oct-Mar")
            destinations = dests
    except Exception:
        pass

    if not destinations:
        destinations = SAMPLE_DESTINATIONS

    recs = get_recommendations(
        destinations=destinations,
        budget=total_budget,
        duration_days=int(duration_days),
        preferred_activities=activities,
        preferred_season=season,
        travel_style=travel_style,
        top_n=top_n,
    )

    if not recs:
        st.warning("No recommendations found. Try adjusting your filters.", icon=":material/warning:")
        st.stop()

    st.subheader(f"Top {len(recs)} destinations for you", anchor=False)

    for idx, rec in enumerate(recs):
        dest = rec["destination"]
        score = rec.get("score", 0)
        img_url = get_destination_image(dest.get("name", ""), dest.get("category", ""))

        with st.container(border=True):
            col_img, col_a, col_b = st.columns([1, 2.5, 1], gap="medium")
            with col_img:
                st.image(img_url, caption=None)
            with col_a:
                st.markdown(f"### #{idx + 1} {dest.get('name')}, {dest.get('country', '')}")
                st.caption(f"**{dest.get('category', '')}** · Best season: {dest.get('season', 'Varies')}")

                subcols = st.columns(4)
                with subcols[0]:
                    st.caption("Budget fit")
                    st.progress(int(rec.get("budget_score", 0)) / 100, text=f"{rec.get('budget_score', 0):.0f}")
                with subcols[1]:
                    st.caption("Activity match")
                    st.progress(int(rec.get("activity_score", 0)) / 100, text=f"{rec.get('activity_score', 0):.0f}")
                with subcols[2]:
                    st.caption("Season")
                    st.progress(int(rec.get("season_score", 0)) / 100, text=f"{rec.get('season_score', 0):.0f}")
                with subcols[3]:
                    st.caption("Popularity")
                    st.progress(int(rec.get("popularity_score", 0)) / 100, text=f"{rec.get('popularity_score', 0):.0f}")

                for reason in rec.get("reasons", []):
                    st.caption(f"• {reason}")

            with col_b:
                st.metric("Score", f"{score:.0f} / 100")
                est = rec.get("estimated_total", 0)
                st.metric("Est. total", format_currency(est))

"""
Destination Discovery page for AI Trip Decision Optimizer.
"""
import streamlit as st
from utils.helpers import get_destinations_with_fallback
from utils.theme import inject_theme_css
from utils.components import render_destination_card

inject_theme_css()

st.title(":material/explore: Destination Discovery", anchor=False)
st.caption("Browse world-class travel destinations, filter by budget, category, or rating, and discover your next adventure.")

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

st.markdown(f"Showing **{len(filtered)}** destination{'s' if len(filtered)!=1 else ''}")

if not filtered:
    st.info("No destinations match your filter criteria. Try relaxing your filters.", icon=":material/search_off:")
else:
    cols = st.columns(3)
    for idx, d in enumerate(filtered):
        with cols[idx % 3]:
            render_destination_card(d, show_details=True)

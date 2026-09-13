import streamlit as st
import plotly.express as px
from database.queries import get_all_destinations
from recommendation.engine import SAMPLE_DESTINATIONS

st.title('Destination discovery', anchor=False)

search_term = st.text_input("Search destinations by name or country")
col1, col2, col3 = st.columns(3)
with col1:
    categories = st.multiselect("Category", ["Beach", "Mountains", "Heritage", "Nature", "City", "Adventure"])
with col2:
    max_budget = st.slider("Max daily budget", 500, 15000, 15000, 500)
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
    if d.get("average_daily_cost", 0) > max_budget:
        continue
    if d.get("rating", 0) < min_rating:
        continue
    filtered_dests.append(d)

st.write(f"Found {len(filtered_dests)} destinations")

if not filtered_dests:
    st.info("No destinations found matching the selected filters.")
else:
    cols = st.columns(3)
    for i, d in enumerate(filtered_dests):
        with cols[i % 3]:
            with st.container(border=True):
                st.markdown(f"**{d.get('name', '')}**")
                st.caption(d.get("country", ""))
                # Using markdown for badge as st.badge might not be available
                st.markdown(f"*{d.get('category', 'Uncategorized')}*")
                st.write(f"Daily cost: ₹{d.get('average_daily_cost', 0)}")
                st.write(f"Rating: {d.get('rating', 0):.1f}/5.0")
                desc = d.get("description", "")
                st.write(desc[:120] + ("..." if len(desc) > 120 else ""))

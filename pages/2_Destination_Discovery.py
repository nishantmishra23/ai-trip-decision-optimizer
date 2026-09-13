import pandas as pd
import streamlit as st

from auth.authentication import require_login
from database.destinations import list_destinations
from database.seed import seed_destinations_if_empty
from utils.ui import error_message, info_card, page_header, section_title

require_login()
page_header("🌍 Destination Discovery", "Browse destinations stored in the optimizer database.")

inserted, seed_error = seed_destinations_if_empty()
if seed_error:
    error_message(seed_error)
    st.stop()
if inserted:
    st.info("Sample destinations were added so you can explore the catalog.")

destinations, dest_error = list_destinations()
if dest_error:
    error_message(dest_error)
    st.stop()
if not destinations:
    error_message("No destinations found.")
    st.stop()

section_title("Highlights")
top = destinations[:3]
cols = st.columns(len(top))
for col, row in zip(cols, top):
    with col:
        info_card(
            row["name"],
            f"{row['rating']:.1f}★" if row.get("rating") is not None else "—",
            f"{row.get('country') or ''} · daily cost {row.get('average_daily_cost') or 0:,.0f}",
        )

section_title("All destinations")
frame = pd.DataFrame(destinations)
display_cols = [c for c in ["name", "country", "average_daily_cost", "popularity_score", "rating"] if c in frame.columns]
st.dataframe(frame[display_cols], use_container_width=True, hide_index=True)

selected_name = st.selectbox("Read more", [row["name"] for row in destinations])
selected = next(row for row in destinations if row["name"] == selected_name)
st.markdown(f"**{selected['name']}, {selected.get('country') or ''}**")
st.write(selected.get("description") or "No description available yet.")

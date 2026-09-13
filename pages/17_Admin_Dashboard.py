import pandas as pd
import streamlit as st

from auth.authentication import require_admin
from database.admin import get_dashboard_stats, list_users
from utils.ui import error_message, info_card, page_header, section_title

require_admin()
page_header("👨‍💼 Admin Dashboard", "Platform overview for administrators.")

stats, stats_error = get_dashboard_stats()
if stats_error:
    error_message(stats_error)
    st.stop()

c1, c2, c3, c4 = st.columns(4)
with c1:
    info_card("Users", stats["users"], "Registered accounts")
with c2:
    info_card("Admins", stats["admins"], "ADMIN role")
with c3:
    info_card("Destinations", stats["destinations"], "Catalog size")
with c4:
    info_card("Trips", stats["trips"], "Saved trip plans")

section_title("Registered users")
users, users_error = list_users()
if users_error:
    error_message(users_error)
    st.stop()

if not users:
    st.info("No users found.")
else:
    frame = pd.DataFrame(users)
    if "created_at" in frame.columns:
        frame["created_at"] = frame["created_at"].astype(str)
    st.dataframe(
        frame[["user_id", "name", "email", "role", "created_at"]],
        use_container_width=True,
        hide_index=True,
    )

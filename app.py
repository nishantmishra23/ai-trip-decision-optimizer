import streamlit as st

from auth.authentication import (
    authenticate_user,
    init_session,
    is_authenticated,
    login_user,
    logout_user,
    register_user,
    render_user_sidebar,
)
from utils.ui import apply_global_styles, error_message, page_header, success_message

st.set_page_config(
    page_title="AI Trip Decision Optimizer",
    page_icon="✈️",
    layout="wide",
)

init_session()
apply_global_styles()
render_user_sidebar()

page_header(
    "✈️ AI Trip Decision Optimizer",
    "AI-powered travel planning and trip optimization",
)


def render_login_form():
    st.markdown("Sign in with the email and password you used at registration.")

    with st.form("login_form", clear_on_submit=False):
        email = st.text_input("Email", placeholder="you@example.com")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Log in", use_container_width=True)

    if submitted:
        user, message = authenticate_user(email, password)
        if user:
            login_user(user)
            success_message(f"Welcome back, {user['name']}.")
            st.rerun()
        else:
            error_message(message)


def render_register_form():
    st.markdown("Create a traveler account. New accounts start with the USER role.")

    with st.form("register_form", clear_on_submit=False):
        name = st.text_input("Full name", placeholder="Your name")
        email = st.text_input("Email", placeholder="you@example.com")
        password = st.text_input("Password", type="password", help="At least 8 characters.")
        confirm_password = st.text_input("Confirm password", type="password")
        submitted = st.form_submit_button("Create account", use_container_width=True)

    if submitted:
        success, message = register_user(name, email, password, confirm_password)
        if success:
            success_message(message)
        else:
            error_message(message)


def render_authenticated_home():
    st.success(f"Signed in as **{st.session_state.name}** ({st.session_state.role})")

    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.markdown("### Traveler")
            st.markdown(f"**{st.session_state.name}**")
            st.caption(st.session_state.email)
    with col2:
        with st.container(border=True):
            st.markdown("### Role")
            st.markdown(f"**{st.session_state.role}**")
            st.caption("USER plans trips. ADMIN manages the platform.")
    with col3:
        with st.container(border=True):
            st.markdown("### Next step")
            st.markdown("**Open Trip Planner**")
            st.caption("Use the sidebar to start optimizing a trip.")

    st.write(
        "Find the best-value trip based on your budget, preferences, "
        "weather, hotels, activities, food and transportation."
    )

    current = st.session_state.get("current_trip")
    if current:
        st.info(
            f"Active trip: **{current.get('destination_name', 'Saved trip')}** "
            f"(ID {current['trip_id']}). Continue in Trip Planner or Saved Trips."
        )
    else:
        st.info("Start in **Trip Planner** to save dates, budget, and preferences.")

    if st.session_state.role == "ADMIN":
        st.info("Admin access is enabled. Open **Admin Dashboard** from the sidebar.")

    if st.button("Log out"):
        logout_user()
        st.rerun()


if is_authenticated():
    render_authenticated_home()
else:
    st.write(
        "Find the best-value trip based on your budget, preferences, "
        "weather, hotels, activities, food and transportation."
    )
    login_tab, register_tab = st.tabs(["Log in", "Create account"])
    with login_tab:
        render_login_form()
    with register_tab:
        render_register_form()

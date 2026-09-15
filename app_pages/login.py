"""
Login / Register page for AI Trip Decision Optimizer.
"""
import streamlit as st
from auth.auth import init_session, login, register, logout

init_session()

if st.session_state.get("logged_in"):
    user = st.session_state.get("user", {}) or {}
    st.title("Your account", icon=":material/person:")
    st.caption("Manage your profile, active sessions, and saved itineraries")

    with st.container(border=True):
        st.success(f"Signed in as **{user.get('name', 'User')}** ({user.get('email', '')})", icon=":material/check_circle:")
        st.caption(f"Account role: **{user.get('role', 'USER')}**")
        if st.button("Sign out", icon=":material/logout:", type="primary"):
            logout()
            st.rerun()
    st.stop()

# ── Hero ───────────────────────────────────────────────────────────────────────
st.title("Welcome to AI Trip Optimizer", icon=":material/flight_takeoff:")
st.caption("Sign in or create an account to unlock AI-powered travel recommendations and saved itineraries")

col_info, col_form = st.columns([1, 1], gap="medium")

with col_info:
    with st.container(border=True):
        st.subheader("Why join us?", icon=":material/star:", anchor=False)
        st.markdown("""
        - :material/psychology: **AI-powered recommendations** — multi-factor scoring tailored to your budget and travel style
        - :material/map: **Smart trip planning** — automatic itinerary generation with daily cost breakdowns
        - :material/wb_sunny: **Weather & transport intelligence** — live insights to choose the perfect time to visit
        - :material/bookmark: **Saved itineraries** — access your planned trips anywhere, anytime
        """)
        st.info("**Demo account:** `demo@example.com` / `demo1234`", icon=":material/key:")

with col_form:
    with st.container(border=True):
        tab_login, tab_register = st.tabs(["Sign in", "Create account"])

        with tab_login:
            with st.form("login_form"):
                email = st.text_input("Email address", placeholder="you@example.com")
                password = st.text_input("Password", type="password")
                submitted = st.form_submit_button("Sign in", icon=":material/login:", type="primary")
                if submitted:
                    ok, result = login(email, password)
                    if ok:
                        st.success(f"Welcome back, {result['name']}!", icon=":material/check_circle:")
                        st.rerun()
                    else:
                        st.error(result, icon=":material/error:")

        with tab_register:
            with st.form("register_form"):
                name = st.text_input("Full name", placeholder="John Doe")
                email_r = st.text_input("Email address", key="reg_email", placeholder="john@example.com")
                pass_r = st.text_input("Password (min 8 chars)", type="password", key="reg_pass")
                confirm_r = st.text_input("Confirm password", type="password", key="reg_confirm")
                submitted_r = st.form_submit_button("Register account", icon=":material/person_add:", type="primary")
                if submitted_r:
                    ok, msg = register(name, email_r, pass_r, confirm_r)
                    if ok:
                        st.success(msg, icon=":material/check_circle:")
                    else:
                        st.error(msg, icon=":material/error:")

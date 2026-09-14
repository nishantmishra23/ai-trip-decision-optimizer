"""
Login / Register page for AI Trip Decision Optimizer.
"""
import streamlit as st
from auth.auth import init_session, login, register, logout
from utils.images import HERO_IMAGES
from utils.theme import inject_theme_css

init_session()
inject_theme_css()

if st.session_state.get("logged_in"):
    user = st.session_state.get("user", {}) or {}
    st.title(":material/account_circle: Your Account", anchor=False)
    
    with st.container(border=True):
        st.success(f"Signed in as **{user.get('name', 'User')}** ({user.get('email', '')})", icon=":material/check_circle:")
        st.caption(f"Account Role: **{user.get('role', 'USER')}**")
        if st.button("Sign out", icon=":material/logout:", type="primary"):
            logout()
            st.rerun()
    st.stop()

# Header image & headline
st.image(HERO_IMAGES["Login"], caption=None)
st.title("Welcome to AI Trip Optimizer", anchor=False)
st.caption("Sign in or create an account to unlock AI-powered recommendations, save trip itineraries, and track travel history.")

col_info, col_form = st.columns([1, 1], gap="medium")

with col_info:
    with st.container(border=True):
        st.subheader(":material/flight_takeoff: Why Join Us?", anchor=False)
        st.markdown("""
        * **AI-Powered Recommendations**: Multi-factor scoring tailored to your budget and travel style.
        * **Smart Trip Planning**: Automatic itinerary generation with daily cost breakdowns.
        * **Weather & Transport Intelligence**: Live insights to choose the perfect time to visit.
        * **Saved Itineraries**: Access your planned trips anywhere, anytime.
        """)
        st.info("💡 **Demo Account:** `demo@example.com` / `demo1234`", icon=":material/key:")

with col_form:
    with st.container(border=True):
        tab_login, tab_register = st.tabs(["Sign in", "Create Account"])

        with tab_login:
            with st.form("login_form"):
                email = st.text_input("Email address", placeholder="you@example.com")
                password = st.text_input("Password", type="password")
                submitted = st.form_submit_button("Sign in", icon=":material/login:")
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
                submitted_r = st.form_submit_button("Register Account", icon=":material/person_add:")
                if submitted_r:
                    ok, msg = register(name, email_r, pass_r, confirm_r)
                    if ok:
                        st.success(msg, icon=":material/check_circle:")
                    else:
                        st.error(msg, icon=":material/error:")

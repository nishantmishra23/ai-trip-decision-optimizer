"""Login / Register page."""
import streamlit as st
from auth.auth import init_session, login, register, logout

init_session()

if st.session_state.get("logged_in"):
    user = st.session_state.get("user", {}) or {}
    st.title("Account", anchor=False)
    st.success(f"You are logged in as **{user.get('name', 'User')}** ({user.get('email', '')})", icon=":material/check_circle:")
    if st.button("Log out", icon=":material/logout:"):
        logout()
        st.rerun()
    st.stop()

st.title("Sign in to AI Trip Optimizer", anchor=False)
st.caption("Log in or create an account to save and manage your trips.")

tab_login, tab_register = st.tabs(["Log in", "Register"])

with tab_login:
    with st.form("login_form"):
        email = st.text_input("Email address", placeholder="you@example.com")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Log in", icon=":material/login:")
        if submitted:
            ok, result = login(email, password)
            if ok:
                st.success(f"Welcome back, {result['name']}!", icon=":material/check_circle:")
                st.rerun()
            else:
                st.error(result, icon=":material/error:")

    st.caption("**Demo credentials:** demo@example.com / demo1234 (no database required)")

with tab_register:
    with st.form("register_form"):
        name = st.text_input("Full name")
        email_r = st.text_input("Email address", key="reg_email")
        pass_r = st.text_input("Password (min 8 chars)", type="password", key="reg_pass")
        confirm_r = st.text_input("Confirm password", type="password", key="reg_confirm")
        submitted_r = st.form_submit_button("Create account", icon=":material/person_add:")
        if submitted_r:
            ok, msg = register(name, email_r, pass_r, confirm_r)
            if ok:
                st.success(msg, icon=":material/check_circle:")
            else:
                st.error(msg, icon=":material/error:")

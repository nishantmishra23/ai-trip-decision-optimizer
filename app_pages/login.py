"""
Student & Traveler Account Portal.
Features Email & Password creation, Sign In, and one-click Google Authentication.
"""
import os
import sys

# Ensure project root is in sys.path
_current_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
ROOT_DIR = os.path.dirname(_current_dir) if "app_pages" in _current_dir else _current_dir
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

import streamlit as st
from auth.auth import init_session, login, register, logout, login_with_google

init_session()

# ── If Already Logged In ────────────────────────────────────────────────────────
if st.session_state.get("logged_in"):
    user = st.session_state.get("user", {}) or {}
    provider = user.get("auth_provider", "Email")
    
    st.title(f"Welcome back, {user.get('name', 'Explorer')}!", icon=":material/account_circle:")
    st.caption("Manage your student profile, saved itineraries, and travel preferences.")

    with st.container(border=True):
        col_avatar, col_details = st.columns([1, 4], gap="medium")
        with col_avatar:
            st.markdown(
                """
                <div style="background: linear-gradient(135deg, #6366f1, #8b5cf6); border-radius: 50%; width: 90px; height: 90px; display: flex; align-items: center; justify-content: center; font-size: 38px; color: white; font-weight: bold; margin: 0 auto;">
                    🎓
                </div>
                """,
                unsafe_allow_html=True
            )
        with col_details:
            st.subheader(user.get("name", "Student Traveler"), anchor=False)
            st.markdown(f"📧 **Email:** `{user.get('email', '')}`")
            st.markdown(f"🛡️ **Account Status:** Active Student Explorer • **Signed in via:** `{provider}`")
            st.badge("Verified Account", color="green")
            st.badge("AI Itinerary Access Enabled", color="blue")
            st.badge("28 States Unlocked", color="violet")

        st.divider()
        col_btn1, col_btn2 = st.columns([1, 3])
        with col_btn1:
            if st.button("Sign out", icon=":material/logout:", type="secondary", use_container_width=True):
                logout()
                st.rerun()

    st.stop()


# ── Guest View / Sign In & Register ─────────────────────────────────────────────
st.title("Student & Traveler Portal", icon=":material/flight_takeoff:")
st.caption("Sign in with Google or create an account to unlock full AI Itinerary generation across all 28 states of India.")

col_benefits, col_auth = st.columns([1, 1], gap="large")

with col_benefits:
    with st.container(border=True):
        st.subheader("🎓 Why Travel With Us?", anchor=False)
        st.markdown("""
        - 🤖 **Gemini 3.6 Flash Engine**: AI-curated custom itineraries tailored to student budgets.
        - 🇮🇳 **All 28 Indian States**: Comprehensive local guides, hidden spots, and budget costs.
        - 🌤️ **Live Weather Intelligence**: Real-time OpenWeather queries for instant trip decisions.
        - 📍 **Instant Google Maps & Places**: Direct links to navigate and explore top monuments.
        - 💾 **Cloud Trip Vault**: Save, edit, and export your dream travel itineraries anytime.
        """)
        
        st.divider()
        st.info("💡 **Quick Demo Account:** `demo@example.com` / `demo1234`", icon=":material/key:")

with col_auth:
    # ── Google Authentication Section ───────────────────────────────────────────
    with st.container(border=True):
        st.markdown("##### Quick Access")
        
        # Google Sign In button with vibrant styling
        google_col1, google_col2 = st.columns([1, 1])
        with google_col1:
            google_name = st.text_input("Google Name", value="Alex Sharma", key="g_name")
        with google_col2:
            google_email = st.text_input("Google Email", value="alex.student@gmail.com", key="g_email")
            
        if st.button(
            "🌐 Continue with Google",
            icon=":material/travel_explore:",
            type="primary",
            use_container_width=True,
            key="btn_google_login"
        ):
            ok, user_dict = login_with_google(email=google_email, name=google_name)
            if ok:
                st.success(f"Signed in as {user_dict['name']} via Google!", icon=":material/check_circle:")
                st.rerun()

    st.markdown("<div style='text-align: center; margin: 8px 0; color: gray;'>— OR USE EMAIL & PASSWORD —</div>", unsafe_allow_html=True)

    # ── Email & Password Tabs ───────────────────────────────────────────────────
    with st.container(border=True):
        tab_login, tab_register = st.tabs(["🔑 Sign In", "📝 Create Account"])

        with tab_login:
            with st.form("login_form"):
                email = st.text_input("Email Address", placeholder="student@university.edu")
                password = st.text_input("Password", type="password")
                submitted = st.form_submit_button("Sign In to Account", icon=":material/login:", type="primary", use_container_width=True)
                
                if submitted:
                    ok, result = login(email, password)
                    if ok:
                        st.success(f"Welcome back, {result['name']}!", icon=":material/check_circle:")
                        st.rerun()
                    else:
                        st.error(result, icon=":material/error:")

        with tab_register:
            with st.form("register_form"):
                name = st.text_input("Full Name", placeholder="Rohan Gupta")
                email_r = st.text_input("Email Address", key="reg_email", placeholder="rohan@gmail.com")
                pass_r = st.text_input("Create Password (min 6 characters)", type="password", key="reg_pass")
                confirm_r = st.text_input("Confirm Password", type="password", key="reg_confirm")
                submitted_r = st.form_submit_button("Create My Account", icon=":material/person_add:", type="primary", use_container_width=True)
                
                if submitted_r:
                    ok, msg = register(name, email_r, pass_r, confirm_r)
                    if ok:
                        st.success(msg, icon=":material/check_circle:")
                    else:
                        st.error(msg, icon=":material/error:")

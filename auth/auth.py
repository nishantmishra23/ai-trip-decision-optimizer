"""
Authentication logic for AI Trip Decision Optimizer.
Handles registration, login, session management using bcrypt.
"""
import bcrypt
import streamlit as st
from database.queries import get_user_by_email, create_user


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(password: str, hashed: str) -> bool:
    try:
        return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
    except Exception:
        return False


def init_session():
    """Initialize session state keys."""
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user" not in st.session_state:
        st.session_state.user = None
    if "user_id" not in st.session_state:
        st.session_state.user_id = None


def login(email: str, password: str):
    """
    Attempt login. Returns (True, user_dict) on success or (False, error_msg).
    Falls back to demo mode if DB unavailable.
    """
    if not email or not password:
        return False, "Email and password are required."

    user = get_user_by_email(email.strip().lower())
    if user is None:
        # DB unavailable — allow demo login
        if email == "demo@example.com" and password == "demo1234":
            demo_user = {
                "user_id": 0,
                "name": "Demo User",
                "email": "demo@example.com",
                "role": "USER",
            }
            st.session_state.logged_in = True
            st.session_state.user = demo_user
            st.session_state.user_id = 0
            return True, demo_user
        return False, "Database unavailable. Use demo@example.com / demo1234."

    if not verify_password(password, user["password_hash"]):
        return False, "Incorrect password."

    st.session_state.logged_in = True
    st.session_state.user = user
    st.session_state.user_id = user["user_id"]
    return True, user


def register(name: str, email: str, password: str, confirm: str):
    """Register a new user. Returns (True, msg) or (False, error)."""
    if not all([name, email, password, confirm]):
        return False, "All fields are required."
    if len(password) < 8:
        return False, "Password must be at least 8 characters."
    if password != confirm:
        return False, "Passwords do not match."
    if "@" not in email:
        return False, "Enter a valid email address."

    existing = get_user_by_email(email.strip().lower())
    if existing is not None:
        return False, "An account with this email already exists."

    hashed = hash_password(password)
    success = create_user(name.strip(), email.strip().lower(), hashed)
    if success:
        return True, "Account created! Please log in."
    return False, "Could not create account. Database may be unavailable."


def logout():
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.user_id = None


def require_login():
    """Call at top of protected pages. Returns user dict or stops page."""
    init_session()
    if not st.session_state.logged_in:
        st.warning("Please log in to access this page.", icon=":material/lock:")
        st.stop()
    return st.session_state.user

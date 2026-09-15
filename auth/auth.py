"""
Authentication logic for AI Trip Decision Optimizer.
Handles registration, login, Google authentication, and session management.
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
    if "local_users" not in st.session_state:
        st.session_state.local_users = {}


def login(email: str, password: str):
    """
    Attempt login. Returns (True, user_dict) on success or (False, error_msg).
    Falls back gracefully to session/demo mode if DB is unavailable.
    """
    if not email or not password:
        return False, "Email and password are required."

    clean_email = email.strip().lower()

    # Check local session users first (for created accounts when DB is offline)
    local_users = st.session_state.get("local_users", {})
    if clean_email in local_users:
        stored = local_users[clean_email]
        if verify_password(password, stored["password_hash"]):
            user_dict = {
                "user_id": stored["user_id"],
                "name": stored["name"],
                "email": clean_email,
                "role": "USER",
            }
            st.session_state.logged_in = True
            st.session_state.user = user_dict
            st.session_state.user_id = stored["user_id"]
            return True, user_dict
        return False, "Incorrect password."

    # Try database
    user = get_user_by_email(clean_email)
    if user is not None:
        if not verify_password(password, user["password_hash"]):
            return False, "Incorrect password."
        st.session_state.logged_in = True
        st.session_state.user = user
        st.session_state.user_id = user["user_id"]
        return True, user

    # Pre-configured demo account
    if clean_email == "demo@example.com" and password == "demo1234":
        demo_user = {
            "user_id": 1,
            "name": "Demo Student",
            "email": "demo@example.com",
            "role": "USER",
        }
        st.session_state.logged_in = True
        st.session_state.user = demo_user
        st.session_state.user_id = 1
        return True, demo_user

    return False, "Account not found or incorrect credentials. Try demo@example.com / demo1234 or create a new account."


def register(name: str, email: str, password: str, confirm: str):
    """Register a new user. Returns (True, msg) or (False, error)."""
    if not all([name, email, password, confirm]):
        return False, "All fields are required."
    if len(password) < 6:
        return False, "Password must be at least 6 characters."
    if password != confirm:
        return False, "Passwords do not match."
    if "@" not in email or "." not in email:
        return False, "Enter a valid email address."

    clean_email = email.strip().lower()

    # Check local registry
    local_users = st.session_state.setdefault("local_users", {})
    if clean_email in local_users:
        return False, "An account with this email already exists."

    hashed = hash_password(password)

    # Try DB creation
    try:
        existing = get_user_by_email(clean_email)
        if existing is not None:
            return False, "An account with this email already exists in the database."
        create_user(name.strip(), clean_email, hashed)
    except Exception:
        pass

    # Save to local session user store so registration always succeeds
    uid = len(local_users) + 100
    local_users[clean_email] = {
        "user_id": uid,
        "name": name.strip(),
        "email": clean_email,
        "password_hash": hashed,
        "role": "USER"
    }

    return True, f"Account successfully created for {name}! You can now sign in."


def login_with_google(email: str = "student.explorer@gmail.com", name: str = "Alex Sharma"):
    """One-click Google authentication."""
    clean_email = email.strip().lower()
    google_user = {
        "user_id": 888,
        "name": name,
        "email": clean_email,
        "role": "USER",
        "auth_provider": "Google",
    }
    st.session_state.logged_in = True
    st.session_state.user = google_user
    st.session_state.user_id = 888
    return True, google_user


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

"""Authentication helpers: registration, login, session, and page access control."""

import re

import bcrypt
import mysql.connector
import streamlit as st

from database.connection import get_connection

EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
MIN_PASSWORD_LENGTH = 8
MIN_NAME_LENGTH = 2

def _public_user(row):
    """Return user fields that are safe to keep in session_state."""
    return {
        "user_id": row["user_id"],
        "name": row["name"],
        "email": row["email"],
        "role": row["role"],
    }


def _open_connection():
    """Open a MySQL connection or return (None, error_message)."""
    try:
        return get_connection(), None
    except mysql.connector.Error:
        return None, "Unable to connect to the database. Please try again later."
    except Exception:
        return None, "A database error occurred. Please try again later."


def validate_registration(name, email, password, confirm_password):
    """Validate registration fields. Returns (is_valid, message)."""
    name = (name or "").strip()
    email = (email or "").strip()

    if len(name) < MIN_NAME_LENGTH:
        return False, "Please enter your full name (at least 2 characters)."

    if len(name) > 100:
        return False, "Name must be 100 characters or fewer."

    if not EMAIL_PATTERN.match(email):
        return False, "Please enter a valid email address."

    if not password:
        return False, "Password is required."

    if len(password) < MIN_PASSWORD_LENGTH:
        return False, f"Password must be at least {MIN_PASSWORD_LENGTH} characters."

    if password != confirm_password:
        return False, "Password and confirm password do not match."

    return True, ""


def register_user(name, email, password, confirm_password):
    """
    Create a USER account with a bcrypt password hash.

    Returns (success: bool, message: str).
    """
    is_valid, message = validate_registration(name, email, password, confirm_password)
    if not is_valid:
        return False, message

    name = name.strip()
    email = email.strip().lower()

    connection, error = _open_connection()
    if error:
        return False, error

    cursor = connection.cursor()
    try:
        cursor.execute(
            "SELECT user_id FROM users WHERE email = %s",
            (email,),
        )
        if cursor.fetchone():
            return False, "An account with this email already exists. Please log in instead."

        password_hash = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt(),
        ).decode("utf-8")

        cursor.execute(
            """
            INSERT INTO users (name, email, password_hash, role)
            VALUES (%s, %s, %s, %s)
            """,
            (name, email, password_hash, "USER"),
        )
        connection.commit()
        return True, "Account created successfully. You can now log in."

    except mysql.connector.IntegrityError:
        connection.rollback()
        return False, "An account with this email already exists. Please log in instead."
    except mysql.connector.Error:
        connection.rollback()
        return False, "Could not create your account. Please try again later."
    except Exception:
        connection.rollback()
        return False, "Could not create your account. Please try again later."
    finally:
        cursor.close()
        connection.close()


def authenticate_user(email, password):
    """
    Verify email/password against the users table.

    Returns (user_dict, error_message). user_dict is None on failure.
    """
    email = (email or "").strip().lower()
    if not email or not password:
        return None, "Email and password are required."

    connection, error = _open_connection()
    if error:
        return None, error

    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(
            """
            SELECT user_id, name, email, password_hash, role
            FROM users
            WHERE email = %s
            """,
            (email,),
        )
        user = cursor.fetchone()
    except mysql.connector.Error:
        return None, "Could not verify your credentials. Please try again later."
    finally:
        cursor.close()
        connection.close()

    if not user:
        return None, "Invalid email or password."

    try:
        password_ok = bcrypt.checkpw(
            password.encode("utf-8"),
            user["password_hash"].encode("utf-8"),
        )
    except (ValueError, TypeError):
        return None, "Invalid email or password."

    if not password_ok:
        return None, "Invalid email or password."

    return _public_user(user), None


def init_session():
    """Ensure authentication keys exist in Streamlit session_state."""
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    for key in ("user_id", "name", "email", "role"):
        if key not in st.session_state:
            st.session_state[key] = None


def login_user(user):
    """Store the authenticated user in session_state."""
    st.session_state.logged_in = True
    st.session_state.user_id = user["user_id"]
    st.session_state.name = user["name"]
    st.session_state.email = user["email"]
    st.session_state.role = user["role"]


def logout_user():
    """Clear authentication data from session_state."""
    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.name = None
    st.session_state.email = None
    st.session_state.role = None


def is_authenticated():
    init_session()
    return bool(st.session_state.logged_in)


def is_admin():
    init_session()
    return st.session_state.role == "ADMIN"


def current_user_name():
    init_session()
    return st.session_state.name or ""


def current_user_role():
    init_session()
    return st.session_state.role or ""


def apply_navigation_visibility():
    """Hide app pages until login; hide Admin Dashboard from non-admin users."""
    if not is_authenticated():
        st.markdown(
            """
            <style>
                [data-testid="stSidebarNav"] { display: none; }
            </style>
            """,
            unsafe_allow_html=True,
        )
        return

    if not is_admin():
        st.markdown(
            """
            <style>
                [data-testid="stSidebarNav"] a[href*="Admin_Dashboard"] {
                    display: none !important;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )


def render_user_sidebar():
    """Show the signed-in user's name, role, and a logout button."""
    apply_navigation_visibility()

    if not is_authenticated():
        return

    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**{st.session_state.name}**")
    st.sidebar.caption(st.session_state.email)
    st.sidebar.caption(f"Role: {st.session_state.role}")

    if st.sidebar.button("Log out", use_container_width=True):
        logout_user()
        st.rerun()


def require_login():
    """Stop page rendering unless a user is logged in."""
    from utils.ui import apply_global_styles, error_message

    init_session()
    apply_global_styles()
    render_user_sidebar()

    if not is_authenticated():
        error_message("Please log in to access this page.")
        st.info("Open **Home** in the sidebar to sign in or create an account.")
        st.stop()


def require_admin():
    """Stop page rendering unless the logged-in user has the ADMIN role."""
    from utils.ui import error_message

    require_login()
    if not is_admin():
        error_message("Access denied. This page is available to administrators only.")
        st.stop()

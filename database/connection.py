"""
Improved database connection with graceful error handling.
Uses @st.cache_resource so the connection pool is shared across reruns.
"""
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


@st.cache_resource
def get_engine():
    """Return a cached MySQL connection pool. Returns None if DB unavailable."""
    try:
        import mysql.connector
        from mysql.connector import pooling
        pool = pooling.MySQLConnectionPool(
            pool_name="trip_pool",
            pool_size=5,
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", 3306)),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "ai_trip_optimizer"),
            autocommit=False,
        )
        return pool
    except Exception:
        return None


def get_connection():
    """Get a connection from the pool. Returns None on failure."""
    try:
        pool = get_engine()
        if pool is None:
            return None
        return pool.get_connection()
    except Exception:
        return None


def db_available():
    """Quick check if DB is reachable."""
    conn = get_connection()
    if conn:
        conn.close()
        return True
    return False
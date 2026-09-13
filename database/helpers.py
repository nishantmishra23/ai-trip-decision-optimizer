"""Shared MySQL helpers used by trip, destination, and admin modules."""

import mysql.connector

from database.connection import get_connection


def open_connection():
    """Return (connection, error_message)."""
    try:
        return get_connection(), None
    except mysql.connector.Error:
        return None, "Unable to connect to the database. Please try again later."
    except Exception:
        return None, "A database error occurred. Please try again later."

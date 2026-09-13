"""Admin-only reads against existing tables. Never returns password hashes."""

import mysql.connector

from database.helpers import open_connection


def get_dashboard_stats():
    """Return (stats_dict, error_message)."""
    connection, error = open_connection()
    if error:
        return None, error

    cursor = connection.cursor()
    try:
        counts = {}
        for key, sql in (
            ("users", "SELECT COUNT(*) FROM users"),
            ("admins", "SELECT COUNT(*) FROM users WHERE role = 'ADMIN'"),
            ("destinations", "SELECT COUNT(*) FROM destinations"),
            ("trips", "SELECT COUNT(*) FROM trips"),
        ):
            cursor.execute(sql)
            counts[key] = cursor.fetchone()[0]
        return counts, None
    except mysql.connector.Error:
        return None, "Could not load admin statistics."
    finally:
        cursor.close()
        connection.close()


def list_users():
    """Return registered users without password hashes."""
    connection, error = open_connection()
    if error:
        return [], error

    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(
            """
            SELECT user_id, name, email, role, created_at
            FROM users
            ORDER BY created_at DESC
            """
        )
        return cursor.fetchall(), None
    except mysql.connector.Error:
        return [], "Could not load users."
    finally:
        cursor.close()
        connection.close()

"""Read destinations from the existing destinations table."""

import mysql.connector

from database.helpers import open_connection


def list_destinations():
    """Return (rows, error_message)."""
    connection, error = open_connection()
    if error:
        return [], error

    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(
            """
            SELECT destination_id, name, country, description,
                   average_daily_cost, popularity_score, rating
            FROM destinations
            ORDER BY popularity_score DESC, name ASC
            """
        )
        return cursor.fetchall(), None
    except mysql.connector.Error:
        return [], "Could not load destinations."
    finally:
        cursor.close()
        connection.close()


def get_destination(destination_id):
    """Return (row, error_message)."""
    if not destination_id:
        return None, None

    connection, error = open_connection()
    if error:
        return None, error

    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(
            """
            SELECT destination_id, name, country, description,
                   average_daily_cost, popularity_score, rating
            FROM destinations
            WHERE destination_id = %s
            """,
            (destination_id,),
        )
        return cursor.fetchone(), None
    except mysql.connector.Error:
        return None, "Could not load the destination."
    finally:
        cursor.close()
        connection.close()

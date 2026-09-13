"""Create and read trips using the existing trips and trip_preferences tables."""

import mysql.connector

from database.helpers import open_connection


def create_trip(
    user_id,
    destination_id,
    start_date,
    end_date,
    travelers,
    total_budget,
    travel_style,
    interests,
    accommodation_preference,
    food_preference,
    weather_preference,
    transport_preference,
):
    """Insert a trip and its preferences. Returns (trip_id, error_message)."""
    connection, error = open_connection()
    if error:
        return None, error

    cursor = connection.cursor()
    try:
        cursor.execute(
            """
            INSERT INTO trips
                (user_id, destination_id, start_date, end_date, travelers, total_budget)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (user_id, destination_id, start_date, end_date, travelers, total_budget),
        )
        trip_id = cursor.lastrowid

        cursor.execute(
            """
            INSERT INTO trip_preferences
                (trip_id, travel_style, interests, accommodation_preference,
                 food_preference, weather_preference, transport_preference)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                trip_id,
                travel_style,
                interests,
                accommodation_preference,
                food_preference,
                weather_preference,
                transport_preference,
            ),
        )
        connection.commit()
        return trip_id, None
    except mysql.connector.Error:
        connection.rollback()
        return None, "Could not save this trip. Please try again later."
    finally:
        cursor.close()
        connection.close()


def list_user_trips(user_id):
    """Return (rows, error_message) for the signed-in user."""
    connection, error = open_connection()
    if error:
        return [], error

    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(
            """
            SELECT
                t.trip_id,
                t.user_id,
                t.destination_id,
                t.start_date,
                t.end_date,
                t.travelers,
                t.total_budget,
                t.created_at,
                d.name AS destination_name,
                d.country,
                p.travel_style,
                p.interests,
                p.accommodation_preference,
                p.food_preference,
                p.weather_preference,
                p.transport_preference
            FROM trips t
            LEFT JOIN destinations d ON d.destination_id = t.destination_id
            LEFT JOIN trip_preferences p ON p.trip_id = t.trip_id
            WHERE t.user_id = %s
            ORDER BY t.created_at DESC
            """,
            (user_id,),
        )
        return cursor.fetchall(), None
    except mysql.connector.Error:
        return [], "Could not load saved trips."
    finally:
        cursor.close()
        connection.close()


def get_user_trip(user_id, trip_id):
    """Return one trip owned by the user, or (None, error)."""
    trips, error = list_user_trips(user_id)
    if error:
        return None, error
    for trip in trips:
        if trip["trip_id"] == trip_id:
            return trip, None
    return None, None

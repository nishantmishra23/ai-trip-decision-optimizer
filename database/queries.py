"""
Database query functions for AI Trip Decision Optimizer.
All functions return None / empty list on DB failure — callers handle fallback.
"""
import streamlit as st
from database.connection import get_connection


# ---------------------------------------------------------------------------
# Destinations
# ---------------------------------------------------------------------------

def get_all_destinations():
    try:
        conn = get_connection()
        if conn is None:
            return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT destination_id, name, country, description,
                   average_daily_cost, popularity_score, rating
            FROM destinations
            ORDER BY popularity_score DESC
        """)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception:
        return []


def get_destination_by_id(dest_id):
    try:
        conn = get_connection()
        if conn is None:
            return None
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM destinations WHERE destination_id = %s", (dest_id,)
        )
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row
    except Exception:
        return None


def insert_destination(name, country, description, avg_cost, popularity, rating):
    try:
        conn = get_connection()
        if conn is None:
            return False
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO destinations
               (name, country, description, average_daily_cost, popularity_score, rating)
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (name, country, description, avg_cost, popularity, rating),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Hotels
# ---------------------------------------------------------------------------

def get_hotels_by_destination(dest_id):
    try:
        conn = get_connection()
        if conn is None:
            return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """SELECT h.*, d.name AS destination_name
               FROM hotels h
               JOIN destinations d ON h.destination_id = d.destination_id
               WHERE h.destination_id = %s
               ORDER BY h.rating DESC""",
            (dest_id,),
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception:
        return []


def get_all_hotels():
    try:
        conn = get_connection()
        if conn is None:
            return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """SELECT h.*, d.name AS destination_name
               FROM hotels h
               JOIN destinations d ON h.destination_id = d.destination_id
               ORDER BY h.rating DESC"""
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception:
        return []


# ---------------------------------------------------------------------------
# Restaurants
# ---------------------------------------------------------------------------

def get_restaurants_by_destination(dest_id):
    try:
        conn = get_connection()
        if conn is None:
            return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """SELECT r.*, d.name AS destination_name
               FROM restaurants r
               JOIN destinations d ON r.destination_id = d.destination_id
               WHERE r.destination_id = %s
               ORDER BY r.rating DESC""",
            (dest_id,),
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception:
        return []


def get_all_restaurants():
    try:
        conn = get_connection()
        if conn is None:
            return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """SELECT r.*, d.name AS destination_name
               FROM restaurants r
               JOIN destinations d ON r.destination_id = d.destination_id
               ORDER BY r.rating DESC"""
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception:
        return []


# ---------------------------------------------------------------------------
# Activities
# ---------------------------------------------------------------------------

def get_activities_by_destination(dest_id):
    try:
        conn = get_connection()
        if conn is None:
            return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """SELECT a.*, d.name AS destination_name
               FROM activities a
               JOIN destinations d ON a.destination_id = d.destination_id
               WHERE a.destination_id = %s
               ORDER BY a.rating DESC""",
            (dest_id,),
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception:
        return []


def get_all_activities():
    try:
        conn = get_connection()
        if conn is None:
            return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """SELECT a.*, d.name AS destination_name
               FROM activities a
               JOIN destinations d ON a.destination_id = d.destination_id
               ORDER BY a.rating DESC"""
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception:
        return []


# ---------------------------------------------------------------------------
# Transportation
# ---------------------------------------------------------------------------

def get_transportation_by_destination(dest_id):
    try:
        conn = get_connection()
        if conn is None:
            return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """SELECT t.*, d.name AS destination_name
               FROM transportation t
               JOIN destinations d ON t.destination_id = d.destination_id
               WHERE t.destination_id = %s
               ORDER BY t.estimated_cost ASC""",
            (dest_id,),
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception:
        return []


def get_all_transportation():
    try:
        conn = get_connection()
        if conn is None:
            return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """SELECT t.*, d.name AS destination_name
               FROM transportation t
               JOIN destinations d ON t.destination_id = d.destination_id
               ORDER BY t.estimated_cost ASC"""
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception:
        return []


# ---------------------------------------------------------------------------
# Weather
# ---------------------------------------------------------------------------

def get_weather_by_destination(dest_id):
    try:
        conn = get_connection()
        if conn is None:
            return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """SELECT w.*, d.name AS destination_name
               FROM weather_records w
               JOIN destinations d ON w.destination_id = d.destination_id
               WHERE w.destination_id = %s
               ORDER BY w.record_date DESC
               LIMIT 30""",
            (dest_id,),
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception:
        return []


# ---------------------------------------------------------------------------
# Trips
# ---------------------------------------------------------------------------

def save_trip(user_id, destination_id, start_date, end_date, travelers, budget):
    try:
        conn = get_connection()
        if conn is None:
            return None
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO trips
               (user_id, destination_id, start_date, end_date, travelers, total_budget)
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (user_id, destination_id, start_date, end_date, travelers, budget),
        )
        conn.commit()
        trip_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return trip_id
    except Exception:
        return None


def save_trip_preferences(trip_id, travel_style, interests, accommodation,
                          food, weather_pref, transport):
    try:
        conn = get_connection()
        if conn is None:
            return False
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO trip_preferences
               (trip_id, travel_style, interests, accommodation_preference,
                food_preference, weather_preference, transport_preference)
               VALUES (%s, %s, %s, %s, %s, %s, %s)""",
            (trip_id, travel_style, interests, accommodation, food,
             weather_pref, transport),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception:
        return False


def get_user_trips(user_id):
    try:
        conn = get_connection()
        if conn is None:
            return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """SELECT t.*, d.name AS destination_name, d.country
               FROM trips t
               LEFT JOIN destinations d ON t.destination_id = d.destination_id
               WHERE t.user_id = %s
               ORDER BY t.created_at DESC""",
            (user_id,),
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception:
        return []


def get_all_trips():
    try:
        conn = get_connection()
        if conn is None:
            return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """SELECT t.*, d.name AS destination_name, u.name AS user_name
               FROM trips t
               LEFT JOIN destinations d ON t.destination_id = d.destination_id
               LEFT JOIN users u ON t.user_id = u.user_id
               ORDER BY t.created_at DESC"""
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception:
        return []


def save_recommendation(trip_id, destination_id, score, explanation):
    try:
        conn = get_connection()
        if conn is None:
            return False
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO recommendations (trip_id, destination_id, score, explanation)
               VALUES (%s, %s, %s, %s)""",
            (trip_id, destination_id, score, explanation),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------

def get_user_by_email(email):
    try:
        conn = get_connection()
        if conn is None:
            return None
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM users WHERE email = %s", (email,)
        )
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row
    except Exception:
        return None


def create_user(name, email, password_hash, role="USER"):
    try:
        conn = get_connection()
        if conn is None:
            return False
        cursor = conn.cursor()
        cursor.execute(
            """INSERT INTO users (name, email, password_hash, role)
               VALUES (%s, %s, %s, %s)""",
            (name, email, password_hash, role),
        )
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception:
        return False


def get_all_users():
    try:
        conn = get_connection()
        if conn is None:
            return []
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT user_id, name, email, role, created_at FROM users ORDER BY created_at DESC"
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except Exception:
        return []


def count_users():
    try:
        conn = get_connection()
        if conn is None:
            return 0
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")
        (count,) = cursor.fetchone()
        cursor.close()
        conn.close()
        return count
    except Exception:
        return 0


def count_destinations():
    try:
        conn = get_connection()
        if conn is None:
            return 0
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM destinations")
        (count,) = cursor.fetchone()
        cursor.close()
        conn.close()
        return count
    except Exception:
        return 0


def count_trips():
    try:
        conn = get_connection()
        if conn is None:
            return 0
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM trips")
        (count,) = cursor.fetchone()
        cursor.close()
        conn.close()
        return count
    except Exception:
        return 0

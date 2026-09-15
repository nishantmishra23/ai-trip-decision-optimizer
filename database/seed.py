"""Insert sample destinations if the table is empty. Does not change the schema."""

import mysql.connector

from database.helpers import open_connection

SAMPLE_DESTINATIONS = [
    ("Goa", "India", "Beaches, nightlife, and relaxed coastal travel.", 4500.00, 9.2, 4.5),
    ("Manali", "India", "Mountain town popular for adventure and scenery.", 3800.00, 8.6, 4.4),
    ("Jaipur", "India", "Heritage palaces, culture, and food.", 3200.00, 8.4, 4.3),
    ("Kochi", "India", "Backwaters, spice markets, and coastal cuisine.", 3000.00, 8.1, 4.4),
    ("Paris", "France", "Museums, cafes, and classic city sightseeing.", 12000.00, 9.5, 4.7),
    ("Tokyo", "Japan", "Modern city travel with food and culture.", 11000.00, 9.4, 4.6),
    ("Bali", "Indonesia", "Temples, beaches, and wellness-focused trips.", 6500.00, 9.0, 4.5),
    ("Dubai", "UAE", "Shopping, architecture, and desert experiences.", 10000.00, 8.8, 4.4),
    ("Singapore", "Singapore", "Compact city break with food and attractions.", 9500.00, 8.7, 4.6),
    ("New York", "USA", "Urban sightseeing, food, and entertainment.", 13000.00, 9.1, 4.5),
]


def seed_destinations_if_empty():
    """
    Add starter destinations only when none exist yet.

    Returns (inserted_count, error_message).
    """
    connection, error = open_connection()
    if error:
        return 0, error

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT COUNT(*) FROM destinations")
        count = cursor.fetchone()[0]
        if count:
            return 0, None

        cursor.executemany(
            """
            INSERT INTO destinations
                (name, country, description, average_daily_cost, popularity_score, rating)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            SAMPLE_DESTINATIONS,
        )
        connection.commit()
        return cursor.rowcount, None
    except mysql.connector.Error:
        connection.rollback()
        return 0, "Could not add sample destinations."
    finally:
        cursor.close()
        connection.close()

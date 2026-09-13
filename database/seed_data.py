"""
Seed script — run once to populate the database with sample data.
Usage: python database/seed_data.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv()

from database.connection import get_connection
from datetime import date, timedelta
import random

DESTINATIONS = [
    {
        "name": "Goa", "country": "India",
        "description": "India's party capital with pristine beaches, Portuguese heritage, vibrant nightlife, and world-class seafood.",
        "avg_cost": 3500, "popularity": 9.2, "rating": 4.5,
        "season": "Oct-Mar", "category": "Beach",
        "hotels": [
            ("The Leela Goa", 12000, 4.8, "Luxury"),
            ("Cidade de Goa", 7500, 4.3, "5-Star"),
            ("Zostel Goa", 600, 4.1, "Hostel"),
            ("Park Hyatt Goa", 15000, 4.9, "Luxury"),
            ("OYO Rooms Calangute", 1200, 3.5, "Budget"),
        ],
        "restaurants": [
            ("Thalassa", "Greek-Mediterranean", 1800, 4.6),
            ("Vinayak Family Restaurant", "Goan Seafood", 600, 4.5),
            ("Gunpowder", "South Indian", 900, 4.4),
            ("Britto's", "Seafood", 1200, 4.3),
            ("Fisherman's Wharf", "Seafood", 1500, 4.5),
        ],
        "activities": [
            ("Scuba Diving at Grande Island", "Water Sports", 3500, 4.7),
            ("Dudhsagar Waterfall Trek", "Adventure", 1200, 4.6),
            ("Old Goa Church Tour", "Heritage", 200, 4.4),
            ("Spice Plantation Tour", "Nature", 800, 4.3),
            ("Nightlife at Tito's", "Entertainment", 1000, 4.0),
        ],
        "transport": [
            ("Flight from Delhi", 4500, 150, 4.2),
            ("Train from Mumbai", 800, 480, 4.0),
            ("Bus from Mumbai", 400, 600, 3.5),
        ],
        "weather": {"temp": 30, "rainfall": 5, "condition": "Sunny"},
    },
    {
        "name": "Manali", "country": "India",
        "description": "Snow-capped Himalayan retreat famous for adventure sports, scenic valleys, and serene monasteries.",
        "avg_cost": 2800, "popularity": 8.8, "rating": 4.6,
        "season": "Oct-Jun", "category": "Mountains",
        "hotels": [
            ("Solang Valley Resort", 8000, 4.6, "Resort"),
            ("Johnson's Hotel", 4500, 4.4, "Boutique"),
            ("The Himalayan", 6500, 4.5, "4-Star"),
            ("Zostel Manali", 700, 4.2, "Hostel"),
            ("Hotel Snow Valley", 2000, 3.8, "Budget"),
        ],
        "restaurants": [
            ("Drifters' Inn", "Continental", 700, 4.5),
            ("Johnson's Café", "Multicuisine", 900, 4.4),
            ("Café 1947", "Indian", 500, 4.3),
            ("Khyber Restaurant", "North Indian", 600, 4.2),
            ("La Plage", "French", 1200, 4.4),
        ],
        "activities": [
            ("Rohtang Pass Snow Trip", "Adventure", 2500, 4.8),
            ("Solang Valley Skiing", "Adventure", 1800, 4.7),
            ("Hadimba Temple Visit", "Heritage", 0, 4.5),
            ("River Rafting on Beas", "Water Sports", 1200, 4.6),
            ("Kullu Paragliding", "Adventure", 2000, 4.7),
        ],
        "transport": [
            ("Flight to Bhuntar + Taxi", 5000, 180, 4.0),
            ("Volvo Bus from Delhi", 1200, 720, 4.1),
            ("Train to Chandigarh + Bus", 900, 900, 3.8),
        ],
        "weather": {"temp": 10, "rainfall": 15, "condition": "Partly Cloudy"},
    },
    {
        "name": "Rajasthan (Jaipur)", "country": "India",
        "description": "The Pink City — regal forts, ornate palaces, vibrant bazaars and royal Rajputana cuisine.",
        "avg_cost": 2500, "popularity": 9.0, "rating": 4.5,
        "season": "Oct-Mar", "category": "Heritage",
        "hotels": [
            ("Rambagh Palace", 35000, 4.9, "Heritage Luxury"),
            ("ITC Rajputana", 9000, 4.6, "5-Star"),
            ("Zostel Jaipur", 650, 4.2, "Hostel"),
            ("Hotel Pearl Palace", 1800, 4.4, "Budget Boutique"),
            ("Jai Mahal Palace", 14000, 4.7, "Heritage"),
        ],
        "restaurants": [
            ("Suvarna Mahal", "Rajasthani", 3000, 4.8),
            ("Laxmi Mishthan Bhandar", "Indian", 200, 4.6),
            ("Bar Palladio", "Italian-Indian", 2000, 4.5),
            ("Spice Court", "Rajasthani", 1200, 4.4),
            ("Chokhi Dhani", "Traditional Rajasthani", 1500, 4.6),
        ],
        "activities": [
            ("Amber Fort Elephant Ride", "Heritage", 1500, 4.7),
            ("City Palace Tour", "Heritage", 700, 4.6),
            ("Hawa Mahal Photography", "Sightseeing", 50, 4.5),
            ("Jaipur Literature Festival", "Cultural", 0, 4.8),
            ("Johari Bazaar Shopping", "Shopping", 0, 4.3),
        ],
        "transport": [
            ("Flight from Delhi", 3000, 60, 4.3),
            ("Train from Delhi", 500, 270, 4.2),
            ("Bus from Delhi", 400, 300, 3.7),
        ],
        "weather": {"temp": 26, "rainfall": 2, "condition": "Clear"},
    },
    {
        "name": "Kerala (Munnar)", "country": "India",
        "description": "God's Own Country — tranquil backwaters, lush tea estates, Ayurvedic retreats, and misty hill stations.",
        "avg_cost": 3000, "popularity": 8.9, "rating": 4.7,
        "season": "Oct-May", "category": "Nature",
        "hotels": [
            ("Windermere Estate", 9500, 4.7, "Boutique"),
            ("Spice Tree Munnar", 12000, 4.8, "Luxury"),
            ("Tea Nest", 4500, 4.5, "Resort"),
            ("Hotel Munnar Castle", 2500, 4.1, "Mid-range"),
            ("Zostel Munnar", 750, 4.3, "Hostel"),
        ],
        "restaurants": [
            ("Saravana Bhavan", "South Indian", 300, 4.5),
            ("Rapsy Restaurant", "Kerala Cuisine", 500, 4.4),
            ("Zaza Bistro", "Continental", 800, 4.3),
            ("Silver Spoon", "Multicuisine", 700, 4.2),
            ("Eco Café", "Organic", 600, 4.5),
        ],
        "activities": [
            ("Tea Plantation Walk", "Nature", 300, 4.7),
            ("Eravikulam National Park", "Wildlife", 150, 4.6),
            ("Mattupetty Dam Boating", "Nature", 200, 4.4),
            ("Ayurvedic Massage", "Wellness", 2500, 4.8),
            ("Top Station Trek", "Adventure", 500, 4.6),
        ],
        "transport": [
            ("Flight to Kochi + Taxi", 5500, 200, 4.1),
            ("Train to Ernakulam + Bus", 1200, 420, 4.0),
            ("Bus from Bangalore", 800, 480, 3.8),
        ],
        "weather": {"temp": 20, "rainfall": 20, "condition": "Misty"},
    },
    {
        "name": "Agra", "country": "India",
        "description": "Home to the iconic Taj Mahal, Agra Fort, and Mughal culinary heritage. A UNESCO World Heritage destination.",
        "avg_cost": 2000, "popularity": 9.5, "rating": 4.4,
        "season": "Oct-Mar", "category": "Heritage",
        "hotels": [
            ("The Oberoi Amarvilas", 40000, 4.9, "Luxury"),
            ("ITC Mughal", 12000, 4.7, "5-Star"),
            ("Hotel Sheela", 1200, 4.2, "Budget"),
            ("Crystall Sarovar Premiere", 6000, 4.4, "4-Star"),
            ("Zostel Agra", 600, 4.1, "Hostel"),
        ],
        "restaurants": [
            ("Peshawri at ITC", "Mughal", 2500, 4.7),
            ("Dasaprakash", "South Indian", 400, 4.4),
            ("Pinch of Spice", "North Indian", 900, 4.5),
            ("Espahan", "Mughal Fine Dining", 3000, 4.8),
            ("Mama Chicken", "Tandoori", 600, 4.3),
        ],
        "activities": [
            ("Taj Mahal Sunrise Visit", "Heritage", 1100, 4.9),
            ("Agra Fort Exploration", "Heritage", 550, 4.6),
            ("Fatehpur Sikri Day Trip", "Heritage", 810, 4.5),
            ("Mehtab Bagh Sunset View", "Sightseeing", 300, 4.7),
            ("Petha Sweet Making Class", "Cultural", 500, 4.3),
        ],
        "transport": [
            ("Train from Delhi (Shatabdi)", 700, 120, 4.5),
            ("Bus from Delhi", 300, 210, 3.6),
            ("Flight + Taxi via Delhi", 4000, 180, 3.9),
        ],
        "weather": {"temp": 25, "rainfall": 1, "condition": "Hazy"},
    },
    {
        "name": "Bali", "country": "Indonesia",
        "description": "Tropical paradise with iconic rice terraces, Hindu temples, world-class surfing, and luxury spas.",
        "avg_cost": 4500, "popularity": 9.4, "rating": 4.8,
        "season": "Apr-Oct", "category": "Beach",
        "hotels": [
            ("Four Seasons Jimbaran", 45000, 4.9, "Luxury"),
            ("Alaya Resort Ubud", 12000, 4.7, "Boutique"),
            ("Potato Head Suites", 18000, 4.8, "Design Hotel"),
            ("Puri Dajuma Cottages", 6000, 4.5, "Eco-Resort"),
            ("Bunk Hostel Bali", 800, 4.2, "Hostel"),
        ],
        "restaurants": [
            ("Locavore", "Modern Indonesian", 4000, 4.9),
            ("Sardine", "Seafood", 3000, 4.7),
            ("Warung Ibu Oka", "Balinese Suckling Pig", 400, 4.6),
            ("Swept Away", "Fine Dining", 5000, 4.8),
            ("Naughty Nuri's", "BBQ Ribs", 600, 4.5),
        ],
        "activities": [
            ("Tanah Lot Temple Sunset", "Heritage", 600, 4.8),
            ("Tegallalang Rice Terrace", "Nature", 300, 4.7),
            ("Kuta Beach Surfing", "Water Sports", 1500, 4.6),
            ("Ubud Monkey Forest", "Wildlife", 400, 4.5),
            ("Traditional Balinese Spa", "Wellness", 2500, 4.8),
        ],
        "transport": [
            ("Flight from Delhi", 18000, 390, 4.3),
            ("Flight from Mumbai", 14000, 330, 4.3),
            ("Bali Driver Rental (daily)", 2500, 0, 4.6),
        ],
        "weather": {"temp": 28, "rainfall": 10, "condition": "Tropical"},
    },
    {
        "name": "Paris", "country": "France",
        "description": "The City of Light — Eiffel Tower, Louvre, haute cuisine, fashion, and timeless romance.",
        "avg_cost": 12000, "popularity": 9.6, "rating": 4.7,
        "season": "Apr-Jun, Sep-Oct", "category": "City",
        "hotels": [
            ("Le Meurice", 80000, 4.9, "Palace"),
            ("Hôtel Plaza Athénée", 70000, 4.9, "Luxury"),
            ("citizenM Paris", 9000, 4.5, "Design"),
            ("Hôtel du Temps", 6500, 4.3, "Boutique"),
            ("Generator Paris Hostel", 1500, 4.1, "Hostel"),
        ],
        "restaurants": [
            ("Guy Savoy", "French Fine Dining", 25000, 4.9),
            ("Septime", "Modern French", 7000, 4.8),
            ("Le Comptoir du Relais", "Bistro", 2500, 4.6),
            ("L'As du Fallafel", "Middle Eastern", 500, 4.7),
            ("Café de Flore", "French Café", 1500, 4.5),
        ],
        "activities": [
            ("Eiffel Tower Summit", "Landmark", 3000, 4.8),
            ("Louvre Museum", "Art & Culture", 2000, 4.9),
            ("Versailles Palace Day Trip", "Heritage", 3500, 4.7),
            ("Seine River Cruise", "Sightseeing", 1800, 4.6),
            ("Montmartre Walking Tour", "Cultural", 0, 4.7),
        ],
        "transport": [
            ("Flight from Delhi (Economy)", 35000, 480, 4.2),
            ("Eurostar from London", 5000, 150, 4.6),
            ("Metro Day Pass Paris", 800, 0, 4.5),
        ],
        "weather": {"temp": 18, "rainfall": 8, "condition": "Overcast"},
    },
    {
        "name": "Rishikesh", "country": "India",
        "description": "Yoga capital of the world — spiritual retreat by the Ganges with thrilling adventure sports and ashram experiences.",
        "avg_cost": 1800, "popularity": 8.7, "rating": 4.5,
        "season": "Sep-Jun", "category": "Adventure",
        "hotels": [
            ("Ananda in the Himalayas", 35000, 4.9, "Luxury Wellness"),
            ("Zostel Rishikesh", 600, 4.3, "Hostel"),
            ("Divine Ganga Cottage", 2500, 4.4, "Boutique"),
            ("Tattva Resort", 5000, 4.3, "Resort"),
            ("Hotel Natraj", 1200, 3.9, "Budget"),
        ],
        "restaurants": [
            ("The Sitting Elephant", "Israeli-Indian", 500, 4.6),
            ("Freedom Café", "Multicuisine", 400, 4.5),
            ("Chotiwala", "Indian", 200, 4.4),
            ("Little Buddha Café", "Continental", 600, 4.5),
            ("60's Restaurant", "Indian-Continental", 500, 4.3),
        ],
        "activities": [
            ("White Water Rafting", "Adventure", 1500, 4.8),
            ("Bungee Jumping", "Extreme Sports", 3500, 4.7),
            ("Beatles Ashram Visit", "Cultural", 150, 4.5),
            ("Yoga & Meditation Retreat", "Wellness", 2000, 4.9),
            ("Lakshmanjhula Trek", "Hiking", 0, 4.4),
        ],
        "transport": [
            ("Train from Delhi", 400, 300, 4.1),
            ("Bus from Delhi", 350, 360, 3.8),
            ("Taxi from Dehradun Airport", 800, 60, 4.2),
        ],
        "weather": {"temp": 22, "rainfall": 12, "condition": "Partly Cloudy"},
    },
    {
        "name": "Andaman Islands", "country": "India",
        "description": "Crystal-clear turquoise waters, pristine white sand beaches, vibrant coral reefs, and untouched tropical forests.",
        "avg_cost": 5000, "popularity": 8.5, "rating": 4.8,
        "season": "Oct-May", "category": "Beach",
        "hotels": [
            ("Barefoot at Havelock", 15000, 4.8, "Eco-Luxury"),
            ("Munjoh Ocean Resort", 12000, 4.7, "Resort"),
            ("Symphony Palms", 8000, 4.5, "4-Star"),
            ("Teal House", 3500, 4.4, "Boutique"),
            ("Aqua Hostel Havelock", 900, 4.3, "Hostel"),
        ],
        "restaurants": [
            ("Anju Coco", "Multicuisine", 600, 4.5),
            ("Full Moon Café", "Seafood", 800, 4.6),
            ("Something Different", "Seafood-Indian", 700, 4.4),
            ("Barefoot Bar", "Continental", 1200, 4.5),
            ("Havelock Social", "Bar-Grill", 1000, 4.3),
        ],
        "activities": [
            ("Radhanagar Beach Sunset", "Sightseeing", 0, 4.9),
            ("Scuba Diving Elephant Beach", "Water Sports", 4000, 4.8),
            ("Cellular Jail Tour", "Heritage", 200, 4.6),
            ("Sea Walk Havelock", "Water Sports", 3500, 4.7),
            ("Kayaking in Mangroves", "Nature", 1500, 4.6),
        ],
        "transport": [
            ("Flight from Chennai", 8000, 120, 4.4),
            ("Flight from Kolkata", 9000, 150, 4.3),
            ("Government Ferry (local)", 300, 120, 3.8),
        ],
        "weather": {"temp": 29, "rainfall": 8, "condition": "Sunny"},
    },
    {
        "name": "Leh-Ladakh", "country": "India",
        "description": "The land of high passes — dramatic moonscapes, Tibetan Buddhist culture, pristine mountain lakes, and epic motorbike routes.",
        "avg_cost": 4000, "popularity": 8.6, "rating": 4.8,
        "season": "Jun-Sep", "category": "Mountains",
        "hotels": [
            ("The Grand Dragon Ladakh", 8000, 4.7, "Luxury"),
            ("Chamba Camp Thiksey", 15000, 4.8, "Glamping"),
            ("Zostel Leh", 800, 4.4, "Hostel"),
            ("Hotel Bijoo", 3500, 4.3, "Mid-range"),
            ("Pangong Eco Camps", 5000, 4.6, "Camp"),
        ],
        "restaurants": [
            ("Gesmo Restaurant", "Tibetan-Indian", 600, 4.6),
            ("Bon Appetit", "Continental", 800, 4.5),
            ("Tibetan Kitchen", "Tibetan", 400, 4.5),
            ("Alchi Kitchen", "Ladakhi", 500, 4.6),
            ("The Bookstore Café", "Café", 350, 4.4),
        ],
        "activities": [
            ("Pangong Lake Visit", "Nature", 2000, 4.9),
            ("Khardung La Pass Bike Ride", "Adventure", 1500, 4.8),
            ("Nubra Valley Camel Safari", "Adventure", 2500, 4.7),
            ("Hemis Monastery", "Cultural", 100, 4.6),
            ("Magnetic Hill", "Sightseeing", 0, 4.3),
        ],
        "transport": [
            ("Flight from Delhi", 8000, 75, 4.5),
            ("Manali-Leh Highway (Bike/Bus)", 1500, 1440, 4.7),
            ("Srinagar-Leh Highway", 1200, 720, 4.6),
        ],
        "weather": {"temp": 15, "rainfall": 3, "condition": "Clear & Dry"},
    },
]


def seed():
    conn = get_connection()
    if conn is None:
        print("ERROR: Could not connect to database. Check your .env file.")
        return

    cursor = conn.cursor()

    print("Seeding destinations...")
    for dest in DESTINATIONS:
        # Insert destination
        cursor.execute(
            """INSERT IGNORE INTO destinations
               (name, country, description, average_daily_cost, popularity_score, rating)
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (dest["name"], dest["country"], dest["description"],
             dest["avg_cost"], dest["popularity"], dest["rating"]),
        )
        conn.commit()
        dest_id = cursor.lastrowid
        if dest_id == 0:
            cursor.execute("SELECT destination_id FROM destinations WHERE name=%s", (dest["name"],))
            dest_id = cursor.fetchone()[0]

        # Hotels
        for h in dest["hotels"]:
            cursor.execute(
                """INSERT IGNORE INTO hotels
                   (destination_id, name, price_per_night, rating, hotel_type)
                   VALUES (%s, %s, %s, %s, %s)""",
                (dest_id, h[0], h[1], h[2], h[3]),
            )

        # Restaurants
        for r in dest["restaurants"]:
            cursor.execute(
                """INSERT IGNORE INTO restaurants
                   (destination_id, name, cuisine, average_cost, rating)
                   VALUES (%s, %s, %s, %s, %s)""",
                (dest_id, r[0], r[1], r[2], r[3]),
            )

        # Activities
        for a in dest["activities"]:
            cursor.execute(
                """INSERT IGNORE INTO activities
                   (destination_id, name, category, price, rating)
                   VALUES (%s, %s, %s, %s, %s)""",
                (dest_id, a[0], a[1], a[2], a[3]),
            )

        # Transport
        for t in dest["transport"]:
            cursor.execute(
                """INSERT IGNORE INTO transportation
                   (destination_id, transport_type, estimated_cost, duration_minutes, rating)
                   VALUES (%s, %s, %s, %s, %s)""",
                (dest_id, t[0], t[1], t[2], t[3]),
            )

        # Weather records (12 months)
        w = dest["weather"]
        base_temp = w["temp"]
        for month in range(12):
            rec_date = date(2024, month + 1, 15)
            temp_var = base_temp + random.uniform(-8, 8)
            rain_var = max(0, w["rainfall"] + random.uniform(-10, 20))
            cursor.execute(
                """INSERT IGNORE INTO weather_records
                   (destination_id, record_date, temperature, rainfall, weather_condition)
                   VALUES (%s, %s, %s, %s, %s)""",
                (dest_id, rec_date, round(temp_var, 1), round(rain_var, 1), w["condition"]),
            )

        print(f"  ✓ {dest['name']}, {dest['country']}")

    conn.commit()
    cursor.close()
    conn.close()
    print("\nSeeding complete! Database is ready.")


if __name__ == "__main__":
    seed()

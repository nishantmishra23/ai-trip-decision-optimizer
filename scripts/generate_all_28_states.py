"""
Comprehensive generator for all 28 states and their 4-8 destinations,
including neighborhoods, places, activities, hotels, and restaurants.
"""
import os
import json
import urllib.parse

def gmaps_url(query):
    return f"https://www.google.com/maps/search/?api=1&query={urllib.parse.quote_plus(query)}"

# Let's define the comprehensive dataset
def build_dataset():
    data = {}
    
    # We will build all 28 states systematically
    # Helper to construct a destination cleanly
    def make_dest(name, tagline, overview, budget_daily, best_time, duration, rating, popularity, travel_style, suitability, weather_city, neighborhoods, places, activities, hotels, restaurants):
        # Ensure gmaps links
        for h in hotels:
            if "gmaps_url" not in h:
                h["gmaps_url"] = gmaps_url(f"{h['name']}, {name}")
        for r in restaurants:
            if "gmaps_url" not in r:
                r["gmaps_url"] = gmaps_url(f"{r['name']}, {name}")
        for p in places:
            if "gmaps_url" not in p:
                p["gmaps_url"] = gmaps_url(f"{p['name']}, {name}")
        return {
            "name": name,
            "tagline": tagline,
            "overview": overview,
            "budget_daily": budget_daily,
            "best_time": best_time,
            "recommended_duration": duration,
            "rating": rating,
            "popularity": popularity,
            "travel_style": travel_style,
            "suitability": suitability,
            "weather_city": weather_city,
            "neighborhoods": neighborhoods,
            "places_to_visit": places,
            "things_to_do": activities,
            "hotels": hotels,
            "restaurants": restaurants
        }

    # 1. Andhra Pradesh
    data["Andhra Pradesh"] = {
        "capital": "Amaravati", "region": "South", "tagline": "The Sunrise State of India",
        "destinations": [
            make_dest(
                "Visakhapatnam", "The Jewel of the East Coast",
                "Port city with blue flag beaches, submarine museum, and scenic hill views over the Bay of Bengal.",
                1800, "Oct–Mar", "3 Days", 4.7, 8.9, "Beach & Coastal City", ["Family", "Couples", "Solo", "Friends"], "Visakhapatnam",
                ["Rushikonda Beach", "RK Beach & Pandurangapuram", "Kailasagiri Hill", "MVP Colony", "Siripuram"],
                [
                    {"name": "Rushikonda Beach", "category": "Beach", "highlight": "Blue flag certified golden sands & water sports", "fee": "Free", "time": "3 hrs"},
                    {"name": "INS Kurusura Submarine Museum", "category": "Museum", "highlight": "Decommissioned Soviet-built submarine on beach", "fee": "₹70", "time": "1.5 hrs"},
                    {"name": "Kailasagiri Hilltop Park", "category": "Viewpoint", "highlight": "Coastline panorama & giant Shiva statue", "fee": "₹20", "time": "2 hrs"},
                    {"name": "Yarada Beach", "category": "Beach", "highlight": "Secluded beach flanked by Dolphin's Nose cliff", "fee": "Free", "time": "2.5 hrs"}
                ],
                [
                    {"name": "Jet Skiing & Speed Boating at Rushikonda", "category": "Water Sports", "cost": 600, "duration": "1 hr"},
                    {"name": "Kailasagiri Ropeway Cable Car Ride", "category": "Scenic Ride", "cost": 150, "duration": "45 mins"},
                    {"name": "Evening Promenade & Seafood Tasting", "category": "Food Walk", "cost": 350, "duration": "2 hrs"},
                ],
                [
                    {"name": "The Park Visakhapatnam", "category": "Luxury 5-Star", "price_per_night": 9500, "rating": 4.7, "area": "RK Beach", "amenities": ["Pool", "Sea View", "Free WiFi", "Spa"], "suitability": ["Couples", "Family"]},
                    {"name": "Radisson Blu Resort", "category": "Luxury Resort", "price_per_night": 11000, "rating": 4.8, "area": "Rushikonda Beach", "amenities": ["Infinity Pool", "Private Beach", "Free WiFi"], "suitability": ["Couples", "Family"]},
                    {"name": "Hotel Novotel Varun Beach", "category": "5-Star Deluxe", "price_per_night": 10500, "rating": 4.8, "area": "RK Beach", "amenities": ["Rooftop Pool", "Ocean View", "Spa"], "suitability": ["Couples", "Family", "Solo"]},
                    {"name": "Keys Select Hotel", "category": "Mid-range Hotel", "price_per_night": 3200, "rating": 4.3, "area": "Siripuram", "amenities": ["Free Breakfast", "Free WiFi", "AC"], "suitability": ["Solo", "Family"]},
                    {"name": "Zostel Visakhapatnam", "category": "Backpacker Hostel", "price_per_night": 850, "rating": 4.4, "area": "Rushikonda Beach", "amenities": ["Free WiFi", "AC Dorms", "Cafe"], "suitability": ["Solo", "Friends"]},
                ],
                [
                    {"name": "Dharani at Dasaprakash", "cuisine": "Andhra & South Indian Thali", "average_cost_for_two": 600, "rating": 4.6, "area": "Siripuram", "popular_dishes": "Royal Andhra Meals, Pesarattu", "is_veg": True},
                    {"name": "Sea Inn (Raju Gari Dhaba)", "cuisine": "Andhra Seafood", "average_cost_for_two": 750, "rating": 4.5, "area": "Rushikonda", "popular_dishes": "Crab Fry, Prawn Biryani", "is_veg": False},
                    {"name": "Bamboo Bay", "cuisine": "Coastal Fine Dining", "average_cost_for_two": 2200, "rating": 4.7, "area": "RK Beach", "popular_dishes": "Tandoori Lobster, Mutton Fry", "is_veg": False},
                    {"name": "Bean Board Coffee", "cuisine": "Specialty Coffee & Cafe", "average_cost_for_two": 450, "rating": 4.6, "area": "MVP Colony", "popular_dishes": "Cold Brew, Croissants", "is_veg": True},
                ]
            ),
            make_dest(
                "Araku Valley", "The Valley of Coffee & Clouds",
                "Hill station in Eastern Ghats with organic coffee estates, indigenous tribal villages, and prehistoric caves.",
                1500, "Sep–Mar", "2 Days", 4.7, 8.5, "Hill Station & Nature", ["Family", "Couples", "Friends", "Solo"], "Araku Valley",
                ["Araku Town Center", "Borra Caves Area", "Chaparai Cascades", "Ananthagiri Hills"],
                [
                    {"name": "Borra Caves", "category": "Caves", "highlight": "Million-year-old limestone stalactite formations", "fee": "₹80", "time": "2 hrs"},
                    {"name": "Chaparai Water Cascades", "category": "Waterfall", "highlight": "Natural stream flowing gently over wide rock slabs", "fee": "₹20", "time": "2 hrs"},
                    {"name": "Coffee Museum & Plantation", "category": "Agri-Tourism", "highlight": "Arabica coffee history and bean tasting", "fee": "₹50", "time": "1 hr"},
                    {"name": "Padmapuram Botanical Gardens", "category": "Gardens", "highlight": "Hanging tree huts and flower terraces", "fee": "₹40", "time": "1.5 hrs"}
                ],
                [
                    {"name": "Vistadome Glass Train Ride through 58 tunnels", "category": "Scenic Train", "cost": 750, "duration": "3 hrs"},
                    {"name": "Bongu (Bamboo) Chicken Cooking & Tasting", "category": "Food Experience", "cost": 300, "duration": "1 hr"},
                    {"name": "Coffee Estate Trekking & Berry Picking", "category": "Agri Trek", "cost": 250, "duration": "2 hrs"}
                ],
                [
                    {"name": "Haritha Valley Resort", "category": "Nature Resort", "price_per_night": 3200, "rating": 4.2, "area": "Araku Town Center", "amenities": ["Garden", "Restaurant", "Balcony View"], "suitability": ["Family", "Couples"]},
                    {"name": "Ananthagiri Haritha Hill Resort", "category": "Hill Resort", "price_per_night": 3800, "rating": 4.3, "area": "Ananthagiri Hills", "amenities": ["Coffee View", "Restaurant", "Trekking"], "suitability": ["Couples", "Family"]},
                    {"name": "Camp Araku Tribals", "category": "Eco Camp", "price_per_night": 1400, "rating": 4.1, "area": "Chaparai Cascades", "amenities": ["Tents", "Campfire", "Meals"], "suitability": ["Friends", "Solo"]},
                ],
                [
                    {"name": "Tribal Bamboo Kitchen", "cuisine": "Tribal Andhra", "average_cost_for_two": 500, "rating": 4.5, "area": "Araku Town Center", "popular_dishes": "Bongu Chicken, Bamboo Rice", "is_veg": False},
                    {"name": "Mayuri Multi-cuisine", "cuisine": "Andhra Meals", "average_cost_for_two": 350, "rating": 4.2, "area": "Araku Center", "popular_dishes": "Unlimited Andhra Thali", "is_veg": True},
                ]
            ),
            make_dest(
                "Tirupati", "The Spiritual Capital of Andhra",
                "World's most visited pilgrimage center situated at the base of the holy Seven Hills of Tirumala.",
                1400, "Sep–Mar", "2 Days", 4.8, 9.7, "Spiritual & Heritage", ["Family", "Solo", "Couples"], "Tirupati",
                ["Tirumala Sacred Hills", "Alipiri Foothills", "Bairagi Patteda", "Chandragiri Road"],
                [
                    {"name": "Sri Venkateswara Swamy Temple", "category": "Temple", "highlight": "Ancient gold-domed sanctum of Lord Balaji", "fee": "₹300", "time": "4 hrs"},
                    {"name": "Chandragiri Fort & Raja Mahal", "category": "Fort", "highlight": "11th-century Vijayanagara palace fortress", "fee": "₹30", "time": "2 hrs"},
                    {"name": "Silathoranam Natural Stone Arch", "category": "Geology", "highlight": "Prehistoric rock arch in Tirumala hills", "fee": "Free", "time": "45 mins"}
                ],
                [
                    {"name": "Alipiri Footpath Trek (3550 Steps)", "category": "Pilgrimage Trek", "cost": 0, "duration": "4 hrs"},
                    {"name": "Tirupati Laddu Prasadam Experience", "category": "Food Culture", "cost": 50, "duration": "30 mins"},
                ],
                [
                    {"name": "Fortune Select Grand Ridge", "category": "Luxury 5-Star", "price_per_night": 6500, "rating": 4.6, "area": "Shilparamam", "amenities": ["Pool", "Pure Veg", "Free WiFi"], "suitability": ["Family", "Couples"]},
                    {"name": "Hotel Bliss", "category": "Mid-range Hotel", "price_per_night": 2800, "rating": 4.3, "area": "Near Railway Station", "amenities": ["Veg Dining", "AC", "Free WiFi"], "suitability": ["Family", "Solo"]},
                    {"name": "Bhimas Deluxe", "category": "Budget Hotel", "price_per_night": 1600, "rating": 4.2, "area": "Car Street", "amenities": ["AC", "Restaurant"], "suitability": ["Family", "Solo"]},
                ],
                [
                    {"name": "Bhimas Pure Veg", "cuisine": "Traditional South Indian", "average_cost_for_two": 350, "rating": 4.6, "area": "Station Road", "popular_dishes": "Ghee Roast Dosa, Thali", "is_veg": True},
                    {"name": "Saravana Bhavan", "cuisine": "Pure Veg South Indian", "average_cost_for_two": 400, "rating": 4.5, "area": "Alipiri Road", "popular_dishes": "Rava Masala Dosa, Filter Coffee", "is_veg": True},
                ]
            ),
            make_dest(
                "Gandikota", "The Grand Canyon of India",
                "Spectacular 300-ft red granite gorge carved by the Pennar River, featuring a medieval fort.",
                1300, "Oct–Feb", "2 Days", 4.7, 8.4, "Adventure & Nature", ["Friends", "Solo", "Couples"], "Kadapa",
                ["Fort Citadel", "Gorge Rim Viewpoint", "Mylavaram Dam Road"],
                [
                    {"name": "Pennar River Gorge", "category": "Canyon", "highlight": "Massive canyon reminiscent of Arizona's Grand Canyon", "fee": "Free", "time": "3 hrs"},
                    {"name": "Gandikota Fort & Jamia Masjid", "category": "Fort", "highlight": "12th-century stone fort and granary", "fee": "Free", "time": "2 hrs"},
                    {"name": "Belum Caves", "category": "Caves", "highlight": "Second longest underground cave network in India", "fee": "₹70", "time": "2.5 hrs"}
                ],
                [
                    {"name": "Canyon Cliffside Stargazing & Camping", "category": "Camping", "cost": 1200, "duration": "Overnight"},
                    {"name": "Kayaking in Pennar River Waters", "category": "Water Sports", "cost": 350, "duration": "1 hr"},
                ],
                [
                    {"name": "Haritha Resort Gandikota", "category": "State Resort", "price_per_night": 2200, "rating": 4.1, "area": "Fort Entrance", "amenities": ["Restaurant", "Parking"], "suitability": ["Family", "Couples"]},
                    {"name": "Freakouts Canyon Camp", "category": "Adventure Camp", "price_per_night": 1400, "rating": 4.4, "area": "Gorge View", "amenities": ["Tents", "Campfire"], "suitability": ["Friends", "Solo"]},
                ],
                [
                    {"name": "Haritha Dining Hall", "cuisine": "Rayalaseema Andhra", "average_cost_for_two": 350, "rating": 4.0, "area": "Haritha Resort", "popular_dishes": "Ragi Sankati, Natu Kodi Pulusu", "is_veg": False},
                ]
            ),
            make_dest(
                "Vijayawada", "The Heart of the Krishna River",
                "Vibrant commercial city with hill temples, rock-cut Buddhist caves, and river island recreation.",
                1600, "Oct–Mar", "2 Days", 4.5, 8.3, "Heritage & River", ["Family", "Business", "Solo"], "Vijayawada",
                ["Bhavani Island", "Indrakeeladri Hill", "MG Road & Governorpet", "Undavalli Caves Area"],
                [
                    {"name": "Kanaka Durga Temple", "category": "Temple", "highlight": "Historic hilltop temple on Indrakeeladri overlooking Krishna River", "fee": "₹100 (Special)", "time": "2 hrs"},
                    {"name": "Undavalli Caves", "category": "Rock-cut Caves", "highlight": "7th-century rock-cut monolithic sculpture of Lord Vishnu", "fee": "₹25", "time": "2 hrs"},
                    {"name": "Bhavani Island", "category": "River Island", "highlight": "133-acre island on Krishna River with water sports and tree houses", "fee": "₹120 (Boat+Entry)", "time": "3 hrs"},
                    {"name": "Prakasam Barrage", "category": "Engineering Landmark", "highlight": "1.2 km long road bridge with evening illumination", "fee": "Free", "time": "1 hr"}
                ],
                [
                    {"name": "Krishna River Speedboat & Jet Ski Ride", "category": "Water Sports", "cost": 450, "duration": "45 mins"},
                    {"name": "Undavalli Cave Heritage Exploration", "category": "History Walk", "cost": 100, "duration": "2 hrs"},
                    {"name": "Evening Street Food at Besant Road", "category": "Food Walk", "cost": 250, "duration": "2 hrs"}
                ],
                [
                    {"name": "Gateway Hotel M.G. Road (IHCL)", "category": "Luxury 5-Star", "price_per_night": 6800, "rating": 4.7, "area": "MG Road", "amenities": ["Pool", "Gym", "Free WiFi", "Fine Dining"], "suitability": ["Family", "Couples"]},
                    {"name": "Novotel Vijayawada Varun", "category": "5-Star Deluxe", "price_per_night": 7200, "rating": 4.7, "area": "Bharathi Nagar", "amenities": ["Rooftop Infinity Pool", "Spa", "Free WiFi"], "suitability": ["Family", "Solo"]},
                    {"name": "Hotel Manorama", "category": "Mid-range Hotel", "price_per_night": 2400, "rating": 4.2, "area": "Governorpet", "amenities": ["AC", "Restaurant", "Free WiFi"], "suitability": ["Family", "Solo"]},
                    {"name": "Haritha Berm Park Resort", "category": "Riverfront Resort", "price_per_night": 2100, "rating": 4.0, "area": "Krishna Riverfront", "amenities": ["Boating Access", "Restaurant"], "suitability": ["Family", "Friends"]}
                ],
                [
                    {"name": "Sweet Magic Restaurant", "cuisine": "Authentic Andhra & Sweets", "average_cost_for_two": 600, "rating": 4.6, "area": "MG Road", "popular_dishes": "Ulavacharu Biryani, Pootharekulu, Andhra Thali", "is_veg": False},
                    {"name": "Babai Hotel", "cuisine": "Iconic South Indian Breakfast", "average_cost_for_two": 250, "rating": 4.7, "area": "Gandhi Nagar", "popular_dishes": "Ghee Idli with Podi & Nethi Dosa", "is_veg": True},
                    {"name": "Gismat Jail Mandi", "cuisine": "Arabian Mandi & Biryani", "average_cost_for_two": 800, "rating": 4.5, "area": "Ring Road", "popular_dishes": "Mutton Juicy Mandi, Kunafa", "is_veg": False},
                    {"name": "Crossroads Multi-Cuisine", "cuisine": "North & South Indian", "average_cost_for_two": 750, "rating": 4.4, "area": "Siddhartha Nagar", "popular_dishes": "Butter Chicken, Paneer Butter Masala", "is_veg": False}
                ]
            )
        ]
    }
    
    return data

print("Data builder helper defined.")

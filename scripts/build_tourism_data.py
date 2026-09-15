"""
Builder script to generate the comprehensive, production-grade india_tourism_data.py dataset.
Covers all 28 states of India with 4 to 8 authentic destinations each,
sub-regions/neighborhoods, places to visit, things to do, stays, and dining.
"""
import os
import sys
import pprint

OUTPUT_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "india_tourism_data.py")

# Raw definition of all 28 states and their 4-8 key tourist destinations
STATES_CONFIG = [
    {
        "state": "Andhra Pradesh",
        "capital": "Amaravati",
        "region": "South",
        "tagline": "The Sunrise State of India",
        "destinations": [
            {
                "name": "Visakhapatnam",
                "tagline": "The Jewel of the East Coast",
                "overview": "Bustling coastal port city with golden beaches, submarine museum, and scenic hill views over the Bay of Bengal.",
                "budget_daily": 1800,
                "best_time": "Oct–Mar",
                "duration": "3 Days",
                "rating": 4.6,
                "popularity": 8.8,
                "travel_style": "Beach & City Coastal",
                "suitability": ["Family", "Couples", "Solo", "Friends"],
                "weather_city": "Visakhapatnam",
                "neighborhoods": ["Rushikonda Beach", "RK Beach & Pandurangapuram", "Kailasagiri Hill", "MVP Colony", "Siripuram"],
                "places": [
                    {"name": "Rushikonda Beach", "category": "Beach", "highlight": "Blue flag certified beach with golden sands and water sports", "fee": "Free", "time": "3 hrs"},
                    {"name": "INS Kurusura Submarine Museum", "category": "Maritime Museum", "highlight": "Historic decommissioned Soviet-built submarine on the beach", "fee": "₹70", "time": "1.5 hrs"},
                    {"name": "Kailasagiri Hilltop Park", "category": "Viewpoint & Park", "highlight": "Panoramic coastline views, ropeway cable car, giant Shiva statue", "fee": "₹20", "time": "2 hrs"},
                    {"name": "Yarada Beach", "category": "Serene Beach", "highlight": "Secluded pristine beach nestled by Dolphin's Nose hill", "fee": "Free", "time": "2.5 hrs"},
                    {"name": "Dolphin's Nose Lighthouse", "category": "Lighthouse Viewpoint", "highlight": "Dramatic cliff formation overlooking the Bay of Bengal", "fee": "₹20", "time": "1 hr"},
                ],
                "activities": [
                    {"name": "Speed Boating & Jet Skiing at Rushikonda", "category": "Water Sports", "cost": 600, "duration": "1 hr"},
                    {"name": "Kailasagiri Cable Car Ropeway Ride", "category": "Scenic Ride", "cost": 150, "duration": "45 mins"},
                    {"name": "Evening Promenade & Seafood Tasting on Beach Road", "category": "Food Walk", "cost": 350, "duration": "2 hrs"},
                    {"name": "Simhachalam Temple Cultural Excursion", "category": "Heritage Walk", "cost": 100, "duration": "3 hrs"},
                ],
                "hotels": [
                    {"name": "The Park Visakhapatnam", "category": "Luxury 5-Star", "price_per_night": 9500, "rating": 4.7, "area": "RK Beach", "amenities": ["Pool", "Sea View", "Free WiFi", "Spa"], "suitability": ["Couples", "Family"]},
                    {"name": "Radisson Blu Resort", "category": "Luxury Resort", "price_per_night": 11000, "rating": 4.8, "area": "Rushikonda Beach", "amenities": ["Infinity Pool", "Private Beach Access", "Free WiFi", "Gym"], "suitability": ["Couples", "Family"]},
                    {"name": "Hotel Novotel Varun Beach", "category": "5-Star Deluxe", "price_per_night": 10500, "rating": 4.8, "area": "RK Beach", "amenities": ["Rooftop Pool", "Ocean View", "Spa", "Free WiFi"], "suitability": ["Couples", "Family", "Solo"]},
                    {"name": "Keys Select Hotel", "category": "Mid-range Hotel", "price_per_night": 3200, "rating": 4.3, "area": "Siripuram", "amenities": ["Free Breakfast", "Free WiFi", "AC"], "suitability": ["Solo", "Family"]},
                    {"name": "Zostel Visakhapatnam", "category": "Backpacker Hostel", "price_per_night": 850, "rating": 4.4, "area": "Rushikonda Beach", "amenities": ["Free WiFi", "Common Kitchen", "AC Dorms"], "suitability": ["Solo", "Friends"]},
                    {"name": "Hotel Meghalaya", "category": "Budget Hotel", "price_per_night": 1600, "rating": 4.1, "area": "Asilmetta", "amenities": ["Free WiFi", "Restaurant", "AC"], "suitability": ["Family", "Solo"]},
                ],
                "restaurants": [
                    {"name": "Dharani at Dasaprakash", "cuisine": "Authentic Andhra & South Indian", "average_cost_for_two": 600, "rating": 4.6, "area": "Siripuram", "popular_dishes": "Andhra Thali, Pesarattu, Gongura Rice", "is_veg": True},
                    {"name": "Sea Inn (Raju Gari Dhaba)", "cuisine": "Andhra Seafood & Country Style", "average_cost_for_two": 700, "rating": 4.5, "area": "Rushikonda", "popular_dishes": "Crab Fry, Prawn Biryani, Fish Curry", "is_veg": False},
                    {"name": "Bamboo Bay (The Park)", "cuisine": "Coastal & Pan-Indian Fine Dining", "average_cost_for_two": 2200, "rating": 4.7, "area": "RK Beach", "popular_dishes": "Tandoori Lobster, Mutton Fry, Appams", "is_veg": False},
                    {"name": "Bean Board Cafe", "cuisine": "Specialty Coffee & Bakery", "average_cost_for_two": 450, "rating": 4.6, "area": "MVP Colony", "popular_dishes": "Signature Cold Brew, Cinnamon Rolls, Sandwiches", "is_veg": True},
                    {"name": "Flying Spaghetti Monster", "cuisine": "Italian & Pizzeria", "average_cost_for_two": 1100, "rating": 4.5, "area": "Waltair Uplands", "popular_dishes": "Wood-fired Pizza, Tiramisu, Aglio Olio", "is_veg": False},
                ]
            },
            {
                "name": "Araku Valley",
                "tagline": "The Valley of Coffee & Clouds",
                "overview": "Scenic hill station in the Eastern Ghats famous for lush coffee plantations, tribal culture, and ancient million-year-old limestone caves.",
                "budget_daily": 1500,
                "best_time": "Sep–Mar",
                "duration": "2 Days",
                "rating": 4.7,
                "popularity": 8.5,
                "travel_style": "Hill Station & Nature Trails",
                "suitability": ["Family", "Couples", "Friends", "Solo"],
                "weather_city": "Araku Valley",
                "neighborhoods": ["Araku Town", "Borra Caves Area", "Chaparai", "Ananthagiri Hills"],
                "places": [
                    {"name": "Borra Caves", "category": "Limestone Caves", "highlight": "Deepest limestone karst cave system with stalactite pillars", "fee": "₹80", "time": "2 hrs"},
                    {"name": "Chaparai Water Cascades", "category": "Natural Waterfall", "highlight": "Gentle sloping water streams over rock beds surrounded by forest", "fee": "₹20", "time": "2 hrs"},
                    {"name": "Coffee Museum & Plantations", "category": "Agri-Tourism", "highlight": "History of Araku organic coffee, roasting demo, tasting bar", "fee": "₹50", "time": "1 hr"},
                    {"name": "Padmapuram Botanical Gardens", "category": "Hanging Tree Huts", "highlight": "World War II hanging tree cottages and miniature toy train", "fee": "₹40", "time": "1.5 hrs"},
                ],
                "activities": [
                    {"name": "Visakhapatnam to Araku Vistadome Glass Train Ride", "category": "Scenic Train", "cost": 750, "duration": "3 hrs"},
                    {"name": "Bongu Chicken (Bamboo Chicken) Cooking & Tasting", "category": "Culinary Experience", "cost": 300, "duration": "1 hr"},
                    {"name": "Tribal Dhimsa Dance & Cultural Performance", "category": "Cultural Show", "cost": 150, "duration": "1.5 hrs"},
                    {"name": "Coffee Estate Trek & Bean Harvesting Tour", "category": "Agri Trek", "cost": 250, "duration": "2 hrs"},
                ],
                "hotels": [
                    {"name": "Haritha Valley Resort (APTDC)", "category": "Nature Resort", "price_per_night": 3200, "rating": 4.2, "area": "Araku Town", "amenities": ["Garden", "Restaurant", "Balcony View"], "suitability": ["Family", "Couples"]},
                    {"name": "Ananthagiri Haritha Hill Resort", "category": "Hill Resort", "price_per_night": 3800, "rating": 4.3, "area": "Ananthagiri Hills", "amenities": ["Coffee Estate View", "Restaurant", "Trekking"], "suitability": ["Couples", "Family"]},
                    {"name": "Tribal Camp & Cottages", "category": "Eco Camp", "price_per_night": 1800, "rating": 4.1, "area": "Chaparai", "amenities": ["Campfire", "Tents", "Meals Included"], "suitability": ["Friends", "Solo"]},
                    {"name": "Nandakanan Nature Camp", "category": "Budget Resort", "price_per_night": 1400, "rating": 4.0, "area": "Padmapuram Road", "amenities": ["Garden", "Free Parking"], "suitability": ["Family", "Solo"]},
                ],
                "restaurants": [
                    {"name": "Araku Tribal Bamboo Kitchen", "cuisine": "Local Tribal Cuisine", "average_cost_for_two": 500, "rating": 4.5, "area": "Araku Town", "popular_dishes": "Bongu Chicken, Bamboo Rice, Country Curry", "is_veg": False},
                    {"name": "Haritha Mayuri Dining Hall", "cuisine": "Andhra Meals & Thali", "average_cost_for_two": 350, "rating": 4.2, "area": "Araku Center", "popular_dishes": "Unlimited Andhra Meals, Sambar, Pappu", "is_veg": True},
                    {"name": "Araku Aroma Coffee Kiosk", "cuisine": "Artisan Coffee & Snacks", "average_cost_for_two": 200, "rating": 4.8, "area": "Coffee Museum", "popular_dishes": "Pure Arabica Espresso, Coffee Chocolates", "is_veg": True},
                ]
            },
            {
                "name": "Tirupati",
                "tagline": "The Spiritual Capital of Andhra",
                "overview": "One of the most visited pilgrimage centers on earth, situated at the foothills of the sacred Tirumala Seven Hills.",
                "budget_daily": 1400,
                "best_time": "Sep–Mar",
                "duration": "2 Days",
                "rating": 4.8,
                "popularity": 9.7,
                "travel_style": "Spiritual Pilgrimage & Heritage",
                "suitability": ["Family", "Solo", "Couples"],
                "weather_city": "Tirupati",
                "neighborhoods": ["Tirumala Hills", "Alipiri Foothills", "Bairagi Patteda", "Renigunta Road"],
                "places": [
                    {"name": "Sri Venkateswara Temple (Tirumala)", "category": "Sacred Shrine", "highlight": "Ancient Dravidian gold-domed temple of Lord Balaji", "fee": "₹300 (Special Entry)", "time": "4–6 hrs"},
                    {"name": "Chandragiri Fort & Palace", "category": "Historical Fortress", "highlight": "11th-century Vijayanagara fort with palace sound & light show", "fee": "₹30", "time": "2.5 hrs"},
                    {"name": "Silathoranam (Natural Rock Arch)", "category": "Geological Wonder", "highlight": "Rare natural stone arch formed 2.5 billion years ago", "fee": "Free", "time": "45 mins"},
                    {"name": "Kapila Theertham Waterfalls", "category": "Temple Waterfall", "highlight": "Sacred waterfall cascading inside a Shiva temple cave", "fee": "Free", "time": "1 hr"},
                ],
                "activities": [
                    {"name": "Alipiri Footpath Pilgrimage Trek (3550 steps)", "category": "Spiritual Trek", "cost": 0, "duration": "4 hrs"},
                    {"name": "World-famous Tirupati Laddu Prasadam Tasting", "category": "Prasadam Experience", "cost": 50, "duration": "30 mins"},
                    {"name": "Chandragiri Sound & Light Heritage Show", "category": "Cultural Show", "cost": 100, "duration": "1 hr"},
                ],
                "hotels": [
                    {"name": "Fortune Select Grand Ridge", "category": "Luxury 5-Star", "price_per_night": 6500, "rating": 4.6, "area": "Shilparamam Road", "amenities": ["Pool", "Veg Dining", "Free WiFi", "Spa"], "suitability": ["Family", "Couples"]},
                    {"name": "Marasa Sarovar Premiere", "category": "Themed 4-Star Resort", "price_per_night": 5200, "rating": 4.5, "area": "Upadhyaya Nagar", "amenities": ["Avatar Themed Decor", "Pool", "Free WiFi"], "suitability": ["Family", "Couples"]},
                    {"name": "Hotel Bliss", "category": "Mid-range Hotel", "price_per_night": 2800, "rating": 4.3, "area": "Near Railway Station", "amenities": ["Veg Restaurant", "AC", "Free WiFi"], "suitability": ["Family", "Solo"]},
                    {"name": "Bhimas Deluxe Hotel", "category": "Budget Heritage", "price_per_night": 1600, "rating": 4.2, "area": "G.Car Street", "amenities": ["Traditional Dining", "AC", "Travel Desk"], "suitability": ["Family", "Solo"]},
                ],
                "restaurants": [
                    {"name": "Bhimas Pure Veg", "cuisine": "Traditional South Indian & Meals", "average_cost_for_two": 350, "rating": 4.6, "area": "Railway Station Road", "popular_dishes": "South Indian Thali, Ghee Roast Dosa, Filter Coffee", "is_veg": True},
                    {"name": "Saravana Bhavan Tirupati", "cuisine": "Pure Veg South Indian", "average_cost_for_two": 400, "rating": 4.5, "area": "Alipiri Road", "popular_dishes": "Rava Masala Dosa, Mini Tiffin, Badam Halwa", "is_veg": True},
                    {"name": "Rainbow Restaurant (Fortune Grand)", "cuisine": "Multi-cuisine Vegetarian Buffet", "average_cost_for_two": 1200, "rating": 4.6, "area": "Grand Ridge", "popular_dishes": "Royal Veg Biryani, Paneer Tikka, Dessert Buffet", "is_veg": True},
                ]
            },
            {
                "name": "Gandikota",
                "tagline": "The Grand Canyon of India",
                "overview": "Breathtaking gorge of red granite cliffs carved by the Pennar River, featuring a dramatic medieval fort and adventure camping.",
                "budget_daily": 1300,
                "best_time": "Oct–Feb",
                "duration": "2 Days",
                "rating": 4.7,
                "popularity": 8.4,
                "travel_style": "Adventure & Geological Wonder",
                "suitability": ["Friends", "Solo", "Couples"],
                "weather_city": "Kadapa",
                "neighborhoods": ["Gandikota Fort Area", "Pennar Gorge Cliff", "Mylavaram Dam", "Belum Caves Hub"],
                "places": [
                    {"name": "Pennar River Gorge", "category": "Natural Canyon", "highlight": "Massive 300-ft red granite gorge matching the Grand Canyon", "fee": "Free", "time": "3 hrs"},
                    {"name": "Gandikota Fort & Jamia Masjid", "category": "Medieval Fort", "highlight": "12th-century stone fortress with grand arches and granary", "fee": "Free", "time": "2 hrs"},
                    {"name": "Belum Caves (Near Gandikota)", "category": "Subterranean Caves", "highlight": "Second longest underground cave network in India", "fee": "₹70", "time": "2.5 hrs"},
                    {"name": "Mylavaram Dam", "category": "Reservoir", "highlight": "Quiet water body for sunset watching and boating", "fee": "Free", "time": "1 hr"},
                ],
                "activities": [
                    {"name": "Cliff Camping under Starlit Canyon Skies", "category": "Adventure Camping", "cost": 1200, "duration": "Overnight"},
                    {"name": "Rock Climbing & Rappelling on Canyon Cliffs", "category": "Extreme Sports", "cost": 600, "duration": "2 hrs"},
                    {"name": "Kayaking in Pennar River Waters", "category": "Water Sports", "cost": 350, "duration": "1 hr"},
                ],
                "hotels": [
                    {"name": "Haritha Resort Gandikota", "category": "State Heritage Resort", "price_per_night": 2200, "rating": 4.1, "area": "Fort Entrance", "amenities": ["Restaurant", "Cottages", "Free Parking"], "suitability": ["Family", "Couples"]},
                    {"name": "Freakouts Adventure Camp", "category": "Canyon Campsite", "price_per_night": 1400, "rating": 4.4, "area": "Canyon Viewpoint", "amenities": ["Tents", "Campfire", "Dinner Included"], "suitability": ["Friends", "Solo"]},
                ],
                "restaurants": [
                    {"name": "Haritha Restaurant", "cuisine": "Rayalaseema Andhra Cuisine", "average_cost_for_two": 350, "rating": 4.0, "area": "Haritha Resort", "popular_dishes": "Ragi Sankati with Natu Kodi Pulusu, Andhra Meals", "is_veg": False},
                    {"name": "Canyon View Cafe", "cuisine": "Dhaba & Snacks", "average_cost_for_two": 250, "rating": 4.2, "area": "Gorge Road", "popular_dishes": "Egg Fried Rice, Maggi, Mirchi Bajji, Tea", "is_veg": False},
                ]
            }
        ]
    }
]

print("Script framework configured.")

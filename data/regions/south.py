"""
South India Tourism Dataset: Andhra Pradesh, Karnataka, Kerala, Tamil Nadu, Telangana.
Each state features 5-8 rich destinations with neighborhoods, places, activities, hotels, and dining.
"""
from data.regions.common import make_destination

SOUTH_STATES = {}

# ── 1. Andhra Pradesh ─────────────────────────────────────────────────────────
SOUTH_STATES["Andhra Pradesh"] = {
    "capital": "Amaravati", "region": "South", "tagline": "The Sunrise State of India",
    "destinations": [
        make_destination(
            "Visakhapatnam", "The Jewel of the East Coast",
            "Bustling coastal port city with golden beaches, submarine museum, and scenic hill views over the Bay of Bengal.",
            1800, "Oct–Mar", "3 Days", 4.7, 8.9, "Beach & Coastal City", ["Family", "Couples", "Solo", "Friends"], "Visakhapatnam",
            ["Rushikonda Beach", "RK Beach & Pandurangapuram", "Kailasagiri Hill", "MVP Colony", "Siripuram"],
            [
                {"name": "Rushikonda Beach", "category": "Beach", "highlight": "Blue flag certified golden sands & water sports", "fee": "Free", "time": "3 hrs"},
                {"name": "INS Kurusura Submarine Museum", "category": "Museum", "highlight": "Decommissioned Soviet submarine on beach", "fee": "₹70", "time": "1.5 hrs"},
                {"name": "Kailasagiri Hilltop Park", "category": "Viewpoint", "highlight": "Coastline panorama and ropeway cable car", "fee": "₹20", "time": "2 hrs"},
                {"name": "Yarada Beach", "category": "Beach", "highlight": "Secluded beach flanked by Dolphin's Nose hill", "fee": "Free", "time": "2.5 hrs"}
            ],
            [
                {"name": "Jet Skiing & Speed Boating at Rushikonda", "category": "Water Sports", "cost": 600, "duration": "1 hr"},
                {"name": "Kailasagiri Ropeway Cable Car Ride", "category": "Scenic Ride", "cost": 150, "duration": "45 mins"},
                {"name": "RK Beach Seafood Promenade Walk", "category": "Food Walk", "cost": 350, "duration": "2 hrs"}
            ],
            [
                {"name": "The Park Visakhapatnam", "category": "Luxury 5-Star", "price_per_night": 9500, "rating": 4.7, "area": "RK Beach", "amenities": ["Pool", "Sea View", "Free WiFi", "Spa"], "suitability": ["Couples", "Family"]},
                {"name": "Radisson Blu Resort", "category": "Luxury Resort", "price_per_night": 11000, "rating": 4.8, "area": "Rushikonda Beach", "amenities": ["Infinity Pool", "Private Beach", "Free WiFi"], "suitability": ["Couples", "Family"]},
                {"name": "Hotel Novotel Varun Beach", "category": "5-Star Deluxe", "price_per_night": 10500, "rating": 4.8, "area": "RK Beach", "amenities": ["Rooftop Pool", "Ocean View", "Spa"], "suitability": ["Couples", "Family", "Solo"]},
                {"name": "Keys Select Hotel", "category": "Mid-range Hotel", "price_per_night": 3200, "rating": 4.3, "area": "Siripuram", "amenities": ["Free Breakfast", "Free WiFi", "AC"], "suitability": ["Solo", "Family"]},
                {"name": "Zostel Visakhapatnam", "category": "Backpacker Hostel", "price_per_night": 850, "rating": 4.4, "area": "Rushikonda Beach", "amenities": ["Free WiFi", "AC Dorms", "Cafe"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Dharani at Dasaprakash", "cuisine": "Andhra & South Indian Thali", "average_cost_for_two": 600, "rating": 4.6, "area": "Siripuram", "popular_dishes": "Royal Andhra Meals, Pesarattu", "is_veg": True},
                {"name": "Sea Inn (Raju Gari Dhaba)", "cuisine": "Andhra Seafood", "average_cost_for_two": 750, "rating": 4.5, "area": "Rushikonda", "popular_dishes": "Crab Fry, Prawn Biryani", "is_veg": False},
                {"name": "Bamboo Bay", "cuisine": "Coastal Fine Dining", "average_cost_for_two": 2200, "rating": 4.7, "area": "RK Beach", "popular_dishes": "Tandoori Lobster, Mutton Fry", "is_veg": False},
                {"name": "Bean Board Coffee", "cuisine": "Specialty Coffee & Cafe", "average_cost_for_two": 450, "rating": 4.6, "area": "MVP Colony", "popular_dishes": "Cold Brew, Croissants", "is_veg": True}
            ]
        ),
        make_destination(
            "Araku Valley", "The Valley of Coffee & Clouds",
            "Hill station in Eastern Ghats with organic coffee estates, indigenous tribal villages, and prehistoric caves.",
            1500, "Sep–Mar", "2 Days", 4.7, 8.5, "Hill Station & Nature", ["Family", "Couples", "Friends", "Solo"], "Araku Valley",
            ["Araku Town Center", "Borra Caves Area", "Chaparai Cascades", "Ananthagiri Hills"],
            [
                {"name": "Borra Caves", "category": "Caves", "highlight": "Million-year-old limestone stalactite formations", "fee": "₹80", "time": "2 hrs"},
                {"name": "Chaparai Water Cascades", "category": "Waterfall", "highlight": "Natural stream flowing gently over wide rock slabs", "fee": "₹20", "time": "2 hrs"},
                {"name": "Coffee Museum & Plantation", "category": "Agri-Tourism", "highlight": "Arabica coffee history and bean tasting", "fee": "₹50", "time": "1 hr"}
            ],
            [
                {"name": "Vistadome Glass Train Ride", "category": "Scenic Train", "cost": 750, "duration": "3 hrs"},
                {"name": "Bongu (Bamboo) Chicken Tasting", "category": "Food Experience", "cost": 300, "duration": "1 hr"}
            ],
            [
                {"name": "Haritha Valley Resort", "category": "Nature Resort", "price_per_night": 3200, "rating": 4.2, "area": "Araku Town Center", "amenities": ["Garden", "Restaurant", "Balcony View"], "suitability": ["Family", "Couples"]},
                {"name": "Camp Araku Tribals", "category": "Eco Camp", "price_per_night": 1400, "rating": 4.1, "area": "Chaparai Cascades", "amenities": ["Tents", "Campfire", "Meals"], "suitability": ["Friends", "Solo"]}
            ],
            [
                {"name": "Tribal Bamboo Kitchen", "cuisine": "Tribal Andhra", "average_cost_for_two": 500, "rating": 4.5, "area": "Araku Town Center", "popular_dishes": "Bongu Chicken, Bamboo Rice", "is_veg": False},
                {"name": "Mayuri Multi-cuisine", "cuisine": "Andhra Meals", "average_cost_for_two": 350, "rating": 4.2, "area": "Araku Center", "popular_dishes": "Unlimited Andhra Thali", "is_veg": True}
            ]
        ),
        make_destination(
            "Tirupati", "The Spiritual Capital of Andhra",
            "World famous pilgrimage center at the base of the holy Seven Hills of Tirumala.",
            1400, "Sep–Mar", "2 Days", 4.8, 9.7, "Spiritual & Heritage", ["Family", "Solo", "Couples"], "Tirupati",
            ["Tirumala Sacred Hills", "Alipiri Foothills", "Bairagi Patteda", "Chandragiri Road"],
            [
                {"name": "Sri Venkateswara Swamy Temple", "category": "Temple", "highlight": "Ancient gold-domed sanctum of Lord Balaji", "fee": "₹300", "time": "4 hrs"},
                {"name": "Chandragiri Fort & Raja Mahal", "category": "Fort", "highlight": "11th-century Vijayanagara palace fortress", "fee": "₹30", "time": "2 hrs"}
            ],
            [
                {"name": "Alipiri Footpath Pilgrimage Trek", "category": "Pilgrimage Trek", "cost": 0, "duration": "4 hrs"},
                {"name": "Tirupati Laddu Prasadam Experience", "category": "Food Culture", "cost": 50, "duration": "30 mins"}
            ],
            [
                {"name": "Fortune Select Grand Ridge", "category": "Luxury 5-Star", "price_per_night": 6500, "rating": 4.6, "area": "Shilparamam", "amenities": ["Pool", "Pure Veg", "Free WiFi"], "suitability": ["Family", "Couples"]},
                {"name": "Hotel Bliss", "category": "Mid-range Hotel", "price_per_night": 2800, "rating": 4.3, "area": "Railway Station", "amenities": ["Veg Dining", "AC", "Free WiFi"], "suitability": ["Family", "Solo"]}
            ],
            [
                {"name": "Bhimas Pure Veg", "cuisine": "Traditional South Indian", "average_cost_for_two": 350, "rating": 4.6, "area": "Station Road", "popular_dishes": "Ghee Roast Dosa, Thali", "is_veg": True},
                {"name": "Woodlands Vegetarian Restaurant", "cuisine": "Pure Veg South Indian & Andhra Thali", "average_cost_for_two": 400, "rating": 4.5, "area": "Near Railway Station", "popular_dishes": "Special Andhra Meal, Filter Coffee, Poori Masala", "is_veg": True}
            ]
        ),
        make_destination(
            "Gandikota", "The Grand Canyon of India",
            "Spectacular 300-ft red granite gorge carved by the Pennar River, featuring a medieval fort.",
            1300, "Oct–Feb", "2 Days", 4.7, 8.4, "Adventure & Nature", ["Friends", "Solo", "Couples"], "Kadapa",
            ["Fort Citadel", "Gorge Rim Viewpoint", "Mylavaram Dam Road"],
            [
                {"name": "Pennar River Gorge", "category": "Canyon", "highlight": "Massive canyon matching Arizona's Grand Canyon", "fee": "Free", "time": "3 hrs"},
                {"name": "Gandikota Fort & Jamia Masjid", "category": "Fort", "highlight": "12th-century stone fort and granary", "fee": "Free", "time": "2 hrs"},
                {"name": "Belum Caves", "category": "Caves", "highlight": "Second longest underground cave network in India", "fee": "₹70", "time": "2.5 hrs"}
            ],
            [
                {"name": "Canyon Cliffside Stargazing & Camping", "category": "Camping", "cost": 1200, "duration": "Overnight"},
                {"name": "Kayaking in Pennar River Waters", "category": "Water Sports", "cost": 350, "duration": "1 hr"}
            ],
            [
                {"name": "Haritha Resort Gandikota", "category": "State Resort", "price_per_night": 2200, "rating": 4.1, "area": "Fort Entrance", "amenities": ["Restaurant", "Parking"], "suitability": ["Family", "Couples"]},
                {"name": "Freakouts Canyon Camp", "category": "Adventure Camp", "price_per_night": 1400, "rating": 4.4, "area": "Gorge View", "amenities": ["Tents", "Campfire"], "suitability": ["Friends", "Solo"]}
            ],
            [
                {"name": "Haritha Dining Hall", "cuisine": "Rayalaseema Andhra", "average_cost_for_two": 350, "rating": 4.0, "area": "Haritha Resort", "popular_dishes": "Ragi Sankati, Natu Kodi Pulusu", "is_veg": False},
                {"name": "Freakouts Canyon Camp Kitchen", "cuisine": "Campfire Barbecue & Desi Meals", "average_cost_for_two": 400, "rating": 4.4, "area": "Canyon Rim", "popular_dishes": "Campfire Chicken BBQ, Veg Pulao, Dal", "is_veg": False}
            ]
        ),
        make_destination(
            "Vijayawada", "The Heart of the Krishna River",
            "Vibrant city with hill temples, rock-cut Buddhist caves, and river island recreation.",
            1600, "Oct–Mar", "2 Days", 4.5, 8.3, "Heritage & River", ["Family", "Business", "Solo"], "Vijayawada",
            ["Bhavani Island", "Indrakeeladri Hill", "MG Road", "Undavalli Caves Area"],
            [
                {"name": "Kanaka Durga Temple", "category": "Temple", "highlight": "Hilltop temple on Indrakeeladri overlooking Krishna River", "fee": "₹100", "time": "2 hrs"},
                {"name": "Undavalli Caves", "category": "Caves", "highlight": "7th-century rock-cut monolithic sculpture of Lord Vishnu", "fee": "₹25", "time": "2 hrs"},
                {"name": "Bhavani Island", "category": "River Island", "highlight": "133-acre island with water sports and tree houses", "fee": "₹120", "time": "3 hrs"}
            ],
            [
                {"name": "Krishna River Speedboat Ride", "category": "Water Sports", "cost": 450, "duration": "45 mins"},
                {"name": "Kondapalli Wooden Toys & Craft Trail", "category": "Handicrafts", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "Gateway Hotel M.G. Road", "category": "Luxury 5-Star", "price_per_night": 6800, "rating": 4.7, "area": "MG Road", "amenities": ["Pool", "Gym", "Free WiFi"], "suitability": ["Family", "Couples"]},
                {"name": "Hotel Manorama", "category": "Mid-range Hotel", "price_per_night": 2400, "rating": 4.2, "area": "Governorpet", "amenities": ["AC", "Restaurant", "Free WiFi"], "suitability": ["Family", "Solo"]}
            ],
            [
                {"name": "Sweet Magic Restaurant", "cuisine": "Andhra & Sweets", "average_cost_for_two": 600, "rating": 4.6, "area": "MG Road", "popular_dishes": "Ulavacharu Biryani, Pootharekulu", "is_veg": False},
                {"name": "Babai Hotel", "cuisine": "Iconic Breakfast", "average_cost_for_two": 250, "rating": 4.7, "area": "Gandhi Nagar", "popular_dishes": "Ghee Idli with Podi & Dosa", "is_veg": True}
            ]
        )
    ]
}

# ── 2. Karnataka ─────────────────────────────────────────────────────────────
SOUTH_STATES["Karnataka"] = {
    "capital": "Bengaluru", "region": "South", "tagline": "One State, Many Worlds",
    "destinations": [
        make_destination(
            "Bengaluru", "The Silicon Valley & Garden City",
            "Modern tech hub with sprawling parks, booming microbrewery culture, and regal palaces.",
            2200, "Year-round", "3 Days", 4.7, 9.6, "Metropolitan & Lifestyle", ["Solo", "Friends", "Couples", "Family"], "Bengaluru",
            ["Koramangala & HSR", "Indiranagar & MG Road", "Cubbon Park & UB City", "Whitefield", "Malleshwaram"],
            [
                {"name": "Cubbon Park & Vidhana Soudha", "category": "Park & Architecture", "highlight": "300 acres green lung & monumental neo-Dravidian statehouse", "fee": "Free", "time": "3 hrs"},
                {"name": "Bangalore Palace", "category": "Palace", "highlight": "Tudor-style royal palace modeled on Windsor Castle", "fee": "₹250", "time": "2 hrs"},
                {"name": "Lalbagh Botanical Garden", "category": "Botanical Garden", "highlight": "Historic glass house and centuries-old trees", "fee": "₹30", "time": "2.5 hrs"}
            ],
            [
                {"name": "Microbrewery Trail in Indiranagar & Koramangala", "category": "Nightlife & Beer", "cost": 1200, "duration": "3 hrs"},
                {"name": "Traditional Heritage Breakfast Trail in Malleshwaram", "category": "Food Walk", "cost": 300, "duration": "2 hrs"}
            ],
            [
                {"name": "The Leela Palace Bengaluru", "category": "Luxury 5-Star", "price_per_night": 22000, "rating": 4.9, "area": "Old Airport Road", "amenities": ["Pool", "Spa", "Palace Decor", "Fine Dining"], "suitability": ["Couples", "Family"]},
                {"name": "The Oberoi Bengaluru", "category": "Luxury 5-Star", "price_per_night": 16000, "rating": 4.8, "area": "MG Road", "amenities": ["Garden", "Pool", "Free WiFi"], "suitability": ["Couples", "Solo"]},
                {"name": "Bloomrooms @ Indiranagar", "category": "Boutique Hotel", "price_per_night": 3800, "rating": 4.5, "area": "Indiranagar", "amenities": ["Free WiFi", "Modern Design", "AC"], "suitability": ["Solo", "Couples"]},
                {"name": "Zostel Bangalore", "category": "Backpacker Hostel", "price_per_night": 950, "rating": 4.4, "area": "Indiranagar", "amenities": ["Free WiFi", "Terrace", "Co-working Space"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Vidyarthi Bhavan", "cuisine": "Iconic Karnataka Tiffin", "average_cost_for_two": 250, "rating": 4.7, "area": "Gandhi Bazaar", "popular_dishes": "Crispy Benne Masala Dosa, Filter Coffee", "is_veg": True},
                {"name": "Toit Brewpub", "cuisine": "Craft Beer & Pub Fare", "average_cost_for_two": 1800, "rating": 4.7, "area": "Indiranagar", "popular_dishes": "Tin Man Craft Ale, Wood-fired Pizza", "is_veg": False},
                {"name": "Karavalli (Taj Gateway)", "cuisine": "Coastal South Indian", "average_cost_for_two": 3500, "rating": 4.8, "area": "Residency Road", "popular_dishes": "Mangalorean Crab Roast, Appams", "is_veg": False},
                {"name": "Central Tiffin Room (Shri Sagar CTR)", "cuisine": "Butter Dosa & Tiffin", "average_cost_for_two": 250, "rating": 4.7, "area": "Malleshwaram", "popular_dishes": "Benne Dosa, Poori Saagu, Coffee", "is_veg": True}
            ]
        ),
        make_destination(
            "Coorg (Kodagu)", "Scotland of India",
            "Misty hill country blanketed in coffee estates, spice plantations, and cascading waterfalls.",
            2300, "Oct–May", "3 Days", 4.8, 9.2, "Nature & Coffee Hills", ["Couples", "Family", "Friends"], "Madikeri",
            ["Madikeri Town", "Kushalnagar & Bylakuppe", "Abbey Falls Road", "Virajpet & Estate Country"],
            [
                {"name": "Abbey Falls", "category": "Waterfall", "highlight": "Waterfall roaring amid lush coffee & pepper plantations", "fee": "₹15", "time": "1.5 hrs"},
                {"name": "Namdroling Monastery (Golden Temple)", "category": "Tibetan Monasteries", "highlight": "40-ft gilded Buddha statues in Tibetan settlement", "fee": "Free", "time": "2 hrs"},
                {"name": "Raja's Seat", "category": "Sunset Viewpoint", "highlight": "Historical sunset pavilion overlooking rolling valleys", "fee": "₹20", "time": "1.5 hrs"},
                {"name": "Dubare Elephant Camp", "category": "Wildlife Interaction", "highlight": "Bathing and feeding Asian elephants along Kaveri River", "fee": "₹100", "time": "2 hrs"}
            ],
            [
                {"name": "Coffee Estate Walk & Spice Tasting", "category": "Agri-Tourism", "cost": 350, "duration": "2 hrs"},
                {"name": "River Rafting on Barapole River", "category": "Adventure Sports", "cost": 1200, "duration": "3 hrs"}
            ],
            [
                {"name": "Evolve Back Coorg", "category": "Luxury Plantation Resort", "price_per_night": 28000, "rating": 4.9, "area": "Siddapur", "amenities": ["Private Pool Villa", "Spa", "Plantation Tour"], "suitability": ["Couples", "Family"]},
                {"name": "The Tamara Coorg", "category": "Luxury Eco Resort", "price_per_night": 21000, "rating": 4.8, "area": "Kabbinakad", "amenities": ["Waterfall View", "Spa", "Yoga"], "suitability": ["Couples"]},
                {"name": "Coorg Cliff Resort", "category": "Mid-range Hill Resort", "price_per_night": 5500, "rating": 4.4, "area": "Pollibetta", "amenities": ["Infinity Pool", "Free WiFi", "Trek"], "suitability": ["Family", "Couples"]},
                {"name": "Zostel Coorg", "category": "Backpacker Hostel", "price_per_night": 900, "rating": 4.4, "area": "Madikeri Outskirts", "amenities": ["Free WiFi", "Bonfire", "Cafe"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Coorg Cuisine", "cuisine": "Authentic Kodava Cuisine", "average_cost_for_two": 650, "rating": 4.6, "area": "Madikeri", "popular_dishes": "Pandi Curry (Pork), Kadambuttu, Akki Roti", "is_veg": False},
                {"name": "Raintree Restaurant", "cuisine": "Kodava & Continental", "average_cost_for_two": 850, "rating": 4.5, "area": "Madikeri", "popular_dishes": "Bamboo Shoot Curry, Chicken Pepper Fry", "is_veg": False},
                {"name": "Big Cup Cafe", "cuisine": "Plantation Coffee & Bakes", "average_cost_for_two": 400, "rating": 4.6, "area": "Mysore-Madikeri Road", "popular_dishes": "Estate Espresso, Cheesecakes", "is_veg": True}
            ]
        ),
        make_destination(
            "Hampi", "The Forgotten Empire of Ruins",
            "UNESCO World Heritage boulder kingdom of the 14th-century Vijayanagara Empire.",
            1600, "Oct–Mar", "3 Days", 4.9, 9.4, "Ancient Heritage & Boulders", ["Solo", "Backpackers", "Couples", "Friends"], "Hospet",
            ["Sacred Center & Virupaksha", "Royal Enclosure", "Hippie Island (Virupapur)", "Kamalapur"],
            [
                {"name": "Virupaksha Temple", "category": "Ancient Temple", "highlight": "7th-century functioning temple with colossal Gopuram", "fee": "₹50", "time": "2 hrs"},
                {"name": "Vijaya Vittala Temple & Stone Chariot", "category": "UNESCO Monument", "highlight": "Iconic Stone Chariot and musical granite pillars", "fee": "₹40", "time": "3 hrs"},
                {"name": "Matanga Hill", "category": "Sunrise Viewpoint", "highlight": "Best 360-degree sunrise view over Hampi boulder landscape", "fee": "Free", "time": "2 hrs"},
                {"name": "Lotus Mahal & Elephant Stables", "category": "Royal Architecture", "highlight": "Indo-Islamic domes and royal stable halls", "fee": "₹40 (Combined)", "time": "2 hrs"}
            ],
            [
                {"name": "Bouldering & Rock Climbing Clinic", "category": "Adventure", "cost": 800, "duration": "3 hrs"},
                {"name": "Tungabhadra Coracle Boat Ride", "category": "Boating", "cost": 250, "duration": "45 mins"},
                {"name": "Bicycle Rental Tour across Temple Ruins", "category": "Cycling", "cost": 150, "duration": "Full Day"}
            ],
            [
                {"name": "Evolve Back Kamalapura Palace", "category": "Luxury Palace Resort", "price_per_night": 26000, "rating": 4.9, "area": "Kamalapur", "amenities": ["Palatial Architecture", "Private Pool", "Spa"], "suitability": ["Couples", "Family"]},
                {"name": "Heritage Resort Hampi", "category": "Heritage Resort", "price_per_night": 6500, "rating": 4.5, "area": "Hosapete Road", "amenities": ["Pool", "Organic Farm", "Free WiFi"], "suitability": ["Family", "Couples"]},
                {"name": "Zostel Hampi (Gangavathi)", "category": "Backpacker Hostel", "price_per_night": 800, "rating": 4.4, "area": "Near Sanapur Lake", "amenities": ["Free WiFi", "Common Room", "Lake Access"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Mango Tree Restaurant", "cuisine": "Multi-cuisine & Israeli", "average_cost_for_two": 500, "rating": 4.6, "area": "Hampi Bazaar", "popular_dishes": "Mango Tree Special Thali, Falafel, Fresh Juice", "is_veg": True},
                {"name": "Laughing Buddha Cafe", "cuisine": "Bohemian Cafe & Pizza", "average_cost_for_two": 600, "rating": 4.4, "area": "Hippie Island", "popular_dishes": "Wood-fired Pizza, Shakshuka, Iced Tea", "is_veg": True}
            ]
        ),
        make_destination(
            "Gokarna", "Bohemian Beaches & Sacred Shores",
            "Laid-back coastal temple town famous for crescent beaches, cliff treks, and beach shack vibes.",
            1500, "Oct–Apr", "3 Days", 4.7, 8.8, "Beach & Trekking", ["Solo", "Couples", "Backpackers", "Friends"], "Gokarna",
            ["Om Beach", "Kudle Beach", "Half Moon & Paradise Beaches", "Gokarna Town"],
            [
                {"name": "Om Beach", "category": "Beach", "highlight": "Naturally shaped like the sacred Hindu Om symbol", "fee": "Free", "time": "3 hrs"},
                {"name": "Kudle Beach", "category": "Beach & Sunset", "highlight": "Wide sandy stretch dotted with bohemian shacks and yoga", "fee": "Free", "time": "3 hrs"},
                {"name": "Mahabaleshwar Temple", "category": "Temple", "highlight": "4th-century Shiva temple housing the sacred Atmalinga", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Five Beach Trek (Kudle to Paradise Beach)", "category": "Trekking", "cost": 0, "duration": "4 hrs"},
                {"name": "Bioluminescence Beach Night Walk", "category": "Nature Tour", "cost": 300, "duration": "1.5 hrs"},
                {"name": "Beach Yoga & Meditation Session", "category": "Wellness", "cost": 300, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Kahani Paradise", "category": "Luxury Boutique Villa", "price_per_night": 24000, "rating": 4.9, "area": "Cliffside", "amenities": ["Infinity Pool", "Estate Grounds", "Sea View"], "suitability": ["Couples"]},
                {"name": "Kudle Beach View Resort", "category": "Mid-range Beach Resort", "price_per_night": 4200, "rating": 4.4, "area": "Kudle Beach", "amenities": ["Pool", "Sea View", "Restaurant"], "suitability": ["Couples", "Family"]},
                {"name": "Zostel Gokarna", "category": "Backpacker Hostel", "price_per_night": 850, "rating": 4.5, "area": "Cliff View", "amenities": ["Cliff Ocean View", "Free WiFi", "Cafe"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Namaste Cafe", "cuisine": "Seafood & Continental", "average_cost_for_two": 650, "rating": 4.5, "area": "Om Beach", "popular_dishes": "Fresh Catch Fish Fry, Nutella Banana Pancake", "is_veg": False},
                {"name": "Chez Christophe", "cuisine": "French Bakery & Cafe", "average_cost_for_two": 550, "rating": 4.6, "area": "Middle Beach", "popular_dishes": "Fresh Croissants, Baguettes, Salad", "is_veg": True},
                {"name": "Pai Hotel", "cuisine": "Pure Veg South Indian", "average_cost_for_two": 250, "rating": 4.4, "area": "Temple Town", "popular_dishes": "Mangalore Buns, Filter Coffee, Thali", "is_veg": True}
            ]
        ),
        make_destination(
            "Mysuru", "The Royal Cultural Capital",
            "Heritage royal city celebrated for the illuminated Mysore Palace, silk sarees, and fragrant sandalwood.",
            1700, "Sep–Mar", "2 Days", 4.7, 9.1, "Royal Heritage & Palaces", ["Family", "Couples", "Solo"], "Mysuru",
            ["Mysore Palace Area", "Chamundi Hill", "Devaraja Market", "Brindavan Gardens Area"],
            [
                {"name": "Mysore Palace (Amba Vilas)", "category": "Royal Palace", "highlight": "Indo-Saracenic palace illuminated by 100,000 light bulbs", "fee": "₹100", "time": "3 hrs"},
                {"name": "Chamundeshwari Temple", "category": "Hilltop Temple", "highlight": "Hilltop shrine overlooking the city with Nandi monolith", "fee": "Free", "time": "2 hrs"},
                {"name": "Brindavan Gardens", "category": "Terrace Gardens", "highlight": "Terraced musical fountain gardens beside KRS Dam", "fee": "₹50", "time": "2.5 hrs"}
            ],
            [
                {"name": "Mysore Palace Evening Illumination & Sound Show", "category": "Night Spectacle", "cost": 120, "duration": "1 hr"},
                {"name": "Devaraja Market Heritage Smell & Color Walk", "category": "Market Tour", "cost": 0, "duration": "2 hrs"},
                {"name": "Mysore Pak Sweet Tasting at Original Guru Sweet Mart", "category": "Culinary Heritage", "cost": 100, "duration": "30 mins"}
            ],
            [
                {"name": "Lalitha Mahal Palace Hotel", "category": "Heritage Palace Hotel", "price_per_night": 7500, "rating": 4.5, "area": "Chamundi Foothills", "amenities": ["Heritage Ballroom", "Pool", "Free WiFi"], "suitability": ["Family", "Couples"]},
                {"name": "Radisson Blu Plaza Hotel", "category": "5-Star Deluxe", "price_per_night": 8200, "rating": 4.7, "area": "Near Race Course", "amenities": ["Pool", "Spa", "Free WiFi"], "suitability": ["Family", "Couples"]},
                {"name": "Roamer's Mysuru", "category": "Backpacker Hostel", "price_per_night": 750, "rating": 4.4, "area": "Jayalakshmipuram", "amenities": ["Free WiFi", "Rooftop Terrace"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Guru Sweet Mart", "cuisine": "Iconic Sweets", "average_cost_for_two": 150, "rating": 4.8, "area": "Devaraja Market", "popular_dishes": "Original Melt-in-mouth Mysore Pak", "is_veg": True},
                {"name": "Mylari Hotel (Original)", "cuisine": "Legendary Dosa", "average_cost_for_two": 200, "rating": 4.7, "area": "Nazarbad", "popular_dishes": "Mylari Butter Dosa with White Butter & Sagu", "is_veg": True},
                {"name": "RRR Restaurant", "cuisine": "Andhra & Mysore Meals", "average_cost_for_two": 600, "rating": 4.5, "area": "Gandhi Square", "popular_dishes": "Biryani on Banana Leaf, Chili Chicken", "is_veg": False}
            ]
        )
    ]
}

# ── 3. Kerala ────────────────────────────────────────────────────────────────
SOUTH_STATES["Kerala"] = {
    "capital": "Thiruvananthapuram", "region": "South", "tagline": "God's Own Country",
    "destinations": [
        make_destination(
            "Munnar", "The Rolling Emerald Tea Hills",
            "Misty high-altitude tea hill station with rare wildlife, trekking peaks, and spice-scented air.",
            2000, "Sep–May", "3 Days", 4.8, 9.5, "Hill Station & Tea Trails", ["Family", "Couples", "Solo", "Friends"], "Munnar",
            ["Old Munnar Town", "Mattupetty & Dam", "Eravikulam National Park Area", "Chithirapuram & Pothamedu"],
            [
                {"name": "Eravikulam National Park", "category": "Wildlife & Peaks", "highlight": "Home of endangered Nilgiri Tahr and Anamudi Peak", "fee": "₹200", "time": "3 hrs"},
                {"name": "KDHP Tea Museum & Factory", "category": "Heritage Industry", "highlight": "100-year-old tea manufacturing machinery and tea tasting", "fee": "₹125", "time": "1.5 hrs"},
                {"name": "Mattupetty Dam & Echo Point", "category": "Reservoir & Hills", "highlight": "Scenic lake speed boating surrounded by tea plantations", "fee": "₹30", "time": "2 hrs"}
            ],
            [
                {"name": "Speed Boating on Mattupetty Dam Lake", "category": "Boating", "cost": 500, "duration": "30 mins"},
                {"name": "Tea Plantation Sunrise Trek to Top Station", "category": "Trekking", "cost": 450, "duration": "4 hrs"},
                {"name": "Traditional Ayurvedic Full-Body Massage", "category": "Wellness", "cost": 1500, "duration": "1 hr"}
            ],
            [
                {"name": "Spice Tree Munnar", "category": "Luxury Eco Resort", "price_per_night": 12000, "rating": 4.8, "area": "Chinnakanal", "amenities": ["Heated Pool", "Spa", "Mountain View"], "suitability": ["Couples", "Family"]},
                {"name": "Windermere Estate", "category": "Boutique Plantation Retreat", "price_per_night": 9500, "rating": 4.7, "area": "Pothamedu", "amenities": ["Coffee & Cardamom View", "Dining"], "suitability": ["Couples"]},
                {"name": "Tea Nest Cottage", "category": "Mid-range Hotel", "price_per_night": 4200, "rating": 4.4, "area": "Old Munnar", "amenities": ["Balcony View", "Free WiFi", "Breakfast"], "suitability": ["Family", "Couples"]},
                {"name": "Zostel Munnar", "category": "Backpacker Hostel", "price_per_night": 950, "rating": 4.3, "area": "Tea Valley", "amenities": ["Free WiFi", "Dorms", "Cafe"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Saravana Bhavan Munnar", "cuisine": "Authentic South Indian & Thali", "average_cost_for_two": 350, "rating": 4.5, "area": "Munnar Town", "popular_dishes": "Kerala Sadya, Ghee Roast Dosa", "is_veg": True},
                {"name": "Rapsy Restaurant", "cuisine": "Traditional Kerala", "average_cost_for_two": 450, "rating": 4.4, "area": "Main Bazar", "popular_dishes": "Kerala Parotta with Beef/Chicken Fry, Biryani", "is_veg": False},
                {"name": "Zaza Bistro", "cuisine": "Continental Bakery & Cafe", "average_cost_for_two": 700, "rating": 4.5, "area": "Near Post Office", "popular_dishes": "Wood-fired Pizza, Fresh Carrot Cake", "is_veg": True}
            ]
        ),
        make_destination(
            "Alleppey (Alappuzha)", "The Venice of the East",
            "World-famous backwater network of canals, lagoons, and overnight traditional thatched houseboats.",
            2400, "Sep–Mar", "2 Days", 4.9, 9.6, "Backwaters & Houseboat", ["Couples", "Family", "Friends"], "Alappuzha",
            ["Punnamada Lake", "Vembanad Backwaters", "Alleppey Beach & Pier", "Marari Beach Area"],
            [
                {"name": "Alleppey Backwater Canals", "category": "Backwaters", "highlight": "Emerald palm-shaded canals and paddy fields below sea level", "fee": "Free", "time": "Full Day"},
                {"name": "Alleppey Beach & Old Sea Bridge Pier", "category": "Beach & Pier", "highlight": "150-year-old colonial wooden pier extending into the sea", "fee": "Free", "time": "2 hrs"},
                {"name": "Marari Beach", "category": "Secluded Beach", "highlight": "Tranquil fishing village beach with coconut palms", "fee": "Free", "time": "3 hrs"}
            ],
            [
                {"name": "Traditional Kettuvallam Overnight Houseboat Cruise", "category": "Houseboat", "cost": 7500, "duration": "24 hrs"},
                {"name": "Shikara Boat Country Canoe Village Cruise", "category": "Canoe Cruise", "cost": 600, "duration": "3 hrs"},
                {"name": "Nehru Trophy Snake Boat Race Viewing", "category": "Cultural Event", "cost": 250, "duration": "4 hrs"}
            ],
            [
                {"name": "Kumarakom Lake Resort", "category": "Luxury Heritage Resort", "price_per_night": 24000, "rating": 4.9, "area": "Lakefront", "amenities": ["Heritage Pool Villas", "Ayurvedic Spa", "Houseboats"], "suitability": ["Couples", "Family"]},
                {"name": "Marari Beach Resort (CGH Earth)", "category": "Eco-Luxury Beach Resort", "price_per_night": 18000, "rating": 4.8, "area": "Marari Beach", "amenities": ["Beach Cottages", "Pool", "Organic Farm"], "suitability": ["Couples", "Family"]},
                {"name": "Zostel Alleppey", "category": "Backpacker Hostel", "price_per_night": 850, "rating": 4.4, "area": "Beach Road", "amenities": ["Beachfront", "Free WiFi", "Common Lounge"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Thaff Restaurant", "cuisine": "Kerala Seafood & Biryani", "average_cost_for_two": 600, "rating": 4.5, "area": "General Hospital Junction", "popular_dishes": "Karimeen Pollichathu, Appam, Mutton Biryani", "is_veg": False},
                {"name": "Halais Restaurant", "cuisine": "Malabar & Arabian", "average_cost_for_two": 650, "rating": 4.4, "area": "Boat Jetty Road", "popular_dishes": "Malabar Parotta, Dragon Chicken, Seafood Platter", "is_veg": False}
            ]
        ),
        make_destination(
            "Kochi & Fort Kochi", "The Queen of the Arabian Sea",
            "Historic spice port blending Portuguese, Dutch, British colonial lanes with Chinese fishing nets.",
            2100, "Sep–Apr", "3 Days", 4.8, 9.4, "Heritage & Coastal Arts", ["Solo", "Couples", "Family", "Friends"], "Kochi",
            ["Fort Kochi Beachfront", "Mattancherry & Jew Town", "Marine Drive & Ernakulam", "Willingdon Island"],
            [
                {"name": "Chinese Fishing Nets (Cheena Vala)", "category": "Maritime Landmark", "highlight": "Cantilevered ancient fishing mechanisms against sunset", "fee": "Free", "time": "1.5 hrs"},
                {"name": "Mattancherry Palace (Dutch Palace)", "category": "Heritage Palace", "highlight": "16th-century murals illustrating Hindu epics", "fee": "₹10", "time": "1.5 hrs"},
                {"name": "Paradesi Jewish Synagogue", "category": "Historic Synagogue", "highlight": "Built in 1568 with hand-painted Chinese willow tiles", "fee": "₹10", "time": "1 hr"},
                {"name": "Jew Town Antique Street", "category": "Bazaar", "highlight": "Aromatic spice warehouses and colonial antique showrooms", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Kathakali Classical Dance & Makeup Show", "category": "Cultural Theater", "cost": 400, "duration": "2 hrs"},
                {"name": "Kochi-Muziris Biennale Contemporary Art Trail", "category": "Art Walk", "cost": 150, "duration": "3 hrs"},
                {"name": "Kochi Harbour Sunset Ferry Cruise", "category": "Ferry", "cost": 15, "duration": "45 mins"}
            ],
            [
                {"name": "Brunton Boatyard (CGH Earth)", "category": "Luxury Heritage 5-Star", "price_per_night": 16000, "rating": 4.8, "area": "Fort Kochi", "amenities": ["Harbour View", "Pool", "Ayurveda Spa"], "suitability": ["Couples", "Family"]},
                {"name": "Old Harbour Hotel", "category": "Boutique Heritage Hotel", "price_per_night": 12000, "rating": 4.7, "area": "Fort Kochi", "amenities": ["Heritage Garden", "Pool", "Gourmet Dining"], "suitability": ["Couples"]},
                {"name": "Zostel Kochi", "category": "Backpacker Hostel", "price_per_night": 850, "rating": 4.4, "area": "Fort Kochi", "amenities": ["Free WiFi", "Art Murals", "AC Dorms"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Kashi Art Cafe", "cuisine": "Contemporary Arts Cafe", "average_cost_for_two": 650, "rating": 4.7, "area": "Burgher Street", "popular_dishes": "Fresh Chocolate Cake, Roast Beef Sandwich, Iced Coffee", "is_veg": True},
                {"name": "Grand Pavilion (Grand Hotel)", "cuisine": "Authentic Kerala Seafood", "average_cost_for_two": 1100, "rating": 4.6, "area": "MG Road Ernakulam", "popular_dishes": "Fish Moly, Prawn Curry, Kerala Sadya", "is_veg": False},
                {"name": "Paragon Restaurant Kochi", "cuisine": "Malabar Cuisine & Biryani", "average_cost_for_two": 700, "rating": 4.6, "area": "Lulu Mall", "popular_dishes": "Malabar Dum Biryani, Fish Mango Curry", "is_veg": False}
            ]
        ),
        make_destination(
            "Wayanad", "The Rainforest & Cave Country",
            "Misty mountain plateau known for heart-shaped lakes, prehistoric rock art caves, and waterfalls.",
            1900, "Oct–May", "3 Days", 4.7, 8.9, "Rainforest & Trekking", ["Friends", "Couples", "Family", "Solo"], "Kalpetta",
            ["Kalpetta Town", "Sulthan Bathery", "Vythiri Rainforest", "Mananthavady"],
            [
                {"name": "Edakkal Caves", "category": "Neolithic Caves", "highlight": "Prehistoric rock engravings dating back to 6000 BC", "fee": "₹50", "time": "2.5 hrs"},
                {"name": "Chembra Peak & Heart Lake", "category": "Peak Trek", "highlight": "Trek up to a natural heart-shaped lake (Hridaya Saras)", "fee": "₹750 (Guide Permit)", "time": "4 hrs"},
                {"name": "Banasura Sagar Dam", "category": "Earth Dam", "highlight": "Largest earthen dam in India with island speed boating", "fee": "₹40", "time": "2 hrs"}
            ],
            [
                {"name": "Bamboo Rafting & Treehouse Stay in Vythiri", "category": "Eco Adventure", "cost": 800, "duration": "3 hrs"},
                {"name": "Wayanad Wildlife Sanctuary Jeep Safari", "category": "Safari", "cost": 650, "duration": "2.5 hrs"}
            ],
            [
                {"name": "Vythiri Resort", "category": "Rainforest Resort & Treehouses", "price_per_night": 14000, "rating": 4.7, "area": "Vythiri", "amenities": ["Treehouse", "Natural Stream", "Spa"], "suitability": ["Couples", "Family"]},
                {"name": "Zostel Wayanad", "category": "Backpacker Hostel", "price_per_night": 800, "rating": 4.3, "area": "Meppadi", "amenities": ["Tea Estate View", "Free WiFi", "Campfire"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "1980's A Nostalgic Restaurant", "cuisine": "Traditional Kerala", "average_cost_for_two": 500, "rating": 4.6, "area": "Kalpetta", "popular_dishes": "Kerala Meals, Nadan Chicken Curry, Puttu", "is_veg": False},
                {"name": "Wilton Restaurant", "cuisine": "Multi-cuisine & Arabian", "average_cost_for_two": 600, "rating": 4.4, "area": "Sulthan Bathery", "popular_dishes": "Al Faham Chicken, Kuboos, Mandi", "is_veg": False}
            ]
        ),
        make_destination(
            "Varkala", "The Cliff Beach & Tibetan Shacks",
            "Red laterite cliffs abutting the Arabian Sea, bohemian clifftop cafes, and holy Papanasam springs.",
            1700, "Oct–Apr", "3 Days", 4.8, 9.1, "Cliffs & Bohemian Beach", ["Solo", "Couples", "Friends"], "Varkala",
            ["North Cliff Promenade", "South Cliff", "Papanasam Beach", "Kappil Beach & Lake"],
            [
                {"name": "Varkala North Cliff", "category": "Coastal Cliff", "highlight": "Promenade of open-air cafes overlooking Arabian Sea sunset", "fee": "Free", "time": "3 hrs"},
                {"name": "Papanasam Beach", "category": "Holy Beach", "highlight": "Natural mineral spring waters believed to wash away sins", "fee": "Free", "time": "2 hrs"},
                {"name": "Janardhanaswamy Temple", "category": "Ancient Temple", "highlight": "2000-year-old Vaishnavite temple with Dutch bell", "fee": "Free", "time": "1 hr"}
            ],
            [
                {"name": "Surfing Lessons at Varkala Beach", "category": "Surfing", "cost": 1200, "duration": "2 hrs"},
                {"name": "Sunset Dining & Live Music on the North Cliff", "category": "Nightlife", "cost": 700, "duration": "3 hrs"}
            ],
            [
                {"name": "Gateway Hotel Varkala (IHCL)", "category": "Luxury 5-Star", "price_per_night": 8500, "rating": 4.6, "area": "Near Cliff", "amenities": ["Cliff View", "Pool", "Spa", "Gym"], "suitability": ["Couples", "Family"]},
                {"name": "Zostel Varkala", "category": "Backpacker Hostel", "price_per_night": 900, "rating": 4.5, "area": "North Cliff", "amenities": ["Free WiFi", "Sea Breeze Terrace", "Cafe"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Coffee Temple", "cuisine": "Artisan Coffee & Breakfast", "average_cost_for_two": 500, "rating": 4.6, "area": "North Cliff", "popular_dishes": "Espresso, Shakshuka, Banana Pancakes", "is_veg": True},
                {"name": "Darjeeling Cafe", "cuisine": "Tibetan & Continental", "average_cost_for_two": 600, "rating": 4.5, "area": "North Cliff", "popular_dishes": "Steamed Momos, Thukpa, Fresh Tuna Steak", "is_veg": False}
            ]
        )
    ]
}

# ── 4. Tamil Nadu ────────────────────────────────────────────────────────────
SOUTH_STATES["Tamil Nadu"] = {
    "capital": "Chennai", "region": "South", "tagline": "Enchanting Tamil Nadu",
    "destinations": [
        make_destination(
            "Ooty", "The Queen of Hill Stations",
            "Iconic Nilgiri Mountain hill resort with toy train heritage, botanical gardens, and pine forests.",
            2000, "Oct–Jun", "3 Days", 4.7, 9.3, "Colonial Hills & Gardens", ["Family", "Couples", "Solo"], "Udhagamandalam",
            ["Ooty Town Center", "Doddabetta Peak Area", "Coonoor Road", "Pykara & Lake Area"],
            [
                {"name": "Nilgiri Mountain Railway Toy Train", "category": "UNESCO Heritage Train", "highlight": "Steam locomotive ride climbing through Nilgiri gorges", "fee": "₹205", "time": "3 hrs"},
                {"name": "Government Botanical Garden", "category": "Gardens", "highlight": "55-acre terraced garden with 20-million-year-old fossil tree", "fee": "₹40", "time": "2 hrs"},
                {"name": "Doddabetta Peak", "category": "Mountain Viewpoint", "highlight": "Highest peak in Nilgiris (8,650 ft) with telescope house", "fee": "₹10", "time": "2 hrs"}
            ],
            [
                {"name": "Boating in Ooty Lake", "category": "Boating", "cost": 250, "duration": "1 hr"},
                {"name": "Handmade Nilgiri Chocolate Tasting Walk", "category": "Food Walk", "cost": 150, "duration": "1 hr"}
            ],
            [
                {"name": "Savoy - IHCL SeleQtions", "category": "Colonial 5-Star Heritage", "price_per_night": 14000, "rating": 4.8, "area": "Sylks Road", "amenities": ["Fireplace", "Heritage Lawn", "Fine Dining"], "suitability": ["Couples", "Family"]},
                {"name": "Zostel Ooty", "category": "Backpacker Hostel", "price_per_night": 850, "rating": 4.4, "area": "Fern Hill", "amenities": ["Free WiFi", "Campfire", "Valley View"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Earl's Secret (Kings Cliff)", "cuisine": "Anglo-Indian Fine Dining", "average_cost_for_two": 1400, "rating": 4.6, "area": "Havelock Road", "popular_dishes": "Roast Chicken, Shepherd's Pie, Sizzler", "is_veg": False},
                {"name": "Shinkows Chinese Restaurant", "cuisine": "Authentic Chinese", "average_cost_for_two": 600, "rating": 4.5, "area": "Commissioner's Road", "popular_dishes": "Cantonese Noodles, Chilli Pork", "is_veg": False}
            ]
        ),
        make_destination(
            "Chennai", "The Cultural Gateway of the South",
            "Metropolis blending ancient Carnatic classical music, Marina beach, British forts, and filter coffee.",
            1900, "Nov–Mar", "3 Days", 4.6, 9.1, "Coastal City & Carnatic Culture", ["Family", "Business", "Solo"], "Chennai",
            ["Mylapore Cultural Hub", "Marina Beach & San Thome", "Besant Nagar (Bessie)", "T. Nagar Shopping"],
            [
                {"name": "Kapaleeshwarar Temple", "category": "Temple", "highlight": "7th-century Dravidian temple with towering rainbow gopuram", "fee": "Free", "time": "2 hrs"},
                {"name": "Marina Beach", "category": "Urban Beach", "highlight": "Second longest natural urban beach in the world", "fee": "Free", "time": "2 hrs"},
                {"name": "Fort St. George & Museum", "category": "Colonial Fortress", "highlight": "First British fortress in India built in 1644", "fee": "₹25", "time": "2 hrs"}
            ],
            [
                {"name": "Mylapore Heritage & Food Walk", "category": "Culture & Food", "cost": 300, "duration": "2.5 hrs"},
                {"name": "Carnatic Music Sabha Concert (Dec Season)", "category": "Classical Music", "cost": 200, "duration": "3 hrs"}
            ],
            [
                {"name": "ITC Grand Chola", "category": "Luxury 5-Star Palace", "price_per_night": 15000, "rating": 4.9, "area": "Guindy", "amenities": ["Chola Architecture", "10 Dining Venues", "Spa"], "suitability": ["Family", "Couples"]},
                {"name": "Taj Coromandel", "category": "5-Star Deluxe", "price_per_night": 12000, "rating": 4.8, "area": "Nungambakkam", "amenities": ["Southern Spice", "Pool", "Spa"], "suitability": ["Family", "Business"]},
                {"name": "Zostel Chennai", "category": "Backpacker Hostel", "price_per_night": 800, "rating": 4.3, "area": "Teynampet", "amenities": ["Free WiFi", "AC", "Common Room"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Murugan Idli Shop", "cuisine": "Iconic South Indian", "average_cost_for_two": 300, "rating": 4.6, "area": "T. Nagar / Besant Nagar", "popular_dishes": "Soft Ghee Podi Idli, 4 Chutneys, Jigarthanda", "is_veg": True},
                {"name": "Southern Spice (Taj Coromandel)", "cuisine": "Royal South Indian Fine Dining", "average_cost_for_two": 4000, "rating": 4.9, "area": "Nungambakkam", "popular_dishes": "Kozhi Varuval, Appam with Stew", "is_veg": False},
                {"name": "Rayar's Mess", "cuisine": "Historic Mylapore Mess", "average_cost_for_two": 200, "rating": 4.8, "area": "Mylapore", "popular_dishes": "Hot Crispy Medu Vada, Pongal, Filter Coffee", "is_veg": True}
            ]
        ),
        make_destination(
            "Madurai", "The Ancient Lotus City",
            "One of the oldest continuously inhabited cities in the world, centered on the grand Meenakshi Temple.",
            1500, "Oct–Mar", "2 Days", 4.8, 9.4, "Ancient Temple Heritage", ["Family", "Solo", "Couples"], "Madurai",
            ["Meenakshi Amman Temple Area", "Thirumalai Nayakkar Mahal", "Town Hall Road", "Anna Nagar"],
            [
                {"name": "Meenakshi Amman Temple", "category": "Dravidian Temple", "highlight": "Colossal 14 sculpted gopurams with 33,000 stone sculptures", "fee": "Free", "time": "3.5 hrs"},
                {"name": "Thirumalai Nayakkar Mahal", "category": "Palace", "highlight": "17th-century palace featuring 82-ft colossal stone pillars", "fee": "₹10", "time": "2 hrs"}
            ],
            [
                {"name": "Temple Night Ceremony (Palli Arai)", "category": "Ritual", "cost": 0, "duration": "1 hr"},
                {"name": "Jigarthanda & Madurai Street Food Tour", "category": "Food Walk", "cost": 250, "duration": "2 hrs"}
            ],
            [
                {"name": "Heritage Madurai", "category": "Luxury Heritage Resort", "price_per_night": 7500, "rating": 4.7, "area": "Kochadai", "amenities": ["Temple View Pool", "Ayurveda Spa", "Lawns"], "suitability": ["Family", "Couples"]},
                {"name": "Courtyard by Marriott Madurai", "category": "4-Star Hotel", "price_per_night": 5200, "rating": 4.6, "area": "Alagarkoil Road", "amenities": ["Pool", "Gym", "Free WiFi"], "suitability": ["Family", "Solo"]}
            ],
            [
                {"name": "Famous Jigarthanda Shop", "cuisine": "Iconic Dessert Drink", "average_cost_for_two": 160, "rating": 4.8, "area": "East Marret Street", "popular_dishes": "Special Famous Jigarthanda", "is_veg": True},
                {"name": "Amma Mess", "cuisine": "Legendary Non-Veg Madurai", "average_cost_for_two": 550, "rating": 4.6, "area": "Thallakulam", "popular_dishes": "Bone Marrow Omelette, Crab Omelette, Biryani", "is_veg": False},
                {"name": "Murugan Idli Shop (Original)", "cuisine": "South Indian Vegetarian", "average_cost_for_two": 300, "rating": 4.6, "area": "West Masi Street", "popular_dishes": "Podi Idli, Onion Uthappam", "is_veg": True}
            ]
        ),
        make_destination(
            "Rameswaram & Kanyakumari", "The Sacred Land's End",
            "Pilgrimage island connected by the Pamban Sea Bridge, and the southern tip where three oceans meet.",
            1600, "Oct–Mar", "3 Days", 4.8, 9.3, "Spiritual Coast & Land's End", ["Family", "Solo", "Friends"], "Rameswaram",
            ["Rameswaram Island & Pamban", "Dhanushkodi Ghost Town", "Kanyakumari Pier", "Vivekananda Rock"],
            [
                {"name": "Ramanathaswamy Temple (Rameswaram)", "category": "Jyotirlinga Temple", "highlight": "Longest temple corridor in the world with 1212 pillars", "fee": "Free", "time": "3 hrs"},
                {"name": "Pamban Sea Bridge", "category": "Cantilever Bridge", "highlight": "Iconic railway bridge over opening sea waters", "fee": "Free", "time": "1 hr"},
                {"name": "Vivekananda Rock Memorial (Kanyakumari)", "category": "Memorial & Island", "highlight": "Rock monument where three seas meet", "fee": "₹50 (Ferry+Entry)", "time": "2 hrs"},
                {"name": "Dhanushkodi Ghost Town", "category": "Ruins & Beach", "highlight": "Submerged church & railway station ruins on sand strip", "fee": "Free", "time": "2.5 hrs"}
            ],
            [
                {"name": "Dhanushkodi 4x4 Jeep Beach Safari", "category": "Safari", "cost": 400, "duration": "2 hrs"},
                {"name": "Sunset and Moonrise Simultaneous Viewing at Kanyakumari", "category": "Natural Phenomenon", "cost": 0, "duration": "1 hr"}
            ],
            [
                {"name": "Daiwik Hotels Rameswaram", "category": "Pilgrimage 4-Star", "price_per_night": 4200, "rating": 4.4, "area": "Near Station", "amenities": ["Vegetarian Dining", "Spa", "Free WiFi"], "suitability": ["Family", "Couples"]},
                {"name": "The Seashore Hotel Kanyakumari", "category": "Seafront Hotel", "price_per_night": 4800, "rating": 4.5, "area": "Main Road Kanyakumari", "amenities": ["Sunrise Ocean View", "Restaurant"], "suitability": ["Family", "Couples"]}
            ],
            [
                {"name": "Gujarat Bhavan Pure Veg (Rameswaram)", "cuisine": "Pure Veg Gujarati & South Indian", "average_cost_for_two": 300, "rating": 4.4, "area": "Temple Street", "popular_dishes": "Unlimited Thali, Idli Vada", "is_veg": True},
                {"name": "The Curry Restaurant (Kanyakumari)", "cuisine": "Coastal Seafood & South Indian", "average_cost_for_two": 600, "rating": 4.4, "area": "Beach Road", "popular_dishes": "Fish Fry, Meen Kulambu", "is_veg": False}
            ]
        )
    ]
}

# ── 5. Telangana ─────────────────────────────────────────────────────────────
SOUTH_STATES["Telangana"] = {
    "capital": "Hyderabad", "region": "South", "tagline": "State of Passion & Pearls",
    "destinations": [
        make_destination(
            "Hyderabad", "The City of Pearls & Biryani",
            "Historic Nizami capital boasting Charminar, Golconda fort acoustics, and legendary Hyderabadi Dum Biryani.",
            1900, "Oct–Mar", "3 Days", 4.8, 9.7, "Nizami Heritage & Tech", ["Family", "Foodies", "Couples", "Solo"], "Hyderabad",
            ["Old City & Charminar", "Banjara Hills & Jubilee Hills", "Hitec City & Gachibowli", "Hussain Sagar & Tank Bund"],
            [
                {"name": "Charminar & Laad Bazaar", "category": "Historic Monument", "highlight": "1591 landmark with 4 minarets and lacquer bangle markets", "fee": "₹25", "time": "2 hrs"},
                {"name": "Golconda Fort", "category": "Fortress", "highlight": "Acoustic wonder fortress with sound and light evening show", "fee": "₹25", "time": "3 hrs"},
                {"name": "Chowmahalla Palace", "category": "Palace", "highlight": "Seat of the Asaf Jahi dynasty with royal vintage car collection", "fee": "₹80", "time": "2 hrs"},
                {"name": "Hussain Sagar Lake & Buddha Statue", "category": "Lake Landmark", "highlight": "World's tallest monolithic Buddha statue standing in lake", "fee": "₹100 (Boat)", "time": "2 hrs"}
            ],
            [
                {"name": "Old City Midnight Biryani & Irani Chai Trail", "category": "Food Walk", "cost": 400, "duration": "2.5 hrs"},
                {"name": "Golconda Fort Sound and Light Show", "category": "Cultural Show", "cost": 140, "duration": "1 hr"},
                {"name": "Pearls & Bangles Shopping in Laad Bazaar", "category": "Shopping", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "Taj Falaknuma Palace", "category": "Ultra Luxury Heritage 5-Star", "price_per_night": 36000, "rating": 4.9, "area": "Engine Bowli", "amenities": ["Royal Horse Carriage", "Palace Tour", "Fine Dining"], "suitability": ["Couples", "Family"]},
                {"name": "ITC Kohenur (Luxury Collection)", "category": "Luxury 5-Star", "price_per_night": 14000, "rating": 4.8, "area": "Hitec City", "amenities": ["Lake View", "Pool", "Spa", "Italian Restaurant"], "suitability": ["Business", "Couples"]},
                {"name": "The Park Hyderabad", "category": "Boutique 5-Star", "price_per_night": 6500, "rating": 4.5, "area": "Somajiguda", "amenities": ["Infinity Pool overlooking lake", "Free WiFi"], "suitability": ["Couples", "Solo"]},
                {"name": "Zostel Hyderabad", "category": "Backpacker Hostel", "price_per_night": 850, "rating": 4.4, "area": "Gachibowli", "amenities": ["Free WiFi", "AC", "Co-working Space"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Paradise Biryani (Secunderabad)", "cuisine": "Iconic Hyderabadi Biryani", "average_cost_for_two": 700, "rating": 4.6, "area": "Secunderabad", "popular_dishes": "Mutton Dum Biryani, Mirchi Ka Salan, Double Ka Meetha", "is_veg": False},
                {"name": "Bawarchi Restaurant", "cuisine": "Authentic Dum Biryani", "average_cost_for_two": 650, "rating": 4.7, "area": "RTC X Roads", "popular_dishes": "Special Mutton Biryani, Boti Kebab", "is_veg": False},
                {"name": "Nimrah Cafe and Bakery", "cuisine": "Irani Chai & Osmania Biscuits", "average_cost_for_two": 150, "rating": 4.8, "area": "Beside Charminar", "popular_dishes": "Irani Chai with Hot Osmania & Khari Biscuits", "is_veg": True},
                {"name": "Chutneys", "cuisine": "South Indian Vegetarian", "average_cost_for_two": 600, "rating": 4.6, "area": "Banjara Hills", "popular_dishes": "Guntur Idli, 7 Varieties of Chutney, Babai Dosa", "is_veg": True}
            ]
        ),
        make_destination(
            "Warangal", "The Kakatiya Capital of Stone",
            "Ancient fortress city renowned for Thousand Pillar Temple and UNESCO-listed Ramappa Temple.",
            1400, "Oct–Mar", "2 Days", 4.6, 8.4, "Kakatiya Heritage & Temples", ["Family", "Solo", "History Lovers"], "Warangal",
            ["Warangal Fort Area", "Hanamkonda (Thousand Pillar)", "Ramappa Lake & Temple Hub"],
            [
                {"name": "Thousand Pillar Temple", "category": "Temple", "highlight": "12th-century Chalukya-Kakatiya masterpiece with monolithic Nandi", "fee": "Free", "time": "2 hrs"},
                {"name": "Warangal Fort & Stone Gateways", "category": "Fort", "highlight": "Four iconic Kakatiya carved stone gateways (Kirti Toranas)", "fee": "₹25", "time": "2.5 hrs"},
                {"name": "Ramappa Temple (UNESCO)", "category": "UNESCO World Heritage", "highlight": "Floating bricks temple with exquisite stone bracket carvings", "fee": "₹40", "time": "2.5 hrs"}
            ],
            [
                {"name": "Ramappa Lake Boating & Sunset", "category": "Boating", "cost": 200, "duration": "1 hr"},
                {"name": "Warangal Fort Sound and Light Heritage Show", "category": "Light Show", "cost": 60, "duration": "1 hr"}
            ],
            [
                {"name": "Haritha Kakatiya Hotel", "category": "State Heritage Hotel", "price_per_night": 2200, "rating": 4.1, "area": "Hanamkonda", "amenities": ["AC", "Restaurant", "Parking"], "suitability": ["Family", "Solo"]},
                {"name": "Hotel Ashoka", "category": "Mid-range Hotel", "price_per_night": 1800, "rating": 4.0, "area": "Main Road", "amenities": ["Free WiFi", "Dining"], "suitability": ["Family", "Solo"]}
            ],
            [
                {"name": "Kakatiya Mess", "cuisine": "Telangana Country Meals", "average_cost_for_two": 350, "rating": 4.5, "area": "Hanamkonda", "popular_dishes": "Telangana Mutton Curry, Spicy Pappu, Jowar Roti", "is_veg": False},
                {"name": "Bay Leaf Restaurant", "cuisine": "North & South Indian", "average_cost_for_two": 500, "rating": 4.3, "area": "Subedari", "popular_dishes": "Biryani, Paneer Tikka", "is_veg": False}
            ]
        ),
        make_destination(
            "Nagarjunasagar", "Massive Masonry Dam & Buddhist Island",
            "World's tallest masonry dam spanning the Krishna River, island museum of Nagarjunakonda, and waterfalls.",
            1500, "Oct–Mar", "2 Days", 4.6, 8.8, "Buddhist Archaeology & River Engineering", ["Family", "Solo", "Couples"], "Nalgonda",
            ["Nagarjuna Konda Island", "Dam Viewpoint", "Ethipothala Falls"],
            [
                {"name": "Nagarjunakonda Island Museum", "category": "Buddhist Island", "highlight": "Island excavated with 3rd-century Buddhist stupas and monastery ruins", "fee": "₹20 (Boat extra)", "time": "3 hrs"},
                {"name": "Ethipothala Waterfalls", "category": "Waterfall & Lagoon", "highlight": "70-ft cascade on Chandravanka river with crocodile breeding pond", "fee": "₹25", "time": "2 hrs"},
                {"name": "Nagarjuna Sagar Dam", "category": "Masonry Dam", "highlight": "Massive 26-crest gate dam with majestic water releases", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Ferry Cruise across Sagar Reservoir to Island", "category": "Ferry Cruise", "cost": 150, "duration": "1.5 hrs"},
                {"name": "Evening Sunset Walk across Dam Viewpoint", "category": "Sightseeing", "cost": 0, "duration": "1 hr"}
            ],
            [
                {"name": "Haritha Vijay Vihar Nagarjunasagar", "category": "State Waterfront Resort", "price_per_night": 2800, "rating": 4.3, "area": "Hill Colony", "amenities": ["Lake Views", "Pool", "Restaurant"], "suitability": ["Family", "Couples"]},
                {"name": "Hotel River View Stay", "category": "Budget Lodge", "price_per_night": 1400, "rating": 4.0, "area": "Near Dam", "amenities": ["AC", "WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Vijay Vihar Restaurant", "cuisine": "Andhra & Telangana Thali", "average_cost_for_two": 450, "rating": 4.2, "area": "Haritha Resort", "popular_dishes": "Fish Fry, Andhra Veg Meals, Chicken Curry", "is_veg": False},
                {"name": "Sagar Highway Dhaba", "cuisine": "Highway Dhaba", "average_cost_for_two": 300, "rating": 4.1, "area": "Dam Bypass", "popular_dishes": "Dal Tadka, Roti, Egg Bhurji", "is_veg": True}
            ]
        ),
        make_destination(
            "Bhadrachalam", "Sacred Temple Town of the Godavari",
            "17th-century Sita Ramachandra Swamy temple on the banks of Godavari, scenic Papi Kondalu boat cruises, and lush hills.",
            1400, "Oct–Mar", "2 Days", 4.6, 8.7, "Pilgrimage & River Hills", ["Family", "Senior Citizens", "Solo"], "Khammam",
            ["Temple Ghats", "Godavari Riverbank", "Papi Kondalu Launch"],
            [
                {"name": "Sri Sita Ramachandra Swamy Temple", "category": "Sacred Temple", "highlight": "17th-century temple built by saint devotee Kancharla Gopanna (Bhakta Ramadasu)", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Papi Kondalu Hills & Gorge", "category": "River Canyon", "highlight": "Narrow forested hill gorge where Godavari river winds majestically", "fee": "Free", "time": "Full Day"}
            ],
            [
                {"name": "Scenic River Cruise from Bhadrachalam through Papi Hills", "category": "River Cruise", "cost": 900, "duration": "5 hrs"},
                {"name": "Godavari Sandbank Sunset Walk", "category": "River Walk", "cost": 0, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Haritha Bhadrachalam Resort", "category": "State Pilgrimage Hotel", "price_per_night": 2200, "rating": 4.2, "area": "Temple Area", "amenities": ["Restaurant", "Parking", "WiFi"], "suitability": ["Family", "Senior Citizens"]},
                {"name": "Hotel Godavari Pride", "category": "Comfort Hotel", "price_per_night": 1600, "rating": 4.0, "area": "Near Bus Stand", "amenities": ["AC", "Room Service"], "suitability": ["Solo", "Family"]}
            ],
            [
                {"name": "Ramadasu Canteen", "cuisine": "Pure Sattvic South Indian", "average_cost_for_two": 250, "rating": 4.5, "area": "Temple Main Gate", "popular_dishes": "Godavari Pulao, Idli Vada, Andhra Thali", "is_veg": True},
                {"name": "Godavari River Treat", "cuisine": "Traditional Telangana Meals", "average_cost_for_two": 350, "rating": 4.2, "area": "Ghat Road", "popular_dishes": "Fish Curry with Rice, Sambar Rice", "is_veg": False}
            ]
        )
    ]
}

print("South India dataset loaded with 5 states and 25 rich destinations.")


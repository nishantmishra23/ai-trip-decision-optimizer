"""
West India Tourism Dataset: Goa, Gujarat, Maharashtra.
Each state features 6-8 destinations with complete neighborhoods, places, activities, hotels, and dining.
"""
from data.regions.common import make_destination

WEST_STATES = {}

# ── 6. Goa ───────────────────────────────────────────────────────────────────
WEST_STATES["Goa"] = {
    "capital": "Panaji", "region": "West", "tagline": "Pearl of the Orient",
    "destinations": [
        make_destination(
            "North Goa (Calangute & Baga)", "The Party & Beach Sports Capital",
            "Vibrant beach strip famous for water sports, beach shacks, night markets, and music clubs.",
            2500, "Nov–Feb", "3 Days", 4.7, 9.8, "Beach Party & Nightlife", ["Friends", "Solo", "Couples"], "Panaji",
            ["Baga Beach", "Calangute Beach", "Candolim & Sinquerim", "Anjuna & Vagator"],
            [
                {"name": "Baga & Calangute Beach", "category": "Beach & Nightlife", "highlight": "Thriving beach strip with water sports and shacks", "fee": "Free", "time": "4 hrs"},
                {"name": "Aguada Fort & Lighthouse", "category": "Portuguese Fort", "highlight": "17th-century coastal fortress overlooking the Arabian Sea", "fee": "₹25", "time": "2 hrs"},
                {"name": "Chapora Fort", "category": "Sunset Fort", "highlight": "Dil Chahta Hai viewpoint over Vagator beach", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Parasailing & Jet Ski Package at Baga", "category": "Water Sports", "cost": 1200, "duration": "1.5 hrs"},
                {"name": "Club Night at Tito's Lane & Cafe Mambo", "category": "Nightlife", "cost": 1500, "duration": "4 hrs"},
                {"name": "Anjuna Flea Market Shopping (Wednesdays)", "category": "Shopping", "cost": 0, "duration": "3 hrs"}
            ],
            [
                {"name": "Taj Fort Aguada Resort & Spa", "category": "Luxury 5-Star", "price_per_night": 16000, "rating": 4.8, "area": "Sinquerim", "amenities": ["Oceanfront", "Pool", "Spa", "Private Beach"], "suitability": ["Couples", "Family"]},
                {"name": "Hard Rock Hotel Goa", "category": "Boutique Hotel", "price_per_night": 7000, "rating": 4.5, "area": "Calangute", "amenities": ["Pool", "Live Music", "Free WiFi"], "suitability": ["Friends", "Couples"]},
                {"name": "Zostel Goa (Calangute)", "category": "Backpacker Hostel", "price_per_night": 950, "rating": 4.4, "area": "Calangute", "amenities": ["Free WiFi", "AC", "Pool", "Common Lounge"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Britto's Beach Shack", "cuisine": "Goan Seafood & Bakery", "average_cost_for_two": 1200, "rating": 4.5, "area": "Baga Beach", "popular_dishes": "Prawn Curry Rice, Crab Xacuti, Bebinca", "is_veg": False},
                {"name": "Thalassa (Siolim/Vagator)", "cuisine": "Greek & Mediterranean", "average_cost_for_two": 2400, "rating": 4.7, "area": "Siolim", "popular_dishes": "Greek Salad, Souvlaki, Sunset Cocktails", "is_veg": False},
                {"name": "Infantaria Cafe", "cuisine": "Continental Breakfast & Bakes", "average_cost_for_two": 600, "rating": 4.4, "area": "Calangute", "popular_dishes": "Croissant, English Breakfast, Bebinca", "is_veg": True}
            ]
        ),
        make_destination(
            "South Goa (Palolem & Agonda)", "Tranquil Sands & Silent Sunsets",
            "Crescent palm-fringed beaches, silent noise parties, dolphin boat trips, and peaceful beach hut stays.",
            2200, "Nov–Mar", "3 Days", 4.8, 9.3, "Serene Beach & Wellness", ["Couples", "Solo", "Family"], "Canacona",
            ["Palolem Beach", "Agonda Beach", "Cola Beach & Lagoon", "Cavelossim"],
            [
                {"name": "Palolem Beach", "category": "Crescent Beach", "highlight": "Picturesque calm beach ideal for swimming and kayaking", "fee": "Free", "time": "Full Day"},
                {"name": "Cola Beach & Emerald Lagoon", "category": "Lagoon & Beach", "highlight": "Freshwater green lagoon meeting the Arabian Sea", "fee": "Free", "time": "3 hrs"},
                {"name": "Cabo de Rama Fort", "category": "Cliff Fort", "highlight": "Cliffside fortress with sheer sea drop viewpoints", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Early Morning Dolphin Spotting Boat Cruise", "category": "Boat Safari", "cost": 400, "duration": "1 hr"},
                {"name": "Kayaking into the Palolem Mangrove Backwaters", "category": "Kayaking", "cost": 300, "duration": "2 hrs"},
                {"name": "Silent Headphone Party (Neptune Point)", "category": "Nightlife", "cost": 700, "duration": "3 hrs"}
            ],
            [
                {"name": "The Leela Goa", "category": "Luxury 5-Star Beach Resort", "price_per_night": 22000, "rating": 4.9, "area": "Cavelossim", "amenities": ["Golf Course", "Lagoon Pool", "Spa", "Beach Access"], "suitability": ["Couples", "Family"]},
                {"name": "Ciaran's Beach Huts", "category": "Boutique Beach Huts", "price_per_night": 4500, "rating": 4.6, "area": "Palolem Beach", "amenities": ["Beachfront", "Restaurant", "Garden"], "suitability": ["Couples", "Solo"]},
                {"name": "Zostel South Goa (Palolem)", "category": "Backpacker Hostel", "price_per_night": 800, "rating": 4.5, "area": "Palolem", "amenities": ["Free WiFi", "AC", "Garden Lounge"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Dropadi Restaurant", "cuisine": "Seafood & Indian", "average_cost_for_two": 900, "rating": 4.6, "area": "Palolem Beach", "popular_dishes": "Butter Garlic Prawns, Kingfish Tandoori", "is_veg": False},
                {"name": "The Fisherman's Wharf", "cuisine": "Goan Coastal & Seafood", "average_cost_for_two": 1800, "rating": 4.7, "area": "Cavelossim", "popular_dishes": "Goan Fish Curry, Prawn Balchão", "is_veg": False}
            ]
        ),
        make_destination(
            "Panaji & Fontainhas", "The Portuguese Heritage Quarter",
            "Colorful Latin Quarter with Portuguese villas, wooden verandas, art galleries, and Mandovi casino cruises.",
            2100, "Year-round", "2 Days", 4.7, 9.1, "Colonial Architecture & Heritage", ["Couples", "Solo", "Family"], "Panaji",
            ["Fontainhas Latin Quarter", "Miramar Beach", "Mandovi River Promenade", "Altinho Hill"],
            [
                {"name": "Fontainhas Latin Quarter", "category": "Heritage Quarter", "highlight": "Pastel-hued Portuguese houses, azulejo tiles, art cafes", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Our Lady of the Immaculate Conception Church", "category": "Baroque Church", "highlight": "1600s white zigzag baroque staircase church", "fee": "Free", "time": "1 hr"}
            ],
            [
                {"name": "Fontainhas Walking Photography Tour", "category": "Photo Walk", "cost": 250, "duration": "2 hrs"},
                {"name": "Mandovi River Sunset Cruise with Goan Folk Dance", "category": "River Cruise", "cost": 500, "duration": "1 hr"}
            ],
            [
                {"name": "Goa Marriott Resort & Spa", "category": "Luxury 5-Star", "price_per_night": 13000, "rating": 4.8, "area": "Miramar", "amenities": ["Bay View", "Pool", "Casino", "Spa"], "suitability": ["Family", "Couples"]},
                {"name": "WelcomHeritage Panjim Inn", "category": "Heritage Hotel", "price_per_night": 4800, "rating": 4.5, "area": "Fontainhas", "amenities": ["Colonial Antiques", "Restaurant"], "suitability": ["Couples", "Solo"]}
            ],
            [
                {"name": "Viva Panjim", "cuisine": "Authentic Portuguese Goan", "average_cost_for_two": 700, "rating": 4.6, "area": "Fontainhas", "popular_dishes": "Pork Vindaloo, Prawn Curry Rice", "is_veg": False},
                {"name": "Ritz Classic", "cuisine": "Traditional Goan Fish Thali", "average_cost_for_two": 600, "rating": 4.7, "area": "18th June Road", "popular_dishes": "Special Fish Thali, Crab Masala", "is_veg": False}
            ]
        ),
        make_destination(
            "Dudhsagar & Mollem", "The Sea of Milk in the Western Ghats",
            "Four-tiered majestic 1017-ft waterfall on Mandovi River with railway bridge crossing and jungle safari.",
            1600, "Jul–Feb", "1 Day", 4.8, 9.4, "Waterfall & Wilderness", ["Friends", "Adventurers", "Family"], "Mollem",
            ["Dudhsagar Base Camp", "Bhagwan Mahavir Wildlife Sanctuary", "Mollem National Park"],
            [
                {"name": "Dudhsagar Waterfalls", "category": "Waterfall", "highlight": "Four-tiered milky cascade where train bridges the mist", "fee": "₹100 (Entry)", "time": "4 hrs"},
                {"name": "Tambdi Surla Mahadev Temple", "category": "Ancient Temple", "highlight": "12th-century Kadamba basalt stone temple hidden in jungle", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "4x4 Open Jeep Jungle Safari through Mollem", "category": "Jeep Safari", "cost": 650, "duration": "2 hrs"},
                {"name": "Freshwater Pool Swimming beneath Dudhsagar", "category": "Nature Swim", "cost": 0, "duration": "1 hr"}
            ],
            [
                {"name": "Dudhsagar Spa Resort", "category": "Eco Jungle Resort", "price_per_night": 4200, "rating": 4.3, "area": "Mollem", "amenities": ["Pool", "Jungle Views", "Restaurant"], "suitability": ["Family", "Friends"]},
                {"name": "Mollem Eco Camp & Tents", "category": "Wilderness Eco Camp", "price_per_night": 1800, "rating": 4.2, "area": "National Park Gate", "amenities": ["Tents", "Campfire", "Jungle Guide"], "suitability": ["Friends", "Solo"]}
            ],
            [
                {"name": "Wild Mushroom Restaurant", "cuisine": "Goan Village Cuisine", "average_cost_for_two": 500, "rating": 4.2, "area": "Mollem", "popular_dishes": "Goan Chicken Xacuti, Local Fish Fry", "is_veg": False},
                {"name": "Mollem Highway Treat", "cuisine": "Highway Indian & Goan", "average_cost_for_two": 350, "rating": 4.1, "area": "NH-4A", "popular_dishes": "Fish Thali, Egg Bhurji, Chai", "is_veg": False}
            ]
        ),
        make_destination(
            "Old Goa Heritage", "The Rome of the East",
            "UNESCO World Heritage complex of monumental 16th-century cathedrals housing sacred relics of St. Francis Xavier.",
            1400, "Year-round", "1 Day", 4.7, 9.2, "UNESCO World Heritage", ["Family", "Solo", "History Lovers"], "Old Goa",
            ["Basilica Complex", "Se Cathedral Square", "Viceroy's Arch Area"],
            [
                {"name": "Basilica of Bom Jesus", "category": "UNESCO Basilica", "highlight": "Mausoleum of St. Francis Xavier with silver casket", "fee": "Free", "time": "2 hrs"},
                {"name": "Se Cathedral", "category": "Cathedral", "highlight": "Largest church in Asia featuring the Golden Bell", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Heritage Walk of Old Goa Portuguese Churches", "category": "Guided Walk", "cost": 250, "duration": "2 hrs"},
                {"name": "Se Cathedral Acoustic Choir & Architecture Walk", "category": "Heritage Walk", "cost": 0, "duration": "1.5 hrs"}
            ],
            [
                {"name": "The Postcard Velha", "category": "Luxury Heritage Retreat", "price_per_night": 14000, "rating": 4.8, "area": "Old Goa Hills", "amenities": ["Boutique Suites", "Fine Dining", "Lawn"], "suitability": ["Couples"]},
                {"name": "Old Goa Heritage Residency (GTDC)", "category": "Comfort Heritage Stay", "price_per_night": 2400, "rating": 4.2, "area": "Near Basilica", "amenities": ["AC", "Restaurant", "Parking"], "suitability": ["Family", "Solo"]}
            ],
            [
                {"name": "Casa Sarita (Near Old Goa)", "cuisine": "Colonial Goan Fine Dining", "average_cost_for_two": 2200, "rating": 4.7, "area": "Bambolim", "popular_dishes": "Lobster Peri Peri, Bebinca", "is_veg": False},
                {"name": "Little Goa Restaurant", "cuisine": "Goan Fish Thali & Portuguese", "average_cost_for_two": 500, "rating": 4.4, "area": "Old Goa Highway", "popular_dishes": "Kingfish Curry, Sol Kadhi, Pao", "is_veg": False}
            ]
        ),
        make_destination(
            "Morjim & Ashwem", "The Bohemian Russian Coast & Turtles",
            "Pristine North Goa shores known as Little Russia, Olive Ridley turtle nesting site, and upscale beach clubs.",
            2300, "Nov–Mar", "2 Days", 4.7, 8.8, "Chic Beach & Turtle Sanctuary", ["Couples", "Friends", "Solo"], "Morjim",
            ["Morjim Beach Strip", "Ashwem Beach", "Chapora River Mouth"],
            [
                {"name": "Morjim Beach & Turtle Nesting Sanctuary", "category": "Eco Beach", "highlight": "Protected nesting habitat for endangered Olive Ridley sea turtles", "fee": "Free", "time": "3 hrs"},
                {"name": "Ashwem White Sand Beach", "category": "Beach", "highlight": "Quiet coconut palm beach lined with minimalist designer shacks", "fee": "Free", "time": "3 hrs"}
            ],
            [
                {"name": "Sunset Cocktails & House Music at La Plage", "category": "Beach Club", "cost": 1500, "duration": "3 hrs"},
                {"name": "Kite Surfing at Morjim Beach", "category": "Extreme Sports", "cost": 2500, "duration": "2 hrs"}
            ],
            [
                {"name": "Rococco Ashvem", "category": "Boutique Beach Resort", "price_per_night": 5800, "rating": 4.4, "area": "Ashwem Beach", "amenities": ["Pool", "Direct Beach Access", "Spa"], "suitability": ["Couples", "Friends"]},
                {"name": "Turtle Beach Resort Morjim", "category": "Chic Beach Hotel", "price_per_night": 3600, "rating": 4.3, "area": "Morjim", "amenities": ["Pool", "Restaurant", "WiFi"], "suitability": ["Couples", "Solo"]}
            ],
            [
                {"name": "La Plage", "cuisine": "French & Mediterranean Beachside", "average_cost_for_two": 2000, "rating": 4.8, "area": "Ashwem Beach", "popular_dishes": "Seared Tuna with Wasabi, Chocolate Thali", "is_veg": False},
                {"name": "Burger Factory Morjim", "cuisine": "Gourmet Burgers", "average_cost_for_two": 850, "rating": 4.7, "area": "Morjim", "popular_dishes": "Gourmet Beef Burger, Avocado Bacon Burger", "is_veg": False}
            ]
        )
    ]
}

# ── 7. Gujarat ───────────────────────────────────────────────────────────────
WEST_STATES["Gujarat"] = {
    "capital": "Gandhinagar", "region": "West", "tagline": "Vibrant Gujarat",
    "destinations": [
        make_destination(
            "Rann of Kutch", "The Great White Salt Desert",
            "World's largest salt desert shimmering white under the full moon, celebrated with the grand Rann Utsav.",
            2200, "Nov–Feb", "3 Days", 4.9, 9.6, "Salt Desert & Culture", ["Family", "Couples", "Photographers", "Solo"], "Bhuj",
            ["Dhordo Tent City", "White Desert Sunset Point", "Kala Dungar (Black Hill)", "Hodka Craft Village"],
            [
                {"name": "White Rann Desert", "category": "Salt Desert", "highlight": "Vast expanse of pure white salt crystals under starlit moonlight", "fee": "₹100 (Permit)", "time": "4 hrs"},
                {"name": "Kala Dungar (Black Hill)", "category": "Highest Viewpoint", "highlight": "Highest point in Kutch with panoramic desert view & Dattatreya temple", "fee": "Free", "time": "2 hrs"},
                {"name": "Hodka & Nirona Handicraft Villages", "category": "Art Villages", "highlight": "Rogan art, copper bells, and Kutchi mirror-work embroidery", "fee": "Free", "time": "3 hrs"}
            ],
            [
                {"name": "Camel Cart Safari into the White Desert at Sunset", "category": "Desert Safari", "cost": 300, "duration": "1.5 hrs"},
                {"name": "Rann Utsav Cultural Folk Dance & Music Night", "category": "Cultural Show", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "The Tent City Dhordo", "category": "Luxury Desert Glamping", "price_per_night": 14000, "rating": 4.7, "area": "Dhordo", "amenities": ["AC Swiss Tents", "All Meals", "Cultural Passes"], "suitability": ["Family", "Couples"]},
                {"name": "Shaam-e-Sarhad Village Resort", "category": "Eco-Ethnic Mud Resort", "price_per_night": 5200, "rating": 4.6, "area": "Hodka", "amenities": ["Traditional Bhungas", "Kutchi Thali"], "suitability": ["Couples", "Solo"]}
            ],
            [
                {"name": "Toran Dining Hall", "cuisine": "Authentic Kutchi & Gujarati Thali", "average_cost_for_two": 500, "rating": 4.6, "area": "Rann Utsav Grounds", "popular_dishes": "Bajra Roti, Ringna No Olo, Gulab Pak", "is_veg": True},
                {"name": "Green Rock Restaurant", "cuisine": "Pure Veg Gujarati & Kathiyawadi", "average_cost_for_two": 400, "rating": 4.5, "area": "Bhuj", "popular_dishes": "Sev Tameta, Lasaniya Batata", "is_veg": True}
            ]
        ),
        make_destination(
            "Ahmedabad", "India's First UNESCO Heritage City",
            "Centuries of historic pols, stepwells, Sabarmati Ashram, and bustling night street food markets.",
            1700, "Oct–Mar", "2 Days", 4.7, 9.2, "Heritage & Street Food", ["Family", "Solo", "Foodies"], "Ahmedabad",
            ["Sabarmati Riverfront", "Old City (Pols)", "Manek Chowk Area", "Adalaj & Gandhinagar"],
            [
                {"name": "Sabarmati Ashram (Gandhi Ashram)", "category": "National Memorial", "highlight": "Mahatma Gandhi's peaceful riverside headquarters from 1917", "fee": "Free", "time": "2 hrs"},
                {"name": "Adalaj Stepwell (Vav)", "category": "Ancient Stepwell", "highlight": "5-story 1498 subterranean architectural wonder with carved pillars", "fee": "Free", "time": "2 hrs"},
                {"name": "Sidi Saiyyed Mosque", "category": "Heritage Mosque", "highlight": "Famed intricate marble Tree of Life lattice window (Jali)", "fee": "Free", "time": "1 hr"}
            ],
            [
                {"name": "Midnight Street Food Extravaganza at Manek Chowk", "category": "Street Food Tour", "cost": 350, "duration": "2 hrs"},
                {"name": "Morning Heritage Walk through Old Ahmedabad Pols", "category": "Guided Walk", "cost": 150, "duration": "2.5 hrs"}
            ],
            [
                {"name": "The House of MG", "category": "Heritage Boutique 5-Star", "price_per_night": 8500, "rating": 4.7, "area": "Old City", "amenities": ["Agashiye Rooftop", "Indoor Pool", "Heritage Decor"], "suitability": ["Couples", "Family"]},
                {"name": "Hyatt Regency Ahmedabad", "category": "5-Star Deluxe", "price_per_night": 7200, "rating": 4.7, "area": "Ashram Road", "amenities": ["Riverfront View", "Pool", "Gym"], "suitability": ["Business", "Family"]},
                {"name": "Zostel Ahmedabad", "category": "Backpacker Hostel", "price_per_night": 750, "rating": 4.4, "area": "Ellisbridge", "amenities": ["Free WiFi", "AC", "Common Lounge"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Agashiye (House of MG)", "cuisine": "Royal Gujarati Thali on Rooftop", "average_cost_for_two": 1800, "rating": 4.8, "area": "Lal Darwaja", "popular_dishes": "Royal Silver Plate Gujarati Thali, Rasawala Dhokla", "is_veg": True},
                {"name": "Manek Chowk Food Street", "cuisine": "Midnight Street Food", "average_cost_for_two": 350, "rating": 4.6, "area": "Old City", "popular_dishes": "Gwalior Dosa, Chocolate Cheese Sandwich, Kulfi", "is_veg": True},
                {"name": "Das Khaman", "cuisine": "Legendary Gujarati Snacks", "average_cost_for_two": 200, "rating": 4.7, "area": "Navrangpura", "popular_dishes": "Vati Dal Khaman, Sev Khamani, Jalebi", "is_veg": True}
            ]
        ),
        make_destination(
            "Gir National Park", "The Only Realm of the Asiatic Lion",
            "The sole surviving wild habitat on Earth for the majestic Asiatic lion in rugged teak forests.",
            2400, "Nov–May", "2 Days", 4.8, 9.4, "Wildlife & Lion Safari", ["Family", "Wildlife Photographers", "Solo"], "Sasan Gir",
            ["Sasan Gir Safari Gate", "Devalia Safari Park", "Hiran River Valley"],
            [
                {"name": "Gir Forest Wildlife Sanctuary", "category": "National Park", "highlight": "Open jungle tracking Asiatic lions, leopards, and marsh crocodiles", "fee": "₹800 (Safari Permit)", "time": "3.5 hrs"},
                {"name": "Devalia Safari Park (Gir Interpretation Zone)", "category": "Wildlife Park", "highlight": "Fenced natural habitat ensuring guaranteed lion sightings", "fee": "₹200", "time": "1.5 hrs"}
            ],
            [
                {"name": "Open 4x4 Gypsy Morning Lion Safari", "category": "Jeep Safari", "cost": 4500, "duration": "3.5 hrs"},
                {"name": "Siddi Tribal Dance & Heritage Cultural Evening", "category": "Tribal Culture", "cost": 300, "duration": "1 hr"}
            ],
            [
                {"name": "The Gateway Hotel Gir Forest (IHCL)", "category": "Luxury 5-Star Safari Lodge", "price_per_night": 12000, "rating": 4.7, "area": "Sasan Gir", "amenities": ["Riverfront", "Pool", "Spa", "Safari Booking"], "suitability": ["Family", "Couples"]},
                {"name": "Woods at Sasan", "category": "Eco Luxury Retreat", "price_per_night": 16000, "rating": 4.8, "area": "Sasan", "amenities": ["Organic Farm", "Pool", "Wellness"], "suitability": ["Couples", "Family"]}
            ],
            [
                {"name": "Gir Kathiyawadi Dhaba", "cuisine": "Kathiyawadi Country Thali", "average_cost_for_two": 450, "rating": 4.6, "area": "Sasan Gir Road", "popular_dishes": "Sev Dungri, Kathiyawadi Lasaniya Bateta, Bajra Rotla", "is_veg": True},
                {"name": "Lion's Den Kathiyawadi Restaurant", "cuisine": "Pure Veg Gujarati & Kathiyawadi", "average_cost_for_two": 500, "rating": 4.5, "area": "Near Safari Gate", "popular_dishes": "Kadhi Khichdi, Ringna No Olo, Chhas", "is_veg": True}
            ]
        ),
        make_destination(
            "Statue of Unity", "World's Tallest Monument",
            "Monumental 182-meter statue of Sardar Vallabhbhai Patel overlooking the Narmada River and Sardar Sarovar Dam.",
            1900, "Year-round", "2 Days", 4.8, 9.5, "Modern Marvel & Scenic Dam", ["Family", "Couples", "Solo"], "Kevadia",
            ["Statue of Unity Complex", "Valley of Flowers", "Narmada Tent City", "Jungle Safari Park"],
            [
                {"name": "Statue of Unity Viewing Gallery", "category": "Monument", "highlight": "Observation deck inside the chest of 182m statue at 153 meters", "fee": "₹380", "time": "3 hrs"},
                {"name": "Valley of Flowers & Butterfly Garden", "category": "Landscaped Gardens", "highlight": "24-acre park of flowering plants with walking trails", "fee": "Included", "time": "2 hrs"},
                {"name": "Sardar Sarovar Dam Viewpoint", "category": "Dam Landmark", "highlight": "One of the world's largest concrete gravity dams", "fee": "Free", "time": "1 hr"}
            ],
            [
                {"name": "Evening Projection Laser & Sound Show on the Statue", "category": "Laser Spectacle", "cost": 0, "duration": "45 mins"},
                {"name": "Electric River Cruise on Narmada", "category": "River Cruise", "cost": 413, "duration": "1 hr"}
            ],
            [
                {"name": "Tent City 1 Narmada", "category": "Luxury Riverside Glamping", "price_per_night": 9000, "rating": 4.6, "area": "Kevadia", "amenities": ["River View", "Swiss Tents", "Buffet Meals Included"], "suitability": ["Family", "Couples"]},
                {"name": "Ramada Encore by Wyndham", "category": "4-Star Hotel", "price_per_night": 5500, "rating": 4.5, "area": "Ekta Nagar", "amenities": ["Pool", "Free WiFi", "Gym"], "suitability": ["Family", "Business"]}
            ],
            [
                {"name": "Narmada Food Court", "cuisine": "Multi-state Cuisines", "average_cost_for_two": 500, "rating": 4.4, "area": "Statue Complex", "popular_dishes": "Gujarati Thali, Punjabi Dal Makhani, Dosa", "is_veg": True},
                {"name": "Ekta Tribal Cafe & Kathiyawadi Kitchen", "cuisine": "Tribal Organic & Kathiyawadi", "average_cost_for_two": 450, "rating": 4.6, "area": "Ekta Nagar", "popular_dishes": "Makai Rotla, Sev Tameta, Fresh Chaas", "is_veg": True}
            ]
        ),
        make_destination(
            "Somnath & Dwarka", "Sacred Shores of Lord Krishna & Shiva",
            "First of the 12 Jyotirlingas on Arabian sea cliffs, and the ancient submerged kingdom capital of Dwarka.",
            1500, "Oct–Mar", "3 Days", 4.8, 9.3, "Spiritual Coast & Pilgrimage", ["Family", "Solo", "Couples"], "Somnath",
            ["Somnath Temple Shoreline", "Dwarkadhish Temple Core", "Bet Dwarka Island", "Shivrajpur Blue Flag Beach"],
            [
                {"name": "Somnath Jyotirlinga Temple", "category": "Jyotirlinga Temple", "highlight": "Shore temple that was rebuilt 7 times, overlooking sea edge", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Dwarkadhish Temple (Jagat Mandir)", "category": "Char Dham Temple", "highlight": "2200-year-old 5-story shrine with 52-yard flag fluttered by breeze", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Shivrajpur Beach", "category": "Blue Flag Beach", "highlight": "Crystal clear sea, white sands, and scuba diving", "fee": "₹30", "time": "3 hrs"}
            ],
            [
                {"name": "Somnath Light and Sound Show by Amitabh Bachchan", "category": "Heritage Show", "cost": 30, "duration": "1 hr"},
                {"name": "Scuba Diving & Coral Exploration at Shivrajpur", "category": "Scuba Diving", "cost": 2500, "duration": "2 hrs"},
                {"name": "Ferry Ride to Bet Dwarka Island", "category": "Ferry", "cost": 30, "duration": "30 mins"}
            ],
            [
                {"name": "The Fern Residency Somnath", "category": "Eco 4-Star", "price_per_night": 4200, "rating": 4.4, "area": "Veraval Bypass", "amenities": ["Veg Dining", "Free WiFi", "AC"], "suitability": ["Family", "Couples"]},
                {"name": "Hawthorn Suites by Wyndham Dwarka", "category": "Luxury Villa Resort", "price_per_night": 6500, "rating": 4.6, "area": "Dwarka Outskirts", "amenities": ["Pool", "Gardens", "Vegetarian Dining"], "suitability": ["Family", "Couples"]}
            ],
            [
                {"name": "Sagar Darshan Dining Hall (Somnath)", "cuisine": "Pure Veg Gujarati Thali with Sea View", "average_cost_for_two": 350, "rating": 4.6, "area": "Temple Trust", "popular_dishes": "Unlimited Gujarati Thali, Shrikhand", "is_veg": True},
                {"name": "Chotiwala Restaurant (Dwarka)", "cuisine": "Pure Veg Multi-cuisine", "average_cost_for_two": 450, "rating": 4.4, "area": "Near Dwarkadhish Temple", "popular_dishes": "Special Kathiyawadi Thali, Paneer Handi", "is_veg": True}
            ]
        ),
        make_destination(
            "Saputara", "The Monsoon Jewel of Sahyadris",
            "Gujarat's only picturesque hill station in the Dang forest plateau, famous for lake boating, ropeway, and waterfalls.",
            1600, "Jul–Feb", "2 Days", 4.6, 8.5, "Hill Station & Tribal Forest", ["Family", "Couples", "Friends"], "Saputara",
            ["Saputara Lake", "Sunset Point & Table Ground", "Gira Waterfalls", "Artist Village"],
            [
                {"name": "Saputara Lake", "category": "Lake", "highlight": "Centerpiece lake offering pedal boating framed by verdant hills", "fee": "₹50 (Boating)", "time": "1.5 hrs"},
                {"name": "Gira Waterfalls", "category": "Waterfall", "highlight": "Roaring 150-ft cascade plunging into Ambika River during monsoon", "fee": "Free", "time": "2 hrs"},
                {"name": "Table Land (Governor's Hill)", "category": "Plateau Viewpoint", "highlight": "Flat table top hill offering camel rides and ropeway cable car", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Pushpak Ropeway Cable Car Ride across the valley", "category": "Ropeway", "cost": 120, "duration": "30 mins"},
                {"name": "Dang Tribal Warli Painting Workshop", "category": "Craft Workshop", "cost": 200, "duration": "2 hrs"}
            ],
            [
                {"name": "Aakar Lords Inn Saputara", "category": "Hill Resort", "price_per_night": 4200, "rating": 4.3, "area": "Lake Road", "amenities": ["Pool", "Vegetarian Dining", "Free WiFi"], "suitability": ["Family", "Couples"]},
                {"name": "Toran Hill Resort (TCGL)", "category": "State Resort", "price_per_night": 2400, "rating": 4.0, "area": "Near Sunset Point", "amenities": ["Valley View", "Restaurant"], "suitability": ["Family", "Solo"]}
            ],
            [
                {"name": "Sugandh Pure Veg", "cuisine": "Gujarati & Kathiyawadi Meals", "average_cost_for_two": 400, "rating": 4.4, "area": "Lake Market", "popular_dishes": "Gujarati Thali, Sweet Puran Poli", "is_veg": True},
                {"name": "Sugar 'N Spice Saputara", "cuisine": "Pure Veg Multi-Cuisine & Fast Food", "average_cost_for_two": 450, "rating": 4.3, "area": "Near Lake", "popular_dishes": "Pav Bhaji, Chole Bhature, Dosa", "is_veg": True}
            ]
        )
    ]
}

# ── 8. Maharashtra ───────────────────────────────────────────────────────────
WEST_STATES["Maharashtra"] = {
    "capital": "Mumbai", "region": "West", "tagline": "Unlimited Maharashtra",
    "destinations": [
        make_destination(
            "Mumbai", "The City of Dreams & Coastal Gateway",
            "India's financial and entertainment capital on the Arabian Sea with Victorian Gothic architecture and vibrant coastal spirit.",
            2400, "Oct–Mar", "3 Days", 4.8, 9.8, "Metropolitan & Coastal Heritage", ["Solo", "Friends", "Couples", "Family"], "Mumbai",
            ["South Mumbai & Fort", "Colaba & Marine Drive", "Bandra West", "Juhu & Vile Parle", "Andheri West", "Powai"],
            [
                {"name": "Gateway of India", "category": "Historical Monument", "highlight": "Colonial arch overlooking Mumbai harbor and Arabian Sea", "fee": "Free", "time": "1.5 hrs"},
                {"name": "Marine Drive (Queen's Necklace)", "category": "Coastal Promenade", "highlight": "3.6 km crescent promenade famous for sunset strolls", "fee": "Free", "time": "2 hrs"},
                {"name": "Elephanta Caves", "category": "UNESCO World Heritage", "highlight": "Ancient rock-cut Shiva sculptures on an island in the bay", "fee": "₹40", "time": "4 hrs"},
                {"name": "Chhatrapati Shivaji Maharaj Terminus", "category": "Victorian Gothic", "highlight": "UNESCO-listed working railway terminal masterpiece", "fee": "Free", "time": "1 hr"},
                {"name": "Bandra Bandstand & Fort", "category": "Seafront & Viewpoint", "highlight": "Bollywood celebrity homes, Portuguese fort, and sea breeze", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Street Food Walk at Chowpatty & Juhu Beach", "category": "Food Experience", "cost": 350, "duration": "2.5 hrs"},
                {"name": "Heritage Walk in Kala Ghoda & Fort Arts District", "category": "Culture Walk", "cost": 150, "duration": "3 hrs"},
                {"name": "Private Sailing Experience at Gateway of India", "category": "Sailing", "cost": 1800, "duration": "2 hrs"},
                {"name": "Cafe-hopping and Thrift Shopping in Bandra", "category": "Lifestyle", "cost": 600, "duration": "3 hrs"}
            ],
            [
                {"name": "The Taj Mahal Palace", "category": "Luxury 5-Star Heritage", "price_per_night": 28000, "rating": 4.9, "area": "Colaba", "amenities": ["Harbour View", "Pool", "Spa", "Fine Dining"], "suitability": ["Couples", "Family"]},
                {"name": "Trident Nariman Point", "category": "5-Star Deluxe", "price_per_night": 14000, "rating": 4.8, "area": "Marine Drive", "amenities": ["Queen's Necklace View", "Pool", "Gym"], "suitability": ["Couples", "Family", "Solo"]},
                {"name": "Residency Hotel Fort", "category": "Boutique Hotel", "price_per_night": 4500, "rating": 4.5, "area": "South Mumbai & Fort", "amenities": ["Free Breakfast", "Free WiFi", "AC"], "suitability": ["Solo", "Couples"]},
                {"name": "Hotel Suba Palace", "category": "Mid-range Hotel", "price_per_night": 5200, "rating": 4.4, "area": "Colaba", "amenities": ["Free Breakfast", "Free WiFi", "AC"], "suitability": ["Family", "Couples"]},
                {"name": "Zostel Mumbai", "category": "Backpacker Hostel", "price_per_night": 1100, "rating": 4.3, "area": "Andheri West", "amenities": ["Free WiFi", "AC", "Common Lounge", "Cafe"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Britannia & Co.", "cuisine": "Parsi & Iranian Heritage", "average_cost_for_two": 900, "rating": 4.6, "area": "South Mumbai & Fort", "popular_dishes": "Berry Pulao, Sali Boti, Caramel Custard", "is_veg": False},
                {"name": "Bademiya", "cuisine": "Mughlai Kebabs & Rolls", "average_cost_for_two": 700, "rating": 4.4, "area": "Colaba", "popular_dishes": "Seekh Kebab, Baida Roti, Chicken Bhuna Roll", "is_veg": False},
                {"name": "Mahesh Lunch Home", "cuisine": "Mangalorean Seafood", "average_cost_for_two": 1600, "rating": 4.6, "area": "Fort", "popular_dishes": "Butter Garlic Crab, Surmai Fry, Neer Dosa", "is_veg": False},
                {"name": "Subko Coffee Roasters", "cuisine": "Specialty Coffee & Bakes", "average_cost_for_two": 800, "rating": 4.7, "area": "Bandra West", "popular_dishes": "Pour-over Coffee, Sourdough Croissants", "is_veg": True},
                {"name": "Swati Snacks", "cuisine": "Gujarati & Mumbai Snacks", "average_cost_for_two": 600, "rating": 4.6, "area": "Tardeo", "popular_dishes": "Panki, Sev Puri, Handvo", "is_veg": True},
                {"name": "Sardar Pav Bhaji", "cuisine": "Mumbai Street Food", "average_cost_for_two": 350, "rating": 4.3, "area": "Tardeo", "popular_dishes": "Extra Amul Butter Pav Bhaji, Masala Pav", "is_veg": True}
            ]
        ),
        make_destination(
            "Pune", "Oxford of the East & Maratha Capital",
            "Thriving student and cultural city with historic Maratha forts, Osho Ashram, and hip cafe quarters.",
            1800, "Jul–Feb", "2 Days", 4.6, 9.1, "Heritage & Student Vibe", ["Solo", "Friends", "Couples", "Family"], "Pune",
            ["Koregaon Park & Kalyani Nagar", "FC Road & Shivajinagar", "Old City & Shaniwar Wada", "Viman Nagar"],
            [
                {"name": "Shaniwar Wada", "category": "Peshwa Fortress", "highlight": "1732 seat of the Peshwas with massive teak gates and fountains", "fee": "₹25", "time": "2 hrs"},
                {"name": "Aga Khan Palace", "category": "Historic Palace", "highlight": "Italian arches and Mahatma Gandhi's freedom struggle memorial", "fee": "₹25", "time": "2 hrs"},
                {"name": "Sinhagad Fort", "category": "Hilltop Fort", "highlight": "Mountain fort battlefield with panoramic Sahyadri views", "fee": "₹50", "time": "3.5 hrs"}
            ],
            [
                {"name": "Sinhagad Fort Trek & Kanda Bhajji Tasting", "category": "Trek & Food", "cost": 250, "duration": "4 hrs"},
                {"name": "Cafe-hopping & Nightlife in Koregaon Park", "category": "Nightlife", "cost": 800, "duration": "3 hrs"}
            ],
            [
                {"name": "JW Marriott Hotel Pune", "category": "Luxury 5-Star", "price_per_night": 11000, "rating": 4.8, "area": "Senapati Bapat Road", "amenities": ["Rooftop Lounge", "Pool", "Spa"], "suitability": ["Couples", "Family"]},
                {"name": "The Westin Pune Koregaon Park", "category": "5-Star Deluxe", "price_per_night": 12000, "rating": 4.7, "area": "Koregaon Park", "amenities": ["Riverfront", "Pool", "Nightclub"], "suitability": ["Couples", "Business"]},
                {"name": "Zostel Pune", "category": "Backpacker Hostel", "price_per_night": 850, "rating": 4.4, "area": "Viman Nagar", "amenities": ["Free WiFi", "AC", "Terrace"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Goodluck Cafe (FC Road)", "cuisine": "Historic Irani Cafe", "average_cost_for_two": 300, "rating": 4.6, "area": "FC Road", "popular_dishes": "Bun Maska with Chai, Keema Ghotala", "is_veg": False},
                {"name": "Vaishali Restaurant", "cuisine": "Iconic South Indian & Snacks", "average_cost_for_two": 350, "rating": 4.7, "area": "FC Road", "popular_dishes": "Mysore Masala Dosa, SPDP (Sev Potato Dahi Puri)", "is_veg": True},
                {"name": "German Bakery", "cuisine": "European Cafe & Bakery", "average_cost_for_two": 800, "rating": 4.5, "area": "Koregaon Park", "popular_dishes": "Apple Strudel, Keema Pav, Cappuccino", "is_veg": False}
            ]
        ),
        make_destination(
            "Lonavala & Khandala", "The Twin Ghat Getaways",
            "Misty Western Ghats hill stations famous for waterfalls, ancient Buddhist rock-cut caves, and crunchy chikki.",
            1900, "Jun–Feb", "2 Days", 4.6, 9.4, "Monsoon Hills & Waterfalls", ["Friends", "Couples", "Family"], "Lonavala",
            ["Tiger's Leap & Sunset Point", "Bhushi Dam Area", "Karla & Bhaja Caves", "Lonavala Market"],
            [
                {"name": "Tiger's Leap (Waghdari)", "category": "Clifftop Viewpoint", "highlight": "650-meter sheer cliff drop with echo point and valley winds", "fee": "Free", "time": "2 hrs"},
                {"name": "Karla & Bhaja Caves", "category": "Buddhist Rock-Cut Caves", "highlight": "2nd-century BC Chaitya prayer halls with carved wooden roof beams", "fee": "₹25", "time": "2.5 hrs"},
                {"name": "Bhushi Dam", "category": "Waterfall Steps", "highlight": "Popular monsoon water cascade overflowing stone steps", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Monsoon Trek to Lohagad Fort", "category": "Fort Trek", "cost": 100, "duration": "3.5 hrs"},
                {"name": "Chikki & Fudge Tasting Trail in Lonavala Bazaar", "category": "Sweet Walk", "cost": 200, "duration": "1 hr"}
            ],
            [
                {"name": "Della Resorts", "category": "Luxury Adventure Resort", "price_per_night": 15000, "rating": 4.7, "area": "Kunegaon", "amenities": ["Adventure Park", "Pool", "Nightclub", "Spa"], "suitability": ["Friends", "Couples", "Family"]},
                {"name": "Fariyas Resort Lonavala", "category": "5-Star Resort", "price_per_night": 9000, "rating": 4.5, "area": "Frichley Hill", "amenities": ["Water Park", "Pool", "Restaurant"], "suitability": ["Family", "Couples"]},
                {"name": "Zostel Plus Lonavala", "category": "Backpacker Resort", "price_per_night": 1200, "rating": 4.6, "area": "Kamshet Lakefront", "amenities": ["Lakefront View", "Infinity Pool", "Dorms"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Maganlal Chikki (Original)", "cuisine": "Iconic Chikki & Fudge", "average_cost_for_two": 250, "rating": 4.8, "area": "Main Market", "popular_dishes": "Crushed Peanut Chikki, Chocolate Walnut Fudge", "is_veg": True},
                {"name": "The Kinara Village Dhaba", "cuisine": "Rustic Dhaba & North Indian", "average_cost_for_two": 850, "rating": 4.4, "area": "Old Mumbai-Pune Highway", "popular_dishes": "Butter Chicken, Paneer Tikka, Tandoori Roti", "is_veg": False}
            ]
        ),
        make_destination(
            "Mahabaleshwar", "The Strawberry Capital of Sahyadris",
            "Lush hill station with strawberry plantations, Venna Lake boating, and viewpoints over deep valleys.",
            2100, "Oct–Jun", "3 Days", 4.7, 9.3, "Hill Station & Strawberry Farms", ["Family", "Couples", "Friends"], "Mahabaleshwar",
            ["Venna Lake & Market", "Panchgani Table Land", "Arthur's Seat & Elphinstone", "Old Kshetra Mahabaleshwar"],
            [
                {"name": "Arthur's Seat (Queen of Points)", "category": "Scenic Cliff Viewpoint", "highlight": "Layered cliff rock formations resembling the Grand Canyon", "fee": "Free", "time": "2 hrs"},
                {"name": "Venna Lake", "category": "Boating Lake", "highlight": "28-acre lake with row boating, horse riding, and corn stalls", "fee": "₹250 (Boat)", "time": "2 hrs"},
                {"name": "Mapro Garden (Panchgani-Mahabaleshwar)", "category": "Agri-Tourism Park", "highlight": "Strawberry fields, chocolate factory, and wood-fired pizza", "fee": "Free", "time": "2.5 hrs"}
            ],
            [
                {"name": "Fresh Strawberry Picking Tour at Local Farms", "category": "Farm Tour", "cost": 250, "duration": "2 hrs"},
                {"name": "Row Boating & Sunset Watch at Venna Lake", "category": "Boating", "cost": 300, "duration": "1 hr"}
            ],
            [
                {"name": "Le Méridien Mahabaleshwar Resort", "category": "Luxury 5-Star Resort", "price_per_night": 18000, "rating": 4.8, "area": "Medha Road", "amenities": ["Infinity Forest Pool", "Spa", "Forest Grounds"], "suitability": ["Couples", "Family"]},
                {"name": "Courtyard by Marriott Mahabaleshwar", "category": "5-Star Resort", "price_per_night": 11000, "rating": 4.7, "area": "Khas-Mahabaleshwar Road", "amenities": ["Valley View", "Pool", "Kids Club"], "suitability": ["Family", "Couples"]},
                {"name": "Zostel Panchgani", "category": "Backpacker Hostel", "price_per_night": 950, "rating": 4.5, "area": "Dandeghar", "amenities": ["Container Architecture", "Valley View", "Cafe"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Mapro Garden Cafe", "cuisine": "Strawberry Delights & Italian", "average_cost_for_two": 700, "rating": 4.7, "area": "Panchgani Road", "popular_dishes": "Fresh Strawberries with Whipped Cream, Foot-long Pizza", "is_veg": True},
                {"name": "Bagicha Corner", "cuisine": "Maharashtrian & Strawberry Shakes", "average_cost_for_two": 450, "rating": 4.5, "area": "Panchgani Road", "popular_dishes": "Fresh Strawberry Shake, Makai Pattice (Corn Cutlet)", "is_veg": True}
            ]
        ),
        make_destination(
            "Nashik", "The Wine Capital of India",
            "Vineyard heartland on the sacred Godavari River, known for wine tastings, Trimbakeshwar Jyotirlinga, and Kumbh lore.",
            1900, "Oct–Mar", "2 Days", 4.7, 9.0, "Wine Tours & Sacred Ghats", ["Couples", "Friends", "Family", "Solo"], "Nashik",
            ["Gangapur Dam & Sula Vineyards", "Panchavati & Godavari Ghats", "Trimbakeshwar Temple Road"],
            [
                {"name": "Sula Vineyards", "category": "Winery & Estate", "highlight": "India's pioneer winery with grape stomping, cellar tours, and tasting room", "fee": "₹500 (Tour+Tasting)", "time": "3.5 hrs"},
                {"name": "Trimbakeshwar Jyotirlinga Temple", "category": "Jyotirlinga Shrine", "highlight": "Ancient temple at the source of River Godavari featuring three-faced linga", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Panchavati & Ramkund", "category": "Sacred Ghats", "highlight": "Holy bathing ghats connected to the Ramayana exile", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Sula Vineyard Winery Tour & Wine Tasting Flight", "category": "Wine Experience", "cost": 500, "duration": "2 hrs"},
                {"name": "Sunset Stargazing & Camping by Gangapur Dam", "category": "Camping", "cost": 1400, "duration": "Overnight"}
            ],
            [
                {"name": "The Source at Sula", "category": "Luxury Vineyard Resort", "price_per_night": 11000, "rating": 4.8, "area": "Sula Vineyards", "amenities": ["Vineyard View Pool", "Wine Bar", "Spa"], "suitability": ["Couples", "Friends"]},
                {"name": "Beyond by Sula", "category": "Luxury Lakefront Villa", "price_per_night": 14000, "rating": 4.8, "area": "Gangapur Dam", "amenities": ["Infinity Pool", "Lake View"], "suitability": ["Couples"]},
                {"name": "Gateway Hotel Ambad Nashik", "category": "5-Star Deluxe", "price_per_night": 7200, "rating": 4.6, "area": "Ambad", "amenities": ["Pool", "Tennis", "Gardens"], "suitability": ["Family", "Business"]}
            ],
            [
                {"name": "Little Italy at Sula", "cuisine": "Italian Fine Dining", "average_cost_for_two": 1500, "rating": 4.6, "area": "Sula Vineyards", "popular_dishes": "Wood-fired Pizza with Sula Dindori Shiraz, Tiramisu", "is_veg": True},
                {"name": "Sadhana Chulivarchi Misal", "cuisine": "Legendary Maharashtrian Misal", "average_cost_for_two": 300, "rating": 4.7, "area": "Gangapur Road", "popular_dishes": "Wood-fire Chulivarchi Spicy Misal Pav, Jalebi", "is_veg": True}
            ]
        ),
        make_destination(
            "Alibaug", "The Coastal Hamptons of Maharashtra",
            "Breezy coastal destination with historic sea forts, quiet coconut groves, water sports, and fresh seafood.",
            2200, "Oct–May", "2 Days", 4.6, 9.0, "Coastal Weekend & Forts", ["Friends", "Couples", "Family"], "Alibaug",
            ["Alibaug Beach & Kolaba Fort", "Nagaon & Akshi Beach", "Kashid Beach", "Mandwa Jetty"],
            [
                {"name": "Kolaba Sea Fort", "category": "Sea Fort", "highlight": "17th-century Shivaji sea fort accessible by walking during low tide", "fee": "₹25", "time": "2 hrs"},
                {"name": "Kashid Beach", "category": "White Sand Beach", "highlight": "Clean white sand beach with water sports against green cliffs", "fee": "Free", "time": "3 hrs"},
                {"name": "Murud-Janjira Fort (Near Alibaug)", "category": "Impregnable Sea Fort", "highlight": "Historic island sea fortress with 572 cannons", "fee": "₹50 (Sailboat)", "time": "3 hrs"}
            ],
            [
                {"name": "Speedboat Transfer from Gateway of India to Mandwa", "category": "Speedboat", "cost": 900, "duration": "20 mins"},
                {"name": "Banana Boat & Bumper Ride at Nagaon Beach", "category": "Water Sports", "cost": 450, "duration": "45 mins"}
            ],
            [
                {"name": "Radisson Blu Resort & Spa Alibaug", "category": "Luxury 5-Star Resort", "price_per_night": 9500, "rating": 4.6, "area": "Gondhalpada", "amenities": ["Huge Pool", "Spa", "Lush Lawns"], "suitability": ["Family", "Couples"]},
                {"name": "Bohemyan Blue Stay", "category": "Boutique Glamping", "price_per_night": 4500, "rating": 4.5, "area": "Mandwa Road", "amenities": ["Glamping Tents", "Pool", "Cafe"], "suitability": ["Couples", "Friends"]},
                {"name": "Zostel Alibaug", "category": "Backpacker Hostel", "price_per_night": 850, "rating": 4.4, "area": "Near Nagaon", "amenities": ["Free WiFi", "Pool", "Open Lawn"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Sanman Restaurant", "cuisine": "Authentic Gomantak Seafood", "average_cost_for_two": 750, "rating": 4.7, "area": "Alibaug City", "popular_dishes": "Surmai Thali, Prawns Masala, Solkadhi", "is_veg": False},
                {"name": "Boardwalk by Flamboyante", "cuisine": "Mediterranean Coastal Dining", "average_cost_for_two": 1800, "rating": 4.6, "area": "Mandwa Jetty", "popular_dishes": "Wood-fired Pizza, Seafood Risotto, Cocktails", "is_veg": False}
            ]
        ),
        make_destination(
            "Chhatrapati Sambhajinagar", "The UNESCO Cave Wonders of Ajanta & Ellora",
            "Gateway to the world's most astonishing rock-cut cave monuments and the Bibi Ka Maqbara (Taj of Deccan).",
            1700, "Oct–Mar", "3 Days", 4.9, 9.5, "UNESCO Rock-cut Wonders", ["Solo", "Family", "Couples", "History Enthusiasts"], "Chhatrapati Sambhajinagar",
            ["Ellora Caves & Khuldabad", "Ajanta Caves Valley", "City Core & Bibi Ka Maqbara", "Daulatabad Fort"],
            [
                {"name": "Kailash Temple (Cave 16, Ellora)", "category": "Monolithic Rock Temple", "highlight": "World's largest monolithic rock excavation carved top-down from single cliff", "fee": "₹40", "time": "3.5 hrs"},
                {"name": "Ajanta Caves (UNESCO)", "category": "Ancient Buddhist Cave Murals", "highlight": "30 rock-cut caves with 2000-year-old Buddhist paintings and frescoes", "fee": "₹40", "time": "4.5 hrs"},
                {"name": "Bibi Ka Maqbara", "category": "Mughal Architecture", "highlight": "1668 marble mausoleum designed by Aurangzeb resembling Taj Mahal", "fee": "₹25", "time": "2 hrs"},
                {"name": "Daulatabad Fort", "category": "Medieval Citadel", "highlight": "Impregnable hilltop fortress with dark subterranean maze (Bhool Bhulaiya)", "fee": "₹25", "time": "3 hrs"}
            ],
            [
                {"name": "Full-day Guided Ellora & Daulatabad Exploration", "category": "Heritage Tour", "cost": 600, "duration": "6 hrs"},
                {"name": "Himroo & Paithani Silk Weaving Workshop Visit", "category": "Crafts Walk", "cost": 0, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Taj Vivanta Aurangabad", "category": "Luxury 5-Star Palace Style", "price_per_night": 8500, "rating": 4.7, "area": "Rauza Baugh", "amenities": ["Palace Lawns", "Pool", "Heritage Decor"], "suitability": ["Couples", "Family"]},
                {"name": "WelcomHotel by ITC Hotels", "category": "5-Star Hotel", "price_per_night": 7200, "rating": 4.6, "area": "Airport Road", "amenities": ["Pool", "Spa", "Free WiFi"], "suitability": ["Family", "Business"]},
                {"name": "Zostel Aurangabad", "category": "Backpacker Hostel", "price_per_night": 750, "rating": 4.4, "area": "Near Station", "amenities": ["Free WiFi", "Tour Desk", "AC Dorms"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Great Sagar Restaurant", "cuisine": "Mughlai & Naan Qalia", "average_cost_for_two": 600, "rating": 4.5, "area": "Buddi Lane", "popular_dishes": "Aurangabad Special Naan Qalia, Mutton Biryani", "is_veg": False},
                {"name": "Bhoj Restaurant", "cuisine": "Authentic Gujarati & Maharashtrian Thali", "average_cost_for_two": 400, "rating": 4.6, "area": "CBS Road", "popular_dishes": "Unlimited Pure Veg Thali, Dal Baati, Shrikhand", "is_veg": True}
            ]
        ),
        make_destination(
            "Ratnagiri", "Alphonso Mangoes & Pristine Konkan Coast",
            "Idyllic Konkan coastal town famed for world-class Alphonso mangoes, Jaigad sea fort, and virgin beaches.",
            1600, "Oct–May", "2 Days", 4.7, 8.6, "Konkan Coast & Mango Orchards", ["Family", "Couples", "Foodies", "Solo"], "Ratnagiri",
            ["Bhatye Beach", "Ganpatipule Beach Core", "Jaigad Fort & Lighthouse", "Ratnadurg Fort"],
            [
                {"name": "Ganpatipule Temple & Beach", "category": "Beach & Temple", "highlight": "400-year-old Ganesha shrine right on the white sand beach", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Ratnadurg Fort & Lighthouse", "category": "Coastal Fort", "highlight": "Horseshoe-shaped coastal fort surrounded on three sides by sea", "fee": "Free", "time": "2 hrs"},
                {"name": "Jaigad Fort & Lighthouse", "category": "Fort Viewpoint", "highlight": "Cliff fortress overlooking the confluence of Shastri River and sea", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Alphonso Mango Orchard Tasting (March–May)", "category": "Agri Tasting", "cost": 300, "duration": "2 hrs"},
                {"name": "Water Sports & Jet Skiing at Ganpatipule Beach", "category": "Water Sports", "cost": 500, "duration": "1 hr"}
            ],
            [
                {"name": "Blue Ocean Resort & Spa (Ganpatipule)", "category": "Luxury Beach Resort", "price_per_night": 7500, "rating": 4.6, "area": "Malgund Beach", "amenities": ["Private Beach", "Infinity Pool", "Spa"], "suitability": ["Couples", "Family"]},
                {"name": "Kohinoor Samudra Beach Resort", "category": "Mid-range Sea Resort", "price_per_night": 4200, "rating": 4.3, "area": "Bhatye Beach", "amenities": ["Cliff View", "Pool", "Restaurant"], "suitability": ["Family", "Couples"]}
            ],
            [
                {"name": "Amantran Restaurant", "cuisine": "Authentic Malvani Seafood", "average_cost_for_two": 600, "rating": 4.7, "area": "Ratnagiri Town", "popular_dishes": "Surmai Fry, Pomfret Thali, Solkadhi, Kombdi Vade", "is_veg": False},
                {"name": "Mehendale's Swaad", "cuisine": "Traditional Konkan Snacks", "average_cost_for_two": 250, "rating": 4.6, "area": "Ganpatipule", "popular_dishes": "Ukadiche Modak, Kaju Usal, Kokum Sharbat", "is_veg": True}
            ]
        )
    ]
}

print("West India dataset loaded with 3 states and 20 destinations.")

"""
Central India Tourism Dataset: Madhya Pradesh, Chhattisgarh.
Rich destinations with authentic neighborhoods, places, activities, hotels, and dining.
"""
from data.regions.common import make_destination

CENTRAL_STATES = {}

# ── 13. Madhya Pradesh ────────────────────────────────────────────────────────
CENTRAL_STATES["Madhya Pradesh"] = {
    "capital": "Bhopal", "region": "Central", "tagline": "The Heart of Incredible India",
    "destinations": [
        make_destination(
            "Khajuraho", "The UNESCO Temples of Love & Erotic Mastery",
            "UNESCO Nagara-style Chandela temple complexes with world-renowned sandstone erotic carvings, Kandariya Mahadeva, and classical dance festivals.",
            1800, "Oct–Mar", "2 Days", 4.9, 9.8, "UNESCO World Heritage & Sculpture Art", ["Couples", "Solo", "Family"], "Khajuraho",
            ["Western Group of Temples", "Eastern Group (Jain)", "Southern Group", "Raneh Falls"],
            [
                {"name": "Western Group of Temples (Kandariya Mahadeva)", "category": "UNESCO Temple Complex", "highlight": "Magnificent sandstone temples with 800+ sculptural figures depicting daily, royal, and sensual celestial life", "fee": "₹40", "time": "3.5 hrs"},
                {"name": "Raneh Falls & Canyon", "category": "Canyon Waterfall", "highlight": "Multi-hued crystalline granite canyon over the Ken river with roaring monsoon cascades", "fee": "₹100", "time": "2 hrs"},
                {"name": "Eastern Group of Jain Temples (Parsvanatha)", "category": "Jain Temples", "highlight": "Intricately detailed figures of women applying kohl, painting feet, and writing letters", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Sound and Light Show at Western Group of Temples", "category": "Light Show", "cost": 250, "duration": "1 hr"},
                {"name": "Bicycle Tour of the Temple Villages & Countryside", "category": "Cycling", "cost": 150, "duration": "2.5 hrs"},
                {"name": "Attending Khajuraho Classical Dance Festival (Feb)", "category": "Classical Dance", "cost": 0, "duration": "3 hrs"}
            ],
            [
                {"name": "The Lalit Temple View Khajuraho", "category": "Luxury 5-Star Hotel", "price_per_night": 9500, "rating": 4.8, "area": "Opposite Circuit House", "amenities": ["Direct Temple Views", "Outdoor Pool", "Rejuve Spa"], "suitability": ["Couples", "Family"]},
                {"name": "Radisson Jass Hotel Khajuraho", "category": "Upscale Resort", "price_per_night": 5500, "rating": 4.5, "area": "By-Pass Road", "amenities": ["Swimming Pool", "Lush Lawns", "Spa"], "suitability": ["Couples", "Family"]},
                {"name": "Zostel Khajuraho", "category": "Backpacker Hostel", "price_per_night": 750, "rating": 4.6, "area": "Jain Temple Road", "amenities": ["Rooftop Cafe", "Courtyard", "Free WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Raja's Cafe", "cuisine": "Swiss-Italian & Indian Breakfast", "average_cost_for_two": 650, "rating": 4.6, "area": "Opposite Western Temples", "popular_dishes": "Woodfired Pizza, Swiss Rosti, Espresso, Temple View", "is_veg": True},
                {"name": "Mediterraneo", "cuisine": "Authentic Italian & Pasta", "average_cost_for_two": 800, "rating": 4.5, "area": "Jain Temple Road", "popular_dishes": "Handmade Gnocchi, Bruschetta, Lasagna", "is_veg": True},
                {"name": "Badri Seth Halwai", "cuisine": "Traditional Sweets & Samosas", "average_cost_for_two": 150, "rating": 4.7, "area": "Main Market", "popular_dishes": "Jalebi with Rabri, Hot Samosa, Chai", "is_veg": True}
            ]
        ),
        make_destination(
            "Pachmarhi", "Queen of the Satpuras & Hill Oasis",
            "Madhya Pradesh's only hill station at 3,500 ft, verdant sal forests, cascading Bee Falls, Jatashankar cave shrine, and Dhoopgarh sunsets.",
            1900, "Oct–Jun", "3 Days", 4.7, 9.4, "Hill Station Nature, Waterfalls & Caves", ["Family", "Couples", "Friends"], "Pachmarhi",
            ["Dhoopgarh", "Bee Falls", "Jatashankar Caves", "Pandav Caves", "Chauragarh"],
            [
                {"name": "Dhoopgarh (Highest Peak in Satpura)", "category": "Summit Viewpoint", "highlight": "Highest point in MP (4,429 ft) with spellbinding 360-degree sunrise and sunset vistas", "fee": "Free", "time": "2 hrs"},
                {"name": "Bee Falls (Jamuna Prapat)", "category": "Plunge Waterfall", "highlight": "115-ft sparkling cascade surrounded by steep cliffs and natural swimming pools", "fee": "₹20", "time": "2.5 hrs"},
                {"name": "Jatashankar & Mahadeo Cave Temples", "category": "Sacred Rock Caverns", "highlight": "Natural stalactite limestone caves resembling the matted dreadlocks of Lord Shiva", "fee": "Free", "time": "2 hrs"},
                {"name": "Chauragarh Peak & Trishul Sanctuary", "category": "Pilgrimage Ridge", "highlight": "1,300-step hike to hilltop shrine where devotees carry colossal steel tridents", "fee": "Free", "time": "4 hrs"}
            ],
            [
                {"name": "Open 4x4 Gypsy Safari across Satpura National Park Forest", "category": "Forest Safari", "cost": 2500, "duration": "4 hrs"},
                {"name": "Trekking down to the Plunge Pool of Bee Falls", "category": "Waterfall Trek", "cost": 0, "duration": "2.5 hrs"},
                {"name": "Sunset Stargazing from Dhoopgarh Plateau", "category": "Sunset Leisure", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "WelcomHeritage Golf View Pachmarhi", "category": "Colonial Heritage Luxury", "price_per_night": 7500, "rating": 4.6, "area": "Golf Course Road", "amenities": ["Victorian Decor", "Golf Course", "Fine Dining"], "suitability": ["Couples", "Family"]},
                {"name": "MPT Glen View (MP Tourism)", "category": "Forest Retreat", "price_per_night": 4200, "rating": 4.4, "area": "Mall Road", "amenities": ["Pine Gardens", "Ayurvedic Massages", "Restaurant"], "suitability": ["Family", "Couples"]},
                {"name": "Hotel Pandav Pachmarhi", "category": "Comfort Hill Stay", "price_per_night": 2200, "rating": 4.1, "area": "Near Bus Stand", "amenities": ["Restaurant", "WiFi", "Travel Desk"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "MPT Glen View Restaurant", "cuisine": "Traditional North Indian & MP Thali", "average_cost_for_two": 600, "rating": 4.4, "area": "Mall Road", "popular_dishes": "Bhutte ka Kees, Dal Bafla, Paneer Tikka", "is_veg": True},
                {"name": "Chunmun Cottage Restaurant", "cuisine": "Multi-Cuisine Vegetarian", "average_cost_for_two": 500, "rating": 4.3, "area": "Near Golf Course", "popular_dishes": "Dum Aloo, Veg Biryani, Gulab Jamun", "is_veg": True},
                {"name": "Pachmarhi Chaat Chowk", "cuisine": "Hillside Street Chaat", "average_cost_for_two": 200, "rating": 4.5, "area": "Near Subhash Park", "popular_dishes": "Pani Puri, Aloo Tikki, Hot Masala Doodh", "is_veg": True}
            ]
        ),
        make_destination(
            "Kanha & Bandhavgarh", "The Real Jungle Book & Tiger Havens",
            "Mowgli's inspiring sal forests, highest tiger density in India at Bandhavgarh, magnificent barasingha swamp deer, and open Jeep safaris.",
            3500, "Oct–Jun", "3 Days", 4.9, 9.9, "Wildlife Safaris & Tiger Tracking", ["Couples", "Family", "Adventure"], "Mandla",
            ["Kanha Meadows & Mukki Zone", "Bandhavgarh Tala Zone", "Bandhavgarh Fort Hill", "Khatia Gate"],
            [
                {"name": "Kanha National Park Core (Mukki / Kanha)", "category": "Premier Tiger Reserve", "highlight": "Expansive green meadows, bamboo thickets, barasingha deer, and royal tigers", "fee": "₹2500 (Safari)", "time": "4.5 hrs"},
                {"name": "Bandhavgarh Tiger Reserve (Tala Zone)", "category": "Highest Tiger Density", "highlight": "Ancient sal forest where royal tigers roam among 2,000-year-old rock sculptures", "fee": "₹2500 (Safari)", "time": "4.5 hrs"},
                {"name": "Shesh Shaiya (Reclining Vishnu Statue)", "category": "Ancient Monolithic Sculpture", "highlight": "35-ft 10th-century reclining stone Vishnu under 7-headed serpent canopy in deep forest", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Early Morning Open-Top 4x4 Tiger Safari", "category": "Wildlife Safari", "cost": 4500, "duration": "4.5 hrs"},
                {"name": "Night Safari at Forest Buffer Zones", "category": "Night Safari", "cost": 3000, "duration": "3 hrs"},
                {"name": "Baiga Tribal Village Cultural Tour", "category": "Tribal Heritage", "cost": 400, "duration": "2 hrs"}
            ],
            [
                {"name": "Taj Banjaar Tola, Kanha", "category": "Luxury 5-Star Tented Suites", "price_per_night": 32000, "rating": 5.0, "area": "Mukki Gate, Kanha", "amenities": ["River Banjaar Overlook", "Private Plunge Pools", "Naturalist Safaris"], "suitability": ["Couples", "Family"]},
                {"name": "Mahua Kothi, Bandhavgarh (Taj)", "category": "Luxury 5-Star Safari Lodge", "price_per_night": 35000, "rating": 5.0, "area": "Tala Gate, Bandhavgarh", "amenities": ["Mud Kutiyas", "Yoga", "Campfire Bush Dinners"], "suitability": ["Couples"]},
                {"name": "Wild Chalet Resort Kanha", "category": "Eco Riverside Lodge", "price_per_night": 5500, "rating": 4.6, "area": "Mocha Village, Khatia", "amenities": ["Riverfront Lawn", "Naturalist Walks", "Bonfires"], "suitability": ["Family", "Friends"]}
            ],
            [
                {"name": "Banjaar Tola Dining Pavilion", "cuisine": "Gourmet Bush Dining & Indian", "average_cost_for_two": 3500, "rating": 4.9, "area": "Mukki Gate", "popular_dishes": "Wild Mushroom Curry, Roasted Chicken, Baiga Breads", "is_veg": False},
                {"name": "Tiger's Den Canteen", "cuisine": "Rustic North Indian & Thali", "average_cost_for_two": 600, "rating": 4.4, "area": "Tala Village, Bandhavgarh", "popular_dishes": "Dal Tadka, Chicken Curry, Jeera Rice, Tandoori Roti", "is_veg": False},
                {"name": "Mocha Village Dhaba", "cuisine": "Highway Dhaba", "average_cost_for_two": 350, "rating": 4.3, "area": "Kanha Highway", "popular_dishes": "Sev Tamatar, Kadhi Pakora, Tandoori Roti", "is_veg": True}
            ]
        ),
        make_destination(
            "Ujjain", "The Eternal City of Mahakal & Kumbh Mela",
            "One of the sacred 12 Jyotirlingas—Mahakaleshwar with its early morning Bhasma Aarti, Ram Ghat on the Shipra river, and Mahakal Lok corridor.",
            1500, "Oct–Mar", "2 Days", 4.8, 9.8, "Sacred Jyotirlinga & Timekeeping Hub", ["Family", "Senior Citizens", "Solo"], "Ujjain",
            ["Mahakal Mandir & Lok Corridor", "Ram Ghat & Shipra River", "Kal Bhairav Temple", "Harsiddhi Mandir"],
            [
                {"name": "Mahakaleshwar Jyotirlinga Temple", "category": "Sacred Dakshinmukhi Jyotirlinga", "highlight": "Only south-facing Jyotirlinga famous for the dawn Bhasma Aarti with sacred ash", "fee": "Free", "time": "3 hrs"},
                {"name": "Shri Mahakal Lok Corridor", "category": "Grand Devotional Corridor", "highlight": "900-meter majestic corridor flanked by 108 grand stone pillars and Shiva murals", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Kal Bhairav Temple", "category": "Unique Tantric Sanctum", "highlight": "Ancient temple where deity mysteriously drinks liquor offerings directly from clay bowls", "fee": "Free", "time": "1.5 hrs"},
                {"name": "Ram Ghat on River Shipra", "category": "Holy Bathing Ghat", "highlight": "Historic ghat of Simhastha Kumbh Mela with evening Shipra Aarti and lamps", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Attending the 4:00 AM Bhasma Aarti at Mahakaleshwar", "category": "Spiritual Ritual", "cost": 200, "duration": "3 hrs"},
                {"name": "Shipra River Evening Deep Daan Aarti at Ram Ghat", "category": "Spiritual Aarti", "cost": 0, "duration": "1.5 hrs"},
                {"name": "Stroll across the Illuminated Mahakal Lok Corridor at Night", "category": "Corridor Walk", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "Anjushree Hotel Ujjain", "category": "Luxury 5-Star Hotel", "price_per_night": 6500, "rating": 4.6, "area": "Indore Road", "amenities": ["Outdoor Pool", "Pure Veg Gourmet", "Spa"], "suitability": ["Couples", "Family"]},
                {"name": "Hotel Rudraksh Club & Resort", "category": "Upscale Leisure Resort", "price_per_night": 5200, "rating": 4.5, "area": "Indore-Ujjain Highway", "amenities": ["Pool", "Gardens", "Vegetarian Dining"], "suitability": ["Family", "Senior Citizens"]},
                {"name": "Hotel Imperial Grand", "category": "City Pilgrim Stay", "price_per_night": 2400, "rating": 4.2, "area": "Near Station / Mahakal", "amenities": ["Vegetarian Restaurant", "AC", "WiFi"], "suitability": ["Solo", "Family"]}
            ],
            [
                {"name": "Shree Ganga Restaurant", "cuisine": "Pure Sattvic Malwi & Gujarati Thali", "average_cost_for_two": 450, "rating": 4.6, "area": "Near Mahakal Temple", "popular_dishes": "Dal Bafla Thali, Sev Tamatar, Malpua", "is_veg": True},
                {"name": "Mahakal Bhojnalaya (Temple Annakshetra)", "cuisine": "Blessed Temple Prasad Meal", "average_cost_for_two": 0, "rating": 4.9, "area": "Inside Mahakal Complex", "popular_dishes": "Holy Prasad Khichdi, Puri Sabzi, Kheer", "is_veg": True},
                {"name": "Bhole Guru Poha Chaat", "cuisine": "Malwi Breakfast Legend", "average_cost_for_two": 120, "rating": 4.8, "area": "Freeganj", "popular_dishes": "Usal Poha with Sev & Jeeravan, Jalebi", "is_veg": True}
            ]
        ),
        make_destination(
            "Gwalior & Orchha", "The Fort of Citadels & The Ram Raja Palace",
            "Mighty Gwalior Fort on basalt rock, Jai Vilas crystal palace, combined with Orchha's medieval Bundela cenotaphs and Ram Raja Temple.",
            1900, "Oct–Mar", "3 Days", 4.8, 9.6, "Bundela & Scindia Royal Heritage", ["Couples", "Family", "Solo"], "Gwalior",
            ["Gwalior Fort & Man Mandir", "Jai Vilas Palace", "Orchha Fort Complex", "Chhatris on Betwa River"],
            [
                {"name": "Gwalior Fort (Pearl in Necklace of Forts)", "category": "Mighty Hill Citadel", "highlight": "8th-century cliff fortress with turquoise-tile Man Mandir palace and rock Jain colossi", "fee": "₹75", "time": "3.5 hrs"},
                {"name": "Jai Vilas Palace & Scindia Museum", "category": "European Royal Palace", "highlight": "400-room palace with world's largest chandeliers and silver miniature train delivering cigars", "fee": "₹300", "time": "2.5 hrs"},
                {"name": "Orchha Fort & Jahangir Mahal", "category": "Bundela Palace Architecture", "highlight": "Stunning blend of Mughal-Rajput palaces overlooking dense teak jungle", "fee": "₹50", "time": "3 hrs"},
                {"name": "Ram Raja Temple & Betwa Chhatris (Orchha)", "category": "Sacred Temple & Cenotaphs", "highlight": "Only temple where Lord Ram is worshipped as a reigning King with police gun salute", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Gwalior Fort Sound and Light Show in Man Mandir Courtyard", "category": "Sound & Light", "cost": 100, "duration": "1 hr"},
                {"name": "Kayaking and Rafting on the Betwa River (Orchha)", "category": "River Kayaking", "cost": 600, "duration": "1.5 hrs"},
                {"name": "Heritage Walk among 14 Chhatris along Betwa Riverbank", "category": "Heritage Walk", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "Taj Usha Kiran Palace, Gwalior", "category": "Luxury 5-Star Heritage Palace", "price_per_night": 14000, "rating": 4.9, "area": "Jayendraganj", "amenities": ["Palace Courtyards", "Jiva Spa", "Billiards"], "suitability": ["Couples", "Family"]},
                {"name": "Amar Mahal, Orchha", "category": "Bundela Heritage Palace Hotel", "price_per_night": 6500, "rating": 4.7, "area": "Betwa River Bank", "amenities": ["Fort Views", "Pool", "Spa", "Lush Lawns"], "suitability": ["Couples", "Family"]},
                {"name": "Hotel Sheesh Mahal (MPT Orchha)", "category": "Fort Stay Heritage", "price_per_night": 3200, "rating": 4.3, "area": "Inside Orchha Fort Complex", "amenities": ["Stay inside Royal Fort Palace", "Courtyard Dining"], "suitability": ["Couples", "Solo"]}
            ],
            [
                {"name": "Silver Saloon (Taj Usha Kiran Palace)", "cuisine": "Royal Maratha & Nepalese Cuisine", "average_cost_for_two": 2500, "rating": 4.8, "area": "Jayendraganj", "popular_dishes": "Maratha Mutton Sukka, Shahi Paneer, Dal Moradabadi", "is_veg": False},
                {"name": "SS Kachori Wala", "cuisine": "Legendary Gwalior Breakfast", "average_cost_for_two": 150, "rating": 4.8, "area": "Naya Bazaar", "popular_dishes": "Crispy Urad Dal Kachori with Tangy Aloo Sabzi", "is_veg": True},
                {"name": "Betwa Tarang (Orchha)", "cuisine": "Rooftop Bundelkhandi & Global", "average_cost_for_two": 600, "rating": 4.5, "area": "Main Market, Orchha", "popular_dishes": "Dal Bafla, Woodfired Pizza, Cold Beer with Fort View", "is_veg": True}
            ]
        )
    ]
}

# ── 5. Chhattisgarh ───────────────────────────────────────────────────────────
CENTRAL_STATES["Chhattisgarh"] = {
    "capital": "Raipur", "region": "Central", "tagline": "Full of Surprises & The Niagara of India",
    "destinations": [
        make_destination(
            "Chitrakote Falls & Bastar", "The Niagara of India & Tribal Bastar",
            "India's widest waterfall plunging 100 ft in a 980-ft horseshoe across the Indravati river, bell-metal Dhokra crafts, and sacred tribal groves.",
            1600, "Jul–Feb", "3 Days", 4.8, 9.5, "Waterfalls, Indigenous Art & Eco-Tourism", ["Friends", "Couples", "Adventure", "Solo"], "Jagdalpur",
            ["Chitrakote Horseshoe Falls", "Kanger Valley National Park", "Kutumsar Limestone Caves", "Tirathgarh Falls"],
            [
                {"name": "Chitrakote Falls (Indravati River)", "category": "Horseshoe Waterfall", "highlight": "Spectacular 980-ft wide horseshoe waterfall illuminated with changing color lights at night", "fee": "Free", "time": "3 hrs"},
                {"name": "Tirathgarh Waterfalls", "category": "Tiered Forest Cascade", "highlight": "White milky 300-ft multi-tiered cascade inside dense sal forest of Kanger Valley", "fee": "₹25", "time": "2.5 hrs"},
                {"name": "Kutumsar Limestone Caves", "category": "Subterranean Stalactite Caves", "highlight": "Dark 330-meter subterranean cave with rare blind fish and natural limestone Shivalingas", "fee": "₹50", "time": "2 hrs"},
                {"name": "Bastar Tribal Craft Markets (Dhokra)", "category": "Indus Metalcraft Village", "highlight": "Ancient 4,000-year-old lost-wax bronze and bell metal casting craft villages", "fee": "Free", "time": "2.5 hrs"}
            ],
            [
                {"name": "Country Wooden Boat Ride to the Base of Chitrakote Mist", "category": "Boat Adventure", "cost": 150, "duration": "1 hr"},
                {"name": "Spelunking and Caving in Kutumsar with Carbide Torches", "category": "Caving Adventure", "cost": 100, "duration": "2 hrs"},
                {"name": "Dhokra Lost-Wax Bell Metal Craft Workshop", "category": "Artisan Craft", "cost": 300, "duration": "2.5 hrs"}
            ],
            [
                {"name": "Dandami Luxury Resort Chitrakote", "category": "Cottages Overlooking Waterfall", "price_per_night": 4500, "rating": 4.6, "area": "Chitrakote Cliff Edge", "amenities": ["Direct Waterfall Views", "Restaurant", "Gardens"], "suitability": ["Couples", "Family"]},
                {"name": "Bastar Jungle Resort", "category": "Eco Tribal Retreat", "price_per_night": 3200, "rating": 4.4, "area": "Kurandi Village / Jagdalpur", "amenities": ["Mud Cottages", "Bonfires", "Tribal Folk Dance"], "suitability": ["Friends", "Family"]},
                {"name": "Hotel Rainbow Jagdalpur", "category": "Comfort City Stay", "price_per_night": 1800, "rating": 4.1, "area": "Near Bus Stand Jagdalpur", "amenities": ["AC", "Restaurant", "WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Dandami Resort Restaurant", "cuisine": "Authentic Chhattisgarhi & North Indian", "average_cost_for_two": 500, "rating": 4.4, "area": "Chitrakote Falls", "popular_dishes": "Chila, Fara, Badi Sabzi, Country Chicken Curry", "is_veg": False},
                {"name": "Bastar Haat Food Stalls", "cuisine": "Traditional Indigenous Tribal", "average_cost_for_two": 200, "rating": 4.6, "area": "Tokapal / Jagdalpur Haat", "popular_dishes": "Chaprah (Red Ant Chutney), Mahua Drink, Rice Beer, Roasted Fish", "is_veg": False},
                {"name": "Aamantran Restaurant", "cuisine": "Vegetarian Thali & South Indian", "average_cost_for_two": 350, "rating": 4.2, "area": "Jagdalpur Main Road", "popular_dishes": "Chhattisgarhi Thali, Masala Dosa, Dal Fry", "is_veg": True}
            ]
        ),
        make_destination(
            "Mainpat", "The Shimla of Chhattisgarh & Tibetan Colony",
            "Lush green plateau at 3,600 ft, Tibetan Buddhist monastery with chanting monks, unique bouncing earth (Jaljali), and Tiger Point falls.",
            1500, "Oct–Mar", "2 Days", 4.6, 8.8, "Highland Tibetan Settlement & Natural Oddities", ["Solo", "Couples", "Friends"], "Ambikapur",
            ["Dhakpo Shedrupling Monastery", "Jaljali (Bouncing Land)", "Tiger Point Waterfall", "Fish Point Falls"],
            [
                {"name": "Dhakpo Shedrupling Tibetan Monastery", "category": "Tibetan Buddhist Temple", "highlight": "Serene monastery built by Tibetan refugees in 1962 with golden Buddha and prayer flags", "fee": "Free", "time": "2 hrs"},
                {"name": "Jaljali (The Bouncing Land)", "category": "Geological Curiosity", "highlight": "Spongy, trembling earth where jumping on the ground creates bouncing ripples underfoot", "fee": "Free", "time": "1.5 hrs"},
                {"name": "Tiger Point & Fish Point Waterfalls", "category": "Forest Waterfalls", "highlight": "60-meter roar plunging into deep wooded canyons once frequented by tigers", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Experiencing the Trampoline-Like Bouncing Earth at Jaljali", "category": "Natural Oddity", "cost": 0, "duration": "1.5 hrs"},
                {"name": "Attending Morning Tibetan Chanting at the Monastery", "category": "Spiritual Chanting", "cost": 0, "duration": "1.5 hrs"},
                {"name": "Tasting Authentic Tibetan Momos in Mainpat Camps", "category": "Culinary Trail", "cost": 150, "duration": "1 hr"}
            ],
            [
                {"name": "Saila Tourist Resort Mainpat (CG Tourism)", "category": "Hilltop Cottage Resort", "price_per_night": 2800, "rating": 4.3, "area": "Ropkhar / Mainpat", "amenities": ["Valley Views", "Restaurant", "Pine Lawns"], "suitability": ["Couples", "Family"]},
                {"name": "Mercury Tents Mainpat", "category": "Glamping Resort", "price_per_night": 3200, "rating": 4.2, "area": "Tiger Point Road", "amenities": ["Swiss Tents", "Bonfires", "Adventure Sports"], "suitability": ["Friends", "Couples"]},
                {"name": "Tibetan Settlement Guesthouse", "category": "Peaceful Guesthouse", "price_per_night": 1200, "rating": 4.4, "area": "Camp No 1", "amenities": ["Clean Rooms", "Home Cooked Tibetan Food"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Tibetan Camp No 1 Eatery", "cuisine": "Authentic Tibetan Momos & Thukpa", "average_cost_for_two": 250, "rating": 4.7, "area": "Camp No 1 Mainpat", "popular_dishes": "Steamed Pork/Chicken Momos, Veg Thukpa, Tingmo", "is_veg": False},
                {"name": "Saila Resort Restaurant", "cuisine": "North Indian & Chhattisgarhi", "average_cost_for_two": 450, "rating": 4.1, "area": "Inside Saila Resort", "popular_dishes": "Chila with Chutney, Dal Tadka, Aloo Paratha", "is_veg": True},
                {"name": "Tiger Point Maggie & Tea Stalls", "cuisine": "Comfort Viewpoint Snacks", "average_cost_for_two": 150, "rating": 4.5, "area": "Tiger Point View", "popular_dishes": "Pahadi Maggi, Sweet Corn, Ginger Masala Chai", "is_veg": True}
            ]
        ),
        make_destination(
            "Raipur & Sirpur", "Ancient Buddhist Capital & Capital Heritage",
            "Excavated 5th-8th century CE international Buddhist monastic city of Sirpur, Laxman brick temple, and Vivekananda Sarovar in modern Raipur.",
            1800, "Oct–Mar", "2 Days", 4.6, 9.0, "Ancient Buddhist Archaeology & Capital Culture", ["Family", "Solo", "Business"], "Raipur",
            ["Sirpur Monastic Ruins", "Laxman Brick Temple", "Swami Vivekananda Sarovar", "Purkhauti Muktangan"],
            [
                {"name": "Sirpur Group of Monuments (UNESCO Tentative)", "category": "Ancient Monastic City", "highlight": "Over 100 excavated Buddhist viharas, underground market complex, and Shiva shrines", "fee": "₹25", "time": "3.5 hrs"},
                {"name": "Laxman Temple (Sirpur)", "category": "7th-Century Brick Masterpiece", "highlight": "One of India's finest surviving red brick temples with ornate erotic carvings and Vishnu avatar pillars", "fee": "₹25", "time": "2 hrs"},
                {"name": "Purkhauti Muktangan (Naya Raipur)", "category": "Open-Air Cultural Eco Museum", "highlight": "Vast 200-acre open-air museum displaying live tribal habitats, crafts, and folk statues", "fee": "₹30", "time": "2.5 hrs"},
                {"name": "Swami Vivekananda Sarovar (Budha Talab)", "category": "Scenic Lake & Colossal Statue", "highlight": "Huge natural lake with a record 37-ft bronze statue of Swami Vivekananda in meditation", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Guided Walk through Surang Tila & Anand Prabhu Vihara in Sirpur", "category": "Archaeology Tour", "cost": 200, "duration": "2.5 hrs"},
                {"name": "Boating and Musical Fountain at Vivekananda Sarovar", "category": "Lake Boating", "cost": 100, "duration": "1.5 hrs"},
                {"name": "Traditional Bell Metal & Kosa Silk Shopping in Raipur", "category": "Shopping", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "Courtyard by Marriott Raipur", "category": "Luxury 5-Star Hotel", "price_per_night": 7500, "rating": 4.7, "area": "NH-6 Labhandi", "amenities": ["Outdoor Pool", "Spa", "International Dining"], "suitability": ["Couples", "Family", "Business"]},
                {"name": "MPT Hi-Way Treat Sirpur (CG Tourism)", "category": "Heritage Transit Lodge", "price_per_night": 2200, "rating": 4.2, "area": "Near Sirpur Monuments", "amenities": ["Lawns", "Restaurant", "Archaeology Proximity"], "suitability": ["Solo", "Family"]},
                {"name": "Babylon Hotel Raipur", "category": "Upscale Business Hotel", "price_per_night": 3800, "rating": 4.3, "area": "VIP Road", "amenities": ["Gym", "Restaurant", "Free WiFi"], "suitability": ["Business", "Solo"]}
            ],
            [
                {"name": "Mocha Cafe & Bar", "cuisine": "Continental, Italian & Cafe", "average_cost_for_two": 1100, "rating": 4.6, "area": "VIP Road", "popular_dishes": "Woodfired Pizza, Mezze Platter, Mocktails", "is_veg": False},
                {"name": "Gadh Kalwa (Traditional Chhattisgarhi Kitchen)", "cuisine": "Authentic State Delicacy Kitchen", "average_cost_for_two": 300, "rating": 4.7, "area": "Telibandha Lake", "popular_dishes": "Chila, Fara, Dubki Kadi, Thetthari, Khurmi", "is_veg": True},
                {"name": "Hi-Way Treat Restaurant Sirpur", "cuisine": "North Indian & Thali", "average_cost_for_two": 400, "rating": 4.2, "area": "Sirpur Site", "popular_dishes": "Chhattisgarhi Dal Bhaat, Aloo Gobi, Roti", "is_veg": True}
            ]
        ),
        make_destination(
            "Barnawapara Wildlife Sanctuary", "Teak Wilderness & Flying Squirrel Haven",
            "Dense teak, sal, and bamboo forest teeming with wild bison (gaur), leopards, sloth bears, and giant flying squirrels.",
            1600, "Nov–Jun", "2 Days", 4.6, 8.7, "Wilderness & Wildlife Safaris", ["Family", "Wildlife Enthusiasts", "Friends"], "Mahasamund",
            ["Barnawapara Gate", "Balamdehi Riverbank", "Pakshi Vihar"],
            [
                {"name": "Barnawapara Wildlife Safari", "category": "Forest Safari", "highlight": "Thick sal jungle home to high populations of Indian bison, wild boar, and barking deer", "fee": "₹1200 (Gypsy)", "time": "3.5 hrs"},
                {"name": "Balamdehi River & Jonk River Confluence", "category": "River Boundary", "highlight": "Scenic freshwater river boundary where animals drink at dusk", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Open 4x4 Gypsy Wildlife Safari through Teak Forest", "category": "Jeep Safari", "cost": 1500, "duration": "3.5 hrs"},
                {"name": "Nocturnal Jungle Birding & Flying Squirrel Watching", "category": "Night Safari", "cost": 500, "duration": "2 hrs"}
            ],
            [
                {"name": "Hareli Eco Resort Barnawapara (CG Tourism)", "category": "Eco Jungle Resort", "price_per_night": 3200, "rating": 4.4, "area": "Barnawapara Gate", "amenities": ["Forest Cottages", "Restaurant", "Safari Desk"], "suitability": ["Family", "Friends"]},
                {"name": "Moha Eco Cottages", "category": "Rustic Forest Stay", "price_per_night": 1800, "rating": 4.1, "area": "Mahasamund Fringe", "amenities": ["Campfires", "Home Cooked Meals"], "suitability": ["Friends", "Solo"]}
            ],
            [
                {"name": "Hareli Resort Canteen", "cuisine": "Traditional Chhattisgarhi & North Indian", "average_cost_for_two": 450, "rating": 4.3, "area": "Inside Hareli Resort", "popular_dishes": "Desi Chicken Curry, Rice, Chila, Dal", "is_veg": False},
                {"name": "Balamdehi Forest Dhaba", "cuisine": "Rustic Highway Meals", "average_cost_for_two": 300, "rating": 4.2, "area": "Sanctuary Approach Road", "popular_dishes": "Sev Tamatar, Roti, Kheer", "is_veg": True}
            ]
        )
    ]
}

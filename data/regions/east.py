"""
East India Tourism Dataset: Bihar, Jharkhand, Odisha, West Bengal.
Rich destinations with authentic neighborhoods, places, activities, hotels, and dining.
"""
from data.regions.common import make_destination

EAST_STATES = {}

# ── 4. Bihar ──────────────────────────────────────────────────────────────────
EAST_STATES["Bihar"] = {
    "capital": "Patna", "region": "East", "tagline": "The Cradle of Buddhism & Ancient Wisdom",
    "destinations": [
        make_destination(
            "Bodh Gaya", "The Seat of Buddha's Enlightenment",
            "UNESCO Mahabodhi Temple, the sacred Bodhi Tree where Siddhartha Gautama attained supreme awakening, and international monasteries.",
            1500, "Oct–Mar", "2 Days", 4.9, 9.8, "Spiritual Enlightenment & World Heritage", ["Solo", "Family", "Couples"], "Gaya",
            ["Mahabodhi Temple Complex", "Japanese & Thai Monasteries", "Bodhi Tree", "Sujata Village"],
            [
                {"name": "Mahabodhi Temple & Sacred Bodhi Tree", "category": "UNESCO World Heritage Site", "highlight": "Ancient stone temple and direct descendant of the tree where Lord Buddha was enlightened", "fee": "Free", "time": "3 hrs"},
                {"name": "The Great Buddha Statue (80 ft)", "category": "Giant Buddhist Icon", "highlight": "Towering 80-foot red granite Buddha statue sculpted in meditation dhyan posture", "fee": "Free", "time": "1 hr"},
                {"name": "Thai & Royal Bhutan Monasteries", "category": "International Architecture", "highlight": "Elaborate gilded Thai pagoda and Bhutanese clay frescoes", "fee": "Free", "time": "2 hrs"},
                {"name": "Dungeshwari (Mahakala) Cave Temples", "category": "Meditation Caves", "highlight": "Cliff caves where Gautama practiced 6 years of intense asceticism before Bodh Gaya", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Morning Walking Meditation around Mahabodhi Stupa", "category": "Meditation", "cost": 0, "duration": "1.5 hrs"},
                {"name": "International Monastery Architectural Walking Tour", "category": "Architecture Walk", "cost": 0, "duration": "2.5 hrs"},
                {"name": "Excursion across Falgu River to Sujata Kuti", "category": "Historical Walk", "cost": 100, "duration": "2 hrs"}
            ],
            [
                {"name": "Maha Bodhi Hotel Resort & Convention Centre", "category": "Luxury 4-Star Pilgrim Resort", "price_per_night": 6500, "rating": 4.6, "area": "Hariharpur", "amenities": ["Outdoor Pool", "Ayurvedic Spa", "Zen Gardens"], "suitability": ["Couples", "Family"]},
                {"name": "Marasa Sarovar Premiere Bodhgaya", "category": "Boutique Architecture Hotel", "price_per_night": 5200, "rating": 4.5, "area": "Near Kalachakra Maidan", "amenities": ["Buddhist Architectural Water Bodies", "Spa", "Dining"], "suitability": ["Couples", "Family"]},
                {"name": "Root Institute Guesthouse", "category": "Spiritual Meditation Retreat", "price_per_night": 1500, "rating": 4.7, "area": "Near Tibetan Monastery", "amenities": ["Quiet Gardens", "Vegetarian Food", "Yoga Hall"], "suitability": ["Solo", "Couples"]}
            ],
            [
                {"name": "Sujata Cafe", "cuisine": "Multi-Cuisine Tibetan, Italian & Indian", "average_cost_for_two": 500, "rating": 4.6, "area": "Opposite Tibetan Monastery", "popular_dishes": "Woodfired Thin Crust Pizza, Thukpa, Lemon Ginger Tea", "is_veg": True},
                {"name": "Be Happy Cafe", "cuisine": "Organic Bakery & Italian", "average_cost_for_two": 600, "rating": 4.7, "area": "Kalachakra Ground", "popular_dishes": "Thin Crust Pizza, Apple Pie with Ice Cream, Filter Coffee", "is_veg": True},
                {"name": "Hari Om International Cafe", "cuisine": "Tibetan & Continental Breakfast", "average_cost_for_two": 400, "rating": 4.4, "area": "Main Road", "popular_dishes": "Steamed Momos, Banana Pancake, Herbal Teas", "is_veg": True}
            ]
        ),
        make_destination(
            "Nalanda", "The World's First Residential University",
            "UNESCO excavated ruins of the 5th-century CE Nalanda Mahavihara where 10,000 global scholars studied, and Hiuen Tsang Memorial.",
            1400, "Oct–Mar", "1 Day", 4.8, 9.4, "Ancient Academic Heritage & Archaeology", ["Family", "Solo", "Couples"], "Nalanda",
            ["Excavated Ruins Complex", "Archaeological Museum", "Hiuen Tsang Memorial", "Kundalpur"],
            [
                {"name": "Nalanda Mahavihara Ruins (UNESCO)", "category": "Ancient University", "highlight": "Staggering red-brick monastery cells, votive stupas, and ancient classroom ruins", "fee": "₹40", "time": "3 hrs"},
                {"name": "Nalanda Archaeological Museum", "category": "Artifacts Museum", "highlight": "Rare Pala bronze sculptures, terracotta seals, and ancient carved stone idols", "fee": "₹20", "time": "1.5 hrs"},
                {"name": "Xuanzang (Hiuen Tsang) Memorial Hall", "category": "Indo-Chinese Memorial", "highlight": "Majestic hall celebrating the 7th-century Chinese monk traveler who studied here", "fee": "₹25", "time": "1.5 hrs"}
            ],
            [
                {"name": "Guided Archaeology Walk through Monastic Cellblocks", "category": "Archaeology Tour", "cost": 250, "duration": "2.5 hrs"},
                {"name": "Visiting Kundalpur Jain Digambar Shrines", "category": "Pilgrimage", "cost": 0, "duration": "1.5 hrs"},
                {"name": "Tasting Famous Silao Khaja Sweet", "category": "Culinary Heritage", "cost": 100, "duration": "1 hr"}
            ],
            [
                {"name": "The Nalanda Heritage Hotel", "category": "Comfort Transit Stay", "price_per_night": 2800, "rating": 4.2, "area": "Nalanda Barlia", "amenities": ["Restaurant", "WiFi", "Lawn"], "suitability": ["Family", "Solo"]},
                {"name": "Hotel Indo Hokke (Rajgir proximity)", "category": "Japanese Hospitality Hotel", "price_per_night": 4800, "rating": 4.4, "area": "Near Rajgir Highway", "amenities": ["Japanese Bath", "Lotus Restaurant", "Zen Gardens"], "suitability": ["Couples", "Family"]},
                {"name": "Gautam Residency", "category": "Budget Traveler Stay", "price_per_night": 1400, "rating": 4.0, "area": "Near University Gate", "amenities": ["Room Service", "AC"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Silao Khaja Sweet Shops (Silao)", "cuisine": "GI-Tagged Crispy Pastry Sweet", "average_cost_for_two": 150, "rating": 4.8, "area": "Silao Market", "popular_dishes": "Original Silao Ka Khaja, Chena Sweets", "is_veg": True},
                {"name": "Lotus Restaurant (Indo Hokke)", "cuisine": "Japanese & Indian Vegetarian", "average_cost_for_two": 900, "rating": 4.5, "area": "Rajgir-Nalanda Road", "popular_dishes": "Japanese Rice Bowl, Tempura, Dal Tadka", "is_veg": True},
                {"name": "Nalanda Highway Green Restaurant", "cuisine": "Bihari & North Indian Thali", "average_cost_for_two": 400, "rating": 4.2, "area": "NH-31", "popular_dishes": "Litti Chokha, Sattu Paratha, Bihari Thali", "is_veg": True}
            ]
        ),
        make_destination(
            "Rajgir", "The Ancient Magadha Capital & Vulture Peak",
            "Surrounded by seven green hills, aerial chairlift ropeway to Vishwa Shanti Stupa, Vulture Peak (Gridhrakuta), and sulfur hot springs.",
            1600, "Oct–Mar", "2 Days", 4.7, 9.2, "Hill Valleys & Multi-Faith Pilgrimage", ["Family", "Couples", "Senior Citizens"], "Rajgir",
            ["Ratnagiri Hill & Ropeway", "Venuvana Monastery", "Brahmakund Springs", "Ghora Katora Lake"],
            [
                {"name": "Vishwa Shanti Stupa & Ropeway", "category": "Peace Stupa & Chairlift", "highlight": "White marble Peace Pagoda atop Ratnagiri hill reached by iconic single-chair ropeway", "fee": "₹100 (Ropeway)", "time": "2 hrs"},
                {"name": "Gridhrakuta Peak (Vulture Peak)", "category": "Sacred Buddhist Hill", "highlight": "Rock promontory where Lord Buddha preached the Lotus Sutra and Heart Sutra", "fee": "Free", "time": "2 hrs"},
                {"name": "Ghora Katora Lake", "category": "Eco Lake & Giant Buddha", "highlight": "Pristine natural valley lake with a colossal pink sandstone Buddha in center", "fee": "₹50 (Tongas)", "time": "2.5 hrs"},
                {"name": "Brahmakund Thermal Hot Springs", "category": "Natural Mineral Springs", "highlight": "Spiritual natural hot water spouts emerging at foot of Vaibhava hill", "fee": "Free", "time": "1 hr"}
            ],
            [
                {"name": "Single-Chair Ropeway Ride over Rajgir Pine Slopes", "category": "Aerial Adventure", "cost": 100, "duration": "45 mins"},
                {"name": "Horse Carriage (Tonga) Ride to Ghora Katora Lake", "category": "Eco Ride", "cost": 300, "duration": "2 hrs"},
                {"name": "Glass Bridge Skywalk at Rajgir Nature Safari", "category": "Skywalk Adventure", "cost": 250, "duration": "2 hrs"}
            ],
            [
                {"name": "The Rajgir Residency", "category": "Upscale Resort Hotel", "price_per_night": 5500, "rating": 4.4, "area": "Kund Market Road", "amenities": ["Indoor Pool", "Sauna", "Multi-Cuisine Dining"], "suitability": ["Couples", "Family"]},
                {"name": "Pandu Pokhar Eco Camp Resort", "category": "Eco Adventure Stay", "price_per_night": 3200, "rating": 4.3, "area": "Pandu Pokhar", "amenities": ["Boating", "Gardens", "Outdoor Games"], "suitability": ["Family", "Friends"]},
                {"name": "Hotel Goroomgo Rajgir", "category": "Budget Pilgrim Stay", "price_per_night": 1200, "rating": 4.0, "area": "Station Road", "amenities": ["Free WiFi", "AC"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Gharana Restaurant", "cuisine": "Bihari, North Indian & Chinese", "average_cost_for_two": 600, "rating": 4.4, "area": "Main Road", "popular_dishes": "Litti Chokha with Ghee, Paneer Butter Masala, Gulab Jamun", "is_veg": True},
                {"name": "Pandu Pokhar Food Court", "cuisine": "Fast Food & Snacks", "average_cost_for_two": 350, "rating": 4.2, "area": "Inside Pandu Pokhar", "popular_dishes": "Chaat, Dosa, Masala Chai, Ice Cream", "is_veg": True},
                {"name": "Green Hotel & Restaurant", "cuisine": "Pure Veg Thali", "average_cost_for_two": 300, "rating": 4.1, "area": "Kund Market", "popular_dishes": "Bihari Thali, Sattu Drink, Poori Sabzi", "is_veg": True}
            ]
        ),
        make_destination(
            "Patna", "Ancient Pataliputra on the Banks of Ganga",
            "Historic capital of Ashoka and Maurya Empire, sacred Takht Sri Patna Sahib gurudwara, Golghar granary, and Bihar Museum.",
            1800, "Oct–Mar", "2 Days", 4.6, 9.0, "Maurya History & Sikh Spiritual Seat", ["Family", "Solo", "Business"], "Patna",
            ["Takht Patna Sahib", "Ganga Riverfront & Ghats", "Bailey Road Museums", "Frazer Road"],
            [
                {"name": "Takht Sri Patna Sahib", "category": "Sikh Temporal Throne", "highlight": "Birthplace of 10th Sikh Guru Sri Guru Gobind Singh Ji built by Maharaja Ranjit Singh", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Bihar Museum", "category": "World-Class Heritage Museum", "highlight": "State-of-the-art museum housing the 2,300-year-old Didarganj Yakshi polished statue", "fee": "₹100", "time": "3 hrs"},
                {"name": "Golghar", "category": "Colonial Beehive Granary", "highlight": "Massive 1786 dome granary offering spiral stairway panoramic view over the Ganga", "fee": "₹10", "time": "1.5 hrs"},
                {"name": "Kumhrar Ancient Mauryan Ruins", "category": "Archaeological Park", "highlight": "80-pillared sandstone hypostyle hall remnants of Emperor Ashoka's capital", "fee": "₹15", "time": "1.5 hrs"}
            ],
            [
                {"name": "Evening Ganga Aarti at NIT Ghat Patna", "category": "Spiritual Aarti", "cost": 0, "duration": "1.5 hrs"},
                {"name": "Curated Tour of Didarganj Yakshi in Bihar Museum", "category": "Museum Tour", "cost": 100, "duration": "2.5 hrs"},
                {"name": "Street Food Exploration of Patna Litti Chokha", "category": "Culinary Trail", "cost": 150, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Maurya Hotel Patna", "category": "Luxury 5-Star Heritage Hotel", "price_per_night": 8500, "rating": 4.7, "area": "Fraser Road, South Gandhi Maidan", "amenities": ["Outdoor Pool", "Vaishali Cafe", "Spacious Lawns"], "suitability": ["Couples", "Family", "Business"]},
                {"name": "Lemon Tree Premier Patna", "category": "Upscale Business Hotel", "price_per_night": 6800, "rating": 4.6, "area": "Exhibition Road", "amenities": ["Rooftop Pool", "Spa", "Fitness Centre"], "suitability": ["Business", "Family"]},
                {"name": "Hotel Patliputra Nirvana", "category": "Comfort Mid-Range", "price_per_night": 2800, "rating": 4.2, "area": "Buddha Marg", "amenities": ["Restaurant", "WiFi", "AC"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Maurya Lok Litti Chokha Corner", "cuisine": "Authentic Charcoal-Roasted Litti", "average_cost_for_two": 180, "rating": 4.8, "area": "Maurya Lok Complex", "popular_dishes": "Litti Dipped in Desi Ghee with Baingan Chokha & Chutneys", "is_veg": True},
                {"name": "Bansi Vihar", "cuisine": "South Indian & Sweets Legend", "average_cost_for_two": 450, "rating": 4.6, "area": "Fraser Road", "popular_dishes": "Ghee Butter Masala Dosa, Filter Coffee, Idli Vada", "is_veg": True},
                {"name": "Pind Balluchi (Revolving Restaurant)", "cuisine": "Punjabi & North Indian", "average_cost_for_two": 1100, "rating": 4.4, "area": "Biscomaun Bhawan 18th Floor", "popular_dishes": "Murgh Pind Se, Dal Makhani, Panoramic Ganga View", "is_veg": False}
            ]
        )
    ]
}

# ── 10. Jharkhand ─────────────────────────────────────────────────────────────
EAST_STATES["Jharkhand"] = {
    "capital": "Ranchi", "region": "East", "tagline": "The Land of Forests & Majestic Waterfalls",
    "destinations": [
        make_destination(
            "Ranchi", "The City of Waterfalls & Tribal Heart",
            "Surrounded by Hundru, Dassam, and Jonha roaring waterfalls, sacred hilltop Pahari Mandir, and rich tribal craft traditions.",
            1700, "Oct–Mar", "2 Days", 4.6, 9.1, "Waterfalls, Hills & Tribal Culture", ["Friends", "Family", "Couples"], "Ranchi",
            ["Hundru & Dassam Falls", "Pahari Mandir", "Kanke Dam & Rock Garden", "Tagore Hill"],
            [
                {"name": "Hundru Falls", "category": "Spectacular Waterfall", "highlight": "Subarnarekha River falling 320 feet over rugged metamorphic rock cliffs", "fee": "₹20", "time": "2.5 hrs"},
                {"name": "Dassam Falls (Dassong)", "category": "Natural Cascade", "highlight": "Kanchi river plunging 144 feet in 10 clear streams into emerald pools", "fee": "₹20", "time": "2.5 hrs"},
                {"name": "Rock Garden & Kanke Dam", "category": "Sculpture Park & Lake", "highlight": "Artfully sculpted rock terraces on Kanke lake with sunset views", "fee": "₹30", "time": "2 hrs"},
                {"name": "Tagore Hill (Morabadi)", "category": "Literary Hilltop Shrine", "highlight": "Hill retreat of Rabindranath Tagore's brother Jyotirindranath with city vistas", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Waterfall Trekking and Rock Scrambling at Hundru", "category": "Adventure Trek", "cost": 0, "duration": "3 hrs"},
                {"name": "Boating and Sunset Viewing at Kanke Dam", "category": "Lake Boating", "cost": 150, "duration": "1.5 hrs"},
                {"name": "Tribal Handicrafts Shopping at Jharcraft Showrooms", "category": "Handicrafts", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "Radisson Blu Hotel Ranchi", "category": "Luxury 5-Star Hotel", "price_per_night": 7500, "rating": 4.7, "area": "Kadru Diversion Road", "amenities": ["Outdoor Pool", "Spa", "Great Kabab Factory"], "suitability": ["Couples", "Family", "Business"]},
                {"name": "Chanakya BNR Hotel", "category": "Heritage Railway Hotel", "price_per_night": 4200, "rating": 4.4, "area": "Station Road", "amenities": ["British Colonial Heritage", "Lawns", "Dining"], "suitability": ["Couples", "Family"]},
                {"name": "Hotel Green Acres", "category": "Comfort Boutique Stay", "price_per_night": 2400, "rating": 4.2, "area": "Hinoo / Airport Road", "amenities": ["Free Airport Pickup", "WiFi", "Restaurant"], "suitability": ["Business", "Solo"]}
            ],
            [
                {"name": "The Great Kabab Factory (Radisson)", "cuisine": "Gourmet Kebabs & Biryani", "average_cost_for_two": 1800, "rating": 4.7, "area": "Kadru Road", "popular_dishes": "Galouti Kebab, Biryani, Dal Makhani", "is_veg": False},
                {"name": "Kaveri Restaurant", "cuisine": "Vegetarian North Indian & Thali", "average_cost_for_two": 550, "rating": 4.5, "area": "Main Road", "popular_dishes": "Special Kaveri Thali, Paneer Butter Masala, Masala Dosa", "is_veg": True},
                {"name": "Dhuska & Chana Ghoogni Stalls", "cuisine": "Traditional Jharkhand Breakfast", "average_cost_for_two": 120, "rating": 4.8, "area": "Morabadi Ground", "popular_dishes": "Hot Dhuska with Black Chana Curry, Samosa Chaat", "is_veg": True}
            ]
        ),
        make_destination(
            "Netarhat", "Queen of Chotanagpur & Magnolia Sunset",
            "Misty hill plateau at 3,700 ft amidst dense sal, pine, and eucalyptus forests, famed for mesmerizing sunrise and sunset points.",
            1500, "Year-round", "2 Days", 4.7, 8.8, "Highland Forest & Sunrise Haven", ["Couples", "Solo", "Friends"], "Netarhat",
            ["Magnolia Sunset Point", "Koel View Point", "Lower Ghaghri Falls", "Pine Forest"],
            [
                {"name": "Magnolia Sunset Point", "category": "Romantic Sunset Vista", "highlight": "Fabled cliff edge named after a British maiden overlooking deep violet valleys", "fee": "Free", "time": "2 hrs"},
                {"name": "Koel River Viewpoint", "category": "Sunrise Point", "highlight": "Watch the golden sun emerge above the snaking Koel river and mist-draped hills", "fee": "Free", "time": "1.5 hrs"},
                {"name": "Lower Ghaghri Falls", "category": "Forest Waterfall", "highlight": "320-ft secluded waterfall hidden inside a dense canopy of sal woods", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Netarhat Pine & Eucalyptus Forests", "category": "Alpine Woodlands", "highlight": "Fragrant pine trees planted during British era with walking trails", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Sunrise Stargazing to Dawn at Koel Viewpoint", "category": "Sunrise View", "cost": 0, "duration": "2 hrs"},
                {"name": "Forest Trek to Upper & Lower Ghaghri Falls", "category": "Nature Trek", "cost": 0, "duration": "3 hrs"},
                {"name": "Campfire and Barbecue on the Plateau", "category": "Campfire", "cost": 400, "duration": "Evening"}
            ],
            [
                {"name": "Prabhat Vihar (Jharkhand Tourism)", "category": "Plateau Viewpoint Lodge", "price_per_night": 2200, "rating": 4.3, "area": "Sunrise Point Road", "amenities": ["Valley Views", "Dining Hall", "Gardens"], "suitability": ["Couples", "Family"]},
                {"name": "Hotel Forest View", "category": "Cozy Pine Stay", "price_per_night": 1600, "rating": 4.1, "area": "Netarhat Forest Fringe", "amenities": ["Campfire", "Restaurant", "Balconies"], "suitability": ["Friends", "Solo"]},
                {"name": "Nature Safari Camp Netarhat", "category": "Eco Glamping Tents", "price_per_night": 2800, "rating": 4.4, "area": "Plateau Ridge", "amenities": ["Swiss Tents", "Bonfires", "Guided Treks"], "suitability": ["Couples", "Friends"]}
            ],
            [
                {"name": "Prabhat Vihar Dining Hall", "cuisine": "Traditional Indian & Bengali", "average_cost_for_two": 450, "rating": 4.2, "area": "Near Sunrise Point", "popular_dishes": "Jharkhand Mutton Curry, Dal Fry, Jeera Rice", "is_veg": False},
                {"name": "Pine View Dhaba", "cuisine": "Comfort Mountain Food", "average_cost_for_two": 300, "rating": 4.3, "area": "Main Chowk", "popular_dishes": "Aloo Parathas, Maggi, Masala Tea, Hot Pakoras", "is_veg": True},
                {"name": "Tribal Flavours Kitchen", "cuisine": "Indigenous Jharkhandi Cuisine", "average_cost_for_two": 400, "rating": 4.5, "area": "Netarhat Market", "popular_dishes": "Dhuska, Bamboo Shoot Curry, Pittha", "is_veg": True}
            ]
        ),
        make_destination(
            "Deoghar (Baidyanath Dham)", "One of the Sacred 12 Jyotirlingas",
            "Revered Baba Baidyanath Jyotirlinga, millions of Kanwariyas during Shravani Mela, Trikuta Parvat ropeway, and Nandan Pahar.",
            1400, "Oct–Mar", "2 Days", 4.8, 9.4, "Holy Jyotirlinga Pilgrimage", ["Family", "Senior Citizens", "Solo"], "Deoghar",
            ["Baba Baidyanath Mandir Complex", "Trikuta Parvat (Trikut Hill)", "Naulakha Mandir", "Tapovan Caves"],
            [
                {"name": "Baba Baidyanath Temple (Jyotirlinga)", "category": "Sacred Jyotirlinga Shrine", "highlight": "Ancient stone temple topped with gold punchshula where Ravana worshipped Shiva", "fee": "Free", "time": "3 hrs"},
                {"name": "Trikuta Parvat (Trikut Hills)", "category": "Triple Peak Hill & Caves", "highlight": "Holy three-peaked mountain with sage Valmiki caves and panoramic viewpoints", "fee": "Free", "time": "3 hrs"},
                {"name": "Naulakha Mandir", "category": "Radha Krishna Temple", "highlight": "146-ft temple resembling Belur Math built with 9 lakh rupees donation in 1940", "fee": "Free", "time": "1.5 hrs"},
                {"name": "Tapovan Caves & Shivalinga", "category": "Meditation Rock Caves", "highlight": "Granite boulders where Sage Valmiki meditated, home to playful monkeys", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Morning VIP Sparsh Darshan at Baba Baidyanath", "category": "Spiritual Ritual", "cost": 250, "duration": "2 hrs"},
                {"name": "Trikuta Hill Nature Trek & Cave Exploration", "category": "Hill Trek", "cost": 0, "duration": "3 hrs"},
                {"name": "Deoghar Peda Tasting in Temple Alleys", "category": "Culinary Tradition", "cost": 150, "duration": "1 hr"}
            ],
            [
                {"name": "Hotel Imperial Deoghar", "category": "Comfort 3-Star Pilgrim Stay", "price_per_night": 2800, "rating": 4.3, "area": "Clock Tower Road", "amenities": ["Pure Veg Restaurant", "WiFi", "AC"], "suitability": ["Family", "Senior Citizens"]},
                {"name": "Hotel Mahadev Palace", "category": "Comfort Stay", "price_per_night": 2200, "rating": 4.2, "area": "Castairs Town", "amenities": ["Restaurant", "Elevator", "Room Service"], "suitability": ["Family", "Solo"]},
                {"name": "GenX Baidyanath Hotel", "category": "Modern Pilgrim Hotel", "price_per_night": 3200, "rating": 4.3, "area": "T.B. Sanatorium Road", "amenities": ["Banquet", "Veg Dining", "WiFi"], "suitability": ["Family", "Business"]}
            ],
            [
                {"name": "Baidyanath Peda Bhandar", "cuisine": "World Famous Khoya Pedas", "average_cost_for_two": 200, "rating": 4.9, "area": "Temple Bada Bazaar", "popular_dishes": "Pure Mawa Peda, Belgrami, Rabri", "is_veg": True},
                {"name": "Mayur Restaurant", "cuisine": "Pure Sattvic Vegetarian Thali", "average_cost_for_two": 450, "rating": 4.5, "area": "Castairs Town", "popular_dishes": "North Indian Thali, Paneer Kadhai, Poori Sabzi", "is_veg": True},
                {"name": "Karnibad Vegetarian Kitchen", "cuisine": "North Indian & South Indian", "average_cost_for_two": 350, "rating": 4.2, "area": "Court Road", "popular_dishes": "Masala Dosa, Chole Bhature, Gulab Jamun", "is_veg": True}
            ]
        ),
        make_destination(
            "Betla National Park & Palamu Forts", "Wilderness & Twin 16th-Century Fortresses",
            "One of India's earliest tiger reserves, wild elephants, sloth bears, waterfalls, and ruined 16th-century forts of Chero kings hidden in dense jungle.",
            2200, "Nov–Apr", "2 Days", 4.6, 8.7, "Jungle Wildlife & Lost Fort Ruins", ["Friends", "Adventure", "Couples"], "Daltonganj",
            ["Betla Safari Forest", "Old & New Palamu Forts", "Kechki River Confluence", "Kamaldah Lake"],
            [
                {"name": "Betla National Park Safari", "category": "Wildlife Tiger Reserve", "highlight": "Sal and bamboo forest inhabited by wild elephants, gaurs, leopards, and chital", "fee": "₹1500 (Jeep)", "time": "3.5 hrs"},
                {"name": "Palamu Twin Forts (Purana & Naya Qila)", "category": "Mughal & Chero Jungle Forts", "highlight": "Hauntingly beautiful stone fortresses deep inside the jungle with grand Nagpuri gate", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Kechki Sangam (Auranga & Koel Rivers)", "category": "River Confluence", "highlight": "Picturesque boulder river confluence where Satyajit Ray filmed Days and Nights in the Forest", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Open Jeep Wildlife Safari into Betla Wilderness", "category": "Jeep Safari", "cost": 1500, "duration": "3.5 hrs"},
                {"name": "Exploration of Jungle Ruins of Palamu Forts", "category": "Heritage Jungle Trek", "cost": 0, "duration": "2.5 hrs"},
                {"name": "Riverside Bird Watching at Kechki Sangam", "category": "Birdwatching", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "Van Vihar (Jharkhand Tourism Betla)", "category": "Forest Edge Lodge", "price_per_night": 2400, "rating": 4.3, "area": "Betla Gate", "amenities": ["Forest Views", "Safari Booking Help", "Dining"], "suitability": ["Adventure", "Family"]},
                {"name": "Betla Forest Rest House", "category": "Colonial Forest Bungalow", "price_per_night": 1800, "rating": 4.2, "area": "Inside Reserve", "amenities": ["Wilderness Setting", "Home Cooked Meals"], "suitability": ["Adventure", "Friends"]},
                {"name": "Hotel Kamlesh", "category": "Transit Hotel", "price_per_night": 1400, "rating": 3.9, "area": "Daltonganj Highway", "amenities": ["AC", "Restaurant"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Van Vihar Canteen", "cuisine": "Rustic North Indian & Jharkhand Thali", "average_cost_for_two": 400, "rating": 4.2, "area": "Betla Park Gate", "popular_dishes": "Country Chicken Curry, Dal Bhaat, Aloo Bhujia", "is_veg": False},
                {"name": "Kechki Riverside Dhaba", "cuisine": "Highway Dhaba", "average_cost_for_two": 300, "rating": 4.4, "area": "Near Kechki Bridge", "popular_dishes": "Fried River Fish, Sattu Paratha, Masala Chai", "is_veg": False},
                {"name": "Betla Jungle Point Canteen", "cuisine": "Snacks & Comfort Food", "average_cost_for_two": 250, "rating": 4.0, "area": "Near Main Gate", "popular_dishes": "Egg Curry, Rice, Poori Sabzi", "is_veg": False}
            ]
        )
    ]
}

# ── 19. Odisha ────────────────────────────────────────────────────────────────
EAST_STATES["Odisha"] = {
    "capital": "Bhubaneswar", "region": "East", "tagline": "India's Best Kept Secret",
    "destinations": [
        make_destination(
            "Puri", "The Holy Abode of Lord Jagannath & Golden Sands",
            "The monumental Jagannath Temple, the eternal chariot festival (Rath Yatra), holy Mahaprasad, and Blue Flag golden beaches.",
            1900, "Oct–Mar", "3 Days", 4.9, 9.8, "Sacred Pilgrimage & Coastal Relaxation", ["Family", "Couples", "Solo", "Senior Citizens"], "Puri",
            ["Jagannath Temple Complex", "Golden Beach & Blue Flag Beach", "Swargadwar", "Chilika Sea Mouth"],
            [
                {"name": "Shri Jagannath Temple", "category": "Char Dham Sanctum", "highlight": "12th-century towering stone temple with mystery flag flying against the wind and world's largest kitchen", "fee": "Free", "time": "3 hrs"},
                {"name": "Puri Blue Flag Golden Beach", "category": "Certified Clean Beach", "highlight": "Pristine, clean golden sand beach with safe swimming zones and seaside boardwalk", "fee": "₹20", "time": "2 hrs"},
                {"name": "Raghurajpur Heritage Craft Village", "category": "UNESCO Craft Village", "highlight": "Every household creates breathtaking Pattachitra scroll paintings and palm leaf etchings", "fee": "Free", "time": "3 hrs"},
                {"name": "Swargadwar Beach Market", "category": "Vibrant Night Market", "highlight": "Bustling coastal market with fried fish stalls, shell crafts, and Odia sweets", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Tasting Sacred Anandabazar Mahaprasad (56 Bhog)", "category": "Temple Culinary Blessing", "cost": 150, "duration": "1.5 hrs"},
                {"name": "Pattachitra Painting Workshop in Raghurajpur", "category": "Artisan Craft", "cost": 300, "duration": "2.5 hrs"},
                {"name": "Morning Sunrise Walk & Bath at Golden Beach", "category": "Coastal Leisure", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "Mayfair Waves Puri", "category": "Luxury 5-Star Beach Resort", "price_per_night": 12000, "rating": 4.8, "area": "Chakratirtha Road", "amenities": ["Oceanfront Pool", "Spa", "Private Beach Access"], "suitability": ["Couples", "Family"]},
                {"name": "The Hans Coco Palms", "category": "Colonial Heritage Beach Resort", "price_per_night": 6500, "rating": 4.5, "area": "Swargadwar Beach", "amenities": ["Palm Groves", "Pool", "Ocean Dining"], "suitability": ["Family", "Couples"]},
                {"name": "Zostel Puri", "category": "Boutique Coastal Hostel", "price_per_night": 850, "rating": 4.6, "area": "VIP Road", "amenities": ["Rooftop Cafe", "Sea Breeze Deck", "WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Ananda Bazar (Jagannath Temple)", "cuisine": "World's Oldest Sacred Mahaprasad", "average_cost_for_two": 200, "rating": 4.9, "area": "Inside Jagannath Temple", "popular_dishes": "Khaja, Kanika Pulao, Dalma, Mahaprasad Pot", "is_veg": True},
                {"name": "Wildgrass Restaurant", "cuisine": "Traditional Authentic Odia Seafood", "average_cost_for_two": 900, "rating": 4.7, "area": "VIP Road", "popular_dishes": "Chingudi Malai Curry, Macha Besara, Dalma with Rice", "is_veg": False},
                {"name": "Chung Wah Chinese Restaurant", "cuisine": "Heritage Indo-Chinese", "average_cost_for_two": 750, "rating": 4.4, "area": "VIP Road", "popular_dishes": "Crispy Prawns, Chilli Chicken, Hakka Noodles", "is_veg": False}
            ]
        ),
        make_destination(
            "Konark", "The Sun Temple & The Chariot of the Gods",
            "UNESCO 13th-century Sun Temple designed as a colossal stone chariot with 24 carved wheels, and serene Chandrabhaga surf beach.",
            1700, "Oct–Mar", "1 Day", 4.9, 9.7, "UNESCO Stone Architecture & Surf Beach", ["Couples", "Family", "Solo"], "Konark",
            ["Sun Temple Complex", "Chandrabhaga Beach", "Konark Museum", "Marine Drive"],
            [
                {"name": "Konark Sun Temple (Black Pagoda)", "category": "UNESCO World Heritage Site", "highlight": "Colossal chariot temple carved with exquisite erotic sculptures, dancers, and sundials", "fee": "₹40", "time": "3 hrs"},
                {"name": "Chandrabhaga Beach", "category": "Pristine Surfing Beach", "highlight": "Blue Flag beach famous for breathtaking sunrises and annual Magha Saptami festival", "fee": "Free", "time": "2 hrs"},
                {"name": "Konark Archaeological Museum", "category": "Sculpture Gallery", "highlight": "Houses 860 master sculptures fallen from the ruined main sanctum spire", "fee": "₹15", "time": "1.5 hrs"}
            ],
            [
                {"name": "Evening Musical Sound and Light Show at Sun Temple", "category": "Sound & Light", "cost": 100, "duration": "1 hr"},
                {"name": "Surfing and Stand-up Paddleboarding at Chandrabhaga", "category": "Surf Sport", "cost": 1200, "duration": "2 hrs"},
                {"name": "Marine Drive Scenic Drive between Puri and Konark", "category": "Coastal Drive", "cost": 0, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Lotus Resort Konark (Eco Cottage)", "category": "Lakeside Eco Resort", "price_per_night": 5800, "rating": 4.6, "area": "Chandrabhaga / Marine Drive", "amenities": ["Kushabhadra River Confluence", "Wooden Cottages", "Ayurvedic Spa"], "suitability": ["Couples", "Family"]},
                {"name": "Yatri Nivas (Odisha Tourism)", "category": "Heritage Comfort Stay", "price_per_night": 2200, "rating": 4.2, "area": "Near Sun Temple", "amenities": ["Gardens", "Restaurant", "Parking"], "suitability": ["Family", "Senior Citizens"]},
                {"name": "Surfer's Surf Lodge", "category": "Beach Shack Lodge", "price_per_night": 1500, "rating": 4.5, "area": "Chandrabhaga Beach", "amenities": ["Surf Equipment", "Campfires", "Cafe"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Kamath Restaurant (Yatri Nivas)", "cuisine": "Vegetarian Odia & South Indian", "average_cost_for_two": 450, "rating": 4.3, "area": "Near Sun Temple", "popular_dishes": "Odia Veg Thali, Dalma, Poori Bhaji, Filter Coffee", "is_veg": True},
                {"name": "Sun Temple Waterfront Restaurant", "cuisine": "Fresh Coastal Seafood & Odia", "average_cost_for_two": 700, "rating": 4.4, "area": "Marine Drive", "popular_dishes": "Crab Curry, Fried Pomfret, Prawn Masala", "is_veg": False},
                {"name": "Chandrabhaga Shacks", "cuisine": "Beach Snacks & Green Coconuts", "average_cost_for_two": 150, "rating": 4.5, "area": "Beachfront", "popular_dishes": "Fresh Tender Coconut, Fried Prawns, Tea", "is_veg": False}
            ]
        ),
        make_destination(
            "Bhubaneswar", "The Temple City of India & Smart Capital",
            "Over 700 ancient stone temples including Lingaraj and Mukteshvara, Udayagiri & Khandagiri Jain caves, and Nandankanan white tigers.",
            2000, "Oct–Mar", "2 Days", 4.7, 9.4, "Ancient Kalinga Architecture & Modern Capital", ["Family", "Solo", "Couples"], "Bhubaneswar",
            ["Old Town Temple Enclave", "Udayagiri & Khandagiri Caves", "Nandankanan Zoo", "Janpath & Saheed Nagar"],
            [
                {"name": "Lingaraj Temple", "category": "Kalinga Architectural Crown", "highlight": "11th-century 180-ft red sandstone temple sanctum dedicated to Harihara (Shiva-Vishnu)", "fee": "Free", "time": "2 hrs"},
                {"name": "Mukteshvara Temple & Torana", "category": "Gem of Odishan Architecture", "highlight": "Exquisitely carved 10th-century arched gateway torana with celestial dancers", "fee": "Free", "time": "1.5 hrs"},
                {"name": "Udayagiri & Khandagiri Rock-Cut Caves", "category": "Jain Monastic Caves", "highlight": "2nd-century BCE rock caves including Hathigumpha containing Emperor Kharavela's edict", "fee": "₹25", "time": "2.5 hrs"},
                {"name": "Nandankanan Zoological Park", "category": "Wildlife Sanctuary", "highlight": "World-famous zoo for breeding white tigers and open safari through natural sal jungle", "fee": "₹50", "time": "3.5 hrs"}
            ],
            [
                {"name": "Ekamra Walks (Guided Old Town Temple Trail)", "category": "Heritage Walk", "cost": 0, "duration": "2.5 hrs"},
                {"name": "White Tiger Safari & Botanical Walk at Nandankanan", "category": "Safari Tour", "cost": 150, "duration": "3 hrs"},
                {"name": "Shopping for Sambalpuri Silk & Silver Filigree (Tarakasi)", "category": "Artisan Craft", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "Mayfair Lagoon, Bhubaneswar", "category": "Luxury 5-Star Eco Resort", "price_per_night": 11000, "rating": 4.9, "area": "Jaydev Vihar", "amenities": ["Private Lagoon", "Villas", "Multiple Award-Winning Restaurants"], "suitability": ["Couples", "Family", "Business"]},
                {"name": "Welcomhotel by ITC Hotels, Bhubaneswar", "category": "Modern Luxury 5-Star", "price_per_night": 8500, "rating": 4.7, "area": "Dumduma", "amenities": ["Infinity Pool", "Kaya Kalp Spa", "Gourmet Dining"], "suitability": ["Family", "Business"]},
                {"name": "Ginger Bhubaneswar", "category": "Smart Budget Stay", "price_per_night": 2600, "rating": 4.1, "area": "Nayapalli", "amenities": ["Free WiFi", "Cafe", "Gym"], "suitability": ["Solo", "Business"]}
            ],
            [
                {"name": "Odiyan / Kanika (Mayfair Lagoon)", "cuisine": "Royal Authentic Odia Cuisine", "average_cost_for_two": 2200, "rating": 4.8, "area": "Jaydev Vihar", "popular_dishes": "Kankada Jhola (Crab Curry), Chingudi Malai, Chhena Poda", "is_veg": False},
                {"name": "Truptee Restaurant", "cuisine": "Vegetarian Odia & North Indian", "average_cost_for_two": 500, "rating": 4.5, "area": "Laxmi Sagar", "popular_dishes": "Dalma with Steamed Rice, Pakhala Thali, Chhena Gaja", "is_veg": True},
                {"name": "Dahi Bara Aloodum Stalls (Master Canteen)", "cuisine": "Iconic Cuttack-Odia Street Food", "average_cost_for_two": 100, "rating": 4.9, "area": "Master Canteen Square", "popular_dishes": "Dahi Bara Aloodum with Ghugni, Sev & Coriander Chutney", "is_veg": True}
            ]
        ),
        make_destination(
            "Chilika Lake (Mangalajodi & Satapada)", "Asia's Largest Brackish Water Lagoon",
            "Over a million migratory birds from Siberia, rare Irrawaddy dolphins at Satapada sea mouth, and picturesque Kalijai island shrine.",
            2200, "Nov–Feb", "2 Days", 4.8, 9.5, "Birdwatching, Wetlands & Dolphin Safaris", ["Family", "Couples", "Friends"], "Balugaon",
            ["Mangalajodi Bird Haven", "Satapada Dolphin Point", "Kalijai Island", "Barkul"],
            [
                {"name": "Satapada Dolphin Sanctuary", "category": "Marine Dolphin Lagoon", "highlight": "Scenic boat cruise spotting elusive Irrawaddy dolphins breaching near the sea mouth", "fee": "₹1500 (Boat)", "time": "3.5 hrs"},
                {"name": "Mangalajodi Wetland Eco-Village", "category": "Global Birdwatching Haven", "highlight": "Poachers-turned-protectors rowing silent wooden boats within inches of rare Siberian birds", "fee": "₹1200 (Boat)", "time": "3 hrs"},
                {"name": "Kalijai Island & Temple", "category": "Island Shrine", "highlight": "Sacred island temple sitting in the middle of blue waters worshipped by local fishermen", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Country Boat Birdwatching Safari in Mangalajodi", "category": "Birdwatching Safari", "cost": 1200, "duration": "3 hrs"},
                {"name": "Speedboat Cruise to Chilika Sea Mouth & Dolphin Point", "category": "Dolphin Cruise", "cost": 1500, "duration": "3 hrs"},
                {"name": "Fresh Lake Crab & Jumbo Prawn Tasting", "category": "Culinary Feast", "cost": 600, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Swosti Chilika Resort", "category": "Luxury 5-Star Eco Resort", "price_per_night": 12500, "rating": 4.8, "area": "Pathara / Chilika Lake", "amenities": ["Lakefront Infinity Pool", "Water Sports", "Ayurvedic Spa"], "suitability": ["Couples", "Family"]},
                {"name": "OTDC Panthanivas Barkul", "category": "Lakeside Tourism Stay", "price_per_night": 2500, "rating": 4.2, "area": "Barkul Jetty", "amenities": ["Lake Views", "Boat Jetty Access", "Odia Restaurant"], "suitability": ["Family", "Couples"]},
                {"name": "Mangalajodi Eco Cottages", "category": "Community Eco Village", "price_per_night": 1800, "rating": 4.6, "area": "Mangalajodi Village", "amenities": ["Community Lodges", "Expert Bird Guides", "Home Cooked Meals"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Chilika Dhaba (Barkul)", "cuisine": "Fresh Lagoon Seafood", "average_cost_for_two": 800, "rating": 4.7, "area": "NH-16 near Barkul", "popular_dishes": "Giant Chilika Prawn Roast, Crab Masala, Fried Bhetki", "is_veg": False},
                {"name": "Panthanivas Restaurant Barkul", "cuisine": "Odia Fish Curry & Rice", "average_cost_for_two": 500, "rating": 4.3, "area": "Barkul Jetty", "popular_dishes": "Chilika Fish Thali, Dalma, Kheer", "is_veg": False},
                {"name": "Mangalajodi Village Kitchen", "cuisine": "Simple Odia Country Meals", "average_cost_for_two": 350, "rating": 4.6, "area": "Eco Camp", "popular_dishes": "Country Chicken Curry, Pakhala Bhaat, Saag Bhaja", "is_veg": False}
            ]
        )
    ]
}

# ── 28. West Bengal ───────────────────────────────────────────────────────────
EAST_STATES["West Bengal"] = {
    "capital": "Kolkata", "region": "East", "tagline": "The Cultural Capital & City of Joy",
    "destinations": [
        make_destination(
            "Kolkata", "The City of Joy & Colonial Renaissance",
            "Victoria Memorial marble splendour, Howrah Bridge over the Hooghly, intellectual Coffee House, tram cars, and mouthwatering Kathi rolls.",
            2000, "Oct–Mar", "3 Days", 4.8, 9.9, "Colonial Architecture, Literature & Gastronomy", ["Solo", "Couples", "Family"], "Kolkata",
            ["Victoria & Maidan", "Park Street", "College Street & North Kolkata", "New Market", "Kumartuli"],
            [
                {"name": "Victoria Memorial Hall & Gardens", "category": "British Colonial Marble Palace", "highlight": "Magnificent Makrana white marble palace housing Queen Victoria's galleries and royal gardens", "fee": "₹50", "time": "2.5 hrs"},
                {"name": "Howrah Bridge & Flower Market", "category": "Cantilever Wonder & Market", "highlight": "Iconic 1943 steel cantilever bridge spanning the Hooghly and vibrant riverside marigold market", "fee": "Free", "time": "2 hrs"},
                {"name": "Dakshineswar Kali Temple & Belur Math", "category": "Sacred River Sanctuaries", "highlight": "Ramakrishna Paramahamsa's riverside 9-spired temple connected by ferry to Belur Math", "fee": "Free", "time": "3.5 hrs"},
                {"name": "College Street & Indian Coffee House", "category": "Intellectual Heritage Hub", "highlight": "World's largest secondhand book market and iconic adda cafe of intellectuals and poets", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Heritage Tram Ride through the Maidan and Esplanade", "category": "Heritage Tram", "cost": 10, "duration": "1 hr"},
                {"name": "Clay Idol Workshop Walk in Kumartuli", "category": "Artisan Craft", "cost": 0, "duration": "2 hrs"},
                {"name": "Historic Park Street Food Crawl (Kathi Rolls, Chelo Kebab & Mishti)", "category": "Culinary Tour", "cost": 500, "duration": "3 hrs"}
            ],
            [
                {"name": "The Oberoi Grand, Kolkata", "category": "Grande Dame of Chowringhee 5-Star", "price_per_night": 14000, "rating": 4.9, "area": "Jawaharlal Nehru Road", "amenities": ["Colonial Courtyard Pool", "Baan Thai", "Spa"], "suitability": ["Couples", "Family", "Business"]},
                {"name": "Taj Bengal, Kolkata", "category": "Luxury 5-Star Hotel", "price_per_night": 12000, "rating": 4.8, "area": "Alipore", "amenities": ["Atrium Gardens", "Pool", "Fine Dining"], "suitability": ["Couples", "Business"]},
                {"name": "Broadway Hotel", "category": "Vintage 1930s Heritage Stay", "price_per_night": 2200, "rating": 4.2, "area": "Chandni Chowk", "amenities": ["Old-World Charm Bar", "High Ceilings", "Restaurant"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Peter Cat", "cuisine": "Continental, Tandoori & Chelo Kebab", "average_cost_for_two": 1200, "rating": 4.8, "area": "Park Street", "popular_dishes": "Famous Chelo Kebab, Sizzlers, Gin Cocktails", "is_veg": False},
                {"name": "6 Ballygunge Place", "cuisine": "Authentic Traditional Bengali Feast", "average_cost_for_two": 1100, "rating": 4.7, "area": "Ballygunge", "popular_dishes": "Daab Chingri (Prawns in Coconut Shell), Kosha Mangsho, Luchi", "is_veg": False},
                {"name": "Nizam's", "cuisine": "Original Inventor of Kathi Rolls", "average_cost_for_two": 350, "rating": 4.6, "area": "New Market", "popular_dishes": "Original Mutton Double Egg Kathi Roll, Chicken Roll", "is_veg": False}
            ]
        ),
        make_destination(
            "Darjeeling", "Queen of the Hills & The Champagne of Teas",
            "UNESCO Himalayan Toy Train, panoramic sunrise over Mt. Kanchenjunga from Tiger Hill, emerald tea gardens, and Tibetan monasteries.",
            2300, "Mar–May & Oct–Dec", "3 Days", 4.8, 9.8, "Himalayan Ridge & UNESCO Toy Train", ["Couples", "Family", "Solo"], "Darjeeling",
            ["Mall Road & Chowrasta", "Tiger Hill", "Happy Valley Tea Estate", "Batasia Loop", "Ghum"],
            [
                {"name": "Tiger Hill Sunrise", "category": "Himalayan Vista", "highlight": "Witnessing the first rays of dawn turn Mt. Kanchenjunga (8,586m) into liquid gold", "fee": "₹50", "time": "2.5 hrs"},
                {"name": "Darjeeling Himalayan Railway (UNESCO Toy Train)", "category": "Heritage Narrow Gauge Steam Train", "highlight": "Steam locomotive chugging through Batasia Loop spiraling across mountain mist", "fee": "₹1000 (Steam)", "time": "2 hrs"},
                {"name": "Happy Valley Tea Estate", "category": "Historic Tea Plantation", "highlight": "Established in 1854; guided tasting of world-famous first flush Muscatel Darjeeling tea", "fee": "₹100", "time": "2 hrs"},
                {"name": "Himalayan Mountaineering Institute (HMI) & Zoo", "category": "Mountaineering Museum & Zoo", "highlight": "Tenzing Norgay memorial and rare red pandas and snow leopards", "fee": "₹110", "time": "2.5 hrs"}
            ],
            [
                {"name": "Joy Ride on the UNESCO Steam Toy Train to Ghum", "category": "Heritage Train", "cost": 1000, "duration": "2 hrs"},
                {"name": "Darjeeling First Flush Tea Tasting Experience", "category": "Tea Tasting", "cost": 200, "duration": "1.5 hrs"},
                {"name": "Evening Stroll and Pony Ride on Chowrasta Mall", "category": "Chowrasta Leisure", "cost": 150, "duration": "2 hrs"}
            ],
            [
                {"name": "The Elgin, Darjeeling", "category": "Colonial Heritage Luxury 5-Star", "price_per_night": 12500, "rating": 4.8, "area": "HD Lama Road", "amenities": ["Victorian Fireplaces", "English Tea Lounge", "Spa"], "suitability": ["Couples", "Family"]},
                {"name": "Windamere Hotel", "category": "Historic British Raj Landmark", "price_per_night": 14000, "rating": 4.7, "area": "Observatory Hill", "amenities": ["Coal Fireplaces", "Afternoon High Tea", "Candlelit Dinners"], "suitability": ["Couples"]},
                {"name": "Hideout Backpackers Hostel", "category": "Cozy Backpacker Stay", "price_per_night": 800, "rating": 4.5, "area": "HD Lama Road", "amenities": ["Kanchenjunga Balcony", "Cafe", "WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Keventers", "cuisine": "Legendary Colonial Breakfast", "average_cost_for_two": 600, "rating": 4.7, "area": "Clubside / Nehru Road", "popular_dishes": "English Breakfast Platter, Pork Sausages, Hot Chocolate with Mountain View", "is_veg": False},
                {"name": "Glenary's Bakery & Pub", "cuisine": "English Bakery, Continental & Live Music", "average_cost_for_two": 850, "rating": 4.8, "area": "Nehru Road", "popular_dishes": "Apple Pie, Chocolate Eclairs, Sizzlers, Darjeeling Tea", "is_veg": False},
                {"name": "Kunga Restaurant", "cuisine": "Authentic Tibetan Family Diner", "average_cost_for_two": 400, "rating": 4.6, "area": "Gandhi Road", "popular_dishes": "Steamed Beef/Chicken Momos, Gyathuk Noodle Soup, Tingmo", "is_veg": False}
            ]
        ),
        make_destination(
            "Sundarbans National Park", "The World's Largest Mangrove Delta & Royal Tigers",
            "UNESCO World Heritage mangrove labyrinth, boat cruises through tidal estuaries, Royal Bengal Tigers swimming across channels, and estuarine crocodiles.",
            2500, "Oct–Mar", "3 Days", 4.8, 9.4, "Mangrove Delta Wildlife & Boat Expeditions", ["Adventure", "Couples", "Solo"], "Gosaba",
            ["Sajnekhali Bird Sanctuary", "Sudhanyakhali Watch Tower", "Dobanki Canopy Walk", "Netidhopani"],
            [
                {"name": "Sudhanyakhali Tiger Watch Tower", "category": "Wildlife Watchtower", "highlight": "Tower overlooking sweet water pond where tigers, spotted deer, and wild boars gather", "fee": "₹100", "time": "2 hrs"},
                {"name": "Dobanki Canopy Walk", "category": "Suspended Forest Skywalk", "highlight": "Half-kilometer caged aerial walkway suspended 20 feet above the mangrove jungle", "fee": "₹100", "time": "2 hrs"},
                {"name": "Sajnekhali Interpretation Centre", "category": "Eco Museum & Watch Tower", "highlight": "Mangrove museum, river terrapin hatchery, and crocodile breeding center", "fee": "₹60", "time": "2 hrs"}
            ],
            [
                {"name": "Full-Day Motorized Boat Cruise through Mangrove Creeks", "category": "Boat Expedition", "cost": 2500, "duration": "Full Day"},
                {"name": "Canopy Skywalk Walkway Experience at Dobanki", "category": "Canopy Walk", "cost": 100, "duration": "1.5 hrs"},
                {"name": "Sundarbans Baul Music and Folk Dance Evening", "category": "Folk Performance", "cost": 300, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Sunderban Tiger Camp (Pakhiralay)", "category": "Eco-Luxury Delta Resort", "price_per_night": 7500, "rating": 4.6, "area": "Dayapur Island", "amenities": ["Waterfront Cottages", "Naturalist Cruises", "Folk Shows"], "suitability": ["Couples", "Family"]},
                {"name": "Sundarban Mangrove Retreat", "category": "Eco Village Resort", "price_per_night": 4500, "rating": 4.4, "area": "Jameshore / Satjalia", "amenities": ["Mud Cottages", "River Cruises", "Organic Farming"], "suitability": ["Friends", "Family"]},
                {"name": "Backpackers Sundarbans Eco Camp", "category": "Community Rustic Camp", "price_per_night": 2000, "rating": 4.5, "area": "Satjalia Island", "amenities": ["Country Boats", "Campfires", "Mud Hut Living"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Tiger Camp Restaurant", "cuisine": "Traditional Bengali Village Feast", "average_cost_for_two": 600, "rating": 4.5, "area": "Dayapur Island", "popular_dishes": "Ilish Macher Jhol, Katla Kalia, Crab Masala, Chutney", "is_veg": False},
                {"name": "Pakhiralay Local Seafood Stalls", "cuisine": "Fresh Delta Fish Fry", "average_cost_for_two": 350, "rating": 4.3, "area": "Pakhiralay Market", "popular_dishes": "Fried Bhetki, Prawn Curry, Steamed Rice", "is_veg": False},
                {"name": "Boat Cruise Fresh Cooked Meal", "cuisine": "Onboard Bengali Home Style", "average_cost_for_two": 400, "rating": 4.7, "area": "Onboard Safari Boat", "popular_dishes": "Khichuri, Beguni, Dim Kosha, Payesh", "is_veg": False}
            ]
        ),
        make_destination(
            "Shantiniketan", "Tagore's Abode of Peace & Red Soil Culture",
            "Open-air classrooms under ancient trees at Visva-Bharati University, red clay Baul singers of Kopai river, and Saturday Sonajhuri Haat.",
            1600, "Oct–Mar", "2 Days", 4.7, 9.2, "Literary Heritage, Art & Baul Folk Music", ["Solo", "Couples", "Family"], "Bolpur",
            ["Visva-Bharati Campus", "Sonajhuri Forest & Haat", "Kopai River", "Kankalitala"],
            [
                {"name": "Visva-Bharati University & Uttarayan Complex", "category": "UNESCO World Heritage Site", "highlight": "Rabindranath Tagore's ashram houses (Udayan, Shyamali) and Rabindra Bhavana museum", "fee": "₹50", "time": "3 hrs"},
                {"name": "Sonajhuri Forest & Saturday Haat (Khoai Mela)", "category": "Open-Air Forest Bazaar", "highlight": "Enchanting red earth forest market where Baul minstrels play ektara and artisans sell kantha quilts", "fee": "Free", "time": "3 hrs"},
                {"name": "Kala Bhavana & Chhatimtala", "category": "Fine Arts Sanctorum", "highlight": "Open-air art studios, Ramkinkar Baij sculptures, and meditation ground under chhatim trees", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Listening to Live Baul Minstrels in Sonajhuri Forest", "category": "Folk Music", "cost": 50, "duration": "2 hrs"},
                {"name": "Cycling Tour of Visva-Bharati Ashram and Red Mud Roads", "category": "Cycling", "cost": 150, "duration": "2.5 hrs"},
                {"name": "Kantha Stitch & Batik Textile Workshop", "category": "Textile Craft", "cost": 300, "duration": "2 hrs"}
            ],
            [
                {"name": "The Garden Bungalow Shantiniketan", "category": "Heritage Boutique Villa", "price_per_night": 5200, "rating": 4.7, "area": "Prantik", "amenities": ["Lotus Ponds", "Terracotta Verandahs", "Organic Bengali Meals"], "suitability": ["Couples", "Family"]},
                {"name": "Rangamati Garden Resort", "category": "Red Earth Nature Resort", "price_per_night": 3200, "rating": 4.3, "area": "Prantik / Bolpur", "amenities": ["Pool", "Open Lawns", "Cultural Performances"], "suitability": ["Family", "Friends"]},
                {"name": "Raktakarabi Karu Ghyar", "category": "Artistic Mud Cottages", "price_per_night": 2400, "rating": 4.5, "area": "Sonajhuri Fringe", "amenities": ["Clay Architecture", "Baul Evenings", "Gardens"], "suitability": ["Solo", "Couples"]}
            ],
            [
                {"name": "Ram-Shyam Village Restaurant", "cuisine": "Traditional Bengali Bell Metal Thali", "average_cost_for_two": 500, "rating": 4.6, "area": "Sonajhuri Road", "popular_dishes": "Luchi with Kosha Mangsho, Shorshe Ilish, Dhokar Dalna", "is_veg": False},
                {"name": "Ghare Baire Restaurant", "cuisine": "Authentic Rural Bengali", "average_cost_for_two": 600, "rating": 4.4, "area": "Bolpur Main Road", "popular_dishes": "Posto Bora, Chital Macher Muitha, Chaler Payesh", "is_veg": False},
                {"name": "Sonajhuri Haat Tea Stalls", "cuisine": "Clay Cup Tea & Snacks", "average_cost_for_two": 100, "rating": 4.7, "area": "Inside Sonajhuri Haat", "popular_dishes": "Bharer Cha, Singara, Telebhaja, Pithe", "is_veg": True}
            ]
        )
    ]
}

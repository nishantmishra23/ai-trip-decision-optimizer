"""
North India Tourism Dataset: Himachal Pradesh, Punjab, Haryana, Rajasthan, Uttar Pradesh, Uttarakhand.
Rich destinations with authentic neighborhoods, places, activities, hotels, and dining.
"""
from data.regions.common import make_destination

NORTH_STATES = {}

# ── 8. Haryana ────────────────────────────────────────────────────────────────
NORTH_STATES["Haryana"] = {
    "capital": "Chandigarh", "region": "North", "tagline": "Pioneer of Modern Progress & Epic Heritage",
    "destinations": [
        make_destination(
            "Kurukshetra", "The Land of the Bhagavad Gita",
            "Ancient sacred land of Mahabharata, massive holy water tanks, epic museums, and pilgrimage shrines.",
            1300, "Oct–Mar", "2 Days", 4.5, 8.4, "Spiritual & Historical Pilgrimage", ["Family", "Senior Citizens", "Solo"], "Kurukshetra",
            ["Brahma Sarovar", "Jyotisar", "Thanesar Heritage", "University Enclave"],
            [
                {"name": "Brahma Sarovar", "category": "Sacred Water Reservoir", "highlight": "Massive ancient tank with twilight Maha Aarti and bronze chariot", "fee": "Free", "time": "2 hrs"},
                {"name": "Jyotisar Birthplace of Gita", "category": "Sacred Banyan", "highlight": "Holy site where Lord Krishna delivered the Gita sermon", "fee": "Free", "time": "2 hrs"},
                {"name": "Sheikh Chilli's Tomb", "category": "Mughal Monument", "highlight": "Stunning Persian marble mausoleum and landscaped gardens", "fee": "₹25", "time": "1.5 hrs"},
                {"name": "Kurukshetra Panorama & Science Centre", "category": "Museum", "highlight": "Gigantic 3D cylindrical diorama of the 18-day battle", "fee": "₹40", "time": "2 hrs"}
            ],
            [
                {"name": "Evening Deep Daan & Aarti at Brahma Sarovar", "category": "Spiritual Ritual", "cost": 0, "duration": "1 hr"},
                {"name": "Sound & Light Show at Jyotisar", "category": "Cultural Show", "cost": 100, "duration": "1 hr"},
                {"name": "Heritage Walk through Thanesar Bazaar", "category": "Heritage Walk", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "Hotel Saffron Kiran", "category": "Comfort Business Hotel", "price_per_night": 2800, "rating": 4.3, "area": "Pipli Road", "amenities": ["Restaurant", "Free WiFi", "AC"], "suitability": ["Family", "Business"]},
                {"name": "The Celestial Beings Resort", "category": "Boutique Resort", "price_per_night": 3500, "rating": 4.4, "area": "GT Road", "amenities": ["Pool", "Lawn", "Multi-cuisine Dining"], "suitability": ["Family", "Couples"]},
                {"name": "Golden Palm Hotel", "category": "Budget Transit Stay", "price_per_night": 1400, "rating": 4.1, "area": "Railway Road", "amenities": ["Free WiFi", "Room Service"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Chaupal Dhaba", "cuisine": "Authentic Haryanvi & Punjabi", "average_cost_for_two": 450, "rating": 4.5, "area": "GT Road", "popular_dishes": "Bajra Roti with Desi Ghee, Dal Makhani, Lassi", "is_veg": True},
                {"name": "Heritage Haveli Restaurant", "cuisine": "North Indian Thali", "average_cost_for_two": 600, "rating": 4.4, "area": "Pipli Bypass", "popular_dishes": "Paneer Tikka, Sarson ka Saag, Makki Roti", "is_veg": True},
                {"name": "Sweet Heart Confectionery", "cuisine": "Sweets & Street Chaat", "average_cost_for_two": 250, "rating": 4.3, "area": "Thanesar", "popular_dishes": "Ghevar, Samosa Chaat, Rabri Jalebi", "is_veg": True}
            ]
        ),
        make_destination(
            "Gurugram (Cyber City & Heritage)", "Millennium City & Sultanpur Bird Sanctuary",
            "High-tech futuristic skyline, vibrant culinary microbreweries, combined with tranquil Sultanpur bird haven.",
            3200, "Oct–Mar", "2 Days", 4.6, 9.1, "Urban Luxury, Nightlife & Birding", ["Friends", "Business", "Couples"], "Gurgaon",
            ["Cyber Hub", "Golf Course Road", "Sultanpur Sanctuary", "Sector 29"],
            [
                {"name": "Cyber Hub & Kingdom of Dreams", "category": "Entertainment Hub", "highlight": "Futuristic amphitheatre, dining hub and live entertainment", "fee": "Free", "time": "3 hrs"},
                {"name": "Sultanpur National Park", "category": "Bird Sanctuary", "highlight": "Ramsar wetland with migratory flamingos, pelicans, and raptors", "fee": "₹10", "time": "3 hrs"},
                {"name": "Aravalli Biodiversity Park", "category": "Nature Reserve", "highlight": "Reclaimed green reserve with walking trails and native flora", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Microbrewery Hop in Sector 29 & Horizon Plaza", "category": "Nightlife & Dining", "cost": 1500, "duration": "3 hrs"},
                {"name": "Bird Photography Safari at Sultanpur", "category": "Wildlife Safari", "cost": 200, "duration": "3 hrs"},
                {"name": "Karting & Adventure at F9 Go Karting", "category": "Adventure Sport", "cost": 750, "duration": "1 hr"}
            ],
            [
                {"name": "The Oberoi, Gurgaon", "category": "Luxury 5-Star", "price_per_night": 18000, "rating": 4.9, "area": "Udyog Vihar", "amenities": ["Olympic Pool", "Luxury Spa", "Fine Dining"], "suitability": ["Couples", "Business"]},
                {"name": "The Leela Ambience Gurugram", "category": "Luxury Hotel & Residences", "price_per_night": 14000, "rating": 4.8, "area": "Ambience Island", "amenities": ["Shopping Mall Attached", "Pool", "Spa"], "suitability": ["Family", "Business"]},
                {"name": "Bloom Boutique Signature Towers", "category": "Boutique Mid-Range", "price_per_night": 3200, "rating": 4.4, "area": "South City", "amenities": ["Cloud Beds", "Free WiFi", "Cafe"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Farzi Cafe Cyber Hub", "cuisine": "Modern Indian Fusion", "average_cost_for_two": 2200, "rating": 4.6, "area": "Cyber Hub", "popular_dishes": "Dal Chawal Arancini, Butter Chicken Bao", "is_veg": False},
                {"name": "Prankster", "cuisine": "Microbrewery & Progressive Indian", "average_cost_for_two": 1800, "rating": 4.5, "area": "Sector 29", "popular_dishes": "Craft Wheat Beer, Pav Bhaji Burger", "is_veg": False},
                {"name": "Roots - Cafe in the Park", "cuisine": "Organic Breakfast & Cafe", "average_cost_for_two": 650, "rating": 4.6, "area": "Leisure Valley Park", "popular_dishes": "Poha, Masala Chai, French Toast", "is_veg": True}
            ]
        ),
        make_destination(
            "Pinjore & Morni Hills", "Mughal Terraced Gardens & Hill Retreat",
            "Haryana's only hill station featuring Tikkar Taal lakes, paired with historic 17th-century Yadavindra Mughal Gardens.",
            1800, "Sep–Apr", "2 Days", 4.4, 8.2, "Nature, Heritage & Scenic Escapes", ["Family", "Couples", "Friends"], "Panchkula",
            ["Pinjore Gardens", "Tikkar Taal Lake", "Morni Fort", "Kalka Foothills"],
            [
                {"name": "Yadavindra (Pinjore) Gardens", "category": "Mughal Terraced Garden", "highlight": "7 terraced Mughal water fountains, Sheesh Mahal, and night illuminations", "fee": "₹30", "time": "2.5 hrs"},
                {"name": "Tikkar Taal Twin Lakes", "category": "Hill Lake & Boating", "highlight": "Serene twin lakes surrounded by green Shivalik ridges", "fee": "Free", "time": "2 hrs"},
                {"name": "Morni Adventure Park", "category": "Adventure Park", "highlight": "Ropes course, climbing wall, and pine forest viewpoints", "fee": "₹150", "time": "2 hrs"}
            ],
            [
                {"name": "Boating and Sunset Viewing at Tikkar Taal", "category": "Lake Boating", "cost": 150, "duration": "1 hr"},
                {"name": "Evening Fountain Light Show at Pinjore Gardens", "category": "Heritage Sightseeing", "cost": 30, "duration": "1.5 hrs"},
                {"name": "Trek through the Pine Ridges of Morni", "category": "Hiking", "cost": 0, "duration": "3 hrs"}
            ],
            [
                {"name": "Morni Heights Resort", "category": "Hillside Resort", "price_per_night": 3200, "rating": 4.3, "area": "Morni Hills", "amenities": ["Valley Views", "Restaurant", "Campfire"], "suitability": ["Couples", "Family"]},
                {"name": "WelcomHeritage Parv Vilas Resort", "category": "Heritage Luxury", "price_per_night": 7500, "rating": 4.6, "area": "Pinjore Kalka Road", "amenities": ["Pool", "Spa", "Lush Lawns"], "suitability": ["Couples", "Family"]},
                {"name": "Hotel Pinjore Regency", "category": "Budget Stay", "price_per_night": 1200, "rating": 4.0, "area": "Near Gardens", "amenities": ["Free WiFi", "Room Service"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Haveli Pinjore", "cuisine": "Punjabi & Haryanvi Dhaba", "average_cost_for_two": 700, "rating": 4.5, "area": "Kalka Shimla Highway", "popular_dishes": "Amritsari Kulcha, Kadai Paneer, Kheer", "is_veg": True},
                {"name": "Lake View Restaurant", "cuisine": "Indian & Chinese", "average_cost_for_two": 500, "rating": 4.2, "area": "Tikkar Taal", "popular_dishes": "Masala Maggi, Pakoras, Chai, Paneer Bhurji", "is_veg": True},
                {"name": "Giani Da Dhaba (Dharampur highway)", "cuisine": "Highway Dhaba", "average_cost_for_two": 600, "rating": 4.4, "area": "Foothills Highway", "popular_dishes": "Lemon Chicken, Dal Fry, Tandoori Roti", "is_veg": False}
            ]
        ),
        make_destination(
            "Damdama Lake & Sohna", "Aravalli Lake Boating & Hot Springs",
            "Tranquil Aravalli getaway famous for one of Haryana's largest natural lakes, rock climbing, and therapeutic sulfur springs.",
            2000, "Oct–Mar", "2 Days", 4.3, 8.0, "Lakeside Adventure & Weekend Getaway", ["Couples", "Friends", "Family"], "Sohna",
            ["Damdama Lakefront", "Sohna Sulfur Springs", "Aravalli Ridge", "Sohna Hilltop"],
            [
                {"name": "Damdama Lake", "category": "Natural Lake", "highlight": "Expansive rainwater lake framed by Aravalli hills with paddle boating", "fee": "Free", "time": "3 hrs"},
                {"name": "Sohna Sulfur Hot Springs", "category": "Natural Springs", "highlight": "Centuries-old hot thermal water spring known for mineral healing", "fee": "Free", "time": "1 hr"},
                {"name": "Sohna Hilltop & Shiva Temple", "category": "Panoramic Viewpoint", "highlight": "Elevated view across Haryana plains and countryside", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Row Boating & Kayaking on Damdama Lake", "category": "Water Adventure", "cost": 250, "duration": "1 hr"},
                {"name": "Aravalli Valley Trekking & Obstacle Course", "category": "Adventure Sports", "cost": 500, "duration": "3 hrs"},
                {"name": "Campfire & Stargazing by the Lakeside", "category": "Camping", "cost": 800, "duration": "Evening"}
            ],
            [
                {"name": "The Gateway Resort Damdama Lake (Taj)", "category": "Luxury Nature Resort", "price_per_night": 13500, "rating": 4.7, "area": "Damdama Lake", "amenities": ["Infinity Pool", "Spa", "Adventure Zone", "Lakefront"], "suitability": ["Family", "Couples"]},
                {"name": "Botanix Nature Resort", "category": "Eco Adventure Camp", "price_per_night": 5500, "rating": 4.4, "area": "Damdama Village", "amenities": ["Organic Farms", "Obstacle Courses", "Swiss Tents"], "suitability": ["Friends", "Family"]},
                {"name": "Dream Island Resort", "category": "Lakeside Island Stay", "price_per_night": 2800, "rating": 4.1, "area": "Lake Bank", "amenities": ["Lake Views", "Boating Access"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Buzz Restaurant (Gateway Resort)", "cuisine": "Gourmet Global & Indian", "average_cost_for_two": 2200, "rating": 4.7, "area": "Off Damdama Lake", "popular_dishes": "Laal Maas, Woodfired Pizza, Brownie Sundae", "is_veg": False},
                {"name": "Sohna Highway Treat", "cuisine": "North Indian Dhaba", "average_cost_for_two": 400, "rating": 4.2, "area": "Sohna Bypass", "popular_dishes": "Dal Tadka, Shahi Paneer, Tandoori Paratha", "is_veg": True},
                {"name": "Botanix Organic Kitchen", "cuisine": "Farm-to-Table Traditional", "average_cost_for_two": 700, "rating": 4.3, "area": "Botanix Resort", "popular_dishes": "Sarson Saag, Chhach, Kheer", "is_veg": True}
            ]
        )
    ]
}

# ── 9. Himachal Pradesh ───────────────────────────────────────────────────────
NORTH_STATES["Himachal Pradesh"] = {
    "capital": "Shimla", "region": "North", "tagline": "Land of the Gods (Devbhoomi)",
    "destinations": [
        make_destination(
            "Manali", "The Snow Peak & High Altitude Adventure Capital",
            "Majestic snow-clad Pir Panjal mountains, Solang Valley adventure sports, Beas river rapids, and Old Manali cafe culture.",
            2400, "Year-round", "4 Days", 4.8, 9.8, "Mountain Adventure & Backpacking", ["Friends", "Couples", "Solo"], "Manali",
            ["Old Manali", "Solang Valley", "Mall Road", "Vashisht Village", "Naggar"],
            [
                {"name": "Solang Valley & Atal Tunnel", "category": "Adventure Valley", "highlight": "Paragliding, snow sledding, and engineering marvel tunnel to Lahaul", "fee": "Free", "time": "5 hrs"},
                {"name": "Hadimba Devi Temple", "category": "Cedar Wood Shrine", "highlight": "16th-century pagoda temple tucked in towering deodar forests", "fee": "Free", "time": "1.5 hrs"},
                {"name": "Jogini Waterfalls & Vashisht", "category": "Waterfall Trek", "highlight": "Scenic waterfall plunging into green valleys and thermal springs", "fee": "Free", "time": "3 hrs"},
                {"name": "Naggar Castle", "category": "Heritage Castle", "highlight": "Medieval wood-and-stone castle with art galleries overlooking the Beas", "fee": "₹30", "time": "2 hrs"}
            ],
            [
                {"name": "Tandem Paragliding at Solang Valley", "category": "Adventure Flight", "cost": 2500, "duration": "1 hr"},
                {"name": "River Rafting on the Beas at Raison", "category": "Water Adventure", "cost": 900, "duration": "1.5 hrs"},
                {"name": "Old Manali Cafe Crawl & Live Acoustic Music", "category": "Cafe Culture", "cost": 600, "duration": "3 hrs"}
            ],
            [
                {"name": "The Himalayan Resort & Spa", "category": "Luxury Victorian Castle", "price_per_night": 14000, "rating": 4.8, "area": "Hadimba Road", "amenities": ["Heated Pool", "Antique Fireplaces", "Orchard Spa"], "suitability": ["Couples", "Family"]},
                {"name": "Larisa Resort Manali", "category": "Boutique Orchard Resort", "price_per_night": 8500, "rating": 4.7, "area": "Haripur / Naggar", "amenities": ["Apple Orchards", "Pool", "Spa"], "suitability": ["Couples", "Family"]},
                {"name": "Zostel Manali (Old Manali)", "category": "Backpacker Hostel", "price_per_night": 850, "rating": 4.6, "area": "Old Manali", "amenities": ["Common Room", "Mountain Balcony", "Cafe"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Cafe 1947", "cuisine": "Italian & Riverside Bistro", "average_cost_for_two": 1100, "rating": 4.6, "area": "Old Manali", "popular_dishes": "Woodfired Pizza, Trout Fry, Apple Crumble", "is_veg": False},
                {"name": "Lazy Dog Lounge", "cuisine": "Continental, Asian & Cocktails", "average_cost_for_two": 1300, "rating": 4.5, "area": "Old Manali Bridge", "popular_dishes": "Sushi Rolls, Grilled Himalayan Trout, Cocktails", "is_veg": False},
                {"name": "Chopsticks Restaurant", "cuisine": "Tibetan & Himalayan Soups", "average_cost_for_two": 600, "rating": 4.4, "area": "The Mall", "popular_dishes": "Thukpa, Steamed Momos, Gyathuk", "is_veg": False}
            ]
        ),
        make_destination(
            "Shimla", "Queen of the Hills & Colonial Summer Capital",
            "Historic British colonial architecture, the heritage Kalka-Shimla toy train, bustling Mall Road, and panoramic pine ridges.",
            2200, "Mar–Jun & Dec–Jan", "3 Days", 4.7, 9.6, "Heritage Hill Retreat", ["Family", "Couples", "Senior Citizens"], "Shimla",
            ["The Ridge & Mall Road", "Jakhu Hill", "Viceregal Lodge", "Kufri", "Mashobra"],
            [
                {"name": "The Ridge & Christ Church", "category": "Colonial Landmark", "highlight": "Open town square framed by neo-Gothic church and snow mountains", "fee": "Free", "time": "2 hrs"},
                {"name": "Viceregal Lodge (Rashtrapati Niwas)", "category": "British Monument", "highlight": "Stately Jacobian mansion where pivotal history of Indian independence was drafted", "fee": "₹50", "time": "2 hrs"},
                {"name": "Jakhu Temple & Giant Hanuman Statue", "category": "Hilltop Shrine", "highlight": "Shimla's highest peak (8,054 ft) reached by cable car ropeway", "fee": "Free", "time": "2 hrs"},
                {"name": "Kufri Snow Point", "category": "Alpine Pasture", "highlight": "Horseback rides, yak safari, and Himalayan Nature Park", "fee": "₹50", "time": "3 hrs"}
            ],
            [
                {"name": "Ride the UNESCO Kalka-Shimla Toy Train", "category": "Heritage Train", "cost": 300, "duration": "4 hrs"},
                {"name": "Jakhu Ropeway Cable Car Ride", "category": "Aerial Cable Car", "cost": 500, "duration": "1 hr"},
                {"name": "Heritage Walk through Colonial Shimla Buildings", "category": "Walking Tour", "cost": 0, "duration": "2.5 hrs"}
            ],
            [
                {"name": "Wildflower Hall, An Oberoi Resort", "category": "Luxury 5-Star Mountain Resort", "price_per_night": 28000, "rating": 4.9, "area": "Mashobra / Charabra", "amenities": ["Heated Outdoor Jacuzzi", "Indoor Heated Pool", "Forest Trails"], "suitability": ["Couples", "Family"]},
                {"name": "The Oberoi Cecil", "category": "Grand Heritage 5-Star", "price_per_night": 17000, "rating": 4.8, "area": "Chaura Maidan", "amenities": ["Spa", "Heritage Ballrooms", "Indoor Pool"], "suitability": ["Couples", "Family"]},
                {"name": "Woodville Palace Hotel", "category": "Royal Heritage Stay", "price_per_night": 5500, "rating": 4.4, "area": "Raj Bhavan Road", "amenities": ["Vintage Antiques", "Tiger Lounge", "Pine Gardens"], "suitability": ["Couples", "Family"]}
            ],
            [
                {"name": "Wake & Bake Cafe", "cuisine": "Crepes, Coffee & Breakfast", "average_cost_for_two": 600, "rating": 4.6, "area": "The Mall", "popular_dishes": "Nutella Crepes, French Press Coffee, Hummus Platter", "is_veg": True},
                {"name": "Cecil Restaurant (Oberoi)", "cuisine": "Fine Dining European & Indian", "average_cost_for_two": 3500, "rating": 4.8, "area": "Chaura Maidan", "popular_dishes": "Wild Mushroom Risotto, Himachali Sepu Vadi", "is_veg": False},
                {"name": "Baljees & Fascination", "cuisine": "Classic North Indian & Desserts", "average_cost_for_two": 700, "rating": 4.4, "area": "The Mall", "popular_dishes": "Gulab Jamun with Ice Cream, Chana Bhatura", "is_veg": True}
            ]
        ),
        make_destination(
            "Dharamshala & McLeod Ganj", "Little Lhasa & The Dhauladhar Sanctuary",
            "Home of His Holiness Dalai Lama, vibrant Tibetan Buddhist monasteries, cedar-lined ridges, and the famous Triund trek.",
            1800, "Mar–Jun & Sep–Nov", "3 Days", 4.7, 9.4, "Spiritual & Himalayan Trekking", ["Solo", "Couples", "Friends"], "Dharamsala",
            ["McLeod Ganj Town", "Tsuglagkhang Complex", "Bhagsunag & Waterfall", "Dharamkot", "Naddi"],
            [
                {"name": "Tsuglagkhang Dalai Lama Temple Complex", "category": "Tibetan Monastery", "highlight": "Spiritual sanctum with chanting monks, prayer wheels, and Tibet Museum", "fee": "Free", "time": "2 hrs"},
                {"name": "Triund Hill Ridge", "category": "Mountain Ridge Trek", "highlight": "Breathtaking cliffside view facing vertical snow-covered Dhauladhar peaks", "fee": "Free", "time": "6 hrs"},
                {"name": "Bhagsunag Waterfall & Shiva Cafe", "category": "Waterfall & Cafe", "highlight": "Rock cascade pool reached by a stone pathway above the village", "fee": "Free", "time": "2 hrs"},
                {"name": "HPCA Dharamshala Cricket Stadium", "category": "Scenic Stadium", "highlight": "One of the world's most stunning mountain-backed cricket venues", "fee": "₹30", "time": "1 hr"}
            ],
            [
                {"name": "Day Trek to Triund Ridge", "category": "Trekking", "cost": 400, "duration": "6 hrs"},
                {"name": "Tibetan Cooking & Momo Workshop", "category": "Culinary Class", "cost": 600, "duration": "2 hrs"},
                {"name": "Sunset View from Naddi Village", "category": "Scenic Sunset", "cost": 0, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Hyatt Regency Dharamshala Resort", "category": "Luxury 5-Star Mountain Resort", "price_per_night": 16000, "rating": 4.8, "area": "Kotwali Bazaar / Forsyth Ganj", "amenities": ["Heated Indoor Pool", "Spa", "Pine Forest View"], "suitability": ["Couples", "Family"]},
                {"name": "Fortune Park Moksha", "category": "Upscale Resort", "price_per_night": 6500, "rating": 4.5, "area": "Strawberry Hills", "amenities": ["Mountain Views", "Spa", "Lawn"], "suitability": ["Family", "Couples"]},
                {"name": "Zostel Plus Dharamkot", "category": "Boutique Hostel", "price_per_night": 900, "rating": 4.7, "area": "Upper Dharamkot", "amenities": ["Common Workspaces", "Valley Cafe", "Yoga Lawn"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Tibmomo & Tibet Kitchen", "cuisine": "Tibetan & Bhutanese", "average_cost_for_two": 600, "rating": 4.6, "area": "Main Square McLeod", "popular_dishes": "Steamed Chicken Momos, Thukpa, Tingmo with Shapta", "is_veg": False},
                {"name": "Illiterati Books & Coffee", "cuisine": "Italian & Book Cafe", "average_cost_for_two": 900, "rating": 4.7, "area": "Jogiwara Road", "popular_dishes": "Belgian Waffles, Ravioli, Organic Coffee", "is_veg": True},
                {"name": "Shiva Cafe", "cuisine": "Mountain Comfort Food", "average_cost_for_two": 500, "rating": 4.3, "area": "Above Bhagsu Waterfall", "popular_dishes": "Nutella Crepes, Maggi, Herbal Tea", "is_veg": True}
            ]
        ),
        make_destination(
            "Spiti Valley (Kaza & Tabo)", "The Middle Land & High Altitude Cold Desert",
            "Dramatic moonscape valleys, 1,000-year-old Buddhist monasteries, highest post office in the world, and crystal stargazing skies.",
            2800, "Jun–Oct", "6 Days", 4.9, 9.2, "High-Altitude Exploration & Stargazing", ["Solo", "Friends", "Adventure"], "Kaza",
            ["Kaza Town", "Key Monastery", "Hikkim & Komic", "Chandratal Lake", "Tabo"],
            [
                {"name": "Key Monastery", "category": "Ancient Fort Monastery", "highlight": "11th-century monastic fortress perched dramatic cliff at 13,668 ft", "fee": "Free", "time": "2 hrs"},
                {"name": "Chandratal (Moon Lake)", "category": "High Alpine Lake", "highlight": "Turquoise crescent lake situated in glacial cirque at 14,100 ft", "fee": "Free", "time": "4 hrs"},
                {"name": "World's Highest Post Office at Hikkim", "category": "Unique Landmark", "highlight": "Send a handwritten postcard stamped at 14,567 ft elevation", "fee": "Free", "time": "1 hr"},
                {"name": "Tabo Monastery (Ajanta of the Himalayas)", "category": "UNESCO Tentative Shrine", "highlight": "Preserved mud-brick murals and stucco sculptures dating back to 996 CE", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Milky Way Astrophotography & Stargazing", "category": "Astronomy Tour", "cost": 0, "duration": "3 hrs"},
                {"name": "Camping near Chandratal Glacier", "category": "Wild Camping", "cost": 1500, "duration": "Overnight"},
                {"name": "Fossil Hunting in Langza Village", "category": "Geological Walk", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "Spiti Valley Grand", "category": "Comfort Mountain Hotel", "price_per_night": 4500, "rating": 4.4, "area": "Kaza Main Market", "amenities": ["Oxygen Cylinders", "Room Heaters", "Restaurant"], "suitability": ["Friends", "Couples"]},
                {"name": "Zostel Spiti (Kaza)", "category": "Backpacker Hostel", "price_per_night": 950, "rating": 4.6, "area": "Rangrik / Kaza", "amenities": ["Cozy Common Room", "Cafe", "Stargazing Deck"], "suitability": ["Solo", "Friends"]},
                {"name": "Norling Homestay Tabo", "category": "Authentic Mud-Brick Homestay", "price_per_night": 1800, "rating": 4.7, "area": "Tabo Village", "amenities": ["Home Cooked Organic Food", "Monastery Proximity"], "suitability": ["Solo", "Couples"]}
            ],
            [
                {"name": "The Himalayan Cafe Kaza", "cuisine": "Tibetan, Israeli & Coffee", "average_cost_for_two": 650, "rating": 4.5, "area": "Kaza New Market", "popular_dishes": "Spiti Sea Buckthorn Tea, Thenthuk, Shakshuka", "is_veg": False},
                {"name": "Cafe Deyzor", "cuisine": "Artisan Continental & Himalayan", "average_cost_for_two": 850, "rating": 4.7, "area": "Behind Kaza BSNL", "popular_dishes": "Yak Cheese Platter, Lamb Stew, Pancakes", "is_veg": False},
                {"name": "Sol Cafe Kaza", "cuisine": "Eco Cafe & Desserts", "average_cost_for_two": 450, "rating": 4.6, "area": "Main Market", "popular_dishes": "Buckwheat Pancakes, Spiti Herbal Infusions", "is_veg": True}
            ]
        ),
        make_destination(
            "Kasol & Parvati Valley", "The Hippie Haven & Himalayan Trekking Valley",
            "Rushing turquoise Parvati river, scenic conifer pine trails, Israeli cafes, and legendary hikes to Kheerganga and Tosh.",
            1600, "Apr–Jun & Sep–Nov", "3 Days", 4.7, 9.3, "River Valley Trekking & Cafe Culture", ["Solo", "Friends", "Couples"], "Kasol",
            ["Kasol Market", "Chalal Village", "Tosh Village", "Kheerganga Trek", "Manikaran"],
            [
                {"name": "Manikaran Sahib Gurudwara & Hot Springs", "category": "Sacred Sikh Shrine", "highlight": "Legendary geothermal boiling springs cooking holy langar food", "fee": "Free", "time": "2 hrs"},
                {"name": "Kheerganga Natural Hot Water Springs", "category": "High Alpine Trek", "highlight": "Bathing in steaming sulfur mineral pool surrounded by snow tops", "fee": "Free", "time": "Full Day"},
                {"name": "Tosh Village & Valley Viewpoint", "category": "Traditional Village", "highlight": "Wood houses and stepped apple terraces overlooking waterfalls", "fee": "Free", "time": "3 hrs"},
                {"name": "Chalal Riverside Pine Trail", "category": "Nature Trail", "highlight": "Gentle suspended bridge walk through mossy deodar forest", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Kheerganga Overnight Trek & Camping", "category": "Mountain Trek", "cost": 1200, "duration": "2 Days"},
                {"name": "Riverside Israeli Cafe Tasting Tour", "category": "Culinary Walk", "cost": 500, "duration": "2 hrs"},
                {"name": "Parvati River Stone Balancing & Meditation", "category": "Nature Wellness", "cost": 0, "duration": "1 hr"}
            ],
            [
                {"name": "The Himalayan Village (Kailash)", "category": "Luxury Machan Resort", "price_per_night": 12000, "rating": 4.8, "area": "Kailash Nagar / Kasol", "amenities": ["Kathkuni Wooden Cottages", "Aroma Spa", "Bar"], "suitability": ["Couples", "Family"]},
                {"name": "Whoopers Hostel Kasol", "category": "Boutique Hostel", "price_per_night": 750, "rating": 4.5, "area": "Old Kasol", "amenities": ["Riverbank Lawn", "Cafe", "Bonfires"], "suitability": ["Solo", "Friends"]},
                {"name": "Parvati Kuteer", "category": "Riverside Wooden Cottages", "price_per_night": 3800, "rating": 4.6, "area": "Kasol Forest", "amenities": ["River Views", "Garden", "Fireplace"], "suitability": ["Couples", "Friends"]}
            ],
            [
                {"name": "Jim Morrison Cafe", "cuisine": "Vegetarian Israeli & Mexican", "average_cost_for_two": 700, "rating": 4.6, "area": "Near Manikaran Road", "popular_dishes": "Falafel Pita Platter, Waffles, Herbal Shakes", "is_veg": True},
                {"name": "Evergreen Cafe", "cuisine": "Israeli, Italian & Middle Eastern", "average_cost_for_two": 800, "rating": 4.5, "area": "Kasol Village", "popular_dishes": "Hummus with Lamb, Woodfired Pizza, Lemon Tart", "is_veg": False},
                {"name": "Moon Dance Cafe", "cuisine": "German Bakery & Breakfast", "average_cost_for_two": 500, "rating": 4.4, "area": "Kasol Main Market", "popular_dishes": "Cinnamon Rolls, Shakshuka, Apple Pie", "is_veg": True}
            ]
        ),
        make_destination(
            "Bir Billing", "World's Premier Paragliding Paradise",
            "World's second-highest paragliding takeoff site, peaceful Tibetan monasteries, deer park institute, and green tea gardens.",
            2000, "Oct–Nov & Mar–Jun", "3 Days", 4.8, 9.1, "Paragliding & Buddhist Heritage", ["Friends", "Solo", "Couples"], "Bir",
            ["Billing Takeoff Point", "Bir Landing Site", "Chokling Monastery", "Bir Tea Gardens"],
            [
                {"name": "Billing Takeoff Point (8,000 ft)", "category": "Paragliding Launch Site", "highlight": "Breathtaking launch point offering thermals over Kangra Valley", "fee": "Free", "time": "2 hrs"},
                {"name": "Chokling Tibetan Monastery", "category": "Buddhist Stupa & Temple", "highlight": "Colourful monastery with grand stupa and fluttering prayer flags", "fee": "Free", "time": "1.5 hrs"},
                {"name": "Deer Park Institute", "category": "Buddhist Centre", "highlight": "Classical Indian wisdom traditions and philosophy retreat centre", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Tandem Paragliding Flight from Billing to Bir", "category": "Paragliding Flight", "cost": 3000, "duration": "45 mins"},
                {"name": "Sunset Picnic at the Landing Site", "category": "Sunset Leisure", "cost": 0, "duration": "2 hrs"},
                {"name": "Bicycle Tour through Bir Tea Plantations", "category": "Cycling", "cost": 250, "duration": "2.5 hrs"}
            ],
            [
                {"name": "The postcard on the Arabian Sea / Bir Retreat", "category": "Boutique Luxury", "price_per_night": 7500, "rating": 4.7, "area": "Bir Tibetan Colony", "amenities": ["Mountain Views", "Garden", "Artisanal Dining"], "suitability": ["Couples", "Solo"]},
                {"name": "Zostel Bir (Billing Road)", "category": "Backpacker Hostel", "price_per_night": 800, "rating": 4.6, "area": "Khasra", "amenities": ["Common Rooftop", "Cafe", "High-Speed WiFi"], "suitability": ["Solo", "Friends"]},
                {"name": "Tatva Bir Tents & Resort", "category": "Glamping Resort", "price_per_night": 3200, "rating": 4.4, "area": "Landing Site", "amenities": ["Bonfires", "Glamping Tents", "Paragliding Views"], "suitability": ["Friends", "Couples"]}
            ],
            [
                {"name": "Avva's Cafe", "cuisine": "Authentic South Indian & Filter Coffee", "average_cost_for_two": 500, "rating": 4.7, "area": "Bir Colony", "popular_dishes": "Ghee Roast Dosa, Idli Vada Platter, Filter Kaapi", "is_veg": True},
                {"name": "Glider's Pizzeria", "cuisine": "Woodfired Artisan Pizza", "average_cost_for_two": 750, "rating": 4.6, "area": "Tibetan Colony", "popular_dishes": "Quattro Formaggi Pizza, Tiramisu", "is_veg": True},
                {"name": "Garden Cafe", "cuisine": "Continental Breakfast & Smoothies", "average_cost_for_two": 450, "rating": 4.5, "area": "Near Chokling", "popular_dishes": "Pancake Stack, Fresh Mint Tea, Organic Salads", "is_veg": True}
            ]
        )
    ]
}

# ── 20. Punjab ────────────────────────────────────────────────────────────────
NORTH_STATES["Punjab"] = {
    "capital": "Chandigarh", "region": "North", "tagline": "The Land of Five Rivers & Golden Faith",
    "destinations": [
        make_destination(
            "Amritsar", "The Spiritual Golden Heart of the Sikhs",
            "The radiant Harmandir Sahib (Golden Temple), poignant Jallianwala Bagh, electrifying Wagah Border retreat, and legendary food streets.",
            2000, "Oct–Mar", "2 Days", 4.9, 9.9, "Sikh Pilgrimage & Culinary Heritage", ["Family", "Solo", "Couples", "Senior Citizens"], "Amritsar",
            ["Golden Temple Complex", "Heritage Street", "Attari Wagah Border", "Ranjit Avenue", "Town Hall"],
            [
                {"name": "Harmandir Sahib (The Golden Temple)", "category": "Sacred Sikh Sanctum", "highlight": "Pure gold-gilded sanctum sitting amidst the sacred nectar pool (Amrit Sarovar)", "fee": "Free", "time": "3 hrs"},
                {"name": "Jallianwala Bagh Memorial", "category": "Historic National Memorial", "highlight": "Martyrs' well, preserved bullet marks, and eternal flame museum", "fee": "Free", "time": "1.5 hrs"},
                {"name": "Attari-Wagah Border Flag Lowering Ceremony", "category": "Military Ceremony", "highlight": "High-octane patriotic drill with thunderous cheers and drill marches", "fee": "Free", "time": "3 hrs"},
                {"name": "Gobindgarh Fort", "category": "Historical Fortress", "highlight": "18th-century fortress of Maharaja Ranjit Singh with 7D show and coin museum", "fee": "₹150", "time": "2.5 hrs"}
            ],
            [
                {"name": "Volunteer Langar Seva at the Golden Temple", "category": "Community Service", "cost": 0, "duration": "2 hrs"},
                {"name": "Amritsar Food Walk (Kulcha, Lassi & Jalebi)", "category": "Culinary Walk", "cost": 350, "duration": "2.5 hrs"},
                {"name": "Evening Palki Sahib Ceremony at Golden Temple", "category": "Spiritual Procession", "cost": 0, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Taj Swarna, Amritsar", "category": "Luxury 5-Star", "price_per_night": 9500, "rating": 4.8, "area": "Majitha Road", "amenities": ["Pool", "Jiva Spa", "Fine Dining"], "suitability": ["Couples", "Family"]},
                {"name": "Hyatt Regency Amritsar", "category": "5-Star Hotel", "price_per_night": 7500, "rating": 4.7, "area": "MBM Farms, GT Road", "amenities": ["Outdoor Pool", "Spa", "Lounge"], "suitability": ["Couples", "Family"]},
                {"name": "Madpackers Hostel Amritsar", "category": "Backpacker Hostel", "price_per_night": 750, "rating": 4.6, "area": "Heritage Street", "amenities": ["Rooftop View", "WiFi", "Walking Tours"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Bhai Kulwant Singh Kulchian Wale", "cuisine": "Authentic Amritsari Kulcha", "average_cost_for_two": 250, "rating": 4.8, "area": "Golden Temple Heritage Walk", "popular_dishes": "Amritsari Aloo Pyaaz Kulcha with Chole & Tamarind Chutney", "is_veg": True},
                {"name": "Kesar Da Dhaba", "cuisine": "Centuries-Old Punjabi Dhaba", "average_cost_for_two": 600, "rating": 4.7, "area": "Chowk Passian", "popular_dishes": "Dal Makhani (Slow-Cooked 24 hrs), Palak Paneer, Phirni", "is_veg": True},
                {"name": "Beera Chicken House", "cuisine": "Legendary Punjabi Tandoori", "average_cost_for_two": 700, "rating": 4.6, "area": "Majitha Road", "popular_dishes": "Whole Roasted Tandoori Chicken, Keema Naan", "is_veg": False}
            ]
        ),
        make_destination(
            "Chandigarh", "The City Beautiful & Le Corbusier's Masterpiece",
            "India's first planned modernist city, Nek Chand's recycled Rock Garden, tranquil Sukhna Lake, and vibrant Sector 17 & 26 cafes.",
            2200, "Sep–Mar", "2 Days", 4.7, 9.4, "Modern Urban Architecture & Gardens", ["Family", "Couples", "Friends"], "Chandigarh",
            ["Sukhna Lake", "Rock Garden", "Sector 17 Plaza", "Rose Garden", "Sector 26"],
            [
                {"name": "Nek Chand's Rock Garden", "category": "Sculpture Wonderland", "highlight": "40-acre sculpture park crafted entirely from urban and industrial waste ceramics", "fee": "₹30", "time": "2.5 hrs"},
                {"name": "Sukhna Lake & Promenade", "category": "Rainfed Lake", "highlight": "Picturesque 3 sq km lake with swan pedal boats against the Shivalik foothills", "fee": "Free", "time": "2 hrs"},
                {"name": "Zakir Hussain Rose Garden", "category": "Botanical Garden", "highlight": "Asia's largest rose garden featuring 50,000 rose bushes of 1,600 varieties", "fee": "Free", "time": "1.5 hrs"},
                {"name": "Capitol Complex (UNESCO)", "category": "Le Corbusier Architecture", "highlight": "Open Hand Monument, High Court, and Secretariat brutalist architecture", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Morning Boating & Jogging at Sukhna Lake", "category": "Lakeside Activity", "cost": 150, "duration": "1.5 hrs"},
                {"name": "Architectural Tour of Capitol Complex", "category": "Guided Architecture", "cost": 0, "duration": "2 hrs"},
                {"name": "Nightlife & Microbrewery Tour in Sector 26", "category": "Nightlife", "cost": 1200, "duration": "3 hrs"}
            ],
            [
                {"name": "JW Marriott Hotel Chandigarh", "category": "Luxury 5-Star", "price_per_night": 12000, "rating": 4.8, "area": "Sector 35B", "amenities": ["Rooftop Pool", "Spa", "Microbrewery Lounge"], "suitability": ["Family", "Couples", "Business"]},
                {"name": "The Lalit Chandigarh", "category": "Luxury 5-Star", "price_per_night": 8500, "rating": 4.6, "area": "IT Park", "amenities": ["Spa", "Pool", "Forest Views"], "suitability": ["Couples", "Business"]},
                {"name": "Hotel Mountview", "category": "Classic Heritage Hotel", "price_per_night": 4500, "rating": 4.3, "area": "Sector 10", "amenities": ["Gardens", "Pool", "Free WiFi"], "suitability": ["Family", "Senior Citizens"]}
            ],
            [
                {"name": "Pal Dhaba (Sector 28)", "cuisine": "Punjabi Highway Legend", "average_cost_for_two": 750, "rating": 4.6, "area": "Sector 28D", "popular_dishes": "Mutton Rogan Josh, Butter Chicken, Dal Makhani", "is_veg": False},
                {"name": "Garg Chaat", "cuisine": "Street Food", "average_cost_for_two": 200, "rating": 4.5, "area": "Sector 23", "popular_dishes": "Gol Gappe, Dahi Bhalla, Papdi Chaat", "is_veg": True},
                {"name": "Backpackers Cafe", "cuisine": "Artisan Continental & Breakfast", "average_cost_for_two": 900, "rating": 4.6, "area": "Sector 9D", "popular_dishes": "Gourmet Burgers, Lasagna, Belgian Hot Chocolate", "is_veg": True}
            ]
        ),
        make_destination(
            "Anandpur Sahib", "The Holy City of Bliss & Khalsa Birthplace",
            "Birthplace of the Khalsa panth, white marble gurudwaras, world-class Virasat-e-Khalsa museum, and colorful Hola Mohalla festival.",
            1500, "Oct–Mar", "2 Days", 4.7, 8.8, "Sikh Faith & Cultural Heritage", ["Family", "Senior Citizens", "Solo"], "Rupnagar",
            ["Takht Sri Kesgarh Sahib", "Virasat-e-Khalsa", "Nangal Dam", "Bhakra Foothills"],
            [
                {"name": "Takht Sri Kesgarh Sahib", "category": "Sikh Temporal Seat", "highlight": "Fortress gurudwara where Guru Gobind Singh baptized the Panj Pyare in 1699", "fee": "Free", "time": "2 hrs"},
                {"name": "Virasat-e-Khalsa", "category": "World-Class Museum", "highlight": "Architectural marvel chronicling Sikh history with multimedia exhibits", "fee": "Free", "time": "3 hrs"},
                {"name": "Bhakra Nangal Dam", "category": "Engineering Wonder", "highlight": "One of India's highest straight gravity dams holding the Gobind Sagar lake", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Virasat-e-Khalsa Comprehensive Audio-Visual Tour", "category": "Museum Experience", "cost": 0, "duration": "3 hrs"},
                {"name": "Witnessing Gatka Martial Arts Demonstration", "category": "Martial Art Show", "cost": 0, "duration": "1.5 hrs"},
                {"name": "Sunset View of Gobind Sagar Reservoir", "category": "Scenic Viewpoint", "cost": 0, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Kikar Lodge Natural Retreat", "category": "Luxury Forest Resort", "price_per_night": 7500, "rating": 4.6, "area": "Nurpur Bedi / Anandpur", "amenities": ["Pool", "Quad Biking", "Forest Spa"], "suitability": ["Couples", "Family"]},
                {"name": "Hotel White City", "category": "Pilgrim Comfort Stay", "price_per_night": 1800, "rating": 4.2, "area": "Near Kesgarh Sahib", "amenities": ["Vegetarian Restaurant", "AC", "WiFi"], "suitability": ["Family", "Senior Citizens"]},
                {"name": "Heritage Haveli Stay", "category": "Heritage Stay", "price_per_night": 2800, "rating": 4.3, "area": "Rupnagar Highway", "amenities": ["Lawns", "Punjabi Dining"], "suitability": ["Family", "Solo"]}
            ],
            [
                {"name": "Kesgarh Sahib Holy Langar", "cuisine": "Blessed Sikh Vegetarian Langar", "average_cost_for_two": 0, "rating": 4.9, "area": "Takht Sri Kesgarh Sahib", "popular_dishes": "Dal, Roti, Kheer, Prasad", "is_veg": True},
                {"name": "Haveli Anandpur Sahib", "cuisine": "Punjabi Thali & Parathas", "average_cost_for_two": 500, "rating": 4.5, "area": "Ropar Highway", "popular_dishes": "Amritsari Naan, Paneer Lababdar, Sweet Lassi", "is_veg": True},
                {"name": "Preet Dhaba", "cuisine": "Traditional Highway Dhaba", "average_cost_for_two": 300, "rating": 4.2, "area": "Nangal Road", "popular_dishes": "Rajma Chawal, Kadhi Pakora, Tandoori Roti", "is_veg": True}
            ]
        ),
        make_destination(
            "Patiala", "The Royal City of Qila Mubarak & Phulkari",
            "Opulent palaces, the Sheesh Mahal mirror chambers, royal Patiala peg traditions, handcrafted juttis, and colourful Phulkari embroidery.",
            1800, "Oct–Mar", "2 Days", 4.5, 8.5, "Royal Sikh Royalty & Handicrafts", ["Family", "Couples", "Solo"], "Patiala",
            ["Qila Mubarak", "Sheesh Mahal", "Baradari Gardens", "AC Market Juttis"],
            [
                {"name": "Qila Mubarak Complex", "category": "Sikh Palace Fortress", "highlight": "10-acre fort complex housing the Ran Baas palace, cannons, and arms", "fee": "₹20", "time": "2 hrs"},
                {"name": "Sheesh Mahal (Palace of Mirrors)", "category": "Mirror Palace & Museum", "highlight": "Intricate mirror work, suspension bridge, and medal gallery", "fee": "₹20", "time": "1.5 hrs"},
                {"name": "Baradari Gardens", "category": "Royal Garden", "highlight": "Historic circular gardens with colonial pavilion and exotic botanicals", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Shopping for Patiala Salwars & Handmade Juttis", "category": "Handicrafts Shopping", "cost": 0, "duration": "2.5 hrs"},
                {"name": "Phulkari Embroidery Village Workshop", "category": "Textile Craft", "cost": 300, "duration": "2 hrs"},
                {"name": "Evening Stroll in Baradari Palace Grounds", "category": "Heritage Walk", "cost": 0, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Neemrana's The Baradari Palace", "category": "Heritage Palace Hotel", "price_per_night": 6500, "rating": 4.6, "area": "Baradari Gardens", "amenities": ["Colonial High Ceilings", "Lush Lawns", "Heritage Courtyard"], "suitability": ["Couples", "Family"]},
                {"name": "Clarion Inn Amps Patiala", "category": "Modern Business Hotel", "price_per_night": 3200, "rating": 4.3, "area": "Rajpura Road", "amenities": ["Restaurant", "Gym", "Free WiFi"], "suitability": ["Business", "Family"]},
                {"name": "Hotel Eqbal Inn", "category": "Comfort Hotel", "price_per_night": 2400, "rating": 4.1, "area": "Near Phul Cinema", "amenities": ["Restaurant", "AC", "Parking"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Nagpal Chole Bhature", "cuisine": "Punjabi Street Legend", "average_cost_for_two": 250, "rating": 4.7, "area": "Anardana Chowk", "popular_dishes": "Paneer Stuffed Bhature, Chole, Spicy Pickle", "is_veg": True},
                {"name": "Gopal's Sweets & Restaurant", "cuisine": "Sweets, Chaat & North Indian", "average_cost_for_two": 500, "rating": 4.5, "area": "Leela Bhawan", "popular_dishes": "Dhokla, Rasmalai, Dal Makhani Thali", "is_veg": True},
                {"name": "Sahni Bakery & Kitchen", "cuisine": "Bakery, Rolls & Snacks", "average_cost_for_two": 350, "rating": 4.3, "area": "Bhupindra Road", "popular_dishes": "Chicken Patties, Walnut Cake, Grilled Sandwiches", "is_veg": False}
            ]
        )
    ]
}

# ── 21. Rajasthan ─────────────────────────────────────────────────────────────
NORTH_STATES["Rajasthan"] = {
    "capital": "Jaipur", "region": "North", "tagline": "The Land of Maharajas & Forts",
    "destinations": [
        make_destination(
            "Jaipur", "The Pink City & Regal Capital",
            "UNESCO World Heritage pink facade, Amer Fort atop the Aravallis, Hawa Mahal winds, and royal astronomer's Jantar Mantar.",
            2500, "Oct–Mar", "3 Days", 4.9, 9.9, "Royal Heritage & Palaces", ["Family", "Couples", "Solo", "Friends"], "Jaipur",
            ["Amer & Nahargarh", "Old Pink City & Hawa Mahal", "C-Scheme", "Malviya Nagar"],
            [
                {"name": "Amer Fort & Sheesh Mahal", "category": "Hilltop Fort", "highlight": "Opulent marble mirror palace, Maota Lake reflections, and elephant path", "fee": "₹100", "time": "3 hrs"},
                {"name": "Hawa Mahal (Palace of Winds)", "category": "Iconic Rajput Architecture", "highlight": "953 latticed jharokha windows built for royal ladies to view city life", "fee": "₹50", "time": "1.5 hrs"},
                {"name": "City Palace & Chandra Mahal", "category": "Royal Residence", "highlight": "Magnificent peacock courtyard and private collections of Jaipur royals", "fee": "₹200", "time": "2.5 hrs"},
                {"name": "Nahargarh Fort Sunset Viewpoint", "category": "Fortress Viewpoint", "highlight": "Cliff edge overlooking the glowing twilight cityscape of Jaipur", "fee": "₹50", "time": "2 hrs"}
            ],
            [
                {"name": "Sunrise Hot Air Balloon Flight over Amer", "category": "Aerial Adventure", "cost": 9000, "duration": "1 hr"},
                {"name": "Block Printing Workshop in Sanganer", "category": "Artisan Craft", "cost": 500, "duration": "2.5 hrs"},
                {"name": "Nahargarh Fort Sunset Cycling Tour", "category": "Cycling", "cost": 600, "duration": "2.5 hrs"}
            ],
            [
                {"name": "Rambagh Palace (Taj)", "category": "Palace of Maharajas 5-Star", "price_per_night": 38000, "rating": 5.0, "area": "Bhawani Singh Road", "amenities": ["Royal Gardens", "Indoor/Outdoor Pools", "Butlers"], "suitability": ["Couples", "Family"]},
                {"name": "Samode Haveli", "category": "Heritage Boutique Hotel", "price_per_night": 14000, "rating": 4.8, "area": "Gangapole", "amenities": ["Mosaic Pool", "Courtyards", "Spa"], "suitability": ["Couples", "Family"]},
                {"name": "Zostel Jaipur", "category": "Backpacker Hostel", "price_per_night": 800, "rating": 4.6, "area": "Hawa Mahal Road", "amenities": ["Rooftop Cafe", "AC Doms", "Walking Tours"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "LMB (Laxmi Misthan Bhandar)", "cuisine": "Authentic Rajasthani Thali & Sweets", "average_cost_for_two": 900, "rating": 4.6, "area": "Johari Bazaar", "popular_dishes": "Royal Rajasthani Thali, Dal Baati Churma, Ghewar", "is_veg": True},
                {"name": "Tapri Central", "cuisine": "Tea Lounge & Street Modern", "average_cost_for_two": 600, "rating": 4.7, "area": "C-Scheme", "popular_dishes": "Handi Chai, Sauteed Mushrooms, Vada Pav, Khakra Pizza", "is_veg": True},
                {"name": "Handi Restaurant", "cuisine": "Mughlai & Rajasthani Meat", "average_cost_for_two": 1200, "rating": 4.5, "area": "MI Road", "popular_dishes": "Handi Meat, Laal Maas, Garlic Naan", "is_veg": False}
            ]
        ),
        make_destination(
            "Udaipur", "The City of Lakes & Romance",
            "Shimmering waters of Lake Pichola, island palaces, white marble City Palace, and cobblestone haveli alleys.",
            2800, "Sep–Mar", "3 Days", 4.9, 9.8, "Romantic Lakeside & Royal Palaces", ["Couples", "Family", "Solo"], "Udaipur",
            ["Lake Pichola & Ghats", "Fateh Sagar Lake", "City Palace Complex", "Old Haveli Quarter"],
            [
                {"name": "Udaipur City Palace Complex", "category": "Grand Palace", "highlight": "Rajasthan's largest royal palace complex with ornate glass tile mosaics", "fee": "₹300", "time": "3 hrs"},
                {"name": "Lake Pichola Sunset Boat Cruise", "category": "Scenic Boat Cruise", "highlight": "Gliding past the floating Lake Palace and Jagmandir Island", "fee": "₹500", "time": "1 hr"},
                {"name": "Saheliyon-ki-Bari", "category": "Royal Courtyard & Fountains", "highlight": "Marble elephant fountains, lotus pools, and shaded bougainvillea", "fee": "₹20", "time": "1.5 hrs"},
                {"name": "Monsoon Palace (Sajjangarh)", "category": "Hilltop Fort", "highlight": "Aravalli hilltop fortress with 360-degree panorama of sunset lakes", "fee": "₹70", "time": "2 hrs"}
            ],
            [
                {"name": "Sunset Boat Cruise on Lake Pichola", "category": "Boat Cruise", "cost": 500, "duration": "1 hr"},
                {"name": "Dharohar Folk Dance Show at Bagore Ki Haveli", "category": "Cultural Dance", "cost": 150, "duration": "1 hr"},
                {"name": "Miniature Painting Workshop in Old Quarter", "category": "Art Class", "cost": 400, "duration": "2 hrs"}
            ],
            [
                {"name": "Taj Lake Palace", "category": "Floating Palace 5-Star", "price_per_night": 45000, "rating": 5.0, "area": "Lake Pichola Island", "amenities": ["Boat Transfer", "Spa Boat", "Royal Butler"], "suitability": ["Couples"]},
                {"name": "The Oberoi Udaivilas", "category": "Ultra Luxury Resort", "price_per_night": 48000, "rating": 5.0, "area": "Haridas Ji Ki Magri", "amenities": ["Moat Pools", "Peacock Sanctuaries", "Spa"], "suitability": ["Couples", "Family"]},
                {"name": "Zostel Udaipur", "category": "Backpacker Hostel", "price_per_night": 850, "rating": 4.7, "area": "Navghat / Old City", "amenities": ["Rooftop Pichola View", "Cafe", "WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Ambrai Restaurant (Amet Haveli)", "cuisine": "Lakeside Royal Rajasthani", "average_cost_for_two": 2400, "rating": 4.8, "area": "Hanuman Ghat", "popular_dishes": "Mewari Mutton, Laal Maas, Paneer Tikka, Sunset Cocktails", "is_veg": False},
                {"name": "Millets of Mewar", "cuisine": "Healthy Rajasthani & Organic Vegan", "average_cost_for_two": 700, "rating": 4.6, "area": "Hanuman Ghat", "popular_dishes": "Millet Pancakes, Dal Baati, Vegan Thali", "is_veg": True},
                {"name": "Jheel's Ginger Coffee Bar & Bakery", "cuisine": "Lakeside Cafe & Desserts", "average_cost_for_two": 500, "rating": 4.7, "area": "Gangaur Ghat", "popular_dishes": "Nutella Pie, Hazelnut Frappe, Woodfired Pizza", "is_veg": True}
            ]
        ),
        make_destination(
            "Jodhpur", "The Blue City & Sun City",
            "Monolithic Mehrangarh Fort towering above cobalt-blue cubic houses, flying fox ziplines, and spicy mirchi vadas.",
            2100, "Oct–Mar", "2 Days", 4.8, 9.5, "Desert Fortress & Blue Alleys", ["Solo", "Couples", "Friends"], "Jodhpur",
            ["Mehrangarh Fort Enclave", "Navchokiya (Blue Quarter)", "Clock Tower & Sardar Market", "Umaid Bhawan"],
            [
                {"name": "Mehrangarh Fort", "category": "Impregnable Citadel", "highlight": "Spectacular 400-ft cliff fortress holding royal palanquins and period rooms", "fee": "₹100", "time": "3.5 hrs"},
                {"name": "Jaswant Thada", "category": "White Marble Cenotaph", "highlight": "Luminously carved marble memorial sitting beside a tranquil desert lake", "fee": "₹30", "time": "1 hr"},
                {"name": "Umaid Bhawan Palace & Museum", "category": "Art Deco Palace", "highlight": "One of the world's largest private residences made of golden sandstone", "fee": "₹30", "time": "2 hrs"},
                {"name": "Mandore Gardens", "category": "Royal Cenotaphs", "highlight": "Ancient Marwar capital with high-rock cenotaphs and playful langurs", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Flying Fox Zipline across Mehrangarh Fort Moats", "category": "Zipline Adventure", "cost": 1800, "duration": "1.5 hrs"},
                {"name": "Blue City Heritage Photography Walking Tour", "category": "Photography Walk", "cost": 300, "duration": "2.5 hrs"},
                {"name": "Bishnoi Village Safari & Blackbuck Watching", "category": "Rural Safari", "cost": 1200, "duration": "4 hrs"}
            ],
            [
                {"name": "Umaid Bhawan Palace (Taj)", "category": "Ultra Luxury Palace 5-Star", "price_per_night": 42000, "rating": 5.0, "area": "Circuit House Road", "amenities": ["Subterranean Pool", "Peacock Lawns", "Museum"], "suitability": ["Couples", "Family"]},
                {"name": "RAAS Jodhpur", "category": "Luxury Boutique Haveli", "price_per_night": 18000, "rating": 4.9, "area": "Tunwar ji ka Jhalra", "amenities": ["Stepwell View", "Fort View Pool", "Fine Dining"], "suitability": ["Couples"]},
                {"name": "Zostel Jodhpur", "category": "Backpacker Hostel", "price_per_night": 750, "rating": 4.6, "area": "Makrana Mohalla", "amenities": ["Rooftop Fort View", "AC", "Common Room"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Janta Sweet Home", "cuisine": "Legendary Marwari Snacks & Sweets", "average_cost_for_two": 300, "rating": 4.7, "area": "Station Road / Sardar Market", "popular_dishes": "Mirchi Vada, Mawa Kachori, Pyaaz Kachori, Lassi", "is_veg": True},
                {"name": "Indique (Pal Haveli)", "cuisine": "Rooftop Royal Rajasthani", "average_cost_for_two": 1600, "rating": 4.7, "area": "Gulab Sagar", "popular_dishes": "Laal Maas, Safed Maas, Gatta Curry, Fort View Cocktails", "is_veg": False},
                {"name": "Shahi Samosa", "cuisine": "Street Snacks", "average_cost_for_two": 150, "rating": 4.6, "area": "Clock Tower", "popular_dishes": "Crispy Spiced Samosa, Kachori", "is_veg": True}
            ]
        ),
        make_destination(
            "Jaisalmer", "The Golden City & Thar Desert Sands",
            "Living golden sandstone fortress, camel caravans in rolling Sam sand dunes, Jain temples, and Arabian Nights desert camps.",
            2300, "Oct–Mar", "3 Days", 4.8, 9.6, "Desert Camping & Living Fortress", ["Friends", "Couples", "Solo", "Family"], "Jaisalmer",
            ["Jaisalmer Fort Inside", "Sam Sand Dunes", "Patwon Ki Haveli", "Gadisar Lake"],
            [
                {"name": "Jaisalmer Fort (Sonar Qila)", "category": "Living Golden Citadel", "highlight": "UNESCO fort inhabited by 4,000 citizens with ancient Jain temples", "fee": "Free", "time": "3 hrs"},
                {"name": "Sam Sand Dunes", "category": "Thar Desert Dunes", "highlight": "Sweeping golden ripples, desert camel safaris, and night stargazing", "fee": "Free", "time": "Half Day"},
                {"name": "Patwon Ki Haveli", "category": "Sandstone Haveli", "highlight": "Cluster of 5 grand merchant havelis with intricate sandstone filigree", "fee": "₹50", "time": "2 hrs"},
                {"name": "Gadisar Lake", "category": "Desert Water Reservoir", "highlight": "Ancient carved gateway arch, shrines, and sunset boating", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Overnight Desert Camping & Folk Music in Sam Dunes", "category": "Desert Camp", "cost": 2200, "duration": "Overnight"},
                {"name": "Camel Trek across the Thar Desert Sunset", "category": "Camel Safari", "cost": 500, "duration": "2 hrs"},
                {"name": "Dune Bashing on 4x4 Jeeps in Thar", "category": "Off-Road Adventure", "cost": 1200, "duration": "1 hr"}
            ],
            [
                {"name": "Suryagarh, Jaisalmer", "category": "Luxury Desert Fortress 5-Star", "price_per_night": 22000, "rating": 4.9, "area": "Khabha Road", "amenities": ["Desert Spa", "Camel Courtyards", "Fine Dining"], "suitability": ["Couples", "Family"]},
                {"name": "The Desert Heritage Resort & Camp", "category": "Luxury Swiss Desert Tents", "price_per_night": 4500, "rating": 4.6, "area": "Sam Sand Dunes", "amenities": ["Bonfire", "Kalbelia Dance", "Buffet"], "suitability": ["Friends", "Family", "Couples"]},
                {"name": "Zostel Jaisalmer", "category": "Backpacker Stay", "price_per_night": 800, "rating": 4.6, "area": "Near Fort Gate", "amenities": ["Fort View Terrace", "Cafe", "WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "The Trio", "cuisine": "Rajasthani & Awadhi", "average_cost_for_two": 1100, "rating": 4.5, "area": "Mandir Palace", "popular_dishes": "Ker Sangri, Laal Maas, Shahi Tukda", "is_veg": False},
                {"name": "Pleasant Haveli Rooftop", "cuisine": "Multi-Cuisine & Sunset Dining", "average_cost_for_two": 700, "rating": 4.6, "area": "Chainpura", "popular_dishes": "Dal Baati Churma, Pasta, Ginger Lemon Tea", "is_veg": True},
                {"name": "Dhanraj Ranmal Bhatia Sweets", "cuisine": "Traditional Confectionery", "average_cost_for_two": 250, "rating": 4.7, "area": "Asani Road", "popular_dishes": "Ghotua Laddoo, Panchdhari Ladoo", "is_veg": True}
            ]
        ),
        make_destination(
            "Pushkar", "The Sacred Lake & Great Camel Fair Haven",
            "The world's rarest Lord Brahma Temple, 52 holy ghats, spiritual evening aartis, Rose gardens, and bohemian desert cafes.",
            1400, "Oct–Mar", "2 Days", 4.6, 9.0, "Spiritual Ghats & Bohemian Vibe", ["Solo", "Couples", "Friends"], "Pushkar",
            ["Pushkar Lake Ghats", "Brahma Temple Chowk", "Savitri Temple Ridge", "Desert Camp Fringe"],
            [
                {"name": "Jagatpita Brahma Temple", "category": "Sacred 14th-Century Shrine", "highlight": "One of the extremely few temples in the world dedicated to Lord Brahma", "fee": "Free", "time": "1.5 hrs"},
                {"name": "Pushkar Holy Lake & 52 Ghats", "category": "Sacred Pilgrimage Lake", "highlight": "Spiritual bathing ghats with evening ringing bells and reflection lamps", "fee": "Free", "time": "2 hrs"},
                {"name": "Savitri Devi Temple & Ropeway", "category": "Mountain Ridge Temple", "highlight": "Highest vantage hill overlooking Pushkar valley and Thar sands", "fee": "Free", "time": "2.5 hrs"}
            ],
            [
                {"name": "Sunrise Hike or Ropeway Ride to Savitri Temple", "category": "Hiking / Ropeway", "cost": 150, "duration": "2 hrs"},
                {"name": "Maha Aarti at Varaha & Brahma Ghat", "category": "Spiritual Aarti", "cost": 0, "duration": "1 hr"},
                {"name": "Desert Sunset Quad Bike & Camel Ride", "category": "Adventure Desert", "cost": 600, "duration": "1.5 hrs"}
            ],
            [
                {"name": "The Westin Pushkar Resort & Spa", "category": "Luxury 5-Star Wellness Resort", "price_per_night": 14000, "rating": 4.7, "area": "Khasra No 1242", "amenities": ["Private Plunge Pools", "Heavenly Spa", "Helipad"], "suitability": ["Couples", "Family"]},
                {"name": "Pushkar Bagh Resort", "category": "Heritage Tent Resort", "price_per_night": 4200, "rating": 4.4, "area": "Motisar Road", "amenities": ["Desert Views", "Pool", "Folk Dance"], "suitability": ["Couples", "Friends"]},
                {"name": "Zostel Pushkar", "category": "Backpacker Hostel & Pool", "price_per_night": 750, "rating": 4.6, "area": "Ganhera", "amenities": ["Swimming Pool", "Garden Cafe", "Common Rooms"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "The Laughing Buddha Cafe", "cuisine": "Vegetarian Organic & Cafe", "average_cost_for_two": 450, "rating": 4.6, "area": "Main Market Road", "popular_dishes": "Falafel Bowl, Woodfired Thin Crust Pizza, Cold Coffee", "is_veg": True},
                {"name": "Halwai Gali Rabri Malpua", "cuisine": "Street Dessert Legend", "average_cost_for_two": 150, "rating": 4.8, "area": "Brahma Temple Road", "popular_dishes": "Rabri Malpua, Gulab Jamun, Lassi", "is_veg": True},
                {"name": "Pink Floyd Cafe", "cuisine": "Bohemian Rooftop", "average_cost_for_two": 500, "rating": 4.3, "area": "Near Pushkar Lake", "popular_dishes": "Israeli Shakshuka, Masala Chai, Pancakes", "is_veg": True}
            ]
        ),
        make_destination(
            "Ajmer", "The Dargah Sharif & Sufi Serenity",
            "The venerated Sufi shrine of Khwaja Moinuddin Chishti, historic Ana Sagar lake, and ancient Taragarh hilltop fortress.",
            1500, "Oct–Mar", "2 Days", 4.6, 9.1, "Sufi Pilgrimage & Lakeside History", ["Family", "Senior Citizens", "Solo"], "Ajmer",
            ["Dargah Sharif", "Ana Sagar Lake", "Taragarh Fort", "Adhai Din Ka Jhonpra"],
            [
                {"name": "Ajmer Sharif Dargah", "category": "Sacred Sufi Shrine", "highlight": "Resting place of saint Khwaja Moinuddin Chishti visited by millions across faiths", "fee": "Free", "time": "2 hrs"},
                {"name": "Ana Sagar Lake & Daulat Bagh", "category": "Historic Artificial Lake", "highlight": "12th-century lake with marble pavilions (Baradari) erected by Shah Jahan", "fee": "Free", "time": "2 hrs"},
                {"name": "Adhai Din Ka Jhonpra", "category": "Indo-Islamic Ruin", "highlight": "12th-century Sanskrit college converted into ornate mosque in 2.5 days", "fee": "Free", "time": "1 hr"}
            ],
            [
                {"name": "Attending Soulful Evening Qawwali at Dargah Sharif", "category": "Sufi Music", "cost": 0, "duration": "2 hrs"},
                {"name": "Boating and Sunset Walk on Ana Sagar Promenade", "category": "Boating", "cost": 150, "duration": "1.5 hrs"},
                {"name": "Trek up to Historic Taragarh Fort", "category": "Fort Trek", "cost": 0, "duration": "2.5 hrs"}
            ],
            [
                {"name": "Pratap Mahal (IHCL SeleQtions)", "category": "Luxury Heritage Resort", "price_per_night": 7500, "rating": 4.6, "area": "Jaipur-Ajmer Bypass", "amenities": ["Aravalli Pool", "Spa", "Lawn Courtyards"], "suitability": ["Couples", "Family"]},
                {"name": "The Royal Melange Beacon", "category": "Modern Comfort Hotel", "price_per_night": 2800, "rating": 4.2, "area": "Jaipur Road", "amenities": ["Restaurant", "Free WiFi", "AC"], "suitability": ["Family", "Business"]},
                {"name": "Hotel Cross Road", "category": "Budget Pilgrim Stay", "price_per_night": 1400, "rating": 4.1, "area": "Near Station / Dargah", "amenities": ["Room Service", "WiFi"], "suitability": ["Solo", "Family"]}
            ],
            [
                {"name": "Madani Dhaba & Restaurant", "cuisine": "Mughlai Biryani & Kebabs", "average_cost_for_two": 600, "rating": 4.6, "area": "Dargah Bazaar", "popular_dishes": "Mutton Biryani, Chicken Korma, Sheermal", "is_veg": False},
                {"name": "Mango Masala", "cuisine": "Vegetarian Multi-Cuisine & Pizza", "average_cost_for_two": 650, "rating": 4.4, "area": "Sardar Patel Marg", "popular_dishes": "Sizzler Platter, Paneer Tikka, Dosa", "is_veg": True},
                {"name": "Mahadev Sohan Halwa", "cuisine": "Heritage Halwa & Sweets", "average_cost_for_two": 200, "rating": 4.7, "area": "Dargah Bazaar", "popular_dishes": "Karachi Halwa, Sohan Halwa", "is_veg": True}
            ]
        ),
        make_destination(
            "Mount Abu", "Rajasthan's Only Hill Station & Dilwara Temples",
            "Lush forested oasis at 4,000 ft, marble craftsmanship of the Dilwara Jain Temples, Nakki Lake boating, and sunset rock points.",
            2000, "Year-round", "2 Days", 4.6, 9.0, "Highland Lake Retreat & Marble Art", ["Couples", "Family", "Friends"], "Mount Abu",
            ["Nakki Lake", "Dilwara Temples", "Guru Shikhar", "Sunset Point"],
            [
                {"name": "Dilwara Jain Temples", "category": "Marble Temple Masterpiece", "highlight": "11th-13th century temples with filigree marble ceilings unmatched globally", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Nakki Lake", "category": "Sacred Hill Lake", "highlight": "Fabled lake dug out by gods using fingernails; paddle boating and Toad Rock", "fee": "Free", "time": "2 hrs"},
                {"name": "Guru Shikhar Peak", "category": "Highest Aravalli Peak", "highlight": "Summit peak (5,650 ft) with temple of Dattatreya and valley views", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Paddle Boating on Nakki Lake", "category": "Lake Boating", "cost": 150, "duration": "1 hr"},
                {"name": "Sunset Viewing from Sunset Point Rocks", "category": "Sunset Viewpoint", "cost": 0, "duration": "1.5 hrs"},
                {"name": "Hike up to Toad Rock", "category": "Rock Hike", "cost": 0, "duration": "1 hr"}
            ],
            [
                {"name": "WelcomHeritage Connaught House", "category": "Colonial Heritage Cottage", "price_per_night": 7200, "rating": 4.6, "area": "Rajendra Marg", "amenities": ["English Gardens", "Fireplaces", "Tea Lounge"], "suitability": ["Couples", "Family"]},
                {"name": "Hotel Hillock", "category": "Premium Hill Resort", "price_per_night": 4800, "rating": 4.4, "area": "Near Nakki Lake", "amenities": ["Pool", "Gardens", "Multi-cuisine Bar"], "suitability": ["Family", "Couples"]},
                {"name": "Chacha Inn - The Fun Resort", "category": "Family Adventure Resort", "price_per_night": 4200, "rating": 4.3, "area": "Main Road", "amenities": ["Garden Waterfall", "Children Play", "Bar"], "suitability": ["Family", "Friends"]}
            ],
            [
                {"name": "Arbuda Restaurant", "cuisine": "North Indian & Gujarati Thali", "average_cost_for_two": 600, "rating": 4.5, "area": "Near Nakki Lake", "popular_dishes": "Gujarati Thali, Paneer Butter Masala, Garlic Naan", "is_veg": True},
                {"name": "Mulberry Tree Restaurant", "cuisine": "Continental, Mughlai & Chinese", "average_cost_for_two": 850, "rating": 4.4, "area": "Near Bus Stand", "popular_dishes": "Chicken Tikka, Pasta, Dal Tadka", "is_veg": False},
                {"name": "Chacha Cafe", "cuisine": "Snacks & Ice Cream", "average_cost_for_two": 350, "rating": 4.2, "area": "Main Market", "popular_dishes": "Sizzling Brownie, Pizza, Masala Chai", "is_veg": True}
            ]
        ),
        make_destination(
            "Bikaner", "The Camel Country & Junagarh Citadel",
            "Unconquered Junagarh Fort, Karni Mata (Rat Temple) of Deshnoke, famous Bikaneri Bhujia, and ICAR National Camel Breeding Farm.",
            1900, "Oct–Mar", "2 Days", 4.6, 8.9, "Desert Forts & Heritage Cuisine", ["Family", "Solo", "Couples"], "Bikaner",
            ["Junagarh Fort", "Lalgarh Palace", "Deshnoke Rat Temple", "Camel Research Farm"],
            [
                {"name": "Junagarh Fort", "category": "Unconquered Desert Fort", "highlight": "16th-century fortress decorated with Italian marble, lacquerwork, and gold leaf", "fee": "₹50", "time": "3 hrs"},
                {"name": "Karni Mata Temple (Deshnoke)", "category": "Sacred White Rat Temple", "highlight": "Ancient temple revered for 25,000 sacred black rats and auspicious white rats", "fee": "Free", "time": "2 hrs"},
                {"name": "National Research Centre on Camel", "category": "Camel Research Centre", "highlight": "Asia's only camel breeding centre with camel milk ice cream parlor", "fee": "₹50", "time": "2 hrs"}
            ],
            [
                {"name": "Tasting Fresh Camel Milk Ice Cream and Kulfi", "category": "Culinary Curiosity", "cost": 50, "duration": "1 hr"},
                {"name": "Sand Dune Camel Cart Safari in Bikaner Outskirts", "category": "Camel Safari", "cost": 600, "duration": "2 hrs"},
                {"name": "Shopping for Authentic Bikaneri Bhujia & Rasgullas", "category": "Food Trail", "cost": 0, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Narendra Bhawan Bikaner", "category": "Grand Heritage Boutique Hotel", "price_per_night": 11000, "rating": 4.8, "area": "Samvit Shiksha Kendra Road", "amenities": ["Rooftop Infinity Pool", "Literary Lounge", "Fine Dining"], "suitability": ["Couples", "Family"]},
                {"name": "Laxmi Niwas Palace", "category": "Indo-Saracenic Royal Palace", "price_per_night": 9000, "rating": 4.7, "area": "Lalgarh Campus", "amenities": ["Royal Courtyard", "Billiards Room", "Lawns"], "suitability": ["Couples", "Family"]},
                {"name": "Hotel Sagar", "category": "Heritage Comfort Stay", "price_per_night": 2500, "rating": 4.2, "area": "Lalgarh Palace Complex", "amenities": ["Courtyard", "Restaurant", "WiFi"], "suitability": ["Family", "Solo"]}
            ],
            [
                {"name": "Chhotu Motu Joshi Sweet Shop", "cuisine": "Legendary Marwari Breakfast", "average_cost_for_two": 250, "rating": 4.7, "area": "Station Road", "popular_dishes": "Poori Bhaaji with Sweet Bundi, Samosa, Rasgulla", "is_veg": True},
                {"name": "Bhikharam Chandmal", "cuisine": "World Famous Bhujia & Namkeen", "average_cost_for_two": 300, "rating": 4.8, "area": "Kote Gate", "popular_dishes": "Authentic Bikaneri Bhujia, Rasgulla, Ghewar", "is_veg": True},
                {"name": "Gallops Restaurant", "cuisine": "Rajasthani & Continental", "average_cost_for_two": 800, "rating": 4.4, "area": "Opposite Junagarh Fort", "popular_dishes": "Gatta Curry, Chicken Junglee, Cold Coffee", "is_veg": False}
            ]
        )
    ]
}

# ── 26. Uttar Pradesh ─────────────────────────────────────────────────────────
NORTH_STATES["Uttar Pradesh"] = {
    "capital": "Lucknow", "region": "North", "tagline": "The Cradle of Indic Heritage & Nawabi Grace",
    "destinations": [
        make_destination(
            "Varanasi (Kashi)", "The Spiritual Capital of the World",
            "Oldest living city on earth, sacred Ganga ghats, transcendental evening Maha Aarti, Kashi Vishwanath temple, and Banarasi silk sarees.",
            1800, "Oct–Mar", "3 Days", 4.9, 10.0, "Spiritual Transcendence & Ancient Ghats", ["Solo", "Family", "Couples", "Senior Citizens"], "Varanasi",
            ["Dashashwamedh & Assi Ghats", "Kashi Vishwanath Corridor", "Sarnath", "Godowlia Market"],
            [
                {"name": "Kashi Vishwanath Temple & Corridor", "category": "Jyotirlinga Sanctum", "highlight": "Golden spires of Lord Shiva's holy jyotirlinga connecting directly to the Ganga", "fee": "Free", "time": "2 hrs"},
                {"name": "Dashashwamedh Ghat Evening Ganga Aarti", "category": "Sacred Ceremony", "highlight": "Mesmerizing multi-tiered brass lamp ritual chanting mantras with thousands of diyas", "fee": "Free", "time": "2 hrs"},
                {"name": "Assi Ghat & Subah-e-Banaras", "category": "Sacred Morning Ghat", "highlight": "Sunrise yoga, classical sitar recitals, and boat departures", "fee": "Free", "time": "2 hrs"},
                {"name": "Sarnath Dhamek Stupa & Deer Park", "category": "Buddhist Sacred Site", "highlight": "Where Lord Buddha preached his first sermon after enlightenment", "fee": "₹25", "time": "3 hrs"}
            ],
            [
                {"name": "Sunrise Hand-Rowed Boat Ride on the Ganga", "category": "Boat Experience", "cost": 300, "duration": "2 hrs"},
                {"name": "Ancient Kashi Alley Food Walk (Kachori, Jalebi & Lassi)", "category": "Culinary Walk", "cost": 250, "duration": "2 hrs"},
                {"name": "Banarasi Handloom Weaving Tour", "category": "Artisan Silk", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "BrijRama Palace, Varanasi", "category": "Luxury Heritage Fortress on Ghats", "price_per_night": 26000, "rating": 4.9, "area": "Darbhanga Ghat", "amenities": ["Private Boat Transfer", "Live Classical Sitar", "Pure Vegetarian Gourmet"], "suitability": ["Couples", "Family"]},
                {"name": "Taj Ganges, Varanasi", "category": "Luxury 5-Star Hotel", "price_per_night": 14000, "rating": 4.8, "area": "Nadesar Palace Grounds", "amenities": ["Swimming Pool", "Jiva Spa", "Lush Lawns"], "suitability": ["Couples", "Family"]},
                {"name": "Zostel Varanasi", "category": "Backpacker Hostel", "price_per_night": 750, "rating": 4.6, "area": "Near Dashashwamedh", "amenities": ["Rooftop Cafe", "AC Dorms", "Walking Tours"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Blue Lassi Shop", "cuisine": "Legendary Artisan Lassi", "average_cost_for_two": 200, "rating": 4.8, "area": "Bangali Tola", "popular_dishes": "Pomegranate Pistachio Lassi, Mango Rabri Lassi", "is_veg": True},
                {"name": "Ram Bhandar", "cuisine": "Banarasi Breakfast Legend", "average_cost_for_two": 150, "rating": 4.8, "area": "Thatheri Bazaar", "popular_dishes": "Kachori Sabzi, Crispy Hot Jalebis", "is_veg": True},
                {"name": "Kashi Chat Bhandar", "cuisine": "Famous Banarasi Chaat", "average_cost_for_two": 250, "rating": 4.7, "area": "Godowlia", "popular_dishes": "Tamatar Chaat, Palak Patta Chaat, Gulab Jamun", "is_veg": True}
            ]
        ),
        make_destination(
            "Agra", "The City of the Taj & Mughal Splendour",
            "The Taj Mahal—wonder of the world, mighty Agra Fort, red sandstone Fatehpur Sikri, and famous Agra petha sweets.",
            2200, "Oct–Mar", "2 Days", 4.9, 10.0, "Mughal Wonder & UNESCO Monuments", ["Couples", "Family", "Solo"], "Agra",
            ["Taj Ganj & East Gate", "Agra Fort Enclave", "Fatehpur Sikri", "Sadar Bazaar"],
            [
                {"name": "Taj Mahal", "category": "Wonder of the World", "highlight": "Shah Jahan's white marble monument to eternal love shimmering in sunrise light", "fee": "₹50", "time": "3 hrs"},
                {"name": "Agra Fort (Red Fort)", "category": "Mughal Citadel", "highlight": "Mighty red sandstone fortress where Shah Jahan spent his final years gazing at the Taj", "fee": "₹50", "time": "2.5 hrs"},
                {"name": "Fatehpur Sikri", "category": "Imperial Mughal Ghost City", "highlight": "Akbar's 16th-century imperial city with soaring Buland Darwaza and Salim Chishti tomb", "fee": "₹50", "time": "3 hrs"},
                {"name": "Mehtab Bagh (Moonlight Garden)", "category": "Mughal Charbagh Garden", "highlight": "Riverbank park with reflection views of the Taj Mahal across the Yamuna", "fee": "₹25", "time": "1.5 hrs"}
            ],
            [
                {"name": "Sunrise Photography Session at Taj Mahal", "category": "Photography Walk", "cost": 50, "duration": "2.5 hrs"},
                {"name": "Sunset Boat View of Taj from Yamuna Bank", "category": "Sunset Experience", "cost": 200, "duration": "1 hr"},
                {"name": "Petha & Street Food Tasting in Sadar Bazaar", "category": "Food Trail", "cost": 150, "duration": "1.5 hrs"}
            ],
            [
                {"name": "The Oberoi Amarvilas, Agra", "category": "Luxury 5-Star with Taj Views", "price_per_night": 48000, "rating": 5.0, "area": "Taj East Gate Road", "amenities": ["Unobstructed Taj Views from Every Room", "Spa", "Pool"], "suitability": ["Couples"]},
                {"name": "ITC Mughal, A Luxury Collection Hotel", "category": "5-Star Mughal Resort", "price_per_night": 9500, "rating": 4.7, "area": "Fatehabad Road", "amenities": ["Kaya Kalp Spa", "Pool", "Lush Lawns"], "suitability": ["Family", "Couples"]},
                {"name": "Zostel Agra", "category": "Backpacker Hostel", "price_per_night": 700, "rating": 4.5, "area": "Taj Ganj", "amenities": ["Rooftop Cafe", "Taj Views", "Free WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Pinch of Spice", "cuisine": "North Indian, Mughlai & Bar", "average_cost_for_two": 1300, "rating": 4.6, "area": "Fatehabad Road", "popular_dishes": "Murg Boti Masala, Dal Makhani, Paneer Lababdar", "is_veg": False},
                {"name": "Panchi Petha Store", "cuisine": "Legendary Agra Sweets", "average_cost_for_two": 250, "rating": 4.8, "area": "Sadar Bazaar", "popular_dishes": "Angoori Petha, Kesar Petha, Paan Petha, Dalmoth", "is_veg": True},
                {"name": "Joney's Place", "cuisine": "Budget Cafe & Lassi", "average_cost_for_two": 350, "rating": 4.5, "area": "Taj Ganj", "popular_dishes": "Special Lassi, Banana Pancakes, Masala Chai", "is_veg": True}
            ]
        ),
        make_destination(
            "Lucknow", "The City of Nawabs & Awadhi Gastronomy",
            "Grand Bara Imambara labyrinth (Bhool Bhulaiya), Rumi Darwaza, melting Galouti kebabs, and exquisite Chikankari embroidery.",
            2000, "Oct–Mar", "3 Days", 4.8, 9.6, "Nawabi Architecture & Haute Cuisine", ["Family", "Solo", "Couples"], "Lucknow",
            ["Old City & Chowk", "Hazratganj", "Gomti Nagar", "Aminabad"],
            [
                {"name": "Bara Imambara & Bhool Bhulaiya", "category": "Nawabi Architectural Marvel", "highlight": "Vast arched hall built without beams and incredible acoustic mystery labyrinth", "fee": "₹50", "time": "3 hrs"},
                {"name": "Rumi Darwaza & Chhota Imambara", "category": "Nawabi Gateway", "highlight": "Majestic 60-ft Ottoman-inspired archway and chandelier palace", "fee": "₹50", "time": "2 hrs"},
                {"name": "British Residency Ruins", "category": "Historical Ruins & Memorial", "highlight": "Preserved 1857 siege ruins with cannon marks in serene landscaped gardens", "fee": "₹25", "time": "2 hrs"},
                {"name": "Ambedkar Memorial Park", "category": "Modern Monumental Park", "highlight": "Massive red sandstone stupa plaza with elephant statues in Gomti Nagar", "fee": "₹20", "time": "1.5 hrs"}
            ],
            [
                {"name": "Navigating the Acoustic Bhool Bhulaiya Maze", "category": "Heritage Discovery", "cost": 100, "duration": "1.5 hrs"},
                {"name": "Legendary Awadhi Kebab Trail in Chowk & Aminabad", "category": "Culinary Tour", "cost": 500, "duration": "3 hrs"},
                {"name": "Chikankari Handloom Shopping in Chowk", "category": "Textile Trail", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "Taj Mahal Lucknow", "category": "Luxury 5-Star Hotel", "price_per_night": 9000, "rating": 4.8, "area": "Gomti Nagar", "amenities": ["Pool", "Spa", "Lush Lawns"], "suitability": ["Couples", "Family", "Business"]},
                {"name": "The Clarks Avadh", "category": "Classic Heritage Stay", "price_per_night": 4500, "rating": 4.4, "area": "MG Marg, Hazratganj", "amenities": ["Rooftop River View", "Restaurant", "WiFi"], "suitability": ["Family", "Business"]},
                {"name": "Lebua Lucknow (Saraca Estate)", "category": "Heritage Art Deco Boutique", "price_per_night": 7500, "rating": 4.7, "area": "Mall Avenue", "amenities": ["Courtyard Dining", "Pool", "Spa"], "suitability": ["Couples", "Family"]}
            ],
            [
                {"name": "Tunday Kababi", "cuisine": "World-Famous Awadhi Kebabs", "average_cost_for_two": 500, "rating": 4.9, "area": "Aminabad / Chowk", "popular_dishes": "Galouti Kebab with Ulte Tawe ka Paratha, Mutton Biryani", "is_veg": False},
                {"name": "Dastarkhwan", "cuisine": "Authentic Mughlai & Awadhi", "average_cost_for_two": 800, "rating": 4.7, "area": "Hazratganj / Lalbagh", "popular_dishes": "Mughlai Chicken, Boti Kebab, Shahi Tukda", "is_veg": False},
                {"name": "Shukla Chaat House", "cuisine": "Street Chaat Legend", "average_cost_for_two": 200, "rating": 4.7, "area": "Hazratganj", "popular_dishes": "Matar Chaat, Aloo Tikki in Desi Ghee, Pani Puri", "is_veg": True}
            ]
        ),
        make_destination(
            "Ayodhya", "The Sacred Birthplace of Lord Rama",
            "The magnificent new Shri Ram Janmabhoomi Mandir, holy Sarayu river ghats, Hanuman Garhi fortress shrine, and spiritual Ramkot.",
            1500, "Oct–Mar", "2 Days", 4.8, 9.7, "Sacred Pilgrimage & Epic Heritage", ["Family", "Senior Citizens", "Solo"], "Ayodhya",
            ["Ram Janmabhoomi Complex", "Hanuman Garhi", "Ram Ki Paidi & Sarayu Ghats", "Kanak Bhawan"],
            [
                {"name": "Shri Ram Janmabhoomi Mandir", "category": "Nagara Style Temple Complex", "highlight": "Majestic carved pink sandstone temple complex dedicated to Lord Ram", "fee": "Free", "time": "3 hrs"},
                {"name": "Hanuman Garhi Fort Temple", "category": "Hilltop Fortress Temple", "highlight": "76-step fortified shrine housing childhood deity of Lord Hanuman", "fee": "Free", "time": "1.5 hrs"},
                {"name": "Ram Ki Paidi & Sarayu River Ghats", "category": "Sacred Steps & Deepotsav", "highlight": "Bathing ghats world-famous for record millions of oil lamps and evening Aarti", "fee": "Free", "time": "2 hrs"},
                {"name": "Kanak Bhawan (Golden Palace)", "category": "Ornate Palace Temple", "highlight": "Gilded shrine gifted to Devi Sita by Queen Kaikeyi upon marriage", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Sarayu River Evening Maha Aarti at Ram Ki Paidi", "category": "Spiritual Ceremony", "cost": 0, "duration": "1.5 hrs"},
                {"name": "Electric Boat Ride on the Sarayu River", "category": "River Boating", "cost": 150, "duration": "1 hr"},
                {"name": "Heritage Walk through Ramkot Temple Alleys", "category": "Heritage Walk", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "Park Inn by Radisson Ayodhya", "category": "Modern Premium Hotel", "price_per_night": 7000, "rating": 4.6, "area": "NH-27 Highway", "amenities": ["Pure Veg Dining", "WiFi", "Gym"], "suitability": ["Family", "Senior Citizens"]},
                {"name": "Cygnett Collection KK Hotel", "category": "Comfort Hotel", "price_per_night": 4200, "rating": 4.3, "area": "Naya Ghat", "amenities": ["Vegetarian Restaurant", "AC", "WiFi"], "suitability": ["Family", "Senior Citizens"]},
                {"name": "Hotel Ramprastha", "category": "Pilgrim Heritage Stay", "price_per_night": 2200, "rating": 4.1, "area": "Ram Ki Paidi Road", "amenities": ["River Proximity", "Room Service"], "suitability": ["Solo", "Family"]}
            ],
            [
                {"name": "Makhan Malai & Sita Rasoi", "cuisine": "Pure Sattvic Vegetarian Thali", "average_cost_for_two": 450, "rating": 4.6, "area": "Ram Path", "popular_dishes": "Awadhi Thali, Poori Sabzi, Rabri Jalebi", "is_veg": True},
                {"name": "Maurya Mishthan Bhandar", "cuisine": "Traditional Sweets & Chaat", "average_cost_for_two": 200, "rating": 4.5, "area": "Near Hanuman Garhi", "popular_dishes": "Laddoo, Khoya Peda, Samosa Chaat", "is_veg": True},
                {"name": "Chandra Sweet House", "cuisine": "Sweets, Lassi & Breakfast", "average_cost_for_two": 250, "rating": 4.4, "area": "Naya Ghat", "popular_dishes": "Dahi Jalebi, Matar Kachori, Sweet Lassi", "is_veg": True}
            ]
        ),
        make_destination(
            "Mathura & Vrindavan", "Brajbhoomi & The Eternal Leela of Krishna",
            "Shri Krishna Janmabhoomi, radiant Prem Mandir illuminated in neon colours, Banke Bihari temple melodies, and fragrant pedas.",
            1500, "Oct–Mar", "2 Days", 4.8, 9.6, "Devotional Krishna Pilgrimage", ["Family", "Senior Citizens", "Couples", "Solo"], "Mathura",
            ["Krishna Janmabhoomi", "Prem Mandir", "Banke Bihari Alleys", "ISKCON Vrindavan"],
            [
                {"name": "Shri Krishna Janmabhoomi Complex", "category": "Sacred Birthplace Temple", "highlight": "Ancient stone prison cell where Lord Krishna manifested at midnight", "fee": "Free", "time": "2 hrs"},
                {"name": "Prem Mandir (Vrindavan)", "category": "Italian White Marble Temple", "highlight": "Carved white marble shrine with spectacular multi-colour musical fountain show", "fee": "Free", "time": "2 hrs"},
                {"name": "Banke Bihari Temple", "category": "Devotional Sanctum", "highlight": "Famed for the curtain darshan ritual avoiding enchanting eye contact with Krishna", "fee": "Free", "time": "1.5 hrs"},
                {"name": "ISKCON Sri Sri Krishna Balaram Temple", "category": "Vibrant International Sanctum", "highlight": "Harmonious kirtan, marble courtyards, and samadhi shrine", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Evening Musical Fountain and Light Show at Prem Mandir", "category": "Light Show", "cost": 0, "duration": "1.5 hrs"},
                {"name": "Yamuna River Aarti at Vishram Ghat Mathura", "category": "Spiritual Aarti", "cost": 0, "duration": "1 hr"},
                {"name": "Parikrama Walk of Govardhan Hill (Optional)", "category": "Sacred Walk", "cost": 0, "duration": "5 hrs"}
            ],
            [
                {"name": "Nidhivan Sarovar Portico Vrindavan", "category": "Comfort 4-Star Pilgrim Hotel", "price_per_night": 4500, "rating": 4.5, "area": "Gopalgarh", "amenities": ["Pure Veg Restaurant", "Spa", "Lawn"], "suitability": ["Family", "Senior Citizens"]},
                {"name": "The Radha Ashok Mathura", "category": "Boutique Resort", "price_per_night": 3800, "rating": 4.3, "area": "NH-2 Bypass", "amenities": ["Pool", "Gardens", "Restaurant"], "suitability": ["Family", "Couples"]},
                {"name": "MVT Guesthouse & Restaurant", "category": "Peaceful Spiritual Retreat", "price_per_night": 2200, "rating": 4.6, "area": "Near ISKCON Vrindavan", "amenities": ["Lush Garden", "Pure Sattvic Cafe", "WiFi"], "suitability": ["Solo", "Couples"]}
            ],
            [
                {"name": "Brijwasi Mithai Wala", "cuisine": "Legendary Mathura Pedas & Snacks", "average_cost_for_two": 300, "rating": 4.8, "area": "Holi Gate, Mathura", "popular_dishes": "Mathura Ke Peda, Rabri, Khasta Kachori with Aloo Jhol", "is_veg": True},
                {"name": "Govinda's Restaurant (ISKCON)", "cuisine": "Pure Sattvic Multi-Cuisine Buffet", "average_cost_for_two": 600, "rating": 4.7, "area": "ISKCON Vrindavan", "popular_dishes": "Sattvic Thali, Paneer Malai Kofta, Gulab Jamun", "is_veg": True},
                {"name": "Shankar Mithai Bhandar", "cuisine": "Traditional Street Breakfast", "average_cost_for_two": 150, "rating": 4.6, "area": "Chowk Bazaar", "popular_dishes": "Kachori Jalebi, Lassi in Kulhad", "is_veg": True}
            ]
        ),
        make_destination(
            "Prayagraj (Allahabad)", "Triveni Sangam & Grand Kumbh City",
            "The sacred confluence of Ganga, Yamuna, and invisible Saraswati, majestic Akbar's Fort, Anand Bhawan, and colonial parks.",
            1600, "Oct–Mar", "2 Days", 4.7, 9.3, "Sacred Confluence & Nationalist Heritage", ["Family", "Senior Citizens", "Solo"], "Allahabad",
            ["Triveni Sangam Ghats", "Allahabad Fort & Akshayavat", "Civil Lines", "Anand Bhawan"],
            [
                {"name": "Triveni Sangam", "category": "Sacred Triple River Confluence", "highlight": "Clear green Yamuna meeting pale mud Ganga where millions take holy dips", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Akbar's Fort & Sacred Akshayavat Tree", "category": "Mughal Fort & Immortal Banyan", "highlight": "Massive 1583 fort containing the subterranean Patalpuri temple and ancient banyan", "fee": "Free", "time": "2 hrs"},
                {"name": "Anand Bhawan & Swaraj Bhawan", "category": "Freedom Struggle Mansion", "highlight": "Ancestral home of the Nehru-Gandhi family filled with independence artifacts", "fee": "₹50", "time": "2 hrs"},
                {"name": "All Saints Cathedral (Patthar Girja)", "category": "Gothic Cathedral", "highlight": "Stunning 19th-century Victorian Gothic stone cathedral with stained glass", "fee": "Free", "time": "1 hr"}
            ],
            [
                {"name": "Wooden Boat Excursion to Sangam Point", "category": "Boat Experience", "cost": 250, "duration": "1.5 hrs"},
                {"name": "Evening Sangam Aarti Ceremony", "category": "Spiritual Aarti", "cost": 0, "duration": "1 hr"},
                {"name": "Civil Lines Colonial Heritage Walk", "category": "Walking Tour", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "Grand Continental Hotel Prayagraj", "category": "Comfort 4-Star Hotel", "price_per_night": 4500, "rating": 4.4, "area": "Civil Lines", "amenities": ["Pool", "Multi-Cuisine Restaurant", "Gym"], "suitability": ["Family", "Business"]},
                {"name": "Kanhashyam Hotel", "category": "Business Comfort Hotel", "price_per_night": 3800, "rating": 4.3, "area": "Civil Lines", "amenities": ["Fine Dining", "AC", "WiFi"], "suitability": ["Family", "Business"]},
                {"name": "Hotel Milan Palace", "category": "City Centre Stay", "price_per_night": 2600, "rating": 4.2, "area": "Civil Lines", "amenities": ["Restaurant", "WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Netram Moolchand & Sons", "cuisine": "Legendary Breakfast & Sweets", "average_cost_for_two": 300, "rating": 4.7, "area": "Katra", "popular_dishes": "Poori Thali in Desi Ghee with 3 Sabzis, Gulab Jamun", "is_veg": True},
                {"name": "Sainik Foods / El Chico", "cuisine": "Continental, Mughlai & Bakery", "average_cost_for_two": 900, "rating": 4.6, "area": "Civil Lines", "popular_dishes": "Baked Fish, Butter Chicken, Pastries", "is_veg": False},
                {"name": "Loknath Chaat Gali", "cuisine": "Street Chaat & Dahi Jalebi", "average_cost_for_two": 200, "rating": 4.6, "area": "Old Katra / Chowk", "popular_dishes": "Samosa Chaat, Dahi Jalebi, Hariya ki Lassi", "is_veg": True}
            ]
        )
    ]
}

# ── 27. Uttarakhand ───────────────────────────────────────────────────────────
NORTH_STATES["Uttarakhand"] = {
    "capital": "Dehradun", "region": "North", "tagline": "Simply Heaven & Devbhoomi",
    "destinations": [
        make_destination(
            "Rishikesh", "The Yoga Capital of the World & Ganga Rapids",
            "Emerald Ganga flowing through Himalayan foothills, world-class white water rafting, iconic suspension bridges, and Beatles Ashram.",
            1800, "Sep–Jun", "3 Days", 4.9, 9.9, "Yoga, River Adventure & Spirituality", ["Solo", "Friends", "Couples"], "Rishikesh",
            ["Tapovan", "Laxman Jhula & Ram Jhula", "Triveni Ghat", "Shivpuri Rapids"],
            [
                {"name": "Triveni Ghat Maha Aarti", "category": "Sacred Ganga Aarti", "highlight": "Resounding conch shells, Vedic chants, and floating oil lamps on the holy river", "fee": "Free", "time": "2 hrs"},
                {"name": "The Beatles Ashram (Chaurasi Kutia)", "category": "Pop Culture Heritage", "highlight": "Forest ashram where The Beatles composed the White Album in 1968", "fee": "₹150", "time": "2.5 hrs"},
                {"name": "Neer Garh Waterfall", "category": "Forest Cascade Trek", "highlight": "Tiered natural turquoise rock pools reached by a forest trail", "fee": "₹30", "time": "2.5 hrs"},
                {"name": "Ram Jhula & Laxman Jhula Bridges", "category": "Suspension Bridges", "highlight": "Iconic iron bridges connecting ashrams, temples, and yoga halls", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "White Water Rafting (16 km Shivpuri to Rishikesh)", "category": "Rafting Adventure", "cost": 1000, "duration": "3 hrs"},
                {"name": "India's Highest Bungee Jump at Mohan Chatti (83m)", "category": "Extreme Adventure", "cost": 3700, "duration": "2 hrs"},
                {"name": "Sunrise Yoga & Sound Healing Class in Tapovan", "category": "Yoga Wellness", "cost": 300, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Ananda in the Himalayas", "category": "World's Premier Luxury Wellness Palace", "price_per_night": 45000, "rating": 5.0, "area": "Narendra Nagar", "amenities": ["Ayurvedic Spa", "Yoga Pavilions", "Golf Course"], "suitability": ["Couples", "Solo"]},
                {"name": "Aloha On The Ganges", "category": "Riverside Premium Resort", "price_per_night": 9500, "rating": 4.7, "area": "Tapovan", "amenities": ["Infinity Pool overlooking Ganga", "Spa", "Gardens"], "suitability": ["Family", "Couples"]},
                {"name": "Zostel Rishikesh (Tapovan)", "category": "Backpacker Hostel", "price_per_night": 850, "rating": 4.6, "area": "Tapovan", "amenities": ["Rooftop Cafe", "AC Doms", "Yoga Deck"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Little Buddha Cafe", "cuisine": "Continental, Israeli & Smoothies", "average_cost_for_two": 700, "rating": 4.6, "area": "Laxman Jhula", "popular_dishes": "Falafel Platter, Woodfired Pizza, Banana Lassi, Ganga View", "is_veg": True},
                {"name": "The Beatles Cafe (Cafe Delmar)", "cuisine": "Vegan, Organic & Healthy Breakfast", "average_cost_for_two": 850, "rating": 4.7, "area": "Paidal Marg, Tapovan", "popular_dishes": "Vegan Burgers, Zucchini Pasta, Berry Smoothies", "is_veg": True},
                {"name": "Chotiwala Restaurant", "cuisine": "Classic Garhwali & North Indian Thali", "average_cost_for_two": 500, "rating": 4.4, "area": "Ram Jhula", "popular_dishes": "Garhwali Thali, Dal Makhani, Poori Sabzi", "is_veg": True}
            ]
        ),
        make_destination(
            "Nainital", "The City of Lakes & Kumaon Queen",
            "Emerald eye-shaped Naini Lake cradled by seven verdant hills, colonial boat clubs, cable car ropeway, and snow viewpoint.",
            2200, "Mar–Jun & Sep–Jan", "3 Days", 4.7, 9.6, "Himalayan Lake Romance", ["Couples", "Family", "Friends"], "Nainital",
            ["Mall Road & Naini Lake", "Tallital & Mallital", "Snow View Point", "Pangot Bird Sanctuary"],
            [
                {"name": "Naini Lake & Naina Devi Temple", "category": "Sacred Mountain Lake", "highlight": "Vibrant pedal boats and vintage yachts reflecting surrounding pine slopes", "fee": "Free", "time": "2 hrs"},
                {"name": "Snow View Point & Aerial Ropeway", "category": "Himalayan Viewpoint", "highlight": "Ropeway ride to panoramic views of Nanda Devi and Trishul peaks", "fee": "₹300", "time": "2 hrs"},
                {"name": "Nainital High Altitude Zoo", "category": "High-Altitude Wildlife", "highlight": "Encounter snow leopards, Himalayan black bears, and Tibetan wolves", "fee": "₹100", "time": "2 hrs"},
                {"name": "Pangot & Kilbury Bird Sanctuary", "category": "Birdwatching Valley", "highlight": "Dense oak and rhododendron forest home to 580 Himalayan bird species", "fee": "Free", "time": "3 hrs"}
            ],
            [
                {"name": "Yachting & Row Boating on Naini Lake", "category": "Boating", "cost": 250, "duration": "1 hr"},
                {"name": "Trek to Tiffin Top (Dorothy's Seat)", "category": "Mountain Hike", "cost": 0, "duration": "3 hrs"},
                {"name": "Evening Stroll along the Colonial Mall Road", "category": "Evening Leisure", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "The Naini Retreat by Leisure Hotels", "category": "Heritage Royal Palace Hotel", "price_per_night": 11000, "rating": 4.7, "area": "Ayarpatta Slopes", "amenities": ["Forest Views", "Antique Billiards", "Spa"], "suitability": ["Couples", "Family"]},
                {"name": "The Manu Maharani", "category": "Luxury 4-Star Resort", "price_per_night": 8500, "rating": 4.6, "area": "Grassmere Estate", "amenities": ["Lake Views", "Spa", "Olive Garden"], "suitability": ["Couples", "Family"]},
                {"name": "Zostel Plus Nainital", "category": "Boutique Hostel & Retreat", "price_per_night": 950, "rating": 4.6, "area": "Pangot Road", "amenities": ["Valley Deck", "Bonfire", "Cafe"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Sakley's Restaurant & Pastry Shop", "cuisine": "Continental, Steaks & Pastries", "average_cost_for_two": 900, "rating": 4.7, "area": "Mallital", "popular_dishes": "Apple Crumble Pie, Roast Chicken, Chocolate Truffle", "is_veg": False},
                {"name": "Zooby's Kitchen", "cuisine": "Mughlai, North Indian & Kumaoni", "average_cost_for_two": 750, "rating": 4.5, "area": "Mall Road", "popular_dishes": "Mutton Rogan Josh, Dal Makhani, Chicken Kanti", "is_veg": False},
                {"name": "Sonam Fast Food", "cuisine": "Tibetan Momos & Thukpa", "average_cost_for_two": 300, "rating": 4.6, "area": "Tibetan Market", "popular_dishes": "Mutton Momos, Veg Chowmein, Thukpa", "is_veg": False}
            ]
        ),
        make_destination(
            "Mussoorie", "Queen of the Hills & The Doon Valley Lookout",
            "Misty horse-drawn colonial mall road, roaring Kempty Falls, panoramic Gun Hill ropeway, and tranquil Landour bakehouses.",
            2300, "Mar–Jun & Sep–Jan", "3 Days", 4.7, 9.5, "Colonial Ridge Romance", ["Couples", "Family", "Friends"], "Mussoorie",
            ["The Mall Road", "Landour & Sister's Bazaar", "Kempty Falls", "Gun Hill"],
            [
                {"name": "Landour Heritage & Sister's Bazaar", "category": "Colonial Cantonment", "highlight": "Peaceful deodar walking trail, Chaar Dukan, and Ruskin Bond's home town", "fee": "Free", "time": "3 hrs"},
                {"name": "Kempty Falls", "category": "Mountain Waterfall", "highlight": "Iconic multi-tiered cascading waterfall with natural plunge pool", "fee": "Free", "time": "2 hrs"},
                {"name": "Gun Hill Point & Ropeway", "category": "Historic Viewpoint", "highlight": "Mussoorie's second-highest point offering vistas of the snow-bound Bandarpoonch", "fee": "₹150", "time": "1.5 hrs"},
                {"name": "Company Garden", "category": "Botanical Garden", "highlight": "Colourful floral garden, artificial waterfall, and paddle boating", "fee": "₹25", "time": "1.5 hrs"}
            ],
            [
                {"name": "Heritage Walk through Landour Pine Forest (Chaar Dukan)", "category": "Scenic Walk", "cost": 0, "duration": "3 hrs"},
                {"name": "Gun Hill Ropeway Cable Car Ride", "category": "Aerial Cable Car", "cost": 150, "duration": "1 hr"},
                {"name": "Tasting Fresh Jam & Cheese at Sister's Bazaar", "category": "Food Trail", "cost": 300, "duration": "1 hr"}
            ],
            [
                {"name": "JW Marriott Mussoorie Walnut Grove Resort & Spa", "category": "Luxury 5-Star Mountain Resort", "price_per_night": 28000, "rating": 4.9, "area": "Kempty Fall Road", "amenities": ["Indoor Heated Pool", "Cedar Spa", "Bowling Alley"], "suitability": ["Couples", "Family"]},
                {"name": "Rokeby Manor Landour", "category": "English Country Manor", "price_per_night": 14000, "rating": 4.8, "area": "Landour Cantonment", "amenities": ["Jacuzzi", "Fireplace Suites", "Tea Garden"], "suitability": ["Couples"]},
                {"name": "Zostel Mussoorie", "category": "Backpacker Stay", "price_per_night": 850, "rating": 4.5, "area": "Kempty Road", "amenities": ["Terrace Views", "Cafe", "WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Chaar Dukan / Anil's Cafe", "cuisine": "Mountain Comfort Snacks", "average_cost_for_two": 400, "rating": 4.7, "area": "Landour", "popular_dishes": "Waffles with Honey, Bun Omelette, Ginger Lemon Honey Tea", "is_veg": True},
                {"name": "Emily's at Rokeby Manor", "cuisine": "Continental, British & Indian", "average_cost_for_two": 1600, "rating": 4.7, "area": "Landour", "popular_dishes": "Shepherd's Pie, Mustard Crusted Chicken, Apple Pie", "is_veg": False},
                {"name": "Kalsang Friends Corner", "cuisine": "Tibetan, Thai & Chinese", "average_cost_for_two": 700, "rating": 4.6, "area": "Mall Road", "popular_dishes": "Devil Momos, Thukpa, Dragon Potatoes", "is_veg": False}
            ]
        ),
        make_destination(
            "Auli & Joshimath", "India's Skiing & Meadow Paradise",
            "Powder snow ski slopes, world's longest ropeway cable cars, panoramic 180-degree vistas of Nanda Devi peak, and alpine meadows (Bugyals).",
            3000, "Dec–Mar (Skiing) & May–Nov (Meadows)", "3 Days", 4.9, 9.4, "Alpine Skiing & High Himalaya Vistas", ["Couples", "Adventure", "Friends"], "Joshimath",
            ["Auli Ski Slopes", "Artificial Lake Auli", "Joshimath Town", "Gorson Bugyal"],
            [
                {"name": "Auli Ski Slopes & Ropeway", "category": "Premier Ski Resort", "highlight": "4-km cable car ropeway from Joshimath to powdery ski slopes at 10,000 ft", "fee": "₹1000", "time": "4 hrs"},
                {"name": "Gorson Bugyal Trek", "category": "Alpine Meadow Trek", "highlight": "Gentle 3-km trek across rolling green/snow meadows facing Nanda Devi (25,643 ft)", "fee": "Free", "time": "4 hrs"},
                {"name": "Auli Artificial Lake", "category": "High Altitude Lake", "highlight": "Pristine man-made snow-making reservoir reflecting sky and mountains", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Beginner Skiing & Snowboarding Lessons", "category": "Winter Sports", "cost": 2000, "duration": "3 hrs"},
                {"name": "Riding the Joshimath-Auli Aerial Tramway Cable Car", "category": "Aerial Cable Car", "cost": 1000, "duration": "1 hr"},
                {"name": "Day Trek to Gorson Bugyal Meadow", "category": "Himalayan Trek", "cost": 400, "duration": "4 hrs"}
            ],
            [
                {"name": "The Chardham Camp Auli", "category": "Luxury Alpine Camp", "price_per_night": 7500, "rating": 4.6, "area": "Auli Road", "amenities": ["Snow Views", "Heated Tents", "Dining"], "suitability": ["Couples", "Adventure"]},
                {"name": "Cliff Top Club Auli", "category": "Ski-in Ski-out Resort", "price_per_night": 8500, "rating": 4.4, "area": "Auli Top", "amenities": ["Slope Proximity", "Restaurant", "Ski Equipment Rental"], "suitability": ["Adventure", "Couples"]},
                {"name": "Blue Poppy Resorts", "category": "Wooden Alpine Cottages", "price_per_night": 5200, "rating": 4.5, "area": "Auli Laga Salude", "amenities": ["Wooden Architecture", "Heaters", "Panoramic Views"], "suitability": ["Couples", "Friends"]}
            ],
            [
                {"name": "Cliff Top Restaurant", "cuisine": "North Indian & Comfort Soups", "average_cost_for_two": 900, "rating": 4.3, "area": "Auli Slopes", "popular_dishes": "Hot Thukpa, Dal Tadka, Tandoori Parathas", "is_veg": False},
                {"name": "Auli 'D' Food Plaza", "cuisine": "Garhwali & Comfort Snacks", "average_cost_for_two": 500, "rating": 4.4, "area": "Near Chairlift", "popular_dishes": "Garhwali Chainsoo, Maggi with Cheese, Hot Masala Tea", "is_veg": True},
                {"name": "Marwari Bhojnalaya (Joshimath)", "cuisine": "Vegetarian Thali", "average_cost_for_two": 350, "rating": 4.4, "area": "Joshimath Market", "popular_dishes": "Pure Veg Thali, Kadhi Chawal, Kheer", "is_veg": True}
            ]
        ),
        make_destination(
            "Jim Corbett National Park", "India's First Tiger Sanctuary & Wilderness",
            "Dense sal forests along the Ramganga river, open-top 4x4 Jeep safaris, Royal Bengal Tigers, wild elephant herds, and luxury forest lodges.",
            3200, "Nov–Jun", "3 Days", 4.8, 9.7, "Wildlife Safari & Nature Lodges", ["Family", "Couples", "Friends"], "Ramnagar",
            ["Dhikala Zone", "Bijrani Zone", "Jhirna Zone", "Ramganga Riverbank"],
            [
                {"name": "Dhikala Forest Zone", "category": "Wild Savannah & Tiger Habitat", "highlight": "Famed grassland zone with the highest density of tigers and river elephants", "fee": "₹2000", "time": "4 hrs"},
                {"name": "Bijrani Safari Zone", "category": "Forest Safari Zone", "highlight": "Rich sal woods and waterways offering excellent tiger and leopard sightings", "fee": "₹1500", "time": "4 hrs"},
                {"name": "Corbett Waterfalls", "category": "Forest Waterfall", "highlight": "66-ft natural waterfall surrounded by thick teak jungle foliage", "fee": "₹50", "time": "1.5 hrs"},
                {"name": "Garjiya Devi Temple", "category": "River Rock Shrine", "highlight": "Sacred shrine perched atop a monolithic rock in the middle of Kosi river", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Open-Top 4x4 Jeep Safari in Bijrani / Jhirna", "category": "Wildlife Safari", "cost": 4500, "duration": "4 hrs"},
                {"name": "Canter Safari in Dhikala Grasslands", "category": "Canter Safari", "cost": 1800, "duration": "4.5 hrs"},
                {"name": "Riverside Birdwatching & Nature Walk with Naturalist", "category": "Birdwatching", "cost": 600, "duration": "2 hrs"}
            ],
            [
                {"name": "Taj Corbett Resort & Spa, Uttarakhand", "category": "Luxury 5-Star River Lodge", "price_per_night": 18000, "rating": 4.8, "area": "Zero Garjia, Dhikuli", "amenities": ["Kosi Riverbank", "Jiva Spa", "Pool", "Wilderness Dining"], "suitability": ["Couples", "Family"]},
                {"name": "Aahana - The Corbett Wilderness", "category": "Eco-Luxury Resort", "price_per_night": 14000, "rating": 4.9, "area": "Sawaldeh", "amenities": ["Organic Farm", "Pool", "Naturo-Therapy Spa"], "suitability": ["Family", "Couples"]},
                {"name": "The Solluna Resort", "category": "Riverside Pebble Resort", "price_per_night": 7500, "rating": 4.5, "area": "Marchula Valley", "amenities": ["River Views", "Outdoor Pool", "Campfires"], "suitability": ["Friends", "Family"]}
            ],
            [
                {"name": "Treetop Restaurant (Taj Corbett)", "cuisine": "Gourmet Kumaoni & Global", "average_cost_for_two": 2600, "rating": 4.8, "area": "Dhikuli", "popular_dishes": "Kumaoni Mutton Curry, Bhang ki Chutney, Grilled River Fish", "is_veg": False},
                {"name": "Corbett Machan Cafe", "cuisine": "North Indian & Barbecue", "average_cost_for_two": 900, "rating": 4.5, "area": "Ramnagar Road", "popular_dishes": "Butter Chicken, Dal Makhani, Paneer Tikka", "is_veg": False},
                {"name": "Village Vatika Restaurant", "cuisine": "Pure Vegetarian & Thali", "average_cost_for_two": 500, "rating": 4.4, "area": "Ramnagar", "popular_dishes": "Kumaoni Thali, Kadhai Paneer, Hot Gulab Jamun", "is_veg": True}
            ]
        )
    ]
}

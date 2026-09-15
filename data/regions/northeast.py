"""
Northeast India Tourism Dataset: Arunachal Pradesh, Assam, Manipur, Meghalaya, Mizoram, Nagaland, Sikkim, Tripura.
Every state features 4-5 authentic destinations with complete neighborhoods, places, activities, hotels, and dining.
"""
from data.regions.common import make_destination

NORTHEAST_STATES = {}

# ── 2. Arunachal Pradesh ──────────────────────────────────────────────────────
NORTHEAST_STATES["Arunachal Pradesh"] = {
    "capital": "Itanagar", "region": "Northeast", "tagline": "The Land of the Dawn-Lit Mountains",
    "destinations": [
        make_destination(
            "Tawang", "The Sacred Monastic Fortress & High Alpine Lakes",
            "India's largest Buddhist monastery at 10,000 ft, snowbound Sela Pass, crystal Madhuri Lake, and heroic Jaswant Garh war memorial.",
            2500, "Mar–Jun & Sep–Nov", "4 Days", 4.9, 9.8, "Buddhist Monasteries & High Altitude Passes", ["Adventure", "Couples", "Solo"], "Tawang",
            ["Tawang Monastery Complex", "Sela Pass & Lake", "Madhuri (Sangetsar) Lake", "War Memorial"],
            [
                {"name": "Tawang Monastery (Galden Namgyal Lhatse)", "category": "Second Largest Global Monastery", "highlight": "400-year-old fortified monastery housing 28-ft gilded Buddha and ancient Sanskrit manuscripts", "fee": "Free", "time": "3 hrs"},
                {"name": "Sela Pass (13,700 ft) & Sela Lake", "category": "High Alpine Snow Pass", "highlight": "Dramatic snow-choked mountain pass with twin frozen sapphire lakes and prayer flags", "fee": "Free", "time": "2 hrs"},
                {"name": "Madhuri (Sangetsar) Lake", "category": "Glacial Lake", "highlight": "Stunning high-altitude lake formed by an earthquake with submerged dead pine tree trunks", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Nuranang (Jang) Falls", "category": "Mountain Cascade", "highlight": "Colossal 100-meter roaring waterfall dropping into white spray along the Tawang river", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Early Morning Chanting & Horn Ceremony at Tawang Monastery", "category": "Spiritual Ceremony", "cost": 0, "duration": "1.5 hrs"},
                {"name": "Snow Walk at Sela Pass Crest", "category": "Alpine Experience", "cost": 0, "duration": "1 hr"},
                {"name": "Tasting Monpa Butter Tea (Suja) and Khura Breads", "category": "Culinary Experience", "cost": 100, "duration": "1 hr"}
            ],
            [
                {"name": "Dondrub Homestay & Resort", "category": "Authentic Monpa Luxury Stay", "price_per_night": 4500, "rating": 4.8, "area": "Near Monastery", "amenities": ["Valley Views", "Heated Blankets", "Organic Monpa Meals"], "suitability": ["Couples", "Family"]},
                {"name": "Hotel Pemaling Tawang", "category": "Comfort Mountain Hotel", "price_per_night": 3200, "rating": 4.4, "area": "Old Market", "amenities": ["Restaurant", "Heaters", "Free WiFi"], "suitability": ["Couples", "Solo"]},
                {"name": "Zostel Tawang", "category": "Backpacker Stay", "price_per_night": 900, "rating": 4.6, "area": "Main Town", "amenities": ["Rooftop Cafe", "Common Lounge", "WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Dragon Restaurant", "cuisine": "Authentic Monpa, Tibetan & Chinese", "average_cost_for_two": 550, "rating": 4.6, "area": "Old Market", "popular_dishes": "Thukpa, Zan (Monpa porridge with meat), Momos, Butter Tea", "is_veg": False},
                {"name": "Orange Restaurant", "cuisine": "Tibetan & Continental Breakfast", "average_cost_for_two": 450, "rating": 4.4, "area": "Nehru Market", "popular_dishes": "Thenthuk, Steamed Momos, Ginger Lemon Honey Tea", "is_veg": False},
                {"name": "Woodland Restaurant", "cuisine": "Indian & Local Comfort", "average_cost_for_two": 500, "rating": 4.3, "area": "Near War Memorial", "popular_dishes": "Chicken Curry, Rice, Momos", "is_veg": False}
            ]
        ),
        make_destination(
            "Ziro Valley", "Apatani Tribal Pine Valley & Music Haven",
            "UNESCO tentative valley home to the gentle Apatani tribe, intricate nose plugs, geometric paddy-fish farming, and Ziro Festival of Music.",
            2000, "Mar–Nov", "3 Days", 4.8, 9.5, "Indigenous Tribal Culture & Pine Valleys", ["Solo", "Couples", "Friends"], "Ziro",
            ["Hong Village", "Hari & Hija Villages", "Kardo Shiva Lingam", "Talley Valley Reserve"],
            [
                {"name": "Hong Apatani Village", "category": "UNESCO Tentative Tribal Village", "highlight": "Largest Apatani village with traditional bamboo houses and elders with facial tattoos and nose plugs (Yaping Hullo)", "fee": "Free", "time": "3 hrs"},
                {"name": "Talley Valley Wildlife Sanctuary", "category": "Biodiversity Hotspot", "highlight": "Subtropical evergreen forest home to the elusive clouded leopard and rare Pleioblastus bamboo", "fee": "₹50", "time": "4 hrs"},
                {"name": "Kardo Siddheshwar Nath Shiva Lingam", "category": "Natural Monolith Shrine", "highlight": "Naturally occurring 25-ft high monolithic rock Shivalinga discovered in dense jungle", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Apatani Village Cultural Walk & Rice Beer Tasting", "category": "Cultural Walk", "cost": 300, "duration": "3 hrs"},
                {"name": "Attending the Ziro Music Festival (September)", "category": "Music Festival", "cost": 2500, "duration": "Full Day"},
                {"name": "Trekking in the Giant Pine and Bamboo Groves", "category": "Nature Trek", "cost": 0, "duration": "2.5 hrs"}
            ],
            [
                {"name": "Ziro Palace Luxury Resort", "category": "Boutique Pine Valley Stay", "price_per_night": 4800, "rating": 4.6, "area": "Hapoli Road", "amenities": ["Paddy Field Views", "Restaurant", "Campfires"], "suitability": ["Couples", "Family"]},
                {"name": "Siiro Resort", "category": "Pine Forest Wooden Cottages", "price_per_night": 3200, "rating": 4.4, "area": "Siiro Village", "amenities": ["Wooden Fireplace", "Gardens", "Tribal Food"], "suitability": ["Couples", "Friends"]},
                {"name": "Abasa Homestay (Apatani Homestay)", "category": "Authentic Village Homestay", "price_per_night": 1800, "rating": 4.8, "area": "Siiro", "amenities": ["Cook with Host Family", "Organic Farm Food", "Fireplace"], "suitability": ["Solo", "Couples"]}
            ],
            [
                {"name": "Abasa Homestay Kitchen", "cuisine": "Authentic Apatani Tribal Feasts", "average_cost_for_two": 500, "rating": 4.9, "area": "Siiro Village", "popular_dishes": "Pike (Bamboo Shoot Stew), Piku Pila, Smoked Pork, Apong (Rice Beer)", "is_veg": False},
                {"name": "A&C Kitchen Hapoli", "cuisine": "Tibetan & North Eastern", "average_cost_for_two": 400, "rating": 4.4, "area": "Hapoli Market", "popular_dishes": "Fried Momos, Pork Ribs with Bamboo Shoot, Thukpa", "is_veg": False},
                {"name": "Misty Valley Cafe", "cuisine": "Cafe, Burgers & Coffee", "average_cost_for_two": 350, "rating": 4.3, "area": "Old Ziro", "popular_dishes": "Filter Coffee, Pancakes, Maggi", "is_veg": True}
            ]
        ),
        make_destination(
            "Dirang & Bomdila", "Orchard Valleys & Mountain Monasteries",
            "Serene kiwi and apple orchards of Sangti Valley, black-necked crane sanctuary, Dirang Dzong heritage fortress, and Bomdila Monastery.",
            1900, "Mar–Jun & Oct–Dec", "2 Days", 4.7, 9.0, "River Valleys, Orchards & Dzong Heritage", ["Family", "Couples", "Solo"], "Bomdila",
            ["Sangti Valley", "Dirang Dzong", "Bomdila Monastery", "Dirang Hot Springs"],
            [
                {"name": "Sangti Valley", "category": "Idyllic Alpine River Basin", "highlight": "Lush green pine valley with grazing sheep, river pebbles, and wintering black-necked cranes", "fee": "Free", "time": "3 hrs"},
                {"name": "Dirang Dzong", "category": "17th-Century Monpa Fortress", "highlight": "Ancient stone fortress village inhabited by Monpas with wooden balconies and Buddhist shrines", "fee": "Free", "time": "2 hrs"},
                {"name": "Bomdila Gontse Gaden Rabgyel Lhing Monastery", "category": "Tibetan Buddhist Complex", "highlight": "Grand monastery overlooking snow peaks with prayer wheels and butter lamp shrine", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Riverside Camping and Trout Fishing in Sangti River", "category": "Camping & Fishing", "cost": 800, "duration": "Half Day"},
                {"name": "Relaxing in Dirang Sulfur Hot Spring Baths", "category": "Thermal Springs", "cost": 0, "duration": "1.5 hrs"},
                {"name": "Kiwi & Apple Orchard Fruit Plucking", "category": "Agri-Tourism", "cost": 150, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Dirang Boutique Cottages", "category": "Riverside Boutique Stay", "price_per_night": 4500, "rating": 4.6, "area": "Sangti Road", "amenities": ["Riverfront Lawn", "Bonfire", "Organic Meals"], "suitability": ["Couples", "Family"]},
                {"name": "Pemaling Lords Eco Inn Dirang", "category": "Comfort Valley Hotel", "price_per_night": 3200, "rating": 4.4, "area": "Dirang Market", "amenities": ["Balcony Views", "Restaurant", "WiFi"], "suitability": ["Family", "Solo"]},
                {"name": "Hotel Tsepal Yangjom Bomdila", "category": "Boutique Heritage Hotel", "price_per_night": 2800, "rating": 4.3, "area": "Main Market Bomdila", "amenities": ["Traditional Wooden Decor", "Dining", "Room Heaters"], "suitability": ["Couples", "Friends"]}
            ],
            [
                {"name": "Sangti Valley River Cafe", "cuisine": "Local Monpa & Indian Comfort", "average_cost_for_two": 450, "rating": 4.6, "area": "Sangti Valley", "popular_dishes": "Fresh River Trout Fry, Steamed Momos, Khura", "is_veg": False},
                {"name": "Sikkim Restaurant Bomdila", "cuisine": "Tibetan & Sikkimese", "average_cost_for_two": 400, "rating": 4.4, "area": "Bomdila Bazaar", "popular_dishes": "Pork Momos, Thukpa, Chowmein", "is_veg": False},
                {"name": "Lha Gyari Restaurant", "cuisine": "Traditional North Eastern", "average_cost_for_two": 350, "rating": 4.2, "area": "Dirang Dzong Road", "popular_dishes": "Zan, Fried Rice, Chicken Curry", "is_veg": False}
            ]
        ),
        make_destination(
            "Itanagar", "The Capital of Forts & Green Valleys",
            "14th-century brick fortress (Ita Fort), tranquil Ganga Lake (Gyakar Sinyi), modern Donyi Polo tribal heritage museum, and Gompa temple.",
            1700, "Oct–Apr", "2 Days", 4.5, 8.6, "Tribal Heritage & Forest Lakes", ["Family", "Solo", "Business"], "Itanagar",
            ["Ita Fort Complex", "Ganga Lake (Gyakar Sinyi)", "State Museum", "Theravada Buddhist Gompa"],
            [
                {"name": "Ita Fort (Fort of Bricks)", "category": "14th-Century Brick Fortress", "highlight": "Ancient Chutiya dynasty brick fort covering 45,000 cubic metres built on hill slopes", "fee": "Free", "time": "2 hrs"},
                {"name": "Ganga Lake (Gyakar Sinyi)", "category": "Secluded Forest Lake", "highlight": "Emerald natural lake surrounded by orchids, tree ferns, and tall bamboo groves", "fee": "₹20", "time": "2.5 hrs"},
                {"name": "Jawaharlal Nehru State Museum", "category": "Tribal Ethnography Museum", "highlight": "Spectacular dioramas of 26 major tribes of Arunachal, weapons, textiles, and woodcarvings", "fee": "₹20", "time": "2 hrs"}
            ],
            [
                {"name": "Boating on Tranquil Ganga Lake Waters", "category": "Lake Boating", "cost": 100, "duration": "1.5 hrs"},
                {"name": "Handloom & Cane Handicraft Shopping at Craft Centre", "category": "Handicrafts", "cost": 0, "duration": "2 hrs"},
                {"name": "Sunset Prayer at Itanagar Buddhist Gompa", "category": "Spiritual Prayer", "cost": 0, "duration": "1 hr"}
            ],
            [
                {"name": "Hotel Donyi Polo Ashok", "category": "Premium Capital Stay", "price_per_night": 4200, "rating": 4.3, "area": "Sector C", "amenities": ["Restaurant", "Bar", "Gardens"], "suitability": ["Business", "Family"]},
                {"name": "Cygnett Inn Trendz Itanagar", "category": "Modern Business Hotel", "price_per_night": 3500, "rating": 4.4, "area": "Ganga Market", "amenities": ["Fitness Centre", "Multi-Cuisine Restaurant", "WiFi"], "suitability": ["Business", "Solo"]},
                {"name": "Hotel Todo", "category": "Comfort City Stay", "price_per_night": 2200, "rating": 4.1, "area": "Bank Tinali", "amenities": ["Restaurant", "AC", "WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Roots Kitchen Itanagar", "cuisine": "Authentic Tribal & Assamese", "average_cost_for_two": 600, "rating": 4.6, "area": "Bank Tinali", "popular_dishes": "Boiled Pork with Bamboo Shoots, Fish Cooked in Banana Leaf, Apong", "is_veg": False},
                {"name": "The Wok Chinese & Thai", "cuisine": "Pan-Asian & Tibetan", "average_cost_for_two": 700, "rating": 4.4, "area": "Ganga Market", "popular_dishes": "Dragon Chicken, Hakka Noodles, Steamed Momos", "is_veg": False},
                {"name": "Cafe ABC", "cuisine": "Coffee, Sandwiches & Desserts", "average_cost_for_two": 400, "rating": 4.5, "area": "Zero Point", "popular_dishes": "Cappuccino, Brownie with Ice Cream, Chicken Sandwich", "is_veg": True}
            ]
        )
    ]
}

# ── 3. Assam ──────────────────────────────────────────────────────────────────
NORTHEAST_STATES["Assam"] = {
    "capital": "Dispur", "region": "Northeast", "tagline": "The Land of the Red River & Blue Hills",
    "destinations": [
        make_destination(
            "Kaziranga National Park", "Home of the Great Indian One-Horned Rhinoceros",
            "UNESCO World Heritage sanctuary harboring two-thirds of the world's great one-horned rhinos, wild water buffalo, Asian elephants, and wetlands.",
            3000, "Nov–Apr", "3 Days", 4.9, 9.9, "UNESCO Wildlife Safari & Rhino Haven", ["Family", "Couples", "Adventure"], "Bokakhat",
            ["Kohora Central Range", "Bagori Western Range", "Kaziranga Orchid Park", "Burapahar Range"],
            [
                {"name": "Kaziranga National Park (Kohora & Bagori)", "category": "UNESCO World Heritage Reserve", "highlight": "Open elephant grass plains with prehistoric one-horned rhinos, royal tigers, and wild buffalo", "fee": "₹2500 (Jeep)", "time": "4.5 hrs"},
                {"name": "Kaziranga National Orchid & Biodiversity Park", "category": "Botanical & Folk Centre", "highlight": "Over 500 indigenous wild orchid species, traditional Bihu dances, and bamboo garden", "fee": "₹100", "time": "2.5 hrs"},
                {"name": "Kakochang Waterfalls", "category": "Jungle Cascade", "highlight": "Pristine waterfall surrounded by tea plantations and rubber gardens", "fee": "Free", "time": "3 hrs"}
            ],
            [
                {"name": "Early Morning Elephant Safari into Rhino Grasslands", "category": "Elephant Safari", "cost": 1000, "duration": "1 hr"},
                {"name": "Open 4x4 Jeep Safari through Bagori Swamp Range", "category": "Jeep Safari", "cost": 2500, "duration": "4 hrs"},
                {"name": "Authentic Assamese Thali Lunch at Kaziranga Orchid Park", "category": "Assamese Culinary Feast", "cost": 250, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Diphlu River Lodge", "category": "Ultra Luxury Eco-Safari Lodge", "price_per_night": 22000, "rating": 4.9, "area": "Kuthuri / Kaziranga", "amenities": ["River Diphlu Verandah", "Naturalist Safaris", "Bonfires"], "suitability": ["Couples", "Family"]},
                {"name": "Borgos Resort Kaziranga", "category": "Luxury 4-Star Resort", "price_per_night": 6800, "rating": 4.6, "area": "Kohora Central Range", "amenities": ["Outdoor Pool", "Spa", "Activity Lawn"], "suitability": ["Family", "Couples"]},
                {"name": "Wild Grass Lodge", "category": "Rustic Pioneer Safari Lodge", "price_per_night": 3200, "rating": 4.4, "area": "Kohora Village", "amenities": ["Colonial Ambiance", "Forest Grounds", "Restaurant"], "suitability": ["Friends", "Solo"]}
            ],
            [
                {"name": "Kaziranga Orchid Park Thali Kitchen", "cuisine": "30-Item Traditional Assamese Thali", "average_cost_for_two": 500, "rating": 4.8, "area": "Durgapur, Kohora", "popular_dishes": "Khar, Masor Tenga (Tangy Fish Curry), Duck Curry, Joha Rice, Pitha", "is_veg": False},
                {"name": "Mai-Hang Restaurant", "cuisine": "Authentic Assamese & Tribal Pork", "average_cost_for_two": 650, "rating": 4.6, "area": "Kohora Market", "popular_dishes": "Pork with Bamboo Shoot, Country Chicken Curry, Pitika", "is_veg": False},
                {"name": "Wild Grass Dining Room", "cuisine": "Continental & Assamese Home-Style", "average_cost_for_two": 700, "rating": 4.4, "area": "Wild Grass Lodge", "popular_dishes": "Roast Chicken, Rohu Curry, Dal with Herbs", "is_veg": False}
            ]
        ),
        make_destination(
            "Guwahati", "The Gateway to Northeast & Sacred Kamakhya",
            "Sacred Shakti Peetha Kamakhya Temple atop Nilachal Hill, mighty Brahmaputra river sunset cruises, and Umananda island temple.",
            2200, "Oct–Apr", "2 Days", 4.7, 9.6, "Shakti Pilgrimage & River Majesty", ["Family", "Solo", "Couples"], "Guwahati",
            ["Kamakhya Hill", "Uzan Bazaar Riverfront", "Umananda Island", "Beltola & GS Road"],
            [
                {"name": "Maa Kamakhya Devalaya", "category": "Ancient Tantric Shakti Peetha", "highlight": "One of India's oldest and most sacred 51 Shakti shrines celebrating divine feminine energy", "fee": "Free", "time": "3 hrs"},
                {"name": "Umananda Island & Peacock Island", "category": "World's Smallest Inhabited River Island", "highlight": "Lord Shiva temple in middle of the Brahmaputra reached by scenic ferry and home to golden langurs", "fee": "₹20 (Ferry)", "time": "2 hrs"},
                {"name": "Guwahati Ropeway over the Brahmaputra", "category": "Longest River Ropeway in India", "highlight": "1.8 km cable car gliding over the mighty river offering birds-eye views of river sands and islands", "fee": "₹150", "time": "1 hr"}
            ],
            [
                {"name": "Evening Sunset Dinner Cruise on the Brahmaputra (Alfresco Grand)", "category": "Dinner Cruise", "cost": 800, "duration": "2 hrs"},
                {"name": "Riding the Aerial Ropeway across the Brahmaputra", "category": "Ropeway Adventure", "cost": 150, "duration": "1 hr"},
                {"name": "Assamese Silk Shopping (Muga & Eri Silk) in Pan Bazaar", "category": "Textile Shopping", "cost": 0, "duration": "2 hrs"}
            ],
            [
                {"name": "Vivanta Guwahati", "category": "Luxury 5-Star Hotel", "price_per_night": 9500, "rating": 4.8, "area": "Khanapara, GS Road", "amenities": ["Outdoor Pool", "Jiva Spa", "Oriental Dining"], "suitability": ["Couples", "Family", "Business"]},
                {"name": "Radisson Blu Hotel Guwahati", "category": "Luxury 5-Star Hotel", "price_per_night": 8500, "rating": 4.7, "area": "NH-37 Gotanagar", "amenities": ["Lake Views", "Pool", "Spa"], "suitability": ["Business", "Family"]},
                {"name": "Brahmaputra Jungle Resort", "category": "Eco Hillside Resort", "price_per_night": 3400, "rating": 4.3, "area": "Near Sonapur", "amenities": ["Zip Lining", "Elephant Safari", "Lake"], "suitability": ["Friends", "Family"]}
            ],
            [
                {"name": "Paradise Restaurant", "cuisine": "Iconic Assamese Parampara Thali", "average_cost_for_two": 800, "rating": 4.7, "area": "Silpukhuri", "popular_dishes": "Assamese Thali, Masor Tenga, Duck Roast, Payox (Kheer)", "is_veg": False},
                {"name": "Khorikaa", "cuisine": "Traditional Charcoal Grilled Assamese", "average_cost_for_two": 600, "rating": 4.6, "area": "Ulubari, GS Road", "popular_dishes": "Smoked Pork Khorikaa, Chicken with Sesame Seeds, Koldil Curry", "is_veg": False},
                {"name": "The Guwahati Address", "cuisine": "Modern Fusion & Bakery", "average_cost_for_two": 750, "rating": 4.5, "area": "Zoo Road", "popular_dishes": "Woodfired Pizza, Filter Coffee, Red Velvet Cake", "is_veg": True}
            ]
        ),
        make_destination(
            "Majuli Island", "World's Largest River Island & Neo-Vaishnavite Satras",
            "UNESCO candidate island in the Brahmaputra, 500-year-old Neo-Vaishnavite Satras (monasteries), traditional mask making, and Mishing stilt huts.",
            1500, "Oct–Mar", "2 Days", 4.8, 9.4, "River Island Culture, Mask Art & Satras", ["Solo", "Couples", "Culture"], "Majuli",
            ["Kamalabari Satra", "Samaguri Mask Satra", "Auniati Satra", "Mishing Tribal Villages"],
            [
                {"name": "Samaguri Satra (Traditional Mask-Making)", "category": "Heritage Mask Craft", "highlight": "Ancient craft of crafting lifelike mythological masks out of bamboo, clay, and cow dung for Bhaona plays", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Auniati Satra & Kamalabari Satra", "category": "Neo-Vaishnavite Monastery", "highlight": "Monasteries founded by Saint Srimanta Sankardev practicing celestial Gayan-Bayan drum and cymbal dance", "fee": "Free", "time": "2 hrs"},
                {"name": "Mishing Tribal Stilt Village", "category": "Indigenous River Tribe", "highlight": "Bamboo stilt houses (Chang Ghar) woven handloom Mirizim shawls and home-brewed Apong", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Live Bamboo Mask-Making Demonstration at Samaguri", "category": "Artisan Demonstration", "cost": 150, "duration": "2 hrs"},
                {"name": "Bicycle Tour across Majuli River Meadows and Embankments", "category": "Cycling Tour", "cost": 150, "duration": "3 hrs"},
                {"name": "Gayan-Bayan Devotional Drumming Recital at Kamalabari", "category": "Devotional Music", "cost": 0, "duration": "1.5 hrs"}
            ],
            [
                {"name": "La Maison de Ananda (The House of Joy)", "category": "Architectural Bamboo Stilt Cottages", "price_per_night": 2200, "rating": 4.8, "area": "Natun Kulamor", "amenities": ["Bamboo Balconies", "Mishing Tribal Meals", "Bicycle Rental"], "suitability": ["Couples", "Solo"]},
                {"name": "Yggdrasill Bamboo Lodge", "category": "Eco Riverfront Lodge", "price_per_night": 2800, "rating": 4.6, "area": "Garamur", "amenities": ["River Views", "Campfires", "Home Cooked Meals"], "suitability": ["Couples", "Friends"]},
                {"name": "Dekasang Majuli", "category": "Eco-Heritage Resort", "price_per_night": 3200, "rating": 4.4, "area": "Sitadar", "amenities": ["Open Lawns", "River Proximity", "Cultural Evenings"], "suitability": ["Family", "Couples"]}
            ],
            [
                {"name": "La Maison Tribal Kitchen", "cuisine": "Authentic Mishing Tribal Feast", "average_cost_for_two": 450, "rating": 4.8, "area": "Natun Kulamor", "popular_dishes": "Pork Cooked in Bamboo Hollow, Sticky Rice, Poroshoni Bhaji, Apong", "is_veg": False},
                {"name": "Ural Restaurant (Garamur)", "cuisine": "Traditional Assamese & Fish", "average_cost_for_two": 400, "rating": 4.5, "area": "Garamur Tiniali", "popular_dishes": "Chitol Fish Curry, Dalma, Bhaat, Aloo Pitika", "is_veg": False},
                {"name": "Satradhikar Canteen", "cuisine": "Pure Sattvic Vegetarian Meal", "average_cost_for_two": 250, "rating": 4.6, "area": "Near Auniati Satra", "popular_dishes": "Sattvic Assamese Khichuri, Payesh, Labra", "is_veg": True}
            ]
        ),
        make_destination(
            "Tezpur", "The City of Eternal Romance & Agnigarh",
            "Mythological city on the Brahmaputra with Agnigarh hill fortress, ancient Da-Parbatia stone doorframe, and lush tea gardens.",
            1600, "Oct–Apr", "2 Days", 4.6, 8.8, "Mythological Heritage & River Promenades", ["Family", "Couples", "Solo"], "Tezpur",
            ["Agnigarh Hill", "Cole Park (Chitralekha Udyan)", "Da-Parbatia Ruins", "Padum Pukhuri"],
            [
                {"name": "Agnigarh Hill & Viewpoint", "category": "Mythological Fortress", "highlight": "Historic circular fortress hill overlooking the Brahmaputra with romantic sculptures of Usha and Aniruddha", "fee": "₹20", "time": "2 hrs"},
                {"name": "Da-Parbatia Ancient Temple Doorframe", "category": "5th-Century Gupta Sculpture", "highlight": "Oldest existing stone sculpture in Assam depicting Ganga and Yamuna river goddesses", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Sunset Stroll along the Brahmaputra Embankment", "category": "River Walk", "cost": 0, "duration": "1.5 hrs"},
                {"name": "Bicycle Ride through surrounding Monabarie Tea Estates", "category": "Tea Garden Cycling", "cost": 150, "duration": "2 hrs"}
            ],
            [
                {"name": "Kanyapur Hotel Tezpur", "category": "Comfort Hotel", "price_per_night": 2200, "rating": 4.2, "area": "Hatipilkhana", "amenities": ["AC", "Restaurant", "WiFi"], "suitability": ["Family", "Solo"]},
                {"name": "Heritage Tezpur Resort", "category": "Tea Heritage Stay", "price_per_night": 3500, "rating": 4.4, "area": "Mission Chariali", "amenities": ["Gardens", "Dining", "Parking"], "suitability": ["Couples", "Family"]}
            ],
            [
                {"name": "The Saffron Restaurant Tezpur", "cuisine": "Assamese & North Indian", "average_cost_for_two": 500, "rating": 4.3, "area": "Main Road", "popular_dishes": "Assamese Fish Thali, Duck Pepper Fry, Joha Rice", "is_veg": False},
                {"name": "Brahmaputra Sweets & Snacks", "cuisine": "Traditional Snacks & Tea", "average_cost_for_two": 200, "rating": 4.5, "area": "Chowk Bazaar", "popular_dishes": "Singara, Rasgulla, Masala Chai", "is_veg": True}
            ]
        ),
        make_destination(
            "Sivasagar", "The Royal Seat of the 600-Year Ahom Dynasty",
            "Imperial monuments of the Ahom kings—Rang Ghar (Asia's oldest amphitheatre), Talatal Ghar underground fortress, and massive Joysagar tank.",
            1500, "Oct–Mar", "2 Days", 4.7, 9.1, "Imperial Ahom Architecture & Royal Tanks", ["Family", "Solo", "History Lovers"], "Sivasagar",
            ["Rang Ghar Pavilion", "Talatal Ghar Citadel", "Sivasagar Sivadol", "Joysagar Lake"],
            [
                {"name": "Rang Ghar (Ahom Royal Pavilion)", "category": "Ancient Amphitheatre", "highlight": "Two-storey royal sports pavilion built in 1744 where Ahom kings watched buffalo fights", "fee": "₹25", "time": "2 hrs"},
                {"name": "Talatal Ghar & Kareng Ghar", "category": "Underground Palace Citadel", "highlight": "7-storey royal palace with secret subterranean tunnels constructed by King Rudra Singha", "fee": "₹25", "time": "2.5 hrs"},
                {"name": "Sivadol Temple & Sivasagar Tank", "category": "Sacred Tallest Shiva Shrine", "highlight": "104-ft high temple on the bank of a colossal 257-acre historic man-made water reservoir", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Heritage Walk through Ahom Royal Ruins", "category": "Heritage Walk", "cost": 0, "duration": "2.5 hrs"},
                {"name": "Sunset Boating on Joysagar Tank", "category": "Lake Boating", "cost": 100, "duration": "1 hr"}
            ],
            [
                {"name": "Hotel Shiva Palace Sivasagar", "category": "Comfort Heritage Stay", "price_per_night": 2400, "rating": 4.2, "area": "Near Sivadol", "amenities": ["AC", "Restaurant", "WiFi"], "suitability": ["Family", "Solo"]},
                {"name": "The Brahmaputra Heritage Stay", "category": "Boutique Hotel", "price_per_night": 3200, "rating": 4.4, "area": "Station Road", "amenities": ["Restaurant", "Tour Desk"], "suitability": ["Couples", "Family"]}
            ],
            [
                {"name": "Ahom Kitchen", "cuisine": "Authentic Traditional Ahom & Assamese", "average_cost_for_two": 450, "rating": 4.6, "area": "Sivadol Road", "popular_dishes": "Smoked Pork with Black Sesame, Fish in Banana Leaf, Joha Rice", "is_veg": False},
                {"name": "Hansa Restaurant", "cuisine": "Assamese & Indian Thali", "average_cost_for_two": 350, "rating": 4.3, "area": "Babu Patty", "popular_dishes": "Masor Tenga, Duck Curry, Mati Mahor Dal", "is_veg": False}
            ]
        )
    ]
}

# ── 15. Manipur ───────────────────────────────────────────────────────────────
NORTHEAST_STATES["Manipur"] = {
    "capital": "Imphal", "region": "Northeast", "tagline": "The Jewel of India",
    "destinations": [
        make_destination(
            "Loktak Lake & Keibul Lamjao", "The World's Only Floating National Park",
            "Vast freshwater lake dotted with circular floating biomass islands (Phumdis), and the endangered brow-antlered dancing deer (Sangai).",
            2000, "Oct–Apr", "2 Days", 4.8, 9.6, "Floating Islands & Sangai Deer Safari", ["Nature", "Couples", "Solo"], "Moirang",
            ["Sendra Island", "Keibul Lamjao Park", "INA War Memorial Moirang", "Thanga Island"],
            [
                {"name": "Keibul Lamjao National Park", "category": "World's Only Floating Sanctuary", "highlight": "Floating thick mat of vegetation harboring the rare dancing deer (Rucervus eldii eldii)", "fee": "₹50", "time": "3 hrs"},
                {"name": "Sendra Island & Tourist Point", "category": "Panoramic Island Vista", "highlight": "Elevated view across hundreds of circular green Phumdi islands on blue Loktak waters", "fee": "Free", "time": "2 hrs"},
                {"name": "INA War Memorial & Museum (Moirang)", "category": "National Freedom Memorial", "highlight": "Where Netaji Subhas Chandra Bose's Indian National Army first hoisted the tricolour on mainland India in 1944", "fee": "₹20", "time": "1.5 hrs"}
            ],
            [
                {"name": "Traditional Wooden Canoe Cruise among Floating Phumdis", "category": "Canoe Safari", "cost": 500, "duration": "2 hrs"},
                {"name": "Spotting the Elusive Sangai Deer from Forest Watchtower", "category": "Wildlife Spotting", "cost": 100, "duration": "2 hrs"},
                {"name": "Homestay Living in a Floating Phumdi Fisherman Hut", "category": "Unique Living", "cost": 800, "duration": "Overnight"}
            ],
            [
                {"name": "Sendra Park & Resort by Classic", "category": "Hilltop Island Resort", "price_per_night": 4500, "rating": 4.6, "area": "Sendra Island", "amenities": ["360 Lake Views", "Restaurant", "Balconies"], "suitability": ["Couples", "Family"]},
                {"name": "Loktak Floating Homestay", "category": "Living on a Floating Phumdi", "price_per_night": 1800, "rating": 4.8, "area": "Thanga / Loktak Lake", "amenities": ["Authentic Floating Hut", "Canoe Rides", "Home Cooked Manipuri Food"], "suitability": ["Adventure", "Couples", "Solo"]},
                {"name": "Hotel Moirang Heritage", "category": "Comfort Transit Hotel", "price_per_night": 2200, "rating": 4.1, "area": "Near INA Memorial Moirang", "amenities": ["AC", "Restaurant", "WiFi"], "suitability": ["Family", "Solo"]}
            ],
            [
                {"name": "Sendra Resort Restaurant", "cuisine": "Traditional Manipuri & Indian", "average_cost_for_two": 650, "rating": 4.5, "area": "Sendra Island", "popular_dishes": "Eromba, Singju Salad, Kangshoi (Manipuri stew), Fried Loktak Fish", "is_veg": False},
                {"name": "Loktak Homestay Kitchen", "cuisine": "Fresh Lake Fishermen Delicacies", "average_cost_for_two": 400, "rating": 4.8, "area": "Thanga Island", "popular_dishes": "Nga Thongba (Fish Curry), Bamboo Shoot Chutney, Black Rice Kheer", "is_veg": False},
                {"name": "Moirang Town Kitchen", "cuisine": "Manipuri Snacks & Tea", "average_cost_for_two": 200, "rating": 4.3, "area": "INA Road", "popular_dishes": "Singju (Spicy Vegetable Salad), Bora (Pakora), Milk Tea", "is_veg": True}
            ]
        ),
        make_destination(
            "Imphal", "The Capital of Polos, Forts & Mother's Market",
            "Ima Keithel (Asia's largest all-women market run by 5,000 mothers), historic Kangla Fort citadel, and polo's historical birthplace.",
            1900, "Oct–Apr", "2 Days", 4.7, 9.2, "Women's Market, Forts & Polo Origins", ["Solo", "Family", "Couples"], "Imphal",
            ["Ima Keithel (Mother's Market)", "Kangla Fort Complex", "Govindaji Temple", "War Cemetery"],
            [
                {"name": "Ima Keithel (Mother's Market)", "category": "World-Famous All-Women Market", "highlight": "500-year-old vibrant market run exclusively by 5,000 married women selling handlooms, fish, and spices", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Kangla Fort & Royal Palace", "category": "Ancient Meitei Royal Citadel", "highlight": "Ancient political and spiritual seat with sacred twin Kangla Sha dragon statues and moat", "fee": "₹20", "time": "2.5 hrs"},
                {"name": "Shree Govindaji Temple", "category": "Golden Twin-Domed Shrine", "highlight": "Ornate Vaishnavite temple famed for classical Manipuri Raas Leela dance recitals", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Walking and Handloom Shopping in Ima Keithel", "category": "Market Walk", "cost": 0, "duration": "2.5 hrs"},
                {"name": "Bicycle Exploration through Vast Kangla Fort Grounds", "category": "Bicycle Tour", "cost": 100, "duration": "2 hrs"},
                {"name": "Attending an Authentic Manipuri Raas Leela Performance", "category": "Classical Dance", "cost": 200, "duration": "2 hrs"}
            ],
            [
                {"name": "The Classic Hotel Imphal", "category": "Luxury 4-Star Hotel", "price_per_night": 4800, "rating": 4.6, "area": "North AOC", "amenities": ["Fitness Centre", "Spa", "Fine Dining"], "suitability": ["Couples", "Family", "Business"]},
                {"name": "Classic Grande, a Member of Radisson Individuals", "category": "Luxury 5-Star Hotel", "price_per_night": 7000, "rating": 4.7, "area": "Chingmeirong", "amenities": ["Outdoor Pool", "Spa", "International Cuisine"], "suitability": ["Couples", "Family", "Business"]},
                {"name": "Hotel Nirmala", "category": "Comfort City Centre Stay", "price_per_night": 2200, "rating": 4.1, "area": "MG Avenue", "amenities": ["Restaurant", "WiFi", "AC"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Luxmi Kitchen", "cuisine": "Legendary Manipuri Traditional Thali", "average_cost_for_two": 450, "rating": 4.7, "area": "Wahengbam Leikai", "popular_dishes": "Manipuri Fish Thali, Eromba, Chamthong, Chakhao Kheer (Black Rice Pudding)", "is_veg": False},
                {"name": "Naoba's Restaurant", "cuisine": "Manipuri & Pan-Asian Fusion", "average_cost_for_two": 750, "rating": 4.5, "area": "Chingmeirong", "popular_dishes": "Smoked Pork Ribs, Singju, Chicken Stew with Herbs", "is_veg": False},
                {"name": "Forage Cafe", "cuisine": "Organic Cafe, Salads & Coffee", "average_cost_for_two": 500, "rating": 4.6, "area": "Kwakeithel", "popular_dishes": "Local Herb Pesto Pasta, Pour-Over Coffee, Carrot Cake", "is_veg": True}
            ]
        ),
        make_destination(
            "Ukhrul", "The Land of the Rare Shirui Lily",
            "Misty highland hills home to the Tangkhul Naga tribe, the world's only natural habitat of the Shirui Lily, and limestone Khangkhui caves.",
            1600, "Apr–Jun (Lilies) & Oct–Mar", "2 Days", 4.7, 8.9, "Highland Wildflowers & Tangkhul Culture", ["Adventure", "Couples", "Solo"], "Ukhrul",
            ["Shirui Kashong Peak", "Khangkhui Cave", "Tangkhul Cultural Quarter"],
            [
                {"name": "Shirui Kashong Peak (8,500 ft)", "category": "Mountain Peak", "highlight": "High peak where the rare pale pink Shirui Lily (Lilium mackliniae) blooms naturally only here", "fee": "Free", "time": "4 hrs"},
                {"name": "Khangkhui Mangsor Limestone Caves", "category": "Prehistoric Caverns", "highlight": "Ancient limestone caves dating back to the Stone Age with deep chambers", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Trek to the Summit of Shirui Kashong Peak", "category": "Mountain Hike", "cost": 0, "duration": "4 hrs"},
                {"name": "Tangkhul Black Pottery Workshop in Longpi Village", "category": "Craft Workshop", "cost": 300, "duration": "2.5 hrs"}
            ],
            [
                {"name": "Shirui Lily Eco Resort", "category": "Mountain Eco Resort", "price_per_night": 2800, "rating": 4.4, "area": "Shirui Foothills", "amenities": ["Valley Views", "Dining", "Campfires"], "suitability": ["Couples", "Friends"]},
                {"name": "Tangkhul Homestay Ukhrul", "category": "Traditional Homestay", "price_per_night": 1500, "rating": 4.6, "area": "Ukhrul Town", "amenities": ["Organic Food", "Local Guide"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Tangkhul Traditional Diner", "cuisine": "Authentic Tangkhul Naga", "average_cost_for_two": 350, "rating": 4.5, "area": "Viewland Market", "popular_dishes": "Smoked Pork with Bamboo Shoot, Chamthong, Red Rice", "is_veg": False},
                {"name": "Ukhrul Cafe & Bakes", "cuisine": "Cafe & Snacks", "average_cost_for_two": 250, "rating": 4.3, "area": "Town Centre", "popular_dishes": "Pork Momos, Ginger Milk Tea, Chowmein", "is_veg": False}
            ]
        ),
        make_destination(
            "Tamenglong", "The Land of Hornbills & Roaring Cascades",
            "Dense virgin tropical rainforests, Barak River waterfalls, migratory Amur falcon roosting grounds, and famous sweet oranges.",
            1500, "Oct–Apr", "2 Days", 4.6, 8.6, "Rainforest Wildlife & Waterfalls", ["Adventure", "Solo", "Friends"], "Tamenglong",
            ["Barak Waterfalls", "Tharon Caves", "Meadow Ridge"],
            [
                {"name": "Barak River Seven Waterfalls", "category": "River Cascades", "highlight": "Series of 7 magnificent cascading waterfalls along the roaring Barak river", "fee": "Free", "time": "3.5 hrs"},
                {"name": "Tharon Cave Network", "category": "Speleology Caves", "highlight": "655-meter ancient underground cave network linked to prehistoric Hoabinhian culture", "fee": "Free", "time": "2.5 hrs"}
            ],
            [
                {"name": "Amur Falcon Birdwatching in Tamenglong Valley (Nov)", "category": "Birdwatching", "cost": 200, "duration": "3 hrs"},
                {"name": "Spelunking in the Tharon Cave System", "category": "Caving", "cost": 100, "duration": "2.5 hrs"}
            ],
            [
                {"name": "Tamenglong Tourist Lodge", "category": "State Hill Lodge", "price_per_night": 1800, "rating": 4.2, "area": "Hilltop Ridge", "amenities": ["Valley Views", "Dining"], "suitability": ["Friends", "Solo"]},
                {"name": "Rainforest Eco Camp Tamenglong", "category": "Adventure Camp", "price_per_night": 1200, "rating": 4.4, "area": "Barak Valley", "amenities": ["Tents", "Campfires", "Trek Guides"], "suitability": ["Adventure", "Solo"]}
            ],
            [
                {"name": "Barak Valley Tribal Kitchen", "cuisine": "Rongmei Naga Traditional", "average_cost_for_two": 350, "rating": 4.4, "area": "Main Market", "popular_dishes": "Smoked Fish with Herbs, Boiled Pork, Tamenglong Orange Slices", "is_veg": False},
                {"name": "Highway Canteen", "cuisine": "North Eastern & Indian", "average_cost_for_two": 250, "rating": 4.1, "area": "Bus Stand", "popular_dishes": "Momos, Rice and Dal, Hot Tea", "is_veg": True}
            ]
        )
    ]
}

# ── 16. Meghalaya ─────────────────────────────────────────────────────────────
NORTHEAST_STATES["Meghalaya"] = {
    "capital": "Shillong", "region": "Northeast", "tagline": "The Abode of the Clouds",
    "destinations": [
        make_destination(
            "Shillong", "The Scotland of the East & Rock Music Capital",
            "Misty pine hills, colonial heritage, vibrant rock band cafes, picturesque Umiam Lake, and bustling Police Bazar.",
            2200, "Year-round", "3 Days", 4.8, 9.8, "Pine Hills, Rock Music & Waterfalls", ["Friends", "Couples", "Solo"], "Shillong",
            ["Police Bazar", "Laitlum Canyons", "Umiam Lake (Barapani)", "Elephant Falls", "Ward's Lake"],
            [
                {"name": "Laitlum Canyons", "category": "Dramatic Canyon Gorge", "highlight": "Deep green cloud-swept ravines dropping sheer into misty gorges of East Khasi Hills", "fee": "₹20", "time": "2.5 hrs"},
                {"name": "Umiam Lake (Barapani)", "category": "Vast Water Reservoir", "highlight": "Sprawling azure blue lake surrounded by conifer forests offering water sports and houseboats", "fee": "Free", "time": "2 hrs"},
                {"name": "Elephant Falls", "category": "Tiered Forest Waterfall", "highlight": "Three-tiered cascade of frothing white water named by the British", "fee": "₹30", "time": "1.5 hrs"},
                {"name": "Don Bosco Museum of Indigenous Cultures", "category": "World-Class Tribal Museum", "highlight": "7-storey cultural hexagon showcasing authentic Northeast tribal heritage", "fee": "₹100", "time": "2.5 hrs"}
            ],
            [
                {"name": "Kayaking and Speed Boating on Umiam Lake", "category": "Water Sports", "cost": 400, "duration": "1.5 hrs"},
                {"name": "Live Rock Band Crawl at Cafe Shillong & Dylan's Cafe", "category": "Live Music Nightlife", "cost": 800, "duration": "3 hrs"},
                {"name": "Trek down the Thousand Steps of Laitlum Gorge", "category": "Canyon Hike", "cost": 0, "duration": "3 hrs"}
            ],
            [
                {"name": "Ri Kynjai - Serenity by the Lake", "category": "Luxury Khasi Thatched Resort 5-Star", "price_per_night": 16000, "rating": 4.9, "area": "Umiam Lake Edge", "amenities": ["Lake View Thatched Cottages", "Ayurvedic Spa", "Gourmet Khasi Dining"], "suitability": ["Couples", "Family"]},
                {"name": "The Heritage Club - Tripura Castle", "category": "Royal Maharaja Heritage Stay", "price_per_night": 7500, "rating": 4.7, "area": "Cleve Colony", "amenities": ["Antique Fireplaces", "Lush Pine Gardens", "Bar"], "suitability": ["Couples", "Family"]},
                {"name": "Zostel Shillong", "category": "Backpacker Hostel", "price_per_night": 900, "rating": 4.6, "area": "Nongrim Hills", "amenities": ["Music Common Room", "Cafe", "WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Cafe Shillong", "cuisine": "Khasi Fusion, Burgers & Live Blues", "average_cost_for_two": 850, "rating": 4.7, "area": "LP Building, Laitumkhrah", "popular_dishes": "Smoked Pork with Bamboo Shoot, Beef Burger, Irish Coffee", "is_veg": False},
                {"name": "Dylan's Cafe", "cuisine": "Bob Dylan-Themed American & Continental", "average_cost_for_two": 750, "rating": 4.7, "area": "Risa Colony", "popular_dishes": "Hot Chocolate with Marshmallows, Pancakes, Waffles, Dylan Tribute Art", "is_veg": True},
                {"name": "Trattoria (Police Bazar)", "cuisine": "Authentic Traditional Khasi Eatery", "average_cost_for_two": 350, "rating": 4.6, "area": "Police Bazar", "popular_dishes": "Jadoh (Rice cooked in meat stock), Dohkhlieh, Tungrymbai", "is_veg": False}
            ]
        ),
        make_destination(
            "Cherrapunji (Sohra)", "The Land of Living Root Bridges & Plunging Waterfalls",
            "Nohkalikai Falls—India's tallest plunge waterfall, ancient living bio-engineering root bridges, limestone Mawsmai caves, and rain-swept valleys.",
            2200, "Year-round (Monsoon for falls)", "3 Days", 4.9, 9.9, "Living Root Bridges & Plunge Waterfalls", ["Adventure", "Couples", "Friends"], "Cherrapunji",
            ["Nohkalikai Falls", "Double Decker Root Bridge (Nongriat)", "Mawsmai Cave", "Seven Sisters Falls", "Wei Sawdong"],
            [
                {"name": "Nohkalikai Falls (1,115 ft)", "category": "India's Tallest Plunge Waterfall", "highlight": "Staggering vertical leap plunging into a turquoise cliff pool framed by emerald ravines", "fee": "₹20", "time": "2 hrs"},
                {"name": "Double Decker Living Root Bridge (Nongriat)", "category": "Living Bio-Engineering Wonder", "highlight": "Two-tier living bridge grown over two centuries from the roots of Ficus elastica trees", "fee": "Free", "time": "Full Day"},
                {"name": "Wei Sawdong Three-Tier Falls", "category": "Lagoon Cascade", "highlight": "Incredible emerald-green stepped natural pools hidden deep in the forest trail", "fee": "₹30", "time": "2.5 hrs"},
                {"name": "Mawsmai Limestone Cave", "category": "Prehistoric Limestone Cavern", "highlight": "Lit subterranean cave system with stalactites, fossils, and narrow squeeze passages", "fee": "₹20", "time": "1.5 hrs"}
            ],
            [
                {"name": "Trek down 3,500 Steps to Nongriat Double Decker Living Root Bridge", "category": "Adventure Hike", "cost": 500, "duration": "6 hrs"},
                {"name": "Swimming in the Turquoise Plunge Pool of Rainbow Falls", "category": "Wild Swimming", "cost": 0, "duration": "2 hrs"},
                {"name": "Caving Exploration in Arwah and Mawsmai Caves", "category": "Caving", "cost": 50, "duration": "2 hrs"}
            ],
            [
                {"name": "Polo Orchid Resort Cherrapunjee", "category": "Luxury 4-Star Canyon Resort", "price_per_night": 9500, "rating": 4.7, "area": "Nohsngithiang Falls View", "amenities": ["Infinity Pool overlooking Seven Sisters", "Spa", "Private Balconies"], "suitability": ["Couples", "Family"]},
                {"name": "Jiva Resort Cherrapunjee", "category": "Upscale Boutique Retreat", "price_per_night": 7800, "rating": 4.6, "area": "Sohra", "amenities": ["Golf Putting", "Gourmet Dining", "Bonfires"], "suitability": ["Couples", "Family"]},
                {"name": "Nongriat Community Homestay", "category": "Living Root Bridge Base Stay", "price_per_night": 1000, "rating": 4.8, "area": "Nongriat Village", "amenities": ["Jungle Setting", "Natural River Pools", "Home Cooked Food"], "suitability": ["Solo", "Friends", "Adventure"]}
            ],
            [
                {"name": "Rain Cafe (Polo Orchid Resort)", "cuisine": "Multi-Cuisine & Canyon View", "average_cost_for_two": 1200, "rating": 4.6, "area": "Seven Sisters Cliff", "popular_dishes": "Khasi Pork Curry, Woodfired Pizza, Chocolate Sizzler", "is_veg": False},
                {"name": "Orange Roots", "cuisine": "Pure Vegetarian South Indian & North Indian", "average_cost_for_two": 450, "rating": 4.5, "area": "Sohra Highway", "popular_dishes": "Masala Dosa, Thali, Filter Coffee", "is_veg": True},
                {"name": "Nongriat Serene Homestay Kitchen", "cuisine": "Khasi Village Comfort Food", "average_cost_for_two": 300, "rating": 4.7, "area": "Nongriat Village", "popular_dishes": "Steamed Rice, Fresh Dal, Egg Omelette, Organic Ginger Tea", "is_veg": True}
            ]
        ),
        make_destination(
            "Dawki & Mawlynnong", "Crystal Umngot River & Asia's Cleanest Village",
            "Transparent Umngot river where boats appear to float in air, Indo-Bangladesh border at Tamabil, and Mawlynnong eco-village.",
            1800, "Nov–Apr", "2 Days", 4.8, 9.7, "Crystal River Boating & Eco Village", ["Couples", "Friends", "Family"], "Dawki",
            ["Umngot River Jetty", "Mawlynnong Clean Village", "Single Root Bridge (Riwai)", "Tamabil Border"],
            [
                {"name": "Umngot River (Dawki)", "category": "Crystal Clear River", "highlight": "World-famous glass-clear emerald water where boat shadows appear cast on riverbed pebbles", "fee": "Free", "time": "3 hrs"},
                {"name": "Mawlynnong Village", "category": "Asia's Cleanest Village Awardee", "highlight": "Spotless floral eco-village with bamboo dustbins, orchid walkways, and Sky Walk bamboo tower", "fee": "Free", "time": "2 hrs"},
                {"name": "Riwai Single Living Root Bridge", "category": "Living Root Bridge", "highlight": "Easily accessible living root bridge arching across a gushing jungle stream", "fee": "₹20", "time": "1.5 hrs"}
            ],
            [
                {"name": "Glass-Clear Country Boat Ride on Umngot River", "category": "Boat Experience", "cost": 800, "duration": "1.5 hrs"},
                {"name": "Riverside Glamping on Shnongpdeng Pebble Beach", "category": "Riverside Camping", "cost": 1500, "duration": "Overnight"},
                {"name": "Cliff Jumping and Snorkeling at Shnongpdeng", "category": "Water Adventure", "cost": 500, "duration": "2 hrs"}
            ],
            [
                {"name": "Betelnut Resort Dawki", "category": "Riverside Eco Resort", "price_per_night": 3500, "rating": 4.4, "area": "Shnongpdeng", "amenities": ["Riverbank Tents", "Bonfires", "Kayaking"], "suitability": ["Couples", "Friends"]},
                {"name": "Mawlynnong Traditional Bamboo Guesthouse", "category": "Floral Village Homestay", "price_per_night": 2000, "rating": 4.6, "area": "Mawlynnong Village", "amenities": ["Garden Living", "Traditional Khasi Meals"], "suitability": ["Family", "Couples"]},
                {"name": "Shnongpdeng Camp Huts", "category": "Riverside Backpacker Camp", "price_per_night": 1200, "rating": 4.5, "area": "Shnongpdeng Beach", "amenities": ["Campfire", "River Access", "BBQ"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Shnongpdeng Riverside Shacks", "cuisine": "Fresh River Fish & Khasi Meals", "average_cost_for_two": 400, "rating": 4.6, "area": "Shnongpdeng Beach", "popular_dishes": "Fried Umngot River Fish, Steamed Rice, Tomato Chutney", "is_veg": False},
                {"name": "Mawlynnong Community Food Kitchen", "cuisine": "Home-Cooked Khasi Meals", "average_cost_for_two": 350, "rating": 4.5, "area": "Mawlynnong Village", "popular_dishes": "Country Chicken Curry, Fresh Forest Vegetables, Rice", "is_veg": False},
                {"name": "Dawki Border View Dhaba", "cuisine": "Indian & Bengali Fish Thali", "average_cost_for_two": 300, "rating": 4.1, "area": "Tamabil Border", "popular_dishes": "Fish Curry Rice, Maggi, Tea", "is_veg": False}
            ]
        ),
        make_destination(
            "Jowai & Krang Suri Falls", "The Turquoise Wonder of Jaintia Hills",
            "Mesmerizing turquoise blue water of Krang Suri cascade, sacred monoliths of Nartiang, and Thadlaskein Lake.",
            1700, "Oct–Apr", "2 Days", 4.7, 9.3, "Turquoise Lagoons & Monolith Heritage", ["Friends", "Couples", "Solo"], "Jowai",
            ["Krang Suri Cascade", "Nartiang Monolith Garden", "Thadlaskein Lake"],
            [
                {"name": "Krang Suri Waterfalls", "category": "Turquoise Pool Waterfall", "highlight": "Breathtaking turquoise green natural plunge pool with swimming and boat rides", "fee": "₹50", "time": "3 hrs"},
                {"name": "Nartiang Monolith Park", "category": "Ancient Megalithic Site", "highlight": "Cluster of gigantic 8-meter stone monoliths erected by Jaintia kings centuries ago", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Swimming with Life Jackets in Krang Suri Pool", "category": "Wild Swimming", "cost": 100, "duration": "2 hrs"},
                {"name": "Camping beside the Cascades of Krang Suri", "category": "Lakeside Camp", "cost": 1200, "duration": "Overnight"}
            ],
            [
                {"name": "Krang Suri Adventure Camp", "category": "Eco Tented Camp", "price_per_night": 2000, "rating": 4.5, "area": "Krang Suri Grounds", "amenities": ["Tents", "Campfire", "River Access"], "suitability": ["Friends", "Couples"]},
                {"name": "Hotel Pegasus Crown Jowai", "category": "Comfort Hill Hotel", "price_per_night": 2400, "rating": 4.1, "area": "Main Road Jowai", "amenities": ["Restaurant", "WiFi"], "suitability": ["Solo", "Family"]}
            ],
            [
                {"name": "Krang Suri Waterfall Cafe", "cuisine": "Local Khasi & Comfort Food", "average_cost_for_two": 400, "rating": 4.6, "area": "Waterfall Base", "popular_dishes": "Jadoh, Fried Chicken, Maggi, Fresh Tea", "is_veg": False},
                {"name": "Jowai Traditional Kitchen", "cuisine": "Jaintia Tribal Cuisine", "average_cost_for_two": 300, "rating": 4.3, "area": "Iawmusiang Market", "popular_dishes": "Dohkhlieh, Steamed Rice, Tomato Chutney", "is_veg": False}
            ]
        )
    ]
}

# ── 17. Mizoram ───────────────────────────────────────────────────────────────
NORTHEAST_STATES["Mizoram"] = {
    "capital": "Aizawl", "region": "Northeast", "tagline": "The Land of the Blue Mountains",
    "destinations": [
        make_destination(
            "Aizawl", "The Serene Ridge City & Mizo Culture",
            "Spectacular city stacked along knife-edge mountain ridges at 3,700 ft, Solomon's Temple, Durtlang Hills, and vibrant Bara Bazar.",
            1800, "Oct–Apr", "3 Days", 4.7, 9.2, "Mountain Ridge Architecture & Mizo Heritage", ["Solo", "Couples", "Culture"], "Aizawl",
            ["Durtlang Hills", "Solomon's Temple", "Bara Bazar", "KV Paradise"],
            [
                {"name": "Solomon's Temple", "category": "Magnificent White Marble Church", "highlight": "Colossal white church with 4 towers built by Kohhran Thianghlim over two decades", "fee": "Free", "time": "2 hrs"},
                {"name": "Durtlang Hills Viewpoint", "category": "Panoramic Ridge Lookout", "highlight": "Highest vantage point offering sweeping view of the multi-tiered cliff city of Aizawl", "fee": "Free", "time": "2 hrs"},
                {"name": "Mizoram State Museum (MacDonald Hill)", "category": "Tribal Heritage Museum", "highlight": "5 galleries of Mizo ethnography, traditional weapons, textiles, and musical instruments", "fee": "₹20", "time": "2 hrs"},
                {"name": "KV Paradise (Taj Mahal of Mizoram)", "category": "Granite Memorial Monument", "highlight": "Gleaming two-storey white church mausoleum erected on a hill slope in memory of a beloved wife", "fee": "₹30", "time": "1.5 hrs"}
            ],
            [
                {"name": "Scenic Walking Trail along Durtlang Ridge", "category": "Ridge Walk", "cost": 0, "duration": "2.5 hrs"},
                {"name": "Shopping for Mizo Puan (Handwoven Shawls) in Bara Bazar", "category": "Textile Trail", "cost": 0, "duration": "2 hrs"},
                {"name": "Sunset Stargazing from KV Paradise Terrace", "category": "Sunset View", "cost": 30, "duration": "1.5 hrs"}
            ],
            [
                {"name": "The Grand Hotel Aizawl", "category": "Modern 4-Star City Stay", "price_per_night": 4500, "rating": 4.5, "area": "Zarkawt", "amenities": ["Valley Views", "Multi-Cuisine Restaurant", "WiFi"], "suitability": ["Couples", "Family", "Business"]},
                {"name": "Hotel Floria", "category": "Upscale Downtown Hotel", "price_per_night": 3800, "rating": 4.4, "area": "Dawrpui", "amenities": ["City Centre", "Restaurant", "Gym"], "suitability": ["Business", "Solo"]},
                {"name": "Berawtlang Tourist Resort", "category": "Quiet Hillside Cottages", "price_per_night": 2200, "rating": 4.3, "area": "Berawtlang", "amenities": ["Gardens", "Panoramic Views", "Dining"], "suitability": ["Couples", "Friends"]}
            ],
            [
                {"name": "Chopstyx Restaurant", "cuisine": "Mizo, Pan-Asian & Tibetan", "average_cost_for_two": 600, "rating": 4.6, "area": "Chanmari", "popular_dishes": "Smoked Pork with Bamboo Shoot, Bai (Mizo Vegetable Stew), Steamed Momos", "is_veg": False},
                {"name": "David's Kitchen", "cuisine": "Authentic Mizo Traditional Delicacies", "average_cost_for_two": 500, "rating": 4.7, "area": "Zarkawt", "popular_dishes": "Mizo Thali, Vawksa Rep (Smoked Pork), Bamboo Shoot Bai", "is_veg": False},
                {"name": "Cafe Deja Vu", "cuisine": "Cafe, Pastries & Coffee", "average_cost_for_two": 400, "rating": 4.5, "area": "Dawrpui", "popular_dishes": "Waffles, Club Sandwiches, Brewed Coffee", "is_veg": True}
            ]
        ),
        make_destination(
            "Reiek & Vantawng Falls", "Dramatic Cliffs & Highest Mizo Waterfall",
            "Spectacular rocky precipice of Reiek peak (5,100 ft), preserved Mizo heritage village, and Vantawng Falls cascading 750 ft inside dense bamboo.",
            1600, "Sep–Mar", "2 Days", 4.7, 8.9, "Cliff Edge Treks & Waterfalls", ["Adventure", "Couples", "Solo"], "Thenzawl",
            ["Reiek Peak & Ridge", "Reiek Heritage Village", "Vantawng Falls", "Thenzawl Handloom Town"],
            [
                {"name": "Reiek Peak & Cliff Edge", "category": "Spectacular Cliff Summit", "highlight": "Breathtaking trek up to knife-edge cliff with panoramic views across Bangladesh plains", "fee": "Free", "time": "3 hrs"},
                {"name": "Vantawng Falls (Thenzawl)", "category": "Highest Waterfall in Mizoram", "highlight": "Magnificent two-tiered 750-foot waterfall surrounded by bamboo forests and gorges", "fee": "₹20", "time": "2 hrs"},
                {"name": "Reiek Mizo Model Heritage Village", "category": "Living Cultural Village", "highlight": "Authentic reconstruction of traditional Mizo chieftain's house, bachelor dormitory (Zawlbuk)", "fee": "₹20", "time": "1.5 hrs"}
            ],
            [
                {"name": "Summit Trek to Reiek Peak through Subtropical Forests", "category": "Mountain Hike", "cost": 0, "duration": "3 hrs"},
                {"name": "Handloom Weaving Exploration in Thenzawl Town", "category": "Textile Craft", "cost": 0, "duration": "2 hrs"},
                {"name": "Photography at Vantawng Falls Lookout Platform", "category": "Sightseeing", "cost": 20, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Reiek Tourist Resort (Mizoram Tourism)", "category": "Mountain Chalet Resort", "price_per_night": 2400, "rating": 4.4, "area": "Reiek Foot", "amenities": ["Peak Views", "Wooden Cottages", "Restaurant"], "suitability": ["Couples", "Friends"]},
                {"name": "Thenzawl Golf Resort", "category": "Luxury Eco Golf Lodge", "price_per_night": 3500, "rating": 4.5, "area": "Thenzawl", "amenities": ["18-Hole Golf Course", "Lush Lawns", "Modern Cottages"], "suitability": ["Couples", "Family"]},
                {"name": "Thenzawl Tourist Lodge", "category": "Budget Comfort Stay", "price_per_night": 1500, "rating": 4.1, "area": "Near Vantawng", "amenities": ["Dining", "Clean Rooms"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Reiek Resort Restaurant", "cuisine": "Traditional Mizo & North Indian", "average_cost_for_two": 450, "rating": 4.3, "area": "Reiek Hill", "popular_dishes": "Mizo Bai, Chicken with Mustard Greens, Rice", "is_veg": False},
                {"name": "Thenzawl Golf View Kitchen", "cuisine": "Continental & Mizo Meals", "average_cost_for_two": 600, "rating": 4.4, "area": "Thenzawl Golf Course", "popular_dishes": "Grilled Pork, Noodles, Hot Coffee", "is_veg": False},
                {"name": "Highway Bamboo Point", "cuisine": "Local Highway Tea & Snacks", "average_cost_for_two": 150, "rating": 4.5, "area": "Thenzawl Highway", "popular_dishes": "Steamed Corn, Mizo Tea, Sweet Biscuits", "is_veg": True}
            ]
        ),
        make_destination(
            "Champhai", "The Rice Bowl of Mizoram & Rih Dil Gateway",
            "Expansive emerald paddy fields framed by Myanmar hills, historic monuments, and ancient Mizo legendary ruins.",
            1600, "Oct–Apr", "2 Days", 4.6, 8.8, "Border Hills & Countryside Vistas", ["Couples", "Solo", "Adventure"], "Champhai",
            ["Champhai Valley View", "Murlen National Park", "Zokhawthar Border"],
            [
                {"name": "Champhai Rice Terraces Viewpoint", "category": "Panoramic Viewpoint", "highlight": "Vast green valley known as the Rice Bowl of Mizoram stretching toward misty blue peaks", "fee": "Free", "time": "2 hrs"},
                {"name": "Murlen National Park", "category": "Subtropical Jungle", "highlight": "Dense virgin canopy so thick sunlight barely touches the forest floor; home to serow and leopards", "fee": "₹50", "time": "4 hrs"}
            ],
            [
                {"name": "Border Trade Walk at Zokhawthar", "category": "Border Walk", "cost": 0, "duration": "2 hrs"},
                {"name": "Vineyard Visit & Tasting at Champhai Winery", "category": "Agri-Tourism", "cost": 200, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Champhai Tourist Lodge (State Lodge)", "category": "Comfort Hill Lodge", "price_per_night": 1800, "rating": 4.2, "area": "Main Town", "amenities": ["Valley Views", "Dining"], "suitability": ["Family", "Solo"]},
                {"name": "Hotel Chawngthu", "category": "Budget City Stay", "price_per_night": 1300, "rating": 4.0, "area": "Bazar Veng", "amenities": ["Room Service", "WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Champhai Town Diner", "cuisine": "Mizo Traditional Dishes", "average_cost_for_two": 350, "rating": 4.4, "area": "Main Market", "popular_dishes": "Mizo Pork Curry, Steamed Rice, Bamboo Shoot Chutney", "is_veg": False},
                {"name": "Border View Kitchen", "cuisine": "Pan-Asian & Indian", "average_cost_for_two": 300, "rating": 4.2, "area": "Near Zokhawthar", "popular_dishes": "Fried Noodles, Momos, Black Tea", "is_veg": False}
            ]
        ),
        make_destination(
            "Lunglei", "The Bridge of Rock & Southern Mist",
            "Southern Mizoram's cultural heart named after a natural rock bridge, Kawmzawl park, and Khawnglung wildlife reserve.",
            1500, "Oct–Apr", "2 Days", 4.5, 8.6, "Quiet Hills & Rock Formations", ["Solo", "Couples", "Nature"], "Lunglei",
            ["Rock Bridge (Lunglei)", "Kawmzawl Park", "Serkawn Cultural Quarter"],
            [
                {"name": "Lunglei Natural Rock Bridge", "category": "Geological Formation", "highlight": "Famous natural stone bridge on the Nghasih river which gives the town its name", "fee": "Free", "time": "1.5 hrs"},
                {"name": "Kawmzawl Forest Park", "category": "Highland Park", "highlight": "Gentle rolling pine park with picnic meadows and sunrise viewpoints", "fee": "₹20", "time": "2 hrs"}
            ],
            [
                {"name": "Pine Forest Trail Walk at Kawmzawl", "category": "Nature Trail", "cost": 0, "duration": "2 hrs"},
                {"name": "Cultural Walk in Serkawn Heritage Hamlet", "category": "Heritage Walk", "cost": 0, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Lunglei Tourist Lodge", "category": "Comfort Hilltop Lodge", "price_per_night": 1700, "rating": 4.2, "area": "Zotlang", "amenities": ["Scenic Balconies", "Dining"], "suitability": ["Family", "Solo"]},
                {"name": "Hotel Vantawng Lunglei", "category": "Transit Hotel", "price_per_night": 1400, "rating": 4.0, "area": "Bazar Area", "amenities": ["WiFi", "Room Service"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Lunglei Food Corner", "cuisine": "Mizo & Tibetan", "average_cost_for_two": 350, "rating": 4.3, "area": "Venglai", "popular_dishes": "Vawksa Rep, Steamed Momos, Bai", "is_veg": False},
                {"name": "Hilltop Tea Stall", "cuisine": "Tea & Mountain Snacks", "average_cost_for_two": 150, "rating": 4.4, "area": "Near Rock Bridge", "popular_dishes": "Special Red Tea, Butter Bread, Boiled Eggs", "is_veg": True}
            ]
        )
    ]
}

# ── 18. Nagaland ──────────────────────────────────────────────────────────────
NORTHEAST_STATES["Nagaland"] = {
    "capital": "Kohima", "region": "Northeast", "tagline": "Land of Festivals & The Hornbill",
    "destinations": [
        make_destination(
            "Kohima & Kisama Heritage", "The Hornbill Festival & World War II Ridge",
            "Kisama Heritage Village hosting the legendary Hornbill Festival in December, poignant Commonwealth WWII War Cemetery, and Angami tribal villages.",
            2200, "Oct–May (Dec for Hornbill)", "3 Days", 4.9, 9.8, "Tribal Festivals, WWII History & Highlands", ["Solo", "Couples", "Friends"], "Kohima",
            ["Kisama Heritage Village", "Kohima War Cemetery", "Kohima Cathedral", "Khonoma Green Village"],
            [
                {"name": "Kisama Heritage Village", "category": "Hornbill Festival Epicentre", "highlight": "Permanent tribal village showcasing traditional architecture of all 17 major Naga tribes", "fee": "₹50 (Free off-season)", "time": "3.5 hrs"},
                {"name": "Kohima World War II War Cemetery", "category": "Historic Commonwealth Memorial", "highlight": "Tennis court battleground where Allied forces halted Japanese invasion of India in 1944", "fee": "Free", "time": "2 hrs"},
                {"name": "Khonoma Green Village", "category": "India's First Green Eco Village", "highlight": "700-year-old Angami village celebrated for banning hunting and preserving Blyth's tragopan", "fee": "Free", "time": "3 hrs"},
                {"name": "Mary Help of Christians Cathedral", "category": "Iconic Wooden Cathedral", "highlight": "Architectural masterpiece incorporating Naga tribal motifs overlooking Kohima town", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Attending the Grand Hornbill Festival (Dec 1-10)", "category": "Grand Festival", "cost": 100, "duration": "Full Day"},
                {"name": "Guided Terraced Paddy & Alder Tree Walk in Khonoma", "category": "Eco Tour", "cost": 300, "duration": "2.5 hrs"},
                {"name": "Tasting Naga Smoked Pork with Raja Mircha (Ghost Pepper)", "category": "Culinary Challenge", "cost": 300, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Vivor Hotel Kohima", "category": "Luxury 4-Star Mountain Hotel", "price_per_night": 5500, "rating": 4.6, "area": "Indira Gandhi Stadium Road", "amenities": ["Valley Views", "Multi-Cuisine Dining", "Terrace"], "suitability": ["Couples", "Family"]},
                {"name": "Hotel Japfu (Nagaland Tourism)", "category": "Heritage City Stay", "price_per_night": 3200, "rating": 4.3, "area": "PR Hill", "amenities": ["Restaurant", "Bar", "Parking"], "suitability": ["Family", "Solo"]},
                {"name": "Morung Lodge & Homestay Khonoma", "category": "Traditional Angami Homestay", "price_per_night": 1800, "rating": 4.8, "area": "Khonoma Village", "amenities": ["Authentic Naga Kitchen", "Village Walks", "Campfires"], "suitability": ["Solo", "Couples"]}
            ],
            [
                {"name": "Orami Kohima", "cuisine": "Authentic Naga Traditional Cuisine", "average_cost_for_two": 600, "rating": 4.7, "area": "PR Hill", "popular_dishes": "Smoked Pork with Axone (Fermented Soybeans), Raja Mircha Chutney, Galho", "is_veg": False},
                {"name": "Dziiko Cafe", "cuisine": "Artisan Coffee, Naga Snacks & Bakery", "average_cost_for_two": 450, "rating": 4.6, "area": "Razhu Point", "popular_dishes": "Smoked Beef Sandwich, Specialty Pour Over Coffee, Cheesecakes", "is_veg": False},
                {"name": "Khonoma Community Kitchen", "cuisine": "Angami Organic Home Meals", "average_cost_for_two": 350, "rating": 4.8, "area": "Khonoma", "popular_dishes": "Boiled Organic Vegetables, Roasted Local Chicken, Rice with Herbs", "is_veg": False}
            ]
        ),
        make_destination(
            "Dzukou Valley", "The Valley of Flowers of the Northeast",
            "Untouched high-altitude rolling green bamboo-turfed valley at 8,000 ft, rare endemic Dzukou lily, and meandering crystal streams.",
            1800, "Jun–Sep (Lilies) & Oct–Mar", "2 Days", 4.9, 9.6, "High-Altitude Wilderness Trek & Wild Camping", ["Adventure", "Friends", "Solo"], "Viswema",
            ["Dzukou Valley Basin", "Viswema Trek Trail", "Jakhama Steep Route", "Natural Rock Caves"],
            [
                {"name": "Dzukou Valley Basin", "category": "High Alpine Valley", "highlight": "Rolling cushion-like dwarf bamboo hills traversed by crystal frozen streams and seasonal wildflowers", "fee": "₹50", "time": "Full Day"},
                {"name": "Natural Dzukou Caves", "category": "Rock Overhang Caverns", "highlight": "Overhanging rock formations used for centuries by Naga hunters and trekkers for campfires", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Trek from Viswema up the Forest Ridge to Dzukou", "category": "Himalayan Trek", "cost": 400, "duration": "5 hrs"},
                {"name": "Camping under Starlit Skies in Dzukou Valley Dormitory", "category": "Wilderness Camping", "cost": 500, "duration": "Overnight"},
                {"name": "Wildflower Photography (Endemic Pink Dzukou Lily in July)", "category": "Nature Photography", "cost": 0, "duration": "3 hrs"}
            ],
            [
                {"name": "Dzukou Valley Trekkers Rest House", "category": "Rustic Alpine Dormitory", "price_per_night": 300, "rating": 4.4, "area": "Valley Crest", "amenities": ["Foam Mattresses", "Fireplace Canteen", "Panoramic Views"], "suitability": ["Adventure", "Solo", "Friends"]},
                {"name": "Camp David Dzukou Tents", "category": "High Altitude Tented Camp", "price_per_night": 1200, "rating": 4.5, "area": "Dzukou Valley", "amenities": ["Tents Provided", "Sleeping Bags", "Campfire"], "suitability": ["Adventure", "Friends"]},
                {"name": "Viswema Village Base Homestay", "category": "Trailhead Village Homestay", "price_per_night": 1500, "rating": 4.6, "area": "Viswema Trailhead", "amenities": ["Hot Water", "Home Cooked Meals", "Trek Guide"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Dzukou Rest House Canteen", "cuisine": "Rustic Trekkers Camp Food", "average_cost_for_two": 300, "rating": 4.5, "area": "Valley Rest House", "popular_dishes": "Hot Maggi with Egg, Black Tea, Plain Dal Rice with Naga Pickle", "is_veg": True},
                {"name": "Viswema Trailhead Eatery", "cuisine": "Traditional Naga Home Cooking", "average_cost_for_two": 350, "rating": 4.4, "area": "Viswema Highway", "popular_dishes": "Pork Stew, Steamed Rice, Red Chilli Chutney", "is_veg": False}
            ]
        ),
        make_destination(
            "Mokokchung", "The Cultural Heart of the Ao Nagas",
            "Scenic ridge villages of the Ao tribe, Longkhum eagle-nest viewpoints, ancient log drums (Tsungrem Mong), and Ungma village.",
            1700, "Oct–May", "2 Days", 4.7, 9.0, "Ao Naga Heritage & Ridge Villages", ["Culture", "Couples", "Solo"], "Mokokchung",
            ["Ungma Ancient Village", "Longkhum Eagle Cliff", "Mokokchung Park"],
            [
                {"name": "Ungma Historic Village", "category": "Oldest Ao Village", "highlight": "Second largest village in Nagaland and ancestral birthplace of the Ao Naga clan", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Longkhum Village & Eagle Crest", "category": "Panoramic Ridge Cliff", "highlight": "Fabled hill village where souls of the dead are believed to rest among rhododendrons", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Inspecting Traditional Ao Log Drums & Morungs", "category": "Cultural Walk", "cost": 0, "duration": "2 hrs"},
                {"name": "Handloom Shawl Weaving Demonstration in Ungma", "category": "Textile Tour", "cost": 150, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Hotel Metsuben Mokokchung", "category": "Boutique Ao Heritage Stay", "price_per_night": 2800, "rating": 4.4, "area": "Main Town", "amenities": ["Naga Decor", "Restaurant", "WiFi"], "suitability": ["Couples", "Solo"]},
                {"name": "Longkhum Tourist Lodge", "category": "Ridge View Lodge", "price_per_night": 1500, "rating": 4.2, "area": "Longkhum Cliff", "amenities": ["Mountain Views", "Home Cooked Meals"], "suitability": ["Friends", "Solo"]}
            ],
            [
                {"name": "Metsuben Kitchen", "cuisine": "Ao Naga Traditional Cuisine", "average_cost_for_two": 450, "rating": 4.6, "area": "Mokokchung Town", "popular_dishes": "Anishi (Fermented Yam Leaves with Pork), Boiled Fish, Sticky Rice", "is_veg": False},
                {"name": "Corner Cafe Mokokchung", "cuisine": "Bakery, Snacks & Coffee", "average_cost_for_two": 300, "rating": 4.3, "area": "Town Square", "popular_dishes": "Pork Momos, Fresh Bread, Filter Coffee", "is_veg": False}
            ]
        ),
        make_destination(
            "Dimapur", "The Ancient Kachari Ruins & Gateway",
            "13th-century mushroom-shaped monolithic pillars of the Kachari Kingdom, vibrant handloom markets, and Triple Falls.",
            1800, "Oct–Mar", "2 Days", 4.5, 8.8, "Kachari Archaeology & Commercial Hub", ["Family", "Solo", "Business"], "Dimapur",
            ["Kachari Ruins Complex", "Diezephe Craft Village", "Triple Falls"],
            [
                {"name": "Kachari Ruins (Rajbari)", "category": "Megalithic Stone Pillars", "highlight": "Mysterious 13th-century mushroom-domed carved stone pillars erected by Kachari rulers", "fee": "Free", "time": "2 hrs"},
                {"name": "Diezephe Craft Village", "category": "Handicrafts Hub", "highlight": "Famous craft village producing exquisite wood carvings and cane furniture", "fee": "Free", "time": "2.5 hrs"}
            ],
            [
                {"name": "Naga Handloom and Shawl Shopping in Hong Kong Market", "category": "Shopping", "cost": 0, "duration": "2.5 hrs"},
                {"name": "Trek to Secluded Triple Falls Cascade", "category": "Nature Hike", "cost": 0, "duration": "3 hrs"}
            ],
            [
                {"name": "Niathu Resort Dimapur", "category": "Luxury Riverside 4-Star Resort", "price_per_night": 5200, "rating": 4.6, "area": "Chumukedima", "amenities": ["Pool", "Spa", "Lush Lawns", "Riverside Dining"], "suitability": ["Couples", "Family"]},
                {"name": "Hotel Acacia Dimapur", "category": "Business Hotel", "price_per_night": 2800, "rating": 4.3, "area": "Opposite Railway Station", "amenities": ["AC", "Restaurant", "WiFi"], "suitability": ["Business", "Solo"]}
            ],
            [
                {"name": "Bambusa Restaurant Dimapur", "cuisine": "Pan-Asian & Naga Fusion", "average_cost_for_two": 700, "rating": 4.5, "area": "Circular Road", "popular_dishes": "Pork with Bamboo Shoot, Dim Sums, Hakka Noodles", "is_veg": False},
                {"name": "Jal Mahal Vegetarian Restaurant", "cuisine": "Pure Veg North & South Indian", "average_cost_for_two": 400, "rating": 4.3, "area": "Nyamo Lotha Road", "popular_dishes": "Masala Dosa, Thali, Paneer Butter Masala", "is_veg": True}
            ]
        )
    ]
}

# ── 22. Sikkim ────────────────────────────────────────────────────────────────
NORTHEAST_STATES["Sikkim"] = {
    "capital": "Gangtok", "region": "Northeast", "tagline": "Small Beautiful & 100% Organic State",
    "destinations": [
        make_destination(
            "Gangtok", "The Clean & Modern Himalayan Capital",
            "Flourishing pedestrian MG Marg, Rumtek Dharma Chakra monastery, Banjhakri waterfall park, and views of Mt. Kanchenjunga.",
            2500, "Mar–Jun & Sep–Dec", "3 Days", 4.8, 9.8, "Organic Clean Living & Tibetan Monasteries", ["Couples", "Family", "Solo"], "Gangtok",
            ["MG Marg Promenade", "Rumtek Monastery", "Tashi Viewpoint", "Enchey Monastery", "Banjhakri Falls"],
            [
                {"name": "MG Marg Clean Promenade", "category": "Litter-Free Pedestrian Boulevard", "highlight": "Spit-and-litter-free pedestrian stone boulevard lined with flowers, cafes, and benches", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Rumtek Monastery (Dharma Chakra Centre)", "category": "Seat of the Karmapa", "highlight": "Grand monastery complex housing sacred Tibetan relics, golden stupa, and 1,000 monks", "fee": "₹20", "time": "2.5 hrs"},
                {"name": "Tashi Viewpoint", "category": "Panoramic Mountain Lookout", "highlight": "Sunrise vista overlooking the snow giants of Mt. Kanchenjunga and Siniolchu", "fee": "Free", "time": "1.5 hrs"},
                {"name": "Banjhakri Waterfalls & Energy Park", "category": "Eco Waterfall Park", "highlight": "100-ft cascading waterfall with paved trails, shamanic sculptures, and bridges", "fee": "₹50", "time": "2 hrs"}
            ],
            [
                {"name": "Cable Car Ropeway Ride from Deorali to Tashiling", "category": "Aerial Cable Car", "cost": 150, "duration": "45 mins"},
                {"name": "Cafe Hopping and Evening Stroll along MG Marg", "category": "Evening Leisure", "cost": 0, "duration": "2.5 hrs"},
                {"name": "Tasting Sikkim's Local Organic Fruit Wines", "category": "Wine Tasting", "cost": 300, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Mayfair Spa Resort & Casino, Gangtok", "category": "Luxury 5-Star Himalayan Palace", "price_per_night": 16000, "rating": 4.9, "area": "Ranipool", "amenities": ["On-site Live Casino", "Heated Pool", "Monastic Spa"], "suitability": ["Couples", "Family"]},
                {"name": "The Elgin Nor-Khill Gangtok", "category": "Royal Chogyal Heritage Hotel", "price_per_night": 11000, "rating": 4.7, "area": "Paljor Stadium Road", "amenities": ["Tibetan Murals", "Fireplaces", "Courtyard Views"], "suitability": ["Couples", "Family"]},
                {"name": "Tag Along Backpackers Hostel", "category": "Cozy Community Hostel", "price_per_night": 850, "rating": 4.6, "area": "Tibet Road", "amenities": ["Cafe", "Travel Library", "High Speed WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "The Square (MG Marg)", "cuisine": "Pan-Asian, Sikkimese & Continental", "average_cost_for_two": 900, "rating": 4.7, "area": "MG Marg", "popular_dishes": "Gyathuk, Steamed Pork Momos, Sikkimese Set Meal with Gundruk", "is_veg": False},
                {"name": "Taste of Tibet", "cuisine": "Authentic Tibetan Diner", "average_cost_for_two": 500, "rating": 4.6, "area": "MG Marg", "popular_dishes": "Shaphalay (Deep Fried Meat Bread), Thukpa, Momos", "is_veg": False},
                {"name": "Baker's Cafe", "cuisine": "Artisan Bakery & Coffee", "average_cost_for_two": 600, "rating": 4.6, "area": "MG Marg", "popular_dishes": "Hot Chocolate, Bagels with Cream Cheese, Apple Pie", "is_veg": True}
            ]
        ),
        make_destination(
            "Tsomgo Lake & Nathula Pass", "Sacred Alpine Lake & The Silk Route Border",
            "Glacial sacred lake at 12,310 ft frozen in winter, decorated yaks, and historic Indo-China Silk Route pass at Nathula (14,140 ft).",
            2800, "Mar–May & Oct–Dec", "1 Day", 4.9, 9.7, "Glacial Alpine Lakes & High Altitude Passes", ["Family", "Couples", "Adventure"], "Gangtok",
            ["Tsomgo (Changu) Lake", "Nathula Pass Border", "Baba Harbhajan Singh Mandir", "Kyongnosla Sanctuary"],
            [
                {"name": "Tsomgo (Changu) Glacial Lake", "category": "Sacred Glacial Oval Lake", "highlight": "Pristine high-altitude oval lake surrounded by snow peaks and Tibetan prayer flags", "fee": "Free", "time": "2.5 hrs"},
                {"name": "Nathula Pass (Indo-China Border)", "category": "Historic Silk Route Pass", "highlight": "14,140-ft pass with international border fence where Indian and Chinese soldiers stand guard", "fee": "Permit Required", "time": "2 hrs"},
                {"name": "Baba Harbhajan Singh Temple", "category": "Heroic Soldier Memorial", "highlight": "Revered shrine dedicated to the folk-hero Indian soldier believed to guard the borders", "fee": "Free", "time": "1.5 hrs"}
            ],
            [
                {"name": "Riding a Decorated Yak along the Shores of Tsomgo Lake", "category": "Yak Ride", "cost": 300, "duration": "45 mins"},
                {"name": "Cable Car Ropeway Ride over Frozen Tsomgo Lake", "category": "Aerial Cable Car", "cost": 400, "duration": "1 hr"},
                {"name": "Sipping Steaming Butter Tea and Maggi at 12,000 ft", "category": "Mountain Comfort Food", "cost": 150, "duration": "1 hr"}
            ],
            [
                {"name": "Summit Golden Crescent Resort (Gangtok Base)", "category": "Comfort Mountain Stay", "price_per_night": 4200, "rating": 4.4, "area": "Near Lower Sichey", "amenities": ["Mountain Views", "Restaurant", "Tour Desk"], "suitability": ["Couples", "Family"]},
                {"name": "The Chumbi Mountain Retreat (Pelling/Sikkim)", "category": "Luxury Boutique Monastery Resort", "price_per_night": 12000, "rating": 4.8, "area": "Naku Chumbong", "amenities": ["Traditional Dottho Stone Bath", "Spa", "Kanchenjunga Views"], "suitability": ["Couples", "Family"]},
                {"name": "Zostel Gangtok", "category": "Backpacker Hostel", "price_per_night": 800, "rating": 4.5, "area": "Tadong", "amenities": ["Common Lounge", "Cafe", "Trek Booking"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Tsomgo Lake Lakeside Stalls", "cuisine": "High Altitude Mountain Comfort", "average_cost_for_two": 300, "rating": 4.6, "area": "Lake Edge", "popular_dishes": "Hot Butter Tea, Vegetable Thukpa, Maggi with Cheese, Wai Wai", "is_veg": True},
                {"name": "Sher-e-Punjab (Gangtok Return Road)", "cuisine": "Highway Punjabi & Dhaba", "average_cost_for_two": 600, "rating": 4.4, "area": "NH-31A", "popular_dishes": "Butter Chicken, Dal Tadka, Tandoori Parathas", "is_veg": False},
                {"name": "Nathula Pass Military Canteen", "cuisine": "Hot Beverages & Snacks", "average_cost_for_two": 150, "rating": 4.7, "area": "Nathula Border", "popular_dishes": "Hot Chai, Samosas, Gulab Jamun at 14,000 ft", "is_veg": True}
            ]
        ),
        make_destination(
            "Pelling & West Sikkim", "Closest Views of Mt. Kanchenjunga & Skywalk",
            "Clear vistas of the third highest peak on earth, India's first glass skywalk at Chenrezig statue, Pemayangtse Monastery, and Rabdentse ruins.",
            2200, "Mar–May & Sep–Dec", "3 Days", 4.8, 9.6, "Himalayan Glass Skywalk & Sacred Monasteries", ["Couples", "Family", "Solo"], "Pelling",
            ["Chenrezig Statue & Skywalk", "Pemayangtse Monastery", "Rabdentse Ruins", "Khecheopalri Lake", "Singshore Bridge"],
            [
                {"name": "Chenrezig Statue & Glass Skywalk", "category": "Glass Skywalk & Colossal Icon", "highlight": "India's first glass skywalk hovering over mist with 137-ft statue of Bodhisattva Chenrezig", "fee": "₹50", "time": "2 hrs"},
                {"name": "Pemayangtse Monastery", "category": "Historic Nyingma Monastery", "highlight": "300-year-old premier monastery with exquisite wooden model of Guru Rinpoche's celestial palace", "fee": "₹20", "time": "2 hrs"},
                {"name": "Rabdentse Ruins", "category": "Ancient Kingdom Ruins", "highlight": "Stone palace ruins of Sikkim's 2nd royal capital surrounded by chestnut forests facing Kanchenjunga", "fee": "Free", "time": "2 hrs"},
                {"name": "Khecheopalri Sacred Lake (Wish-Fulfilling Lake)", "category": "Sacred Wish Lake", "highlight": "Sacred lake where leaves are believed to be plucked instantly from water by birds", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Walking on the Transparent Glass Skywalk with Valley Drop", "category": "Skywalk Experience", "cost": 50, "duration": "1.5 hrs"},
                {"name": "Heritage Walk through the Chestnut Forest to Rabdentse Ruins", "category": "Heritage Walk", "cost": 0, "duration": "2.5 hrs"},
                {"name": "Bungee Jumping / Sky Walking at Singshore Bridge", "category": "Bridge Walk", "cost": 100, "duration": "1.5 hrs"}
            ],
            [
                {"name": "The Chumbi Mountain Retreat", "category": "Luxury Traditional Heritage Resort", "price_per_night": 12500, "rating": 4.9, "area": "Naku Chumbong", "amenities": ["Organic Herbal Stone Baths", "Kanchenjunga Views", "Movie Lounge"], "suitability": ["Couples", "Family"]},
                {"name": "Elgin Mount Pandim Pelling", "category": "Royal Chogyal 4-Star Resort", "price_per_night": 9500, "rating": 4.7, "area": "Monastery Road", "amenities": ["Direct Mountain Views", "Gardens", "Victorian Lounge"], "suitability": ["Couples", "Family"]},
                {"name": "Hotel Simvo Pelling", "category": "Comfort Hill Hotel", "price_per_night": 2400, "rating": 4.2, "area": "Upper Pelling", "amenities": ["Balcony Views", "Restaurant", "WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Lotus Bakery", "cuisine": "Tibetan Bakes, Coffee & Desserts", "average_cost_for_two": 350, "rating": 4.6, "area": "Near Pemayangtse", "popular_dishes": "Fresh Cinnamon Buns, Apple Strudel, Filter Coffee", "is_veg": True},
                {"name": "Melting Point Restaurant", "cuisine": "Sikkimese & Chinese", "average_cost_for_two": 550, "rating": 4.5, "area": "Upper Pelling", "popular_dishes": "Pork Momos, Thukpa, Chicken Kothey, Tingmo", "is_veg": False},
                {"name": "Kanchenjunga View Restaurant", "cuisine": "North Indian & Nepali Thali", "average_cost_for_two": 450, "rating": 4.3, "area": "Middle Pelling", "popular_dishes": "Nepali Thali, Gundruk Soup, Kalo Dal", "is_veg": True}
            ]
        ),
        make_destination(
            "Lachung & Yumthang Valley", "The Valley of Rhododendrons & Zero Point",
            "High-altitude valley of flowers at 11,800 ft with 24 species of blooming rhododendrons, hot springs, and snowbound Zero Point (Yumesamdong).",
            3000, "Mar–Jun & Oct–Dec", "3 Days", 4.9, 9.7, "Alpine Valley of Flowers & Snow Glaciers", ["Adventure", "Couples", "Solo"], "Lachung",
            ["Yumthang Valley Basin", "Zero Point (15,300 ft)", "Lachung Village", "Hot Sulfur Springs"],
            [
                {"name": "Yumthang Valley of Flowers", "category": "Alpine Sanctuary", "highlight": "Rolling meadows surrounded by snow peaks and carpeted with blooming wild rhododendrons", "fee": "Free", "time": "4 hrs"},
                {"name": "Zero Point (Yumesamdong)", "category": "High Snow Glacier Point", "highlight": "15,300-ft high mountain pass where civilian road ends into pristine snow glaciers", "fee": "Permit", "time": "3 hrs"}
            ],
            [
                {"name": "Bathing in Natural Sulfuric Hot Springs of Yumthang", "category": "Thermal Springs", "cost": 50, "duration": "1 hr"},
                {"name": "Snow Sledding and Snowball Fights at Zero Point", "category": "Snow Activity", "cost": 200, "duration": "2 hrs"}
            ],
            [
                {"name": "Yarlam Resort Lachung", "category": "Luxury 4-Star Mountain Resort", "price_per_night": 7500, "rating": 4.6, "area": "Lachung Village", "amenities": ["Mountain Views", "Heated Blankets", "Bar"], "suitability": ["Couples", "Family"]},
                {"name": "OurGuest Camp Lachung", "category": "Eco Alpine Cottages", "price_per_night": 3800, "rating": 4.4, "area": "Singring", "amenities": ["Wooden Architecture", "Campfire", "Buffet"], "suitability": ["Friends", "Solo"]}
            ],
            [
                {"name": "Yarlam Dining Hall", "cuisine": "Sikkimese, Tibetan & Indian", "average_cost_for_two": 700, "rating": 4.5, "area": "Lachung", "popular_dishes": "Hot Thukpa, Steamed Momos, Chicken Curry", "is_veg": False},
                {"name": "Zero Point Snow Canteen", "cuisine": "High-Altitude Comfort Snacks", "average_cost_for_two": 250, "rating": 4.7, "area": "Zero Point", "popular_dishes": "Hot Maggi, Brandy Coffee, Steaming Momos in Snow", "is_veg": True}
            ]
        )
    ]
}

# ── 25. Tripura ───────────────────────────────────────────────────────────────
NORTHEAST_STATES["Tripura"] = {
    "capital": "Agartala", "region": "Northeast", "tagline": "The Crown Jewel of the East",
    "destinations": [
        make_destination(
            "Agartala", "The Royal Palace City & Heritage Capital",
            "Gleaming white Ujjayanta Palace, Indo-Bangla Akhaura border beating retreat, Jagannath temple, and Purbasha bamboo crafts.",
            1700, "Oct–Mar", "2 Days", 4.6, 9.1, "Tripuri Royal Palaces & Border Ceremonies", ["Family", "Solo", "Couples"], "Agartala",
            ["Ujjayanta Palace Complex", "Akhaura Integrated Border", "Heritage Park", "Jagannath Mandir"],
            [
                {"name": "Ujjayanta Palace (Tripura State Museum)", "category": "Neoclassical Royal Palace", "highlight": "Gleaming white royal palace surrounded by Mughal gardens, fountains, and high domes", "fee": "₹20", "time": "2.5 hrs"},
                {"name": "Akhaura Indo-Bangladesh Border", "category": "International Border Retreat", "highlight": "Joint military flag-lowering parade between BSF and Border Guards Bangladesh", "fee": "Free", "time": "2 hrs"},
                {"name": "Heritage Park Agartala", "category": "Eco Miniature Park", "highlight": "Landscaped 12-acre park displaying miniature replicas of all Tripura historical sites", "fee": "₹20", "time": "1.5 hrs"}
            ],
            [
                {"name": "Attending the Akhaura Border Flag Lowering Ceremony", "category": "Border Ceremony", "cost": 0, "duration": "2 hrs"},
                {"name": "Shopping for Fine Bamboo & Cane Furniture at Purbasha", "category": "Handicrafts Shopping", "cost": 0, "duration": "2 hrs"},
                {"name": "Evening Fountain & Musical Light Show at Ujjayanta", "category": "Light Show", "cost": 50, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Hotel Polo Lake Resort / Polo Towers Agartala", "category": "Luxury 5-Star Hotel", "price_per_night": 6500, "rating": 4.7, "area": "VIP Road", "amenities": ["Outdoor Pool", "Grand Ballroom", "Fine Dining"], "suitability": ["Couples", "Family", "Business"]},
                {"name": "Ginger Agartala", "category": "Smart Business Stay", "price_per_night": 2600, "rating": 4.2, "area": "Khejur Bagan", "amenities": ["Cafe", "Gym", "Free WiFi"], "suitability": ["Business", "Solo"]},
                {"name": "Hotel Welcome Palace", "category": "City Centre Stay", "price_per_night": 2000, "rating": 4.1, "area": "Hari Ganga Basak Road", "amenities": ["Restaurant", "AC", "Room Service"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Kurry Club (Hotel Polo Towers)", "cuisine": "Tripuri Royal, Bengali & Pan-Asian", "average_cost_for_two": 1200, "rating": 4.6, "area": "VIP Road", "popular_dishes": "Mui Borok (Tripuri Traditional Fish), Kosha Mangsho, Dim Pulao", "is_veg": False},
                {"name": "Abhula Restaurant", "cuisine": "Authentic Traditional Tripuri Delicacies", "average_cost_for_two": 450, "rating": 4.7, "area": "Melarmath", "popular_dishes": "Chakhwi, Berma Chutney (Fermented Fish), Wahan Mosdeng (Pork Salad)", "is_veg": False},
                {"name": "Momos & More Agartala", "cuisine": "Tibetan & Street Snacks", "average_cost_for_two": 250, "rating": 4.3, "area": "Banamalipur", "popular_dishes": "Steamed Chicken Momos, Thukpa, Chowmein", "is_veg": False}
            ]
        ),
        make_destination(
            "Neermahal & Unakoti", "The Floating Water Palace & Colossal Rock Carvings",
            "Neermahal—eastern India's only water palace floating in Rudrasagar Lake, combined with Unakoti's 9th-century rock-cut Shaivite giant sculptures.",
            1800, "Oct–Mar", "2 Days", 4.8, 9.4, "Floating Water Palaces & Ancient Rock Carvings", ["Culture", "Couples", "Solo"], "Melaghar",
            ["Neermahal Water Palace", "Rudrasagar Lake", "Unakoti Rock Sculptures", "Kailashahar"],
            [
                {"name": "Neermahal (Twijilikma Water Palace)", "category": "Floating Lake Palace", "highlight": "Stunning 1930s royal summer palace floating in the centre of Rudrasagar Lake reached by boat", "fee": "₹30 (Boat extra)", "time": "3 hrs"},
                {"name": "Unakoti Rock-Cut Shaivite Reliefs", "category": "Ancient Rock Carving Sanctuary", "highlight": "Hundreds of colossal stone faces of Lord Shiva (Unakotiswara Kal Bhairav 30 ft) carved into a jungle ravine", "fee": "Free", "time": "3.5 hrs"},
                {"name": "Rudrasagar Lake", "category": "Ramsar Wetland Lake", "highlight": "Expansive blue lake hosting migratory birds and royal motorized boats", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Motorboat Cruise across Rudrasagar Lake to Neermahal", "category": "Boat Experience", "cost": 100, "duration": "1.5 hrs"},
                {"name": "Guided Archaeology Walk through the Rock Faces of Unakoti", "category": "Archaeology Walk", "cost": 150, "duration": "2.5 hrs"},
                {"name": "Rudrasagar Sunset Photography", "category": "Sunset Photography", "cost": 0, "duration": "1 hr"}
            ],
            [
                {"name": "Sagarmahal Tourist Lodge (Tripura Tourism)", "category": "Lakefront Heritage Lodge", "price_per_night": 2200, "rating": 4.3, "area": "Rudrasagar Lake Bank, Melaghar", "amenities": ["Neermahal Views", "Restaurant", "Boat Jetty Access"], "suitability": ["Couples", "Family"]},
                {"name": "Unakoti Tourist Lodge (Kailashahar)", "category": "Forest Tourism Stay", "price_per_night": 1800, "rating": 4.2, "area": "Kailashahar", "amenities": ["Unakoti Proximity", "Restaurant", "Gardens"], "suitability": ["Solo", "Friends"]},
                {"name": "Hotel Royal Guest House", "category": "Budget Transit Stay", "price_per_night": 1200, "rating": 3.9, "area": "Melaghar Town", "amenities": ["Room Service", "WiFi"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Sagarmahal Lodge Restaurant", "cuisine": "Traditional Bengali & Fresh Fish", "average_cost_for_two": 450, "rating": 4.2, "area": "Rudrasagar Lake", "popular_dishes": "Fresh Rudrasagar Katla Fish Curry, Dal, Bhaat, Aloo Bhaja", "is_veg": False},
                {"name": "Melaghar Sweet Corner", "cuisine": "Traditional Bengali Sweets & Snacks", "average_cost_for_two": 150, "rating": 4.5, "area": "Melaghar Bazaar", "popular_dishes": "Hot Rasgullas, Chena Sweets, Samosas", "is_veg": True},
                {"name": "Unakoti Footpath Canteen", "cuisine": "Rustic North Eastern Snacks", "average_cost_for_two": 200, "rating": 4.3, "area": "Unakoti Entrance", "popular_dishes": "Puri Sabzi, Maggi, Ginger Tea", "is_veg": True}
            ]
        ),
        make_destination(
            "Jampui Hills", "The Eternal Spring & Orange Ridge",
            "Highest hill range in Tripura at 3,200 ft with panoramic sunrise views of Chittagong hill tracts, orange orchards, and Mizo villages.",
            1500, "Oct–Mar", "2 Days", 4.6, 8.7, "Highland Orange Orchards & Ridge Views", ["Couples", "Solo", "Nature"], "Kanchanpur",
            ["Betlingchhip Peak", "Vanghmun Village", "Orange Orchards"],
            [
                {"name": "Betlingchhip Peak (3,050 ft)", "category": "Highest Peak in Tripura", "highlight": "Highest summit offering vistas spanning Mizoram valleys and Bangladesh plains", "fee": "Free", "time": "2 hrs"},
                {"name": "Vanghmun Model Mizo Village", "category": "Clean Village", "highlight": "Picturesque highland village known for floral gardens and clean cobblestone pathways", "fee": "Free", "time": "2 hrs"}
            ],
            [
                {"name": "Trek up to Betlingchhip Watchtower for Sunrise", "category": "Sunrise Hike", "cost": 0, "duration": "2.5 hrs"},
                {"name": "Orange Orchard Harvesting Tour (Nov-Dec)", "category": "Agri-Tourism", "cost": 100, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Eden Tourist Lodge Jampui (Tripura Tourism)", "category": "Hilltop Viewpoint Lodge", "price_per_night": 1800, "rating": 4.3, "area": "Vanghmun", "amenities": ["Panoramic Balconies", "Dining"], "suitability": ["Couples", "Solo"]},
                {"name": "Jampui Valley Homestay", "category": "Mizo Village Homestay", "price_per_night": 1200, "rating": 4.5, "area": "Phuldungsei", "amenities": ["Home Cooked Meals", "Gardens"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Eden Lodge Restaurant", "cuisine": "Mizo & Bengali Comfort Meals", "average_cost_for_two": 350, "rating": 4.2, "area": "Eden Lodge", "popular_dishes": "Country Chicken Curry, Steamed Rice, Bamboo Chutney", "is_veg": False},
                {"name": "Vanghmun Village Tea Stall", "cuisine": "Tea & Mountain Snacks", "average_cost_for_two": 120, "rating": 4.5, "area": "Village Square", "popular_dishes": "Hot Spiced Tea, Biscuits, Boiled Eggs", "is_veg": True}
            ]
        ),
        make_destination(
            "Sepahijala Wildlife Sanctuary", "Clouded Leopard Sanctuary & Forest Lakes",
            "Biodiversity sanctuary famous for breeding clouded leopards, capped langurs, botanical gardens, and pedal boating on Amrit Sagar lake.",
            1400, "Oct–Apr", "1 Day", 4.5, 8.6, "Clouded Leopard Sanctuary & Lake Boating", ["Family", "Wildlife Enthusiasts", "Solo"], "Bishalgarh",
            ["Sepahijala Zoo", "Amrit Sagar Lake", "Botanical Garden"],
            [
                {"name": "Clouded Leopard Breeding Centre", "category": "Rare Wildlife Sanctuary", "highlight": "Renowned sanctuary successfully conserving the elusive clouded leopard and spectacled monkey (Phayre's langur)", "fee": "₹30", "time": "3 hrs"},
                {"name": "Amrit Sagar Lake & Toy Train", "category": "Lake Boating", "highlight": "Forest lake offering pedal boating and mini toy train ride through teak woods", "fee": "₹50", "time": "2 hrs"}
            ],
            [
                {"name": "Pedal Boating across Amrit Sagar Lake", "category": "Boating", "cost": 100, "duration": "1 hr"},
                {"name": "Botanical and Medicinal Plant Garden Walk", "category": "Botanical Walk", "cost": 0, "duration": "1.5 hrs"}
            ],
            [
                {"name": "Sepahijala Forest Rest House", "category": "Forest Edge Lodge", "price_per_night": 1500, "rating": 4.1, "area": "Sanctuary Campus", "amenities": ["Forest Views", "Dining"], "suitability": ["Family", "Solo"]},
                {"name": "Bishalgarh Highway Stay", "category": "Comfort Transit Hotel", "price_per_night": 1400, "rating": 4.0, "area": "Bishalgarh", "amenities": ["AC", "Room Service"], "suitability": ["Solo", "Friends"]}
            ],
            [
                {"name": "Sepahijala Canteen", "cuisine": "Bengali & Tripuri Meals", "average_cost_for_two": 300, "rating": 4.2, "area": "Near Zoo Gate", "popular_dishes": "Fish Curry with Rice, Dal, Aloo Bhaja", "is_veg": False},
                {"name": "Lake View Snacks Stall", "cuisine": "Light Refreshments", "average_cost_for_two": 150, "rating": 4.3, "area": "Amrit Sagar Jetty", "popular_dishes": "Chai, Samosa, Green Coconut", "is_veg": True}
            ]
        )
    ]
}

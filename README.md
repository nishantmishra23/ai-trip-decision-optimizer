# AI Trip Decision Optimizer

> An intelligent, multi-factor AI-powered travel planning platform built with Streamlit and Python — designed as a full-stack academic mini-project demonstrating real-world data engineering, recommendation algorithms, and modern web application design.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.40%2B-FF4B4B?logo=streamlit)](https://streamlit.io)
[![Google Gemini](https://img.shields.io/badge/Gemini%20AI-Powered-4285F4?logo=google)](https://ai.google.dev/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?logo=mysql)](https://www.mysql.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📖 Overview

The **AI Trip Decision Optimizer** is a comprehensive, multi-page Streamlit web application designed to streamline travel planning using artificial intelligence, real-time weather data, and advanced recommendation algorithms. 

The platform integrates:
- **Multi-factor weighted scoring** to rank travel destinations based on budget fit, activities, season, and popularity
- **Google Gemini AI** for generating day-by-day trip itineraries with intelligent cost breakdowns  
- **Real-time weather intelligence** for destination climate analysis and travel suitability
- **Budget optimization** using configurable expense distribution models
- **Transportation route comparison** across flights, trains, buses, and self-drive options

This project was developed as a B.Tech/MCA Mini Project, demonstrating applied knowledge of software engineering, machine learning recommendation systems, database management, and modern UI/UX design.

---

## ✨ Key Features

### 🧠 AI Recommendation Engine
A custom weighted multi-factor scoring algorithm ranks destinations across five dimensions:
| Factor | Weight |
|---|---|
| Budget fit (daily cost vs. user's budget per day) | 30% |
| Activity & interest match | 25% |
| Season suitability | 20% |
| Popularity & traveller rating | 15% |
| Cost efficiency | 10% |

Destinations are scored 0–100 and ranked in real time based on user-provided preferences.

### 📅 AI Itinerary Generator (Gemini AI)
- Connects to **Google Gemini 1.5 Flash** to generate structured day-by-day travel schedules
- Each slot includes: time, activity title, estimated cost per person, and practical traveller tips
- Falls back to a deterministic rule-based system when the API key is unavailable
- Outputs a per-day cost chart and total trip cost summary

### 🌦️ Weather Intelligence
- Fetches live weather data via **OpenWeatherMap API** (falls back to static estimates if unavailable)
- Displays temperature, humidity, wind speed, and travel suitability badge
- Shows 12-month temperature and rainfall trend charts

### 💰 Smart Budget Optimizer
- Models expense distribution across 5 categories: Transport (25%), Accommodation (35%), Food (20%), Activities (15%), and Miscellaneous (5%)
- Adjustable multipliers for accommodation tier (hostel / mid-range / luxury) and dining preference
- Outputs surplus/deficit analysis with actionable saving tips

### ✈️ Transportation & Route Analysis
- Pre-loaded route data for all 10 destinations covering flights, express trains, overnight buses, and road options
- Side-by-side cost and travel time bar charts for rapid comparison

### 🗺️ Interactive Trip Planner
- Full-form trip builder with date selection, budget input, traveller count, and activity preferences
- Budget breakdown donut chart
- AI-recommended destination alternatives ranked by match score
- Save trip to MySQL database (if connected)

### 🏨 Stays & Experiences
- Hotel recommendations with per-night pricing for all 10 destinations
- Restaurant discovery with cuisine tags and average meal cost
- Activity tour listings with duration and pricing

### 📊 Platform Analytics
- Scatter plot: Daily cost vs. rating across all destinations
- Country distribution bar chart
- Interactive destination data table with formatted columns

---

## 🗺️ Application Architecture

```
ai-trip-decision-optimizer/
│
├── app.py                          # Main entry point (st.navigation multi-page)
│
├── app_pages/                      # Individual page scripts (19 pages)
│   ├── home.py                     # Landing dashboard
│   ├── login.py                    # Authentication (login / register)
│   ├── trip_planner.py             # Interactive trip builder
│   ├── budget_optimizer.py         # Budget allocation engine
│   ├── ai_itinerary.py             # Gemini AI day-by-day itinerary
│   ├── ai_recommendations.py       # Multi-factor destination scoring
│   ├── ai_trip_optimizer.py        # Inline multi-factor optimizer with score charts
│   ├── destination_discovery.py    # Filterable destination browser
│   ├── destination_comparison.py   # Side-by-side radar + bar comparison
│   ├── hotel_recommendations.py    # Hotel catalog per destination
│   ├── restaurant_recommendations.py # Restaurant catalog per destination
│   ├── activity_recommendations.py # Activity / tour catalog
│   ├── weather_intelligence.py     # Live weather + climate trend charts
│   ├── transportation_analysis.py  # Route cost & duration comparison
│   ├── analytics.py                # Platform-wide analytics dashboard
│   ├── saved_trips.py              # Saved itineraries (DB-backed)
│   ├── trip_history.py             # Historical trips with spend chart
│   ├── trip_summary.py             # Full trip summary + packing checklist
│   └── admin_dashboard.py          # Admin control panel (role-gated)
│
├── auth/
│   └── auth.py                     # Session management, login/register, bcrypt hashing
│
├── database/
│   ├── connection.py               # MySQL connection pool
│   ├── queries.py                  # All CRUD database operations
│   └── schema.sql                  # Database schema DDL
│
├── recommendation/
│   └── engine.py                   # Weighted multi-factor scoring & ranking engine
│
├── services/
│   ├── weather_service.py          # OpenWeatherMap API integration
│   └── llm_service.py              # Google Gemini AI itinerary generation
│
├── utils/
│   ├── theme.py                    # Plotly chart theme adapter
│   ├── helpers.py                  # Shared utility functions (currency, stars, cache)
│   └── components.py               # Reusable Streamlit UI card components
│
├── tests/
│   └── test_features.py            # Unit tests for core modules
│
├── .streamlit/
│   └── config.toml                 # Native Streamlit light/dark theme + font config
│
└── requirements.txt                # Python package dependencies
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- MySQL 8.0+ (optional — app runs in sample-data mode without it)
- OpenWeatherMap API key (optional — falls back to static data)
- Google Gemini API key (optional — falls back to rule-based itinerary)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/nishantmishra23/ai-trip-decision-optimizer.git
cd ai-trip-decision-optimizer

# 2. Create and activate virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Environment Configuration

Create a `.env` file (or set system environment variables):

```env
# MySQL Database (optional — app runs without this)
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=ai_trip_optimizer
DB_PORT=3306

# OpenWeatherMap API (optional)
WEATHER_API_KEY=your_openweathermap_api_key

# Google Gemini AI (optional)
GEMINI_API_KEY=your_gemini_api_key
```

### Database Setup (optional)

```bash
# Create the MySQL database and tables
mysql -u root -p < database/schema.sql
```

### Running the Application

```bash
streamlit run app.py
```

The app will open at **http://localhost:8501**

**Demo account:** `demo@example.com` / `demo1234`

---

## 🎨 Design & Theming

The application uses **native Streamlit theming** via `.streamlit/config.toml` — no custom CSS injection. This ensures:
- Full compatibility with future Streamlit versions
- Clean, consistent rendering across browsers
- Native **light/dark mode toggle** via the Streamlit settings menu (⚙️ top-right corner)

**Theme palette:**
| Mode | Primary | Background | Accent |
|---|---|---|---|
| Light | Indigo `#4F46E5` | `#F9FAFB` | Clean white cards |
| Dark | Violet `#818CF8` | Slate `#0F172A` | Dark card surfaces |

**Typography:** [Inter](https://fonts.google.com/specimen/Inter) (Google Fonts) for body & headings, [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) for code.

---

## 🧪 Testing

```bash
# Run the full test suite
python -m pytest tests/ -v

# Run with coverage report
python -m pytest tests/ --cov=. --cov-report=term-missing
```

**Test coverage includes:**
- Multi-factor recommendation engine (scoring, ranking, edge cases)
- Weather service (live API + static fallback paths)
- Currency formatting (edge cases: zero, thousands, lakhs)
- User authentication (password hashing and verification)
- Session state initialization

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| **Frontend** | Streamlit 1.40+ |
| **Language** | Python 3.9+ |
| **AI / LLM** | Google Gemini 1.5 Flash |
| **Database** | MySQL 8.0 via `mysql-connector-python` |
| **Charts** | Plotly Express & Plotly Graph Objects |
| **Weather API** | OpenWeatherMap REST API |
| **Authentication** | bcrypt password hashing |
| **Data Processing** | pandas, NumPy |
| **Theming** | Native Streamlit config.toml + Google Fonts (Inter) |

---

## 📚 Academic Context

This project was developed as part of the **B.Tech / MCA Mini Project** curriculum, applying concepts from:

- **Software Engineering**: MVC-inspired modular architecture, separation of concerns across `services/`, `database/`, `recommendation/`, and `utils/`
- **Artificial Intelligence**: Weighted decision-making algorithm, LLM API integration (Gemini)
- **Database Management Systems**: Relational schema design, parameterized SQL queries, connection pooling
- **Human-Computer Interaction**: Multi-page navigation, responsive layout, light/dark mode theming
- **API Integration**: REST APIs for weather data and AI model calls, graceful degradation patterns

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "feat: add your feature"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please ensure all tests pass before opening a PR:
```bash
python -m pytest tests/ -v
```

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Nishant Mishra**  
B.Tech / MCA Student | Mini Project — AI & Data Engineering  
GitHub: [@nishantmishra23](https://github.com/nishantmishra23)

---

*Built with ❤️ using Streamlit, Google Gemini AI, and Python.*
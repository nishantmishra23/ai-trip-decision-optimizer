"""
Home / Main Hub for AI Trip Decision Optimizer.
Vibrant student-friendly travel hub featuring all 28 states, AI planning, and live weather.
"""
import streamlit as st
from auth.auth import init_session
from data.india_states_places import ALL_28_STATES, get_all_states, get_google_maps_url
from services.weather_service import get_weather

init_session()

user = st.session_state.get("user", {}) or {}
name = user.get("name", "Student Explorer")

# ── Vibrant Hero Banner ────────────────────────────────────────────────────────
st.markdown(
    """
    <div style="background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #db2777 100%); padding: 32px 28px; border-radius: 16px; color: white; margin-bottom: 24px; box-shadow: 0 10px 25px -5px rgba(79, 70, 229, 0.3);">
        <div style="font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; opacity: 0.9; margin-bottom: 6px;">
            🎓 Smart Travel Intelligence Platform
        </div>
        <div style="font-size: 2.2rem; font-weight: 800; line-height: 1.2; margin-bottom: 10px;">
            Plan Epic Trips Across All 28 States of India
        </div>
        <div style="font-size: 1.05rem; opacity: 0.92; max-width: 780px; line-height: 1.5;">
            Powered by Google Gemini 3.6 Flash and live OpenWeatherMap data. Get day-by-day itineraries, instant student budget breakdowns, live climate checks, and direct Google Maps navigation.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ── Key Statistics Row (Vibrant Cards) ─────────────────────────────────────────
col_s1, col_s2, col_s3, col_s4 = st.columns(4)
with col_s1:
    with st.container(border=True):
        st.markdown("🇮🇳 **All 28 States**")
        st.caption("100% India Covered")
        st.badge("Complete Guide", color="blue")
with col_s2:
    with st.container(border=True):
        st.markdown("💰 **Student Budgets**")
        st.caption("From ₹1,200/day")
        st.badge("Hostels & Thalis", color="green")
with col_s3:
    with st.container(border=True):
        st.markdown("🌤️ **Live Weather**")
        st.caption("OpenWeatherMap API")
        st.badge("Real-Time", color="orange")
with col_s4:
    with st.container(border=True):
        st.markdown("🤖 **Gemini 3.6 Flash**")
        st.caption("AI Day-by-Day Plans")
        st.badge("Instant Generation", color="violet")

st.markdown("<br>", unsafe_allow_html=True)

# ── Quick Jump & Search ────────────────────────────────────────────────────────
with st.container(border=True):
    st.markdown("##### 🔍 Jump to Any State or Destination")
    c_input, c_btn = st.columns([3, 1], gap="medium")
    with c_input:
        chosen_state = st.selectbox(
            "Select State",
            [s["name"] for s in ALL_28_STATES],
            index=8, # Himachal Pradesh default
            label_visibility="collapsed"
        )
    with c_btn:
        if st.button("Explore This State", type="primary", use_container_width=True, icon=":material/arrow_forward:"):
            st.session_state["selected_state_search"] = chosen_state
            st.switch_page("app_pages/all_states_explorer.py")

st.markdown("<br>", unsafe_allow_html=True)

# ── 6 Featured State Spotlights (Unique Non-Repeating Images) ───────────────────
st.subheader("🌟 Featured Student Travel Spotlights", anchor=False)
st.caption("Hand-picked states with student-friendly hostels, cafes, and unforgettable vistas.")

# 6 unique curated destination images — strictly unique, zero repeats
SPOTLIGHTS = [
    {
        "name": "Himachal Pradesh",
        "tagline": "Manali, Spiti & Paragliding in Solang",
        "cost": "₹2,000 / day",
        "category": "Mountains & Snow",
        "badge_color": "blue",
        "city": "Shimla",
        "image": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=800&auto=format&fit=crop&q=80"
    },
    {
        "name": "Goa",
        "tagline": "Sun-drenched beaches, shacks & scooters",
        "cost": "₹2,500 / day",
        "category": "Beach & Nightlife",
        "badge_color": "violet",
        "city": "Panaji",
        "image": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=800&auto=format&fit=crop&q=80"
    },
    {
        "name": "Kerala",
        "tagline": "Munnar tea gardens & Alleppey backwaters",
        "cost": "₹2,200 / day",
        "category": "Backwaters & Nature",
        "badge_color": "green",
        "city": "Kochi",
        "image": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=800&auto=format&fit=crop&q=80"
    },
    {
        "name": "Rajasthan",
        "tagline": "Pink City palaces, desert dunes & forts",
        "cost": "₹2,000 / day",
        "category": "Royal Heritage",
        "badge_color": "orange",
        "city": "Jaipur",
        "image": "https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800&auto=format&fit=crop&q=80"
    },
    {
        "name": "Uttarakhand",
        "tagline": "Rishikesh river rafting & Himalayan treks",
        "cost": "₹1,800 / day",
        "category": "Adventure & Yoga",
        "badge_color": "teal",
        "city": "Dehradun",
        "image": "https://images.unsplash.com/photo-1605649487212-47bdab064df7?w=800&auto=format&fit=crop&q=80"
    },
    {
        "name": "Uttar Pradesh",
        "tagline": "Ganga Aarti at Varanasi & Taj Mahal in Agra",
        "cost": "₹1,500 / day",
        "category": "Spiritual & Wonder",
        "badge_color": "red",
        "city": "Varanasi",
        "image": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=800&auto=format&fit=crop&q=80"
    },
]

cols_spot = st.columns(3)
for idx, spot in enumerate(SPOTLIGHTS):
    with cols_spot[idx % 3]:
        with st.container(border=True):
            # Unique image
            st.image(spot["image"], use_container_width=True)
            st.markdown(f"### {spot['name']}")
            st.caption(spot["tagline"])
            st.badge(spot["category"], color=spot["badge_color"])
            st.badge(spot["cost"], color="green")
            
            c_w, c_go = st.columns([1, 1])
            with c_w:
                w_btn_key = f"spot_w_{idx}"
                if st.button("🌤️ Weather", key=w_btn_key, use_container_width=True):
                    st.session_state[f"show_spot_{idx}"] = True
            with c_go:
                if st.button("Explore ➔", key=f"spot_exp_{idx}", type="primary", use_container_width=True):
                    st.session_state["selected_state_search"] = spot["name"]
                    st.switch_page("app_pages/all_states_explorer.py")

            if st.session_state.get(f"show_spot_{idx}", False):
                w_data = get_weather(spot["city"])
                st.info(
                    f"**{spot['city']} Live:** {w_data.get('temp')}°C, {w_data.get('condition')} ({w_data.get('description')}), Wind: {w_data.get('wind_speed')} km/h",
                    icon=":material/wb_sunny:"
                )

st.markdown("<br>", unsafe_allow_html=True)

# ── Core Action Shortcuts ──────────────────────────────────────────────────────
st.subheader("⚡ Quick Launchpad", anchor=False)
q1, q2, q3, q4 = st.columns(4)

with q1:
    with st.container(border=True):
        st.markdown("🗺️ **All 28 States**")
        st.caption("Discover all regions, capitals, and places with Google links.")
        st.page_link("app_pages/all_states_explorer.py", label="Open 28 States Explorer", icon=":material/arrow_forward:")

with q2:
    with st.container(border=True):
        st.markdown("🤖 **AI Itinerary**")
        st.caption("Let Gemini 3.6 Flash build day-by-day customized travel plans.")
        st.page_link("app_pages/ai_itinerary.py", label="Generate Itinerary", icon=":material/auto_awesome:")

with q3:
    with st.container(border=True):
        st.markdown("🌤️ **Weather Intelligence**")
        st.caption("Check real-time temperatures, rain alerts, and packing tips.")
        st.page_link("app_pages/weather_intelligence.py", label="Check Live Weather", icon=":material/wb_sunny:")

with q4:
    with st.container(border=True):
        st.markdown("💰 **Budget Optimizer**")
        st.caption("Optimize stays, dining, and transit to save student cash.")
        st.page_link("app_pages/budget_optimizer.py", label="Optimize Budget", icon=":material/calculate:")

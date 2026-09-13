"""
Recommendation / scoring engine for AI Trip Decision Optimizer.
Works entirely without a database — uses provided destination data.
"""
from __future__ import annotations
from typing import List, Dict, Any


# ---------------------------------------------------------------------------
# Sample destination data (fallback when DB is unavailable)
# ---------------------------------------------------------------------------
SAMPLE_DESTINATIONS = [
    {"destination_id": 1, "name": "Goa", "country": "India", "average_daily_cost": 3500,
     "popularity_score": 9.2, "rating": 4.5, "category": "Beach", "season": "Oct-Mar",
     "description": "India's party capital with pristine beaches, Portuguese heritage, vibrant nightlife, and world-class seafood."},
    {"destination_id": 2, "name": "Manali", "country": "India", "average_daily_cost": 2800,
     "popularity_score": 8.8, "rating": 4.6, "category": "Mountains", "season": "Oct-Jun",
     "description": "Snow-capped Himalayan retreat with adventure sports, scenic valleys, and monasteries."},
    {"destination_id": 3, "name": "Jaipur", "country": "India", "average_daily_cost": 2500,
     "popularity_score": 9.0, "rating": 4.5, "category": "Heritage", "season": "Oct-Mar",
     "description": "The Pink City — regal forts, ornate palaces, and royal Rajputana cuisine."},
    {"destination_id": 4, "name": "Munnar", "country": "India", "average_daily_cost": 3000,
     "popularity_score": 8.9, "rating": 4.7, "category": "Nature", "season": "Oct-May",
     "description": "God's Own Country — lush tea estates, backwaters, and Ayurvedic retreats."},
    {"destination_id": 5, "name": "Agra", "country": "India", "average_daily_cost": 2000,
     "popularity_score": 9.5, "rating": 4.4, "category": "Heritage", "season": "Oct-Mar",
     "description": "Home to the iconic Taj Mahal and Mughal culinary heritage."},
    {"destination_id": 6, "name": "Bali", "country": "Indonesia", "average_daily_cost": 4500,
     "popularity_score": 9.4, "rating": 4.8, "category": "Beach", "season": "Apr-Oct",
     "description": "Tropical paradise with rice terraces, Hindu temples, and luxury spas."},
    {"destination_id": 7, "name": "Paris", "country": "France", "average_daily_cost": 12000,
     "popularity_score": 9.6, "rating": 4.7, "category": "City", "season": "Apr-Jun",
     "description": "The City of Light — Eiffel Tower, Louvre, haute cuisine, and romance."},
    {"destination_id": 8, "name": "Rishikesh", "country": "India", "average_daily_cost": 1800,
     "popularity_score": 8.7, "rating": 4.5, "category": "Adventure", "season": "Sep-Jun",
     "description": "Yoga capital of the world with adventure sports and spiritual retreats."},
    {"destination_id": 9, "name": "Andaman Islands", "country": "India", "average_daily_cost": 5000,
     "popularity_score": 8.5, "rating": 4.8, "category": "Beach", "season": "Oct-May",
     "description": "Crystal-clear waters, pristine beaches, and vibrant coral reefs."},
    {"destination_id": 10, "name": "Leh-Ladakh", "country": "India", "average_daily_cost": 4000,
     "popularity_score": 8.6, "rating": 4.8, "category": "Mountains", "season": "Jun-Sep",
     "description": "Dramatic moonscapes, Tibetan Buddhist culture, and epic mountain routes."},
]

CATEGORY_ACTIVITY_MAP = {
    "Beach": ["Beach & Water Sports", "Relaxation", "Scuba Diving", "Surfing", "Snorkeling"],
    "Mountains": ["Adventure", "Trekking", "Skiing", "Photography", "Camping"],
    "Heritage": ["Sightseeing", "History", "Photography", "Architecture", "Culture"],
    "Nature": ["Wildlife", "Trekking", "Photography", "Bird Watching", "Eco-tourism"],
    "City": ["Shopping", "Food & Cuisine", "Nightlife", "Museums", "Architecture"],
    "Adventure": ["Rafting", "Bungee Jumping", "Paragliding", "Yoga", "Camping"],
}

SEASON_MAP = {
    "Summer (Apr-Jun)": ["Apr-Jun", "Apr-Oct", "Jun-Sep"],
    "Monsoon (Jul-Sep)": ["Jun-Sep", "Jul-Sep"],
    "Winter (Oct-Dec)": ["Oct-Mar", "Oct-May", "Oct-Jun", "Sep-Jun"],
    "Spring (Jan-Mar)": ["Oct-Mar", "Jan-Mar", "Oct-May"],
    "Any season": None,
}


def _budget_score(daily_cost: float, budget_per_day: float) -> float:
    """Score 0-100: 100 = perfectly matches budget, decreasing as cost diverges."""
    if budget_per_day <= 0:
        return 50.0
    ratio = daily_cost / budget_per_day
    if ratio <= 1.0:
        # Under budget — good, small penalty for being too cheap (could be low quality)
        return max(60.0, 100.0 - (1.0 - ratio) * 30)
    else:
        # Over budget — strong penalty
        return max(0.0, 100.0 - (ratio - 1.0) * 80)


def _activity_score(dest_category: str, preferred_activities: List[str]) -> float:
    """Score 0-100 based on how well destination category matches preferred activities."""
    if not preferred_activities:
        return 70.0
    dest_acts = CATEGORY_ACTIVITY_MAP.get(dest_category, [])
    if not dest_acts:
        return 50.0
    matches = sum(
        1 for pa in preferred_activities
        if any(pa.lower() in da.lower() or da.lower() in pa.lower() for da in dest_acts)
    )
    return min(100.0, 50.0 + (matches / max(len(preferred_activities), 1)) * 50.0)


def _season_score(dest_season: str, preferred_season: str) -> float:
    """Score 0-100 based on season compatibility."""
    if preferred_season == "Any season" or not preferred_season:
        return 80.0
    good_seasons = SEASON_MAP.get(preferred_season, [])
    if good_seasons is None:
        return 80.0
    for s in good_seasons:
        if s in dest_season or dest_season in s:
            return 100.0
    return 40.0


def _popularity_score(popularity: float, rating: float) -> float:
    """Score 0-100 from popularity (0-10) and rating (0-5)."""
    pop_normalized = (popularity / 10.0) * 50
    rat_normalized = (rating / 5.0) * 50
    return pop_normalized + rat_normalized


def score_destination(
    dest: Dict[str, Any],
    budget_per_day: float,
    duration_days: int,
    preferred_activities: List[str],
    preferred_season: str,
    travel_style: str,
) -> Dict[str, Any]:
    """
    Score a destination 0-100 and return explanation bullets.
    Weights:
        Budget fit:     30%
        Activity match: 25%
        Season match:   20%
        Popularity:     15%
        Cost efficiency:10%
    """
    daily_cost = float(dest.get("average_daily_cost", 3000))
    category = dest.get("category", "")
    season = dest.get("season", "")
    popularity = float(dest.get("popularity_score", 7.0))
    rating = float(dest.get("rating", 4.0))

    b_score = _budget_score(daily_cost, budget_per_day)
    a_score = _activity_score(category, preferred_activities)
    s_score = _season_score(season, preferred_season)
    p_score = _popularity_score(popularity, rating)
    # Cost efficiency — cheaper but still well-rated is efficient
    eff_score = min(100.0, (rating / 5.0) * 100 * (1 + max(0, budget_per_day - daily_cost) / (budget_per_day + 1) * 0.3))

    total = (
        b_score * 0.30
        + a_score * 0.25
        + s_score * 0.20
        + p_score * 0.15
        + eff_score * 0.10
    )

    # Build explanation
    reasons = []
    if b_score >= 80:
        reasons.append(f"Great budget fit — estimated ₹{daily_cost:,.0f}/day within your ₹{budget_per_day:,.0f}/day budget")
    elif b_score >= 50:
        reasons.append(f"Reasonable cost at ₹{daily_cost:,.0f}/day (your budget: ₹{budget_per_day:,.0f}/day)")
    else:
        reasons.append(f"Above your budget at ₹{daily_cost:,.0f}/day vs ₹{budget_per_day:,.0f}/day")

    if a_score >= 80:
        reasons.append(f"Excellent match for {', '.join(preferred_activities[:2]) if preferred_activities else 'your interests'}")
    elif a_score >= 60:
        reasons.append(f"Good {category.lower()} destination for your preferred activities")

    if s_score >= 90:
        reasons.append(f"Ideal time to visit during {preferred_season}")
    elif s_score < 50:
        reasons.append(f"Best visited in {season} — check dates")

    if rating >= 4.5:
        reasons.append(f"Highly rated by travellers ({rating}/5.0)")

    total_cost = daily_cost * duration_days
    reasons.append(f"Estimated total trip cost: ₹{total_cost:,.0f} for {duration_days} days")

    return {
        "destination": dest,
        "score": round(total, 1),
        "budget_score": round(b_score, 1),
        "activity_score": round(a_score, 1),
        "season_score": round(s_score, 1),
        "popularity_score": round(p_score, 1),
        "efficiency_score": round(eff_score, 1),
        "reasons": reasons,
        "estimated_total": daily_cost * duration_days,
    }


def get_recommendations(
    destinations: List[Dict],
    budget: float,
    duration_days: int,
    preferred_activities: List[str],
    preferred_season: str,
    travel_style: str,
    top_n: int = 5,
) -> List[Dict]:
    """Score all destinations and return top N sorted by score."""
    if not destinations:
        destinations = SAMPLE_DESTINATIONS

    budget_per_day = budget / max(duration_days, 1)
    scored = [
        score_destination(d, budget_per_day, duration_days,
                          preferred_activities, preferred_season, travel_style)
        for d in destinations
    ]
    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:top_n]


def get_sample_destinations() -> List[Dict]:
    return SAMPLE_DESTINATIONS

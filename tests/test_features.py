import pytest
from services.llm_service import _generate_fallback_itinerary, generate_itinerary
from recommendation.engine import score_destination
from unittest.mock import patch, MagicMock

def test_gemini_fallback():
    """Test the static fallback itinerary generation."""
    result = _generate_fallback_itinerary("Goa", 3, "Relaxed")
    assert result["status"] == "success"
    assert result["source"] == "fallback"
    assert len(result["itinerary"]) == 3
    assert result["itinerary"][0]["day"] == "Day 1"

@patch('services.llm_service._init_gemini_model')
def test_generate_itinerary_fallback_when_fails(mock_init):
    """Test that it falls back to static when Gemini fails."""
    mock_model = MagicMock()
    mock_model.generate_content.side_effect = Exception("API Error")
    mock_init.return_value = mock_model
    result = generate_itinerary("Goa", 2, "Relaxed", 2, 40000, ["Beach"])
    assert result["source"] == "fallback"
    assert len(result["itinerary"]) == 2

def test_personalization_boost():
    """Test that a destination gets a boost if it matches user history."""
    dest = {"name": "Goa", "category": "Beach", "average_daily_cost": 3000, "rating": 4.5, "popularity_score": 9.0}
    
    user_history = [{"destination_name": "Bali"}] # Bali is Beach category
    
    scored_without = score_destination(dest, 3000, 3, ["Beach & Water Sports"], "Any season", "Budget")
    scored_with = score_destination(dest, 3000, 3, ["Beach & Water Sports"], "Any season", "Budget", user_history)
    
    assert scored_with["score"] > scored_without["score"]
    assert any("Personalised" in reason for reason in scored_with["reasons"])

def test_budget_scoring():
    """Test that budget scores appropriately."""
    dest = {"name": "Paris", "category": "City", "average_daily_cost": 12000, "rating": 4.8, "popularity_score": 9.5}
    
    # Excellent budget fit
    score_good = score_destination(dest, 15000, 3, [], "Any season", "Mid-range")
    
    # Poor budget fit
    score_bad = score_destination(dest, 3000, 3, [], "Any season", "Mid-range")
    
    assert score_good["budget_score"] > score_bad["budget_score"]
    assert any("budget" in r.lower() for r in score_good["reasons"])


def test_weather_service_static_fallback():
    """Test that weather service returns valid data for known destinations."""
    from services.weather_service import get_weather
    data = get_weather("Goa")
    assert isinstance(data, dict)
    assert "temp" in data
    assert "humidity" in data
    assert "condition" in data
    assert data["source"] in ["sample", "live"]


def test_weather_service_unknown_city():
    """Test that weather service gracefully handles unknown cities."""
    from services.weather_service import get_weather
    data = get_weather("AtlantisNonExistentCityXYZ")
    assert isinstance(data, dict)
    assert "temp" in data
    assert "condition" in data


def test_format_currency():
    """Test currency formatting utility."""
    from utils.helpers import format_currency
    assert format_currency(500) == "₹500"
    assert format_currency(5000) == "₹5.0K"
    assert format_currency(150000) == "₹1.5L"


def test_password_hash_and_verify():
    """Test bcrypt password hashing and verification in auth."""
    from auth.auth import hash_password, verify_password
    plain = "SecureTripPassword123!"
    hashed = hash_password(plain)
    assert verify_password(plain, hashed) is True
    assert verify_password("WrongPassword!", hashed) is False

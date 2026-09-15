import pytest
from services.llm_service import _generate_fallback_itinerary, generate_itinerary
from recommendation.engine import score_destination
from unittest.mock import patch

def test_gemini_fallback():
    """Test the static fallback itinerary generation."""
    result = _generate_fallback_itinerary("Goa", 3, "Relaxed")
    assert result["status"] == "success"
    assert result["source"] == "fallback"
    assert len(result["itinerary"]) == 3
    assert result["itinerary"][0]["day"] == "Day 1"

@patch('services.llm_service.model')
def test_generate_itinerary_fallback_when_fails(mock_model):
    """Test that it falls back to static when Gemini fails."""
    mock_model.generate_content.side_effect = Exception("API Error")
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

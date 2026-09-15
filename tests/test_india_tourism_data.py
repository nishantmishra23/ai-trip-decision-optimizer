"""
Tests for India Tourism Dataset and All 28 States Expansion.
Verifies complete 28-state coverage, destination counts, data integrity,
and filtering operations.
"""
import pytest
from data.india_tourism_data import (
    get_all_state_names,
    get_state_data,
    get_destinations_by_state,
    get_destination_data,
    filter_hotels,
    filter_restaurants,
    filter_activities,
    get_stats,
    STATES_DATA
)

EXPECTED_28_STATES = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand",
    "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur",
    "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

def test_all_28_states_present():
    """Verify that all 28 official Indian states exist in the dataset."""
    state_names = get_all_state_names()
    assert len(state_names) == 28, f"Expected 28 states, got {len(state_names)}"
    for expected in EXPECTED_28_STATES:
        assert expected in state_names, f"State '{expected}' missing from dataset"

def test_each_state_has_4_to_8_destinations():
    """Verify that each state has at least 4 authentic destinations."""
    for state_name in EXPECTED_28_STATES:
        dests = get_destinations_by_state(state_name)
        assert len(dests) >= 4, f"{state_name} has only {len(dests)} destinations, expected >= 4"
        assert len(dests) <= 8, f"{state_name} has {len(dests)} destinations, expected <= 8"

def test_destination_structure_integrity():
    """Verify that every destination contains complete places, activities, stays, and dining."""
    for state_name, state_data in STATES_DATA.items():
        assert "capital" in state_data
        assert "tagline" in state_data
        assert "region" in state_data
        
        for dest in state_data["destinations"]:
            assert "name" in dest
            assert "tagline" in dest
            assert "overview" in dest
            assert "places_to_visit" in dest and len(dest["places_to_visit"]) >= 2
            assert "things_to_do" in dest and len(dest["things_to_do"]) >= 2
            assert "hotels" in dest and len(dest["hotels"]) >= 2
            assert "restaurants" in dest and len(dest["restaurants"]) >= 2
            
            # Verify Google Maps URLs
            for h in dest["hotels"]:
                assert "gmaps_url" in h
                assert "google.com/maps" in h["gmaps_url"]
                assert "price_per_night" in h
                assert "rating" in h
                
            for r in dest["restaurants"]:
                assert "gmaps_url" in r
                assert "google.com/maps" in r["gmaps_url"]
                assert "average_cost_for_two" in r
                assert "rating" in r

def test_filter_hotels_functionality():
    """Test hotel filtering by price, category, rating, and suitability."""
    dest = get_destination_data("Maharashtra", "Mumbai")
    assert dest is not None
    
    # Filter by budget
    budget_hotels = filter_hotels(dest, max_price=3000)
    assert len(budget_hotels) > 0
    assert all(h["price_per_night"] <= 3000 for h in budget_hotels)
    
    # Filter by category
    luxury_hotels = filter_hotels(dest, category="Luxury")
    assert len(luxury_hotels) > 0
    assert any("luxury" in h["category"].lower() for h in luxury_hotels)

def test_filter_restaurants_functionality():
    """Test restaurant filtering by veg-only, budget, and cuisine."""
    dest = get_destination_data("Goa", "North Goa (Calangute & Baga)")
    assert dest is not None
    
    # Filter veg-only
    veg_only = filter_restaurants(dest, is_veg_only=True)
    assert len(veg_only) > 0
    assert all(r["is_veg"] is True for r in veg_only)
    
    # Filter max cost
    budget_dining = filter_restaurants(dest, max_cost=1000)
    assert len(budget_dining) > 0
    assert all(r["average_cost_for_two"] <= 1000 for r in budget_dining)

def test_get_stats():
    """Verify aggregated stats summary."""
    stats = get_stats()
    assert stats["states_count"] == 28
    assert stats["destinations_count"] >= 112
    assert stats["hotels_count"] >= 300
    assert stats["restaurants_count"] >= 300
    assert stats["activities_count"] >= 300

"""
Central India Tourism Data Hub.
Aggregates all 28 states from regional modules (South, West, North, East, Central, Northeast)
providing clean query and filtering APIs for Stays, Dining, Activities, and State Discovery.
"""
import os
import sys

# Ensure root directory is in sys.path
_current_dir = os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()
_root_dir = os.path.dirname(_current_dir) if "data" in _current_dir else _current_dir
if _root_dir not in sys.path:
    sys.path.insert(0, _root_dir)

from data.regions.south import SOUTH_STATES
from data.regions.west import WEST_STATES
from data.regions.north import NORTH_STATES
from data.regions.east import EAST_STATES
from data.regions.central import CENTRAL_STATES
from data.regions.northeast import NORTHEAST_STATES
from data.regions.common import gmaps_url

# Aggregate all 28 states into a unified master dictionary
STATES_DATA = {}
STATES_DATA.update(SOUTH_STATES)
STATES_DATA.update(WEST_STATES)
STATES_DATA.update(NORTH_STATES)
STATES_DATA.update(EAST_STATES)
STATES_DATA.update(CENTRAL_STATES)
STATES_DATA.update(NORTHEAST_STATES)

# Canonical list of all 28 Indian states
ALL_28_STATES = sorted(list(STATES_DATA.keys()))

def get_all_state_names():
    """Return an alphabetically sorted list of all 28 states in India."""
    return ALL_28_STATES

def get_state_data(state_name: str):
    """Get full state object including capital, tagline, region, and destinations."""
    return STATES_DATA.get(state_name, None)

def get_destinations_by_state(state_name: str):
    """Get the list of destination dictionaries for a given state."""
    state = STATES_DATA.get(state_name)
    if not state:
        return []
    return state.get("destinations", [])

def get_destination_names(state_name: str):
    """Get the list of destination names for a given state."""
    dests = get_destinations_by_state(state_name)
    return [d["name"] for d in dests]

def get_destination_data(state_name: str, destination_name: str):
    """Retrieve full data object for a specific destination within a state."""
    dests = get_destinations_by_state(state_name)
    for d in dests:
        if d["name"] == destination_name:
            return d
    return dests[0] if dests else None

def filter_hotels(
    destination_data: dict,
    max_price: int = None,
    category: str = None,
    min_rating: float = None,
    suitability: str = None,
    amenity: str = None
):
    """Filter hotel listings of a destination based on criteria."""
    if not destination_data or "hotels" not in destination_data:
        return []
    
    results = destination_data["hotels"]
    if max_price is not None:
        results = [h for h in results if h.get("price_per_night", 0) <= max_price]
    if category and category != "All Categories":
        results = [h for h in results if category.lower() in h.get("category", "").lower()]
    if min_rating is not None:
        results = [h for h in results if h.get("rating", 0.0) >= min_rating]
    if suitability and suitability != "All":
        results = [h for h in results if suitability in h.get("suitability", [])]
    if amenity and amenity != "All Amenities":
        results = [h for h in results if any(amenity.lower() in a.lower() for a in h.get("amenities", []))]
    return results

def filter_restaurants(
    destination_data: dict,
    max_cost: int = None,
    cuisine: str = None,
    is_veg_only: bool = False,
    min_rating: float = None
):
    """Filter restaurant listings of a destination based on criteria."""
    if not destination_data or "restaurants" not in destination_data:
        return []
    
    results = destination_data["restaurants"]
    if max_cost is not None:
        results = [r for r in results if r.get("average_cost_for_two", 0) <= max_cost]
    if cuisine and cuisine != "All Cuisines":
        results = [r for r in results if cuisine.lower() in r.get("cuisine", "").lower()]
    if is_veg_only:
        results = [r for r in results if r.get("is_veg", False) is True]
    if min_rating is not None:
        results = [r for r in results if r.get("rating", 0.0) >= min_rating]
    return results

def filter_activities(
    destination_data: dict,
    max_cost: int = None,
    category: str = None
):
    """Filter activities of a destination."""
    if not destination_data or "things_to_do" not in destination_data:
        return []
    
    results = destination_data["things_to_do"]
    if max_cost is not None:
        results = [a for a in results if a.get("cost", 0) <= max_cost]
    if category and category != "All Categories":
        results = [a for a in results if category.lower() in a.get("category", "").lower()]
    return results

def filter_places(destination_data: dict, category: str = None):
    """Filter places to visit in a destination."""
    if not destination_data or "places_to_visit" not in destination_data:
        return []
    
    results = destination_data["places_to_visit"]
    if category and category != "All Categories":
        results = [p for p in results if category.lower() in p.get("category", "").lower()]
    return results

def get_stats():
    """Return high-level statistics across all 28 states."""
    total_states = len(STATES_DATA)
    total_destinations = sum(len(s.get("destinations", [])) for s in STATES_DATA.values())
    total_hotels = sum(
        sum(len(d.get("hotels", [])) for d in s.get("destinations", []))
        for s in STATES_DATA.values()
    )
    total_restaurants = sum(
        sum(len(d.get("restaurants", [])) for d in s.get("destinations", []))
        for s in STATES_DATA.values()
    )
    total_activities = sum(
        sum(len(d.get("things_to_do", [])) for d in s.get("destinations", []))
        for s in STATES_DATA.values()
    )
    return {
        "states_count": total_states,
        "destinations_count": total_destinations,
        "hotels_count": total_hotels,
        "restaurants_count": total_restaurants,
        "activities_count": total_activities
    }

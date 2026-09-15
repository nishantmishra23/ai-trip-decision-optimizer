import sys
import os
sys.path.insert(0, os.getcwd())

from data.india_tourism_data import STATES_DATA

print("=== Checking Destination Counts (Must be >= 4) ===")
for state, sdata in STATES_DATA.items():
    dests = sdata.get('destinations', [])
    if len(dests) < 4:
        print(f"FAILED: {state} has {len(dests)} destinations")

print("\n=== Checking Elements (Places, Activities, Hotels, Restaurants >= 2) ===")
for state, sdata in STATES_DATA.items():
    dests = sdata.get('destinations', [])
    for d in dests:
        p = len(d.get('places_to_visit', []))
        a = len(d.get('things_to_do', []))
        h = len(d.get('hotels', []))
        r = len(d.get('restaurants', []))
        if p < 2 or a < 2 or h < 2 or r < 2:
            print(f"FAILED: {state} -> {d['name']}: places={p}, activities={a}, hotels={h}, restaurants={r}")

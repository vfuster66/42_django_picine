#!/usr/bin/python3

import sys

def get_capital_city(state_name, states, capital_cities):
    """Get capital city for a given state."""
    state_name = state_name.strip()
    for state, code in states.items():
        if state.lower() == state_name.lower():
            return capital_cities.get(code)
    return None

def get_state(capital_name, states, capital_cities):
    """Get state for a given capital city."""
    capital_name = capital_name.strip()
    for code, capital in capital_cities.items():
        if capital.lower() == capital_name.lower():
            for state, state_code in states.items():
                if state_code == code:
                    return state
    return None

def check_entry(entry, states, capital_cities):
    """Check if entry is a state or capital and return appropriate message."""
    entry = entry.strip()
    if not entry:  # Skip empty entries
        return None
    
    # Try to find it as a state first
    capital = get_capital_city(entry, states, capital_cities)
    if capital:
        return f"{capital} is the capital of {entry}"
    
    # Try to find it as a capital
    state = get_state(entry, states, capital_cities)
    if state:
        return f"{entry} is the capital of {state}"
    
    return f"{entry} is neither a capital city nor a state"

def all_in():
    """Main function to process states and capitals."""
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if len(sys.argv) != 2:
        return

    entries = sys.argv[1].split(',')
    
    # Check for consecutive commas
    if any(not entry.strip() for entry in entries):
        return
        
    results = []
    for entry in entries:
        result = check_entry(entry, states, capital_cities)
        if result:
            results.append(result)
    
    print('\n'.join(results))

if __name__ == '__main__':
    all_in()
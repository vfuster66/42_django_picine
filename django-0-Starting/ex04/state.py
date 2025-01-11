import sys

def get_state(capital):
    # Dictionnaires fournis
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    # Inverser le dictionnaire capital_cities pour trouver l'état
    inverted_capitals = {v: k for k, v in capital_cities.items()}

    # Vérifier si la capitale est dans le dictionnaire inversé
    state_code = inverted_capitals.get(capital)
    if state_code:
        # Trouver l'état correspondant au code
        for state, code in states.items():
            if code == state_code:
                return state
    return "Unknown capital city"

if __name__ == "__main__":
    # Vérifier les arguments
    if len(sys.argv) != 2:
        sys.exit()

    capital = sys.argv[1]
    state = get_state(capital)
    print(state)

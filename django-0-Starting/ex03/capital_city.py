import sys


def get_capital_city(state):
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

    # Vérifier si l'état est dans le dictionnaire
    state_code = states.get(state)
    if state_code:
        return capital_cities.get(state_code, "Unknown state")
    return "Unknown state"


if __name__ == "__main__":
    # Vérifier les arguments
    if len(sys.argv) != 2:
        sys.exit()

    state = sys.argv[1]
    capital = get_capital_city(state)
    print(capital)

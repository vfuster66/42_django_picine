def create_structure():
    # Dictionnaires fournis
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    # Création de la liste de tuples
    structure = []
    for state, abbr in states.items():
        capital = cities.get(abbr, "Unknown")
        structure.append((state, abbr, capital))

    return states, cities, structure

if __name__ == "__main__":
    states, cities, structure = create_structure()

    # Afficher la structure
    print("States:", states)
    print("Cities:", cities)
    print("Structure:")
    for item in structure:
        print(item)

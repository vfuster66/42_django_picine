from my_struct import create_structure

def test_my_struct():
    # Résultats attendus
    expected_states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }

    expected_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    expected_structure = [
        ("Oregon", "OR", "Salem"),
        ("Alabama", "AL", "Montgomery"),
        ("New Jersey", "NJ", "Trenton"),
        ("Colorado", "CO", "Denver")
    ]

    # Appeler la fonction
    states, cities, structure = create_structure()

    # Vérifications avec détails et couleurs
    def print_colored(message, color):
        colors = {
            "green": "\033[92m",
            "red": "\033[91m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "reset": "\033[0m"
        }
        print(f"{colors[color]}{message}{colors['reset']}")

    print("\n--- Testing States ---")
    print_colored("Expected States:", "blue")
    print(expected_states)
    print_colored("Got States:", "blue")
    print(states)
    if states == expected_states:
        print_colored("[PASSED] States test passed.", "green")
    else:
        print_colored("[FAILED] States test failed.", "red")

    print("\n--- Testing Cities ---")
    print_colored("Expected Cities:", "blue")
    print(expected_cities)
    print_colored("Got Cities:", "blue")
    print(cities)
    if cities == expected_cities:
        print_colored("[PASSED] Cities test passed.", "green")
    else:
        print_colored("[FAILED] Cities test failed.", "red")

    print("\n--- Testing Structure ---")
    print_colored("Expected Structure:", "blue")
    for item in expected_structure:
        print(item)
    print_colored("Got Structure:", "blue")
    for item in structure:
        print(item)
    if structure == expected_structure:
        print_colored("[PASSED] Structure test passed.", "green")
    else:
        print_colored("[FAILED] Structure test failed.", "red")

    # Assertions finales
    assert states == expected_states, "States do not match expected values."
    assert cities == expected_cities, "Cities do not match expected values."
    assert structure == expected_structure, "Structure does not match expected values."

    print_colored("\nAll tests passed.", "green")

if __name__ == "__main__":
    test_my_struct()

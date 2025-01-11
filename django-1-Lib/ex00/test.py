import subprocess

def test_geohashing():
    # Définir les cas de test
    test_cases = [
        ("37.421542", "-122.085589", "2005-05-26-10458.68"),
        ("40.748817", "-73.985428", "2015-07-23-12345.67"),
    ]

    for latitude, longitude, date_hash in test_cases:
        print(f"\nTesting with latitude={latitude}, longitude={longitude}, date_hash={date_hash}")
        try:
            result = subprocess.run(
                ["python3", "geohashing.py", latitude, longitude, date_hash],
                capture_output=True,
                text=True
            )

            # Vérification du retour standard
            print("Standard Output:")
            print(result.stdout)

            # Vérification des erreurs (si présentes)
            if result.stderr:
                print("Standard Error:")
                print(result.stderr)

            # Afficher les résultats attendus et obtenus
            print("\nExpected Result: See browser geohash coordinates.")
            print("Actual Result:")
            print(result.stdout.strip())

            # Tester si le script retourne une erreur
            assert result.returncode == 0, f"Le script a échoué avec le code {result.returncode}"
            print("[PASSED] Test passed.")

        except Exception as e:
            print(f"[FAILED] Une exception s'est produite : {e}")

if __name__ == "__main__":
    test_geohashing()

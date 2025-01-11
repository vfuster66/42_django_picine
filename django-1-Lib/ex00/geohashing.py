import sys
import antigravity

def main():
    try:
        # Vérifier que 3 arguments sont fournis (latitude, longitude, et date hashée)
        if len(sys.argv) != 4:
            print("Usage: python3 geohashing.py <latitude> <longitude> <date_hash>")
            sys.exit(1)

        # Récupérer les arguments
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        date_hash = sys.argv[3].encode('utf-8')

        # Appeler la fonction geohash
        antigravity.geohash(latitude, longitude, date_hash)

    except ValueError:
        print("Erreur : Veuillez fournir des coordonnées valides (latitude et longitude numériques).")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

if __name__ == "__main__":
    main()

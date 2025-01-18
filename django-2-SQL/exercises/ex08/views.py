from django.http import HttpResponse
from django.db import connection
import os
from django.conf import settings


def init(request):
    try:
        with connection.cursor() as cursor:
            # Création de la table planets
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex08_planets (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                climate VARCHAR(128),
                diameter INTEGER,
                orbital_period INTEGER,
                population BIGINT,
                rotation_period INTEGER,
                surface_water REAL,
                terrain VARCHAR(128)
            );
            """)

            # Création de la table people avec la clé étrangère
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex08_people (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INTEGER,
                mass REAL,
                homeworld VARCHAR(64) REFERENCES ex08_planets(name)
            );
            """)
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")


def parse_csv_ameliore(file_path, expected_columns):
    """
    Parse un fichier CSV en gérant les délimiteurs et les valeurs NULL.
    """
    rows = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            # Séparation par tabulations
            fields = line.strip().split('\t')

            # Traitement de chaque champ
            processed_row = []
            for field in fields[:expected_columns]:
                field = field.strip()
                if field in ('NULL', 'null', '', 'None'):
                    processed_row.append(None)
                else:
                    # Conversion des valeurs numériques
                    try:
                        if '.' in field:
                            processed_row.append(float(field))
                        elif field.isdigit() or (
                                field[0] == '-' and field[1:].isdigit()):
                            processed_row.append(int(field))
                        else:
                            processed_row.append(field)
                    except ValueError:
                        processed_row.append(field)

            # Ajout de None pour les colonnes manquantes
            while len(processed_row) < expected_columns:
                processed_row.append(None)

            rows.append(processed_row)
    return rows


def populate(request):
    try:
        # Chemins des fichiers CSV
        planets_path = os.path.join(
            settings.BASE_DIR, "ex08", "data", "planets.csv"
        )
        people_path = os.path.join(
            settings.BASE_DIR, "ex08", "data", "people.csv"
        )

        inserted_planets = 0
        inserted_people = 0

        with connection.cursor() as cursor:
            # Insertion des planètes
            planets_data = parse_csv_ameliore(planets_path, 8)
            for row in planets_data:
                try:
                    cursor.execute("""
                        INSERT INTO ex08_planets (
                            name, climate, diameter, orbital_period,
                            population, rotation_period, surface_water, terrain
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (name) DO UPDATE SET
                            climate = EXCLUDED.climate,
                            diameter = EXCLUDED.diameter,
                            orbital_period = EXCLUDED.orbital_period,
                            population = EXCLUDED.population,
                            rotation_period = EXCLUDED.rotation_period,
                            surface_water = EXCLUDED.surface_water,
                            terrain = EXCLUDED.terrain;
                    """, row)
                    inserted_planets += 1
                except Exception as e:
                    print(
                        f"Erreur lors de l'insertion de la planète "
                        f"{row[0] if row else 'inconnue'}: {str(e)}"
                    )

            # Insertion des personnages
            people_data = parse_csv_ameliore(people_path, 8)
            for row in people_data:
                try:
                    cursor.execute("""
                        INSERT INTO ex08_people (
                            name, birth_year, gender, eye_color,
                            hair_color, height, mass, homeworld
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (name) DO UPDATE SET
                            birth_year = EXCLUDED.birth_year,
                            gender = EXCLUDED.gender,
                            eye_color = EXCLUDED.eye_color,
                            hair_color = EXCLUDED.hair_color,
                            height = EXCLUDED.height,
                            mass = EXCLUDED.mass,
                            homeworld = EXCLUDED.homeworld;
                    """, row)
                    inserted_people += 1
                except Exception as e:
                    print(
                        f"Erreur lors de l'insertion du personnage "
                        f"{row[0] if row else 'inconnu'}: {str(e)}"
                    )

        return HttpResponse(
            f"Insertion réussie de {inserted_planets} planètes et "
            f"{inserted_people} personnages."
        )
    except Exception as e:
        return HttpResponse(f"Erreur: {str(e)}")


def display(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT p.name, p.homeworld, pl.climate
            FROM ex08_people p
            INNER JOIN ex08_planets pl ON p.homeworld = pl.name
            WHERE pl.climate LIKE '%windy%'
            ORDER BY p.name;
            """)
            rows = cursor.fetchall()

        if not rows:
            return HttpResponse("No data available")

        result = "<table border='1'>"
        result += "<tr><th>Name</th><th>Homeworld</th><th>Climate</th></tr>"
        for row in rows:
            result += (
                f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"
            )
        result += "</table>"
        return HttpResponse(result)

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

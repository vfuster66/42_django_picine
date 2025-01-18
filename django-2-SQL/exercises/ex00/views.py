import psycopg2
from django.http import HttpResponse
from decouple import config


def init(request):
    try:
        # Connexion à la base de données PostgreSQL
        conn = psycopg2.connect(
            dbname=config('DB_NAME'),
            user=config('DB_USER'),
            password=config('DB_PASSWORD'),
            host=config('DB_HOST'),
            port=config('DB_PORT'),
        )
        cursor = conn.cursor()

        # Requête SQL pour créer la table si elle n'existe pas
        create_table_query = """
        CREATE TABLE IF NOT EXISTS ex00_movies (
            title VARCHAR(64) UNIQUE NOT NULL,
            episode_nb SERIAL PRIMARY KEY,
            opening_crawl TEXT,
            director VARCHAR(32) NOT NULL,
            producer VARCHAR(128) NOT NULL,
            release_date DATE NOT NULL
        );
        """
        cursor.execute(create_table_query)
        conn.commit()  # Appliquer les modifications

        # Fermeture de la connexion
        cursor.close()
        conn.close()

        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

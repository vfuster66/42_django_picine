import psycopg2
from django.http import HttpResponse
from decouple import config


def get_connection():
    return psycopg2.connect(
        dbname=config('DB_NAME'),
        user=config('DB_USER'),
        password=config('DB_PASSWORD'),
        host=config('DB_HOST'),
        port=config('DB_PORT'),
    )


def init(request):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS ex02_movies (
        episode_nb SERIAL PRIMARY KEY,
        title VARCHAR(64) UNIQUE NOT NULL,
        opening_crawl TEXT,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR(128) NOT NULL,
        release_date DATE NOT NULL
    );
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()
        cursor.close()
        conn.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error creating table: {str(e)}")


def populate(request):
    data = [
        (1, "The Phantom Menace", "George Lucas", "Rick McCallum",
         "1999-05-19"),
        (2, "Attack of the Clones", "George Lucas", "Rick McCallum",
         "2002-05-16"),
        (3, "Revenge of the Sith", "George Lucas", "Rick McCallum",
         "2005-05-19"),
        (4, "A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum",
         "1977-05-25"),
        (5, "The Empire Strikes Back", "Irvin Kershner",
         "Gary Kurtz, Rick McCallum", "1980-05-17"),
        (6, "Return of the Jedi", "Richard Marquand",
         "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
        (7, "The Force Awakens", "J. J. Abrams",
         "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
    ]

    try:
        conn = get_connection()
        cursor = conn.cursor()

        results = []
        for entry in data:
            try:
                cursor.execute(
                    """
                    INSERT INTO ex02_movies (
                        episode_nb, title, director, producer, release_date
                    )
                    VALUES (%s, %s, %s, %s, %s);
                    """, entry)
                results.append(f"{entry[1]}: OK")
            except Exception as e:
                results.append(f"{entry[1]}: {str(e)}")

        conn.commit()
        cursor.close()
        conn.close()

        return HttpResponse("<br>".join(results))
    except Exception as e:
        return HttpResponse(f"Error populating data: {str(e)}")


def display(request):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ex02_movies;")
        rows = cursor.fetchall()

        if not rows:
            return HttpResponse("No data available")

        # Construction du tableau HTML
        result = "<table border='1'>"
        result += (
            "<tr><th>Episode</th><th>Title</th><th>Opening Crawl</th>"
            "<th>Director</th><th>Producer</th><th>Release Date</th></tr>"
        )
        for row in rows:
            result += (
                f"<tr><td>{row[0]}</td><td>{row[1]}</td>"
                f"<td>{row[2] or 'N/A'}</td><td>{row[3]}</td>"
                f"<td>{row[4]}</td><td>{row[5]}</td></tr>"
            )
        result += "</table>"

        cursor.close()
        conn.close()

        return HttpResponse(result)
    except Exception as e:
        return HttpResponse(f"Error displaying data: {str(e)}")

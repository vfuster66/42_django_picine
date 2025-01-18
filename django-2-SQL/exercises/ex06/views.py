from django.http import HttpResponse
from django.db import connection
from .models import Ex06Movies
from django.shortcuts import render
from django.http import HttpResponseRedirect


def init(request):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS ex06_movies (
        episode_nb SERIAL PRIMARY KEY,
        title VARCHAR(64) UNIQUE NOT NULL,
        opening_crawl TEXT,
        director VARCHAR(32) NOT NULL,
        producer VARCHAR(128) NOT NULL,
        release_date DATE NOT NULL,
        created TIMESTAMP DEFAULT now() NOT NULL,
        updated TIMESTAMP DEFAULT now() NOT NULL
    );
    """

    create_function_query = """
    CREATE OR REPLACE FUNCTION update_changetimestamp_column()
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.updated = now();
        NEW.created = OLD.created;
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    """

    create_trigger_query = """
    CREATE TRIGGER update_films_changetimestamp
    BEFORE UPDATE ON ex06_movies
    FOR EACH ROW EXECUTE FUNCTION update_changetimestamp_column();
    """

    try:
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
            cursor.execute(create_function_query)
            cursor.execute(create_trigger_query)
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")


def populate(request):
    data = [
        {
            "episode_nb": 1,
            "title": "The Phantom Menace",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "1999-05-19"
        },
        {
            "episode_nb": 2,
            "title": "Attack of the Clones",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2002-05-16"
        },
        {
            "episode_nb": 3,
            "title": "Revenge of the Sith",
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2005-05-19"
        },
        {
            "episode_nb": 4,
            "title": "A New Hope",
            "director": "George Lucas",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1977-05-25"
        },
        {
            "episode_nb": 5,
            "title": "The Empire Strikes Back",
            "director": "Irvin Kershner",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1980-05-17"
        },
        {
            "episode_nb": 6,
            "title": "Return of the Jedi",
            "director": "Richard Marquand",
            "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "release_date": "1983-05-25"
        },
        {
            "episode_nb": 7,
            "title": "The Force Awakens",
            "director": "J. J. Abrams",
            "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            "release_date": "2015-12-11"
        },
    ]

    results = []
    for movie_data in data:
        try:
            movie = Ex06Movies(**movie_data)
            movie.save()
            results.append(f"{movie.title}: OK")
        except Exception as e:
            results.append(f"{movie_data['title']}: {str(e)}")

    return HttpResponse("<br>".join(results))


def display(request):
    movies = Ex06Movies.objects.all()

    if not movies.exists():
        return HttpResponse("No data available")

    result = "<table border='1'>"
    result += (
        "<tr><th>Episode</th><th>Title</th><th>Opening Crawl</th>"
        "<th>Director</th><th>Producer</th><th>Release Date</th>"
        "<th>Created</th><th>Updated</th></tr>"
    )

    for movie in movies:
        result += (
            f"<tr><td>{movie.episode_nb}</td><td>{movie.title}</td>"
            f"<td>{movie.opening_crawl or 'N/A'}</td>"
            f"<td>{movie.director}</td><td>{movie.producer}</td>"
            f"<td>{movie.release_date}</td>"
            f"<td>{movie.created}</td>"
            f"<td>{movie.updated}</td></tr>"
        )

    result += "</table>"
    return HttpResponse(result)


def update(request):
    movies = Ex06Movies.objects.all()

    if not movies.exists():
        return HttpResponse("No data available")

    if request.method == "POST":
        title_to_update = request.POST.get("title")
        new_text = request.POST.get("opening_crawl")
        try:
            movie = Ex06Movies.objects.get(title=title_to_update)
            movie.opening_crawl = new_text
            movie.save()
            return HttpResponseRedirect(request.path)
        except Ex06Movies.DoesNotExist:
            return HttpResponse("Movie not found")

    return render(request, "ex06/update.html", {"movies": movies})

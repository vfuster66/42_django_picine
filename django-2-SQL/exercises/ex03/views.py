from django.http import HttpResponse
from .models import Ex03Movies


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
            movie = Ex03Movies(**movie_data)
            movie.save()
            results.append(f"{movie.title}: OK")
        except Exception as e:
            results.append(f"{movie_data['title']}: {str(e)}")

    return HttpResponse("<br>".join(results))


def display(request):
    movies = Ex03Movies.objects.all()

    if not movies.exists():
        return HttpResponse("No data available")

    result = "<table border='1'>"
    result += (
        "<tr><th>Episode</th><th>Title</th><th>Opening Crawl</th>"
        "<th>Director</th><th>Producer</th><th>Release Date</th></tr>"
    )

    for movie in movies:
        result += (
            f"<tr><td>{movie.episode_nb}</td><td>{movie.title}</td>"
            f"<td>{movie.opening_crawl or 'N/A'}</td>"
            f"<td>{movie.director}</td><td>{movie.producer}</td>"
            f"<td>{movie.release_date}</td></tr>"
        )

    result += "</table>"
    return HttpResponse(result)

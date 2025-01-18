from django.http import HttpResponse
from .models import Ex07Movies
from django.shortcuts import render
from django.http import HttpResponseRedirect


def populate(request):
    Ex07Movies.objects.all().delete()

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
        if Ex07Movies.objects.filter(
            episode_nb=movie_data["episode_nb"]
        ).exists():
            results.append(f"{movie_data['title']}: Already exists")
        else:
            try:
                movie = Ex07Movies(**movie_data)
                movie.save()
                results.append(f"{movie.title}: OK")
            except Exception as e:
                results.append(f"{movie_data['title']}: {str(e)}")

    return HttpResponse("<br>".join(results))


def display(request):
    movies = Ex07Movies.objects.all()

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
    movies = Ex07Movies.objects.all()

    if not movies.exists():
        return HttpResponse("No data available")

    if request.method == "POST":
        episode_nb = request.POST.get("movie_id")
        new_text = request.POST.get("new_text")
        try:
            movie = Ex07Movies.objects.get(episode_nb=episode_nb)
            movie.opening_crawl = new_text
            movie.save()
            return HttpResponseRedirect(request.path)
        except Ex07Movies.DoesNotExist:
            return HttpResponse("Movie not found")

    return render(request, "ex07/update.html", {"movies": movies})

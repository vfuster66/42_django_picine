from django.http import HttpResponse
from django.shortcuts import render
from .models import People


def index(request):
    if request.method == 'POST':
        min_date = request.POST.get('min_date')
        max_date = request.POST.get('max_date')
        min_diameter = request.POST.get('min_diameter')
        gender = request.POST.get('gender')

        # Vérification que tous les champs sont remplis
        if not all([min_date, max_date, min_diameter, gender]):
            return HttpResponse("All fields are required.")

        try:
            # Requête pour trouver les résultats correspondants
            results = (
                People.objects.filter(
                    gender=gender,
                    movies__release_date__range=[min_date, max_date],
                    homeworld__diameter__gte=int(min_diameter)
                )
                .select_related('homeworld')
                .prefetch_related('movies')
            )

            if not results.exists():
                return HttpResponse("Nothing corresponding to your research.")

            # Affichage des résultats
            return render(request, 'ex10/results.html', {'results': results})
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")

    # Récupérer les genres disponibles pour la liste déroulante
    genders = People.objects.values_list('gender', flat=True).distinct()
    return render(request, 'ex10/index.html', {'genders': genders})

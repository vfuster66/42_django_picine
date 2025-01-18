from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'title': 'Ex01 Index'})


def django_page(request):
    return render(
        request, 'django.html', {'title': 'Ex01: Django, framework web.'}
    )


def affichage(request):
    return render(
        request, 'affichage.html', {'title': 'Ex01: Processus d’affichage'}
    )


def templates(request):
    return render(
        request, 'templates.html', {'title': 'Ex01: Moteur de template'}
    )

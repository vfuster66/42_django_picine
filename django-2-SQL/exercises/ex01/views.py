from django.http import HttpResponse
from django.core.management import call_command


def init(request):
    try:
        # Appliquer les migrations pour créer la table
        call_command('migrate', 'ex01')
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

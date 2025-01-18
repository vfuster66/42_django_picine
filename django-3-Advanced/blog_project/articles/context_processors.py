from django.contrib.auth.forms import AuthenticationForm

def login_form(request):
    form = AuthenticationForm()
    form.request = request  # Ajouter la request au formulaire
    return {
        'login_form': form,
        'request': request  # Passer aussi la request au contexte
    }
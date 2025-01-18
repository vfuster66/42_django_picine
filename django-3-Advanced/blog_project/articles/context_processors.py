from django.contrib.auth.forms import AuthenticationForm


def login_form(request):
    form = AuthenticationForm()
    form.request = request
    return {
        'login_form': form,
        'request': request
    }

from django.shortcuts import render, redirect
from django.conf import settings
from datetime import datetime
from .forms import TextForm


def index(request):
    form = TextForm()
    history = []

    # Lire l'historique existant
    try:
        with open(settings.LOG_FILE, 'r') as f:
            history = f.readlines()
    except FileNotFoundError:
        pass

    # Traiter la soumission du formulaire
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_entry = f"{timestamp} {text}\n"
            
            # Écrire dans le fichier de logs
            with open(settings.LOG_FILE, 'a') as f:
                f.write(log_entry)
            
            # Rediriger vers GET pour éviter la resoumission du formulaire
            return redirect('index')
    
    return render(request, 'index.html', {
        'form': form,
        'history': history
    })
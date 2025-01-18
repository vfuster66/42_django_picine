from django.shortcuts import render


def generate_shades(base_color, steps):
    """
    Génère des nuances à partir d'une couleur de base très claire
    vers une couleur intense.
    """
    shades = []
    for i in range(steps):
        intensity = int((255 / (steps - 1)) * i)
        if base_color == 'red':
            shades.append(f'rgb(255, {255 - intensity}, {255 - intensity})')
        elif base_color == 'green':
            shades.append(f'rgb({255 - intensity}, 255, {255 - intensity})')
        elif base_color == 'blue':
            shades.append(f'rgb({255 - intensity}, {255 - intensity}, 255)')
        elif base_color == 'black':
            shades.append(
                f'rgb({255 - intensity}, {255 - intensity}, {255 - intensity})'
            )
    return shades


def index(request):
    # Préparation des données pour le tableau
    colors = list(zip(
        generate_shades('black', 50),
        generate_shades('red', 50),
        generate_shades('green', 50),
        generate_shades('blue', 50),
    ))

    return render(request, 'ex03/index.html', {'colors': colors})

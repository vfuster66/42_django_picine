import sys
import os
import re
import settings


def render_template(template_file):
    # Vérifier l'extension du fichier
    if not template_file.endswith(".template"):
        print("Erreur : le fichier doit avoir l'extension .template.")
        sys.exit(1)

    # Vérifier si le fichier existe
    if not os.path.exists(template_file):
        print(f"Erreur : le fichier {template_file} est introuvable.")
        sys.exit(1)

    # Lire le contenu du fichier template
    try:
        with open(template_file, "r") as file:
            content = file.read()
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        sys.exit(1)

    # Remplacer les placeholders par les valeurs définies dans settings
    try:
        content = re.sub(
            r"\{(\w+)\}",
            lambda match: str(
                getattr(settings, match.group(1), match.group(0))
            ),
            content
        )
    except Exception as e:
        print(f"Erreur lors du rendu du template : {e}")
        sys.exit(1)

    # Générer le nom du fichier de sortie
    output_file = template_file.replace(".template", ".html")

    # Écrire le contenu dans le fichier HTML
    try:
        with open(output_file, "w") as file:
            file.write(content)
        print(f"Fichier généré : {output_file}")
    except Exception as e:
        print(f"Erreur lors de l'écriture du fichier HTML : {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Vérifier le nombre d'arguments
    if len(sys.argv) != 2:
        print("Usage : python3 render.py <fichier.template>")
        sys.exit(1)

    # Lancer le rendu
    render_template(sys.argv[1])

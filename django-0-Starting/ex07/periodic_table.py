import sys

def read_periodic_table(file_path):
    """Lit le fichier et retourne une liste de dictionnaires représentant les éléments."""
    elements = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Séparer le nom de l'élément et ses attributs
                name, attributes = line.split('=', 1)
                name = name.strip()
                attributes = attributes.strip()

                # Créer un dictionnaire pour les attributs
                attr_dict = {'name': name}
                for attr in attributes.split(','):
                    key, value = attr.split(':', 1)
                    attr_dict[key.strip()] = value.strip()

                # Convertir les types pour certaines clés spécifiques
                attr_dict['position'] = int(attr_dict['position'])
                attr_dict['number'] = int(attr_dict['number'])
                attr_dict['molar'] = float(attr_dict['molar'])
                elements.append(attr_dict)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}", file=sys.stderr)
        sys.exit(1)
    return elements

def generate_css():
    """Crée un fichier periodic_table.css avec des styles améliorés et responsifs."""
    css_content = """
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f9;
        color: #333;
        margin: 20px;
        padding: 0;
    }
    table {
        border-collapse: collapse;
        margin: 0 auto;
        width: 100%;
        max-width: 1000px;
    }
    td {
        border: 1px solid #ccc;
        padding: 10px;
        text-align: center;
        vertical-align: top;
        width: calc(100% / 18); /* Équilibrer les colonnes */
        height: auto;
        background-color: #f9f9f9;
    }
    td.empty {
        background-color: #e0e0e0;
    }
    h4 {
        margin: 0;
        font-size: 1em;
    }
    ul {
        list-style: none;
        padding: 0;
        margin: 5px 0 0;
        font-size: 0.8em;
    }
    ul li {
        margin: 3px 0;
    }
    /* Responsivité */
    @media (max-width: 768px) {
        td {
            padding: 5px;
            font-size: 0.7em;
        }
        h4 {
            font-size: 0.9em;
        }
        ul {
            font-size: 0.7em;
        }
    }
    @media (max-width: 480px) {
        td {
            padding: 3px;
            font-size: 0.6em;
        }
        ul li {
            margin: 2px 0;
        }
    }
    """
    with open("periodic_table.css", "w") as css_file:
        css_file.write(css_content)
    print("CSS file generated: periodic_table.css")

def generate_html(elements, output_file):
    """Génère un tableau périodique HTML."""
    try:
        with open(output_file, 'w') as file:
            file.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<title>Periodic Table</title>\n')
            file.write('<link rel="stylesheet" href="periodic_table.css">\n')
            file.write('</head>\n<body>\n<h1>Periodic Table of Elements</h1>\n<table>\n')

            for period in range(1, 8):  # 7 périodes pour le tableau périodique
                file.write('<tr>\n')
                for position in range(18):  # 18 groupes dans le tableau
                    element = next((e for e in elements if e['position'] == position and e['number'] // 10 == period - 1), None)
                    if element:
                        file.write('<td>\n')
                        file.write(f"<h4>{element['name']}</h4>\n")
                        file.write('<ul>\n')
                        file.write(f"<li>Atomic Number: {element['number']}</li>\n")
                        file.write(f"<li>Symbol: {element['small']}</li>\n")
                        file.write(f"<li>Atomic Mass: {element['molar']}</li>\n")
                        file.write(f"<li>Electrons: {element['electron']}</li>\n")
                        file.write('</ul>\n')
                        file.write('</td>\n')
                    else:
                        file.write('<td class="empty"></td>\n')
                file.write('</tr>\n')

            file.write('</table>\n</body>\n</html>\n')
        print(f"HTML file generated: {output_file}")
    except Exception as e:
        print(f"Erreur lors de la génération du fichier HTML : {e}", file=sys.stderr)
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 periodic_table.py <input_file>", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = 'periodic_table.html'

    elements = read_periodic_table(input_file)
    generate_css()
    generate_html(elements, output_file)

if __name__ == '__main__':
    main()

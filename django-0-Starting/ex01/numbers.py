def read_and_print_numbers(file_path):
    try:
        with open(file_path, 'r') as file:
            # Lire le contenu du fichier
            content = file.read()
            # Séparer les nombres par les virgules
            numbers = content.split(',')
            # Afficher chaque nombre sur une nouvelle ligne
            for number in numbers:
                print(number.strip())
    except FileNotFoundError:
        print(f"Erreur : le fichier {file_path} est introuvable.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")


if __name__ == "__main__":
    # Chemin du fichier à lire
    file_path = "numbers.txt"
    read_and_print_numbers(file_path)

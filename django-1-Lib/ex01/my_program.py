import sys
sys.path.append('local_lib')

from path import Path

def main():
    # Créer un dossier
    folder = Path("test_folder")
    folder.mkdir_p()  # Crée le dossier et ses parents si nécessaire

    # Créer un fichier dans ce dossier
    file = folder / "test_file.txt"
    file.write_text("Hello, this is a test file!")  # Écrire du texte dans le fichier

    # Lire et afficher le contenu du fichier
    content = file.read_text()  # Lire le contenu du fichier
    print(content)

if __name__ == "__main__":
    main()

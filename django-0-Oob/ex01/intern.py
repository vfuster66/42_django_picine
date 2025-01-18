class Intern:
    """Classe représentant un stagiaire."""

    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        """Constructeur prenant un nom en paramètre ou assignant un nom par
        défaut."""
        self.name = name

    def __str__(self):
        """Retourne le nom du stagiaire."""
        return self.name

    class Coffee:
        """Classe représentant un café préparé par un stagiaire."""

        def __str__(self):
            """Retourne une description du café."""
            return "This is the worst coffee you ever tasted."

    def work(self):
        """Tente de faire travailler le stagiaire,
        mais déclenche une exception."""
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        """Prépare un café."""
        return self.Coffee()


# Tests
if __name__ == "__main__":
    # Instanciation des stagiaires
    intern1 = Intern()  # Sans nom
    intern2 = Intern("Mark")  # Avec nom

    # Affichage des noms
    print(intern1)  # Affiche : My name? I’m nobody, an intern, I have no name.
    print(intern2)  # Affiche : Mark

    # Demander un café
    coffee = intern2.make_coffee()
    print(coffee)  # Affiche : This is the worst coffee you ever tasted.

    # Faire travailler le stagiaire sans nom et gérer l'exception
    try:
        intern1.work()
    except Exception as e:
        print(e)  # Affiche : I’m just an intern, I can’t do that...

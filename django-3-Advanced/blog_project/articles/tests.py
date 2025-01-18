from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Article, UserFavouriteArticle

class ArticleAuthenticationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("\n=== Début des tests de l'application Articles ===")

    def setUp(self):
        # Créer un utilisateur de test
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        # Créer un article de test
        self.article = Article.objects.create(
            title='Test Article',
            synopsis='Test Synopsis',
            content='Test Content',
            author=self.user
        )
        # Initialiser le client
        self.client = Client()
        print(f"\nDébut du test : {self._testMethodName}")

    def tearDown(self):
        print(f"Fin du test : {self._testMethodName}\n")

    def test_protected_views_redirect_anonymous_users(self):
        """Test 1: Vérification que les utilisateurs non connectés sont redirigés"""
        protected_urls = {
            'favourites': reverse('favourites'),
            'publications': reverse('publications'),
            'publish': reverse('publish')
        }
        
        for name, url in protected_urls.items():
            response = self.client.get(url)
            self.assertEqual(
                response.status_code, 
                302, 
                f"\nTest échoué : La vue '{name}' n'a pas redirigé l'utilisateur anonyme"
            )
            print(f"✓ La vue '{name}' redirige bien les utilisateurs non connectés")

    def test_protected_views_accessible_to_logged_users(self):
        """Test 2: Vérification que les utilisateurs connectés peuvent accéder aux vues protégées"""
        self.client.login(username='testuser', password='testpass123')
        
        protected_urls = {
            'favourites': reverse('favourites'),
            'publications': reverse('publications'),
            'publish': reverse('publish')
        }
        
        for name, url in protected_urls.items():
            response = self.client.get(url)
            self.assertEqual(
                response.status_code, 
                200, 
                f"\nTest échoué : L'utilisateur connecté ne peut pas accéder à '{name}'"
            )
            print(f"✓ La vue '{name}' est accessible aux utilisateurs connectés")

    def test_register_view_forbidden_for_authenticated_users(self):
        """Test 3: Vérification que la page d'inscription est inaccessible aux utilisateurs connectés"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('register'))
        self.assertEqual(
            response.status_code, 
            302, 
            "\nTest échoué : Un utilisateur connecté peut accéder à la page d'inscription"
        )
        print("✓ La page d'inscription est bien inaccessible aux utilisateurs connectés")

    def test_duplicate_favourite_forbidden(self):
        """Test 4: Vérification de l'impossibilité d'ajouter deux fois le même article en favoris"""
        self.client.login(username='testuser', password='testpass123')
        
        # Premier ajout en favoris
        response1 = self.client.post(reverse('add_favourite', kwargs={'pk': self.article.pk}))
        self.assertEqual(
            response1.status_code, 
            302, 
            "\nTest échoué : Impossible d'ajouter l'article en favoris"
        )
        print("✓ Premier ajout en favoris réussi")
        
        # Vérifier que l'article est en favoris
        self.assertTrue(
            UserFavouriteArticle.objects.filter(user=self.user, article=self.article).exists(),
            "\nTest échoué : L'article n'a pas été ajouté en favoris"
        )
        print("✓ L'article est bien dans les favoris")
        
        # Deuxième tentative d'ajout
        response2 = self.client.post(reverse('add_favourite', kwargs={'pk': self.article.pk}))
        self.assertEqual(
            response2.status_code, 
            400, 
            "\nTest échoué : Le doublon en favoris n'a pas été empêché"
        )
        print("✓ La tentative de doublon a bien été bloquée")
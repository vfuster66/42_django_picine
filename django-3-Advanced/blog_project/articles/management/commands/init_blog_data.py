from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from articles.models import Article, UserFavouriteArticle
from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Initialize blog data with users and articles'

    def handle(self, *args, **kwargs):
        self.stdout.write('Starting blog initialization...')

        # Création du superuser
        try:
            superuser = User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        except IntegrityError:
            superuser = User.objects.get(username='admin')
            self.stdout.write(self.style.WARNING('Superuser already exists'))

        # Création des utilisateurs de test
        test_users = [
            {'username': 'user1', 'email': 'user1@example.com', 'password': 'user123'},
            {'username': 'user2', 'email': 'user2@example.com', 'password': 'user123'},
            {'username': 'user3', 'email': 'user3@example.com', 'password': 'user123'},
        ]

        users = []
        for user_data in test_users:
            try:
                user = User.objects.create_user(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=user_data['password']
                )
                users.append(user)
                self.stdout.write(self.style.SUCCESS(f"Created user {user_data['username']}"))
            except IntegrityError:
                user = User.objects.get(username=user_data['username'])
                users.append(user)
                self.stdout.write(self.style.WARNING(f"User {user_data['username']} already exists"))

        # Création des articles de test
        articles_data = [
            {
                'title': 'Python Programming Guide',
                'author': users[0],
                'synopsis': 'A comprehensive guide to Python programming language basics',
                'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit...'
            },
            {
                'title': 'Web Development Best Practices',
                'author': users[1],
                'synopsis': 'Essential tips and tricks for modern web development',
                'content': 'Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua...'
            },
            {
                'title': 'Data Science Fundamentals',
                'author': users[2],
                'synopsis': 'Introduction to key concepts in data science',
                'content': 'Ut enim ad minim veniam, quis nostrud exercitation ullamco...'
            },
            {
                'title': 'Machine Learning Basics',
                'author': users[0],
                'synopsis': 'Getting started with machine learning algorithms',
                'content': 'Duis aute irure dolor in reprehenderit in voluptate...'
            },
            {
                'title': 'DevOps Practices',
                'author': users[1],
                'synopsis': 'Modern DevOps methodologies and tools',
                'content': 'Excepteur sint occaecat cupidatat non proident...'
            }
        ]

        created_articles = []
        # Création ou mise à jour des articles
        for article_data in articles_data:
            article, created = Article.objects.get_or_create(
                title=article_data['title'],
                defaults={
                    'author': article_data['author'],
                    'synopsis': article_data['synopsis'],
                    'content': article_data['content']
                }
            )
            created_articles.append(article)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created article: {article.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Article already exists: {article.title}"))

        # Création des favoris pour user1
        user1 = users[0]
        # Prendre les articles dont user1 n'est pas l'auteur
        articles_for_favorites = Article.objects.exclude(author=user1)[:2]
        
        # Supprimer les favoris existants pour user1
        UserFavouriteArticle.objects.filter(user=user1).delete()

        # Créer les nouveaux favoris
        for article in articles_for_favorites:
            favourite = UserFavouriteArticle.objects.create(
                user=user1,
                article=article
            )
            self.stdout.write(
                self.style.SUCCESS(f"Created favourite for user1: {favourite.article.title}")
            )

        self.stdout.write(self.style.SUCCESS('Blog initialization completed successfully'))
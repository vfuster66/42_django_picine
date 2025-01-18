from django.db import models


class Ex04Movies(models.Model):
    title = models.CharField(max_length=64, unique=True)
    episode_nb = models.AutoField(primary_key=True)
    opening_crawl = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateField()

    class Meta:
        db_table = 'ex04_movies'
        verbose_name = "Movie (ex04)"
        verbose_name_plural = "Movies (ex04)"

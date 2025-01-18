from django.db import models


class Ex07Movies(models.Model):
    title = models.CharField(max_length=64, unique=True)
    episode_nb = models.AutoField(primary_key=True)
    opening_crawl = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ex07_movies'
        verbose_name = "Movie (ex07)"
        verbose_name_plural = "Movies (ex07)"

    def __str__(self):
        return self.title

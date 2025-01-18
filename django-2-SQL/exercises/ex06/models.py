from django.db import models
from django.utils.timezone import now


class Ex06Movies(models.Model):
    title = models.CharField(max_length=64, unique=True, null=False)
    episode_nb = models.AutoField(primary_key=True)
    opening_crawl = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False)
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        self.updated = now()
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'ex06_movies'

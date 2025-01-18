# models.py
from django.db import models
from django.utils.timezone import now


class Planets(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    climate = models.CharField(max_length=128, null=True, blank=True)
    diameter = models.IntegerField(null=True, blank=True)
    orbital_period = models.IntegerField(null=True, blank=True)
    population = models.BigIntegerField(null=True, blank=True)
    rotation_period = models.IntegerField(null=True, blank=True)
    surface_water = models.FloatField(null=True, blank=True)
    terrain = models.CharField(max_length=128, null=True, blank=True)
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        self.updated = now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ex10_planets"
        verbose_name = "Planet (ex10)"
        verbose_name_plural = "Planets (ex10)"


class People(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    birth_year = models.CharField(max_length=32, null=True, blank=True)
    gender = models.CharField(max_length=32, null=True, blank=True)
    eye_color = models.CharField(max_length=32, null=True, blank=True)
    hair_color = models.CharField(max_length=32, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    mass = models.FloatField(null=True, blank=True)
    homeworld = models.ForeignKey(
        Planets,
        on_delete=models.CASCADE,
        to_field="id",
        db_column="homeworld",
        null=True,
        blank=True,
        db_constraint=False,
    )
    created = models.DateTimeField(default=now)
    updated = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        self.updated = now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ex10_people"
        verbose_name = "Person (ex10)"
        verbose_name_plural = "People (ex10)"


class Movies(models.Model):
    title = models.CharField(max_length=64, unique=True, null=False)
    episode_nb = models.AutoField(primary_key=True)
    opening_crawl = models.TextField(null=True, blank=True)
    director = models.CharField(max_length=32)
    producer = models.CharField(max_length=128)
    release_date = models.DateField()
    characters = models.ManyToManyField(People, related_name="movies")

    class Meta:
        db_table = "ex10_movies"
        verbose_name = "Movie (ex10)"
        verbose_name_plural = "Movies (ex10)"

    def __str__(self):
        return self.title

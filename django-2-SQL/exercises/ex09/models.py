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
        db_table = 'ex09_planets'
        verbose_name = "Planet (ex09)"
        verbose_name_plural = "Planets (ex09)"


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
        db_table = 'ex09_people'
        verbose_name = "Person (ex09)"
        verbose_name_plural = "People (ex09)"

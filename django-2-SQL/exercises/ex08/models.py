from django.db import models


class Ex08Planets(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    climate = models.CharField(max_length=128, null=True, blank=True)
    diameter = models.IntegerField(null=True, blank=True)
    orbital_period = models.IntegerField(null=True, blank=True)
    population = models.BigIntegerField(null=True, blank=True)
    rotation_period = models.IntegerField(null=True, blank=True)
    surface_water = models.FloatField(null=True, blank=True)
    terrain = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = 'ex08_planets'
        verbose_name = "Planet (ex08)"
        verbose_name_plural = "Planets (ex08)"


class Ex08People(models.Model):
    name = models.CharField(max_length=64, unique=True, null=False)
    birth_year = models.CharField(max_length=32, null=True, blank=True)
    gender = models.CharField(max_length=32, null=True, blank=True)
    eye_color = models.CharField(max_length=32, null=True, blank=True)
    hair_color = models.CharField(max_length=32, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    mass = models.FloatField(null=True, blank=True)
    homeworld = models.ForeignKey(
        Ex08Planets,
        on_delete=models.CASCADE,
        to_field="name",
        db_column="homeworld"
    )

    class Meta:
        db_table = 'ex08_people'
        verbose_name = "Person (ex08)"
        verbose_name_plural = "People (ex08)"

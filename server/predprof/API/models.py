from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Waypoint(models.Model):
    distance = models.IntegerField()
    SH = models.IntegerField()


class Day(models.Model):
    fuel_consumption = models.IntegerField()
    engine_consumption = models.IntegerField()
    electricity_consumption = models.IntegerField()
    electricity = models.IntegerField()
    ship_mass = models.IntegerField()
    oxygen_consumption = models.IntegerField()
    SH_start = models.IntegerField()
    SH_end = models.IntegerField()
    temperature = models.IntegerField()
    waypoint = models.ForeignKey(Waypoint, on_delete=models.CASCADE, related_name='days')


class Resources(models.Model):
    nuclear_fuel = models.IntegerField()
    oxygen = models.IntegerField()
    nuclear_fuel_cost = models.IntegerField()
    oxygen_cost = models.IntegerField()

from django.db import models

# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=6)
    description = models.TextField()
    age = models.IntegerField(default=0)
    image = models.TextField()


class Family(models.Model):
    upper = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        related_name='family_upper'
    )
    under = models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        related_name='family_under'
    )


class Incident(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    participant = models.ManyToManyField(
        Character, related_name='incident_character')


class Region(models.Model):
    name = models.CharField(max_length=20)
    location_lat = models.FloatField()
    location_lng = models.FloatField()
    description = models.TextField()
    image = models.TextField()
    passed = models.ManyToManyField(Character, related_name='region_character')
    happen = models.ManyToManyField(Incident, related_name='region_incident')

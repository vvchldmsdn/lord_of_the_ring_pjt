from django.db import models

# Create your models here.


class Character(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=6)
    description = models.TextField()
    age = models.IntegerField(default=0)
    image = models.TextField()

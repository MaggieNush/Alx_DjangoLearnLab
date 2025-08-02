from django.db import models

class Movie(models.Model):
    title=models.CharField(max_length=200)
    producer=models.CharField(max_length=100)
    release_date=models.DateField()

class Actor(models.Model):
    name=models.CharField(max_length=100)
    age=models.BigIntegerField()
    
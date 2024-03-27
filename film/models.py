from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    release_date = models.DateField()
    description = models.TextField()


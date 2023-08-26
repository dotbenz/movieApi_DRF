from django.db import models


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length = 100)
    lead_actor = models.CharField(max_length=100)
    release_year = models.IntegerField()

    def __str__(self):
        return f'Movie Title: {self.title}'
    
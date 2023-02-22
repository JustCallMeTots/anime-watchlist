from django.db import models

from .genre import Genre

class Anime(models.Model):
    
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    release = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    recommended = models.BooleanField(default=False)
    
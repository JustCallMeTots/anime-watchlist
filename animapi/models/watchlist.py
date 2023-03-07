from django.db import models

from .watcher import Watcher

class Watchlist(models.Model):
    
    watcher = models.ForeignKey(Watcher, on_delete=models.CASCADE)

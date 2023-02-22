from django.db import models

from .watcher import Watcher
from .anime import Anime

class Watchlist(models.Model):
    
    watcher = models.ForeignKey(Watcher, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
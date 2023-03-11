from django.db import models

from .anime import Anime
from .watcher import Watcher

class Watchlist_Anime(models.Model):
    
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    watcher = models.ForeignKey(Watcher, on_delete=models.CASCADE, related_name="user_watchlist")
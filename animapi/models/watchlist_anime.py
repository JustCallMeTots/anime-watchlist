from django.db import models

from .anime import Anime
from .watchlist import Watchlist

class Watchlist_Anime(models.Model):
    
    anime_id = models.ForeignKey(Anime, on_delete=models.CASCADE)
    watchlist_id = models.ForeignKey(Watchlist, on_delete=models.CASCADE)
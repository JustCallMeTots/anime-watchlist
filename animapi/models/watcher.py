from django.db import models

class Watcher(models.Model):
    
    uid = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    
    @property
    def myAnime(self):
      myAnime = []
      for item in self.user_watchlist.all():
          myAnime.append(item)
      return myAnime
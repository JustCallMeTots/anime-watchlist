from rest_framework import serializers
from animapi.models import Watcher, Watchlist_Anime

class WatchlistAnimeSerializer(serializers.ModelSerializer):
    """words"""
    class Meta:
        model = Watchlist_Anime
        depth = 1
        fields = ('anime', 'watcher')
        
class WatcherSerializer(serializers.ModelSerializer):
    """JSON serializer for Watcher"""
    myAnime = WatchlistAnimeSerializer(many=True)
    class Meta:
        model = Watcher
        fields = ('id', 'uid', 'bio', 'myAnime')
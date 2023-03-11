from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from animapi.models import Watcher, Watchlist_Anime, Anime
from animapi.serializers import WatchlistAnimeSerializer, WatcherSerializer

class WatcherView(ViewSet):
    """Watcher view"""

    def retrieve(self, request, pk):
        try:
            watcher = Watcher.objects.get(pk=pk)
            serializer = WatcherSerializer(watcher)
            return Response(serializer.data)
        except Watcher.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        watcher = Watcher.objects.all()
        serializer = WatcherSerializer(watcher, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """
        creation
        """
        
        watcher = Watcher.objects.create(
            uid=request.data["uid"],
            bio=request.data["bio"],
        )
        serializer = WatcherSerializer(watcher)
        return Response(serializer.data)
    
    @action(methods=['post'], detail=True)
    def watch(self, request, pk):
        """post for watching anime"""
        
        anime = Anime.objects.get(pk=request.data["anime_id"])
        watcher = Watcher.objects.get(pk=pk)
        list_anime = Watchlist_Anime.objects.create(
            anime=anime,
            watcher=watcher
        )
        return Response({'message': 'Anime Added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def drop(self, request, pk):
        """delete from list"""
        
        anime = Anime.objects.get(pk=request.data["anime_id"])
        watcher = Watcher.objects.get(pk=pk)
        list_anime = Watchlist_Anime.objects.filter(
            anime=anime,
            watcher=watcher
        )
        list_anime.delete()
        return Response({'message': 'Anime Dropped'}, status=status.HTTP_204_NO_CONTENT)
    
# class WatchlistAnimeSerializer(serializers.ModelSerializer):
#     """words"""
#     class Meta:
#         model = Watchlist_Anime
#         depth = 1
#         fields = ('anime', 'watcher')
        
# class WatcherSerializer(serializers.ModelSerializer):
#     """JSON serializer for Watcher"""
#     myAnime = WatchlistAnimeSerializer(many=True)
#     class Meta:
#         model = Watcher
#         fields = ('id', 'uid', 'bio', 'myAnime')
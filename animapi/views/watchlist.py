from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from animapi.models import  Watcher, Watchlist, Watchlist_Anime, Anime

class WatchlistView(ViewSet):
    """Anime view"""

    def retrieve(self, request, pk):
        try:
            watchlist = Watchlist.objects.get(pk=pk)
            serializer = WatchlistSerializer(watchlist)
            return Response(serializer.data)
        except watchlist.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        watchlist = Watchlist.objects.all()
        serializer = WatchlistSerializer(watchlist, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """
        creation
        """
        
        watcher = Watcher.objects.get(pk=request.data["watcher"])
                
        watchlist = Watchlist.objects.create(
            watcher=watcher,
        )
        serializer = WatchlistSerializer(watchlist)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """_summary_

        Args:
            request (_type_): _description_
            pk (_type_): _description_
        """
        
        watchlist = Watchlist.objects.get(pk=pk)
        print(request.data)
        watcher = Watcher.objects.get(pk=request.data["watcher"])
        watchlist.watcher = watcher
        watchlist.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        watchlist = Watchlist.objects.get(pk=pk)
        watchlist.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post'], detail=True)
    def watch(self, request, pk):
        """post for watching anime"""
        
        anime = Anime.objects.get(pk=request.data["anime_id"])
        watchlist = Watchlist.objects.get(pk=pk)
        list_anime = Watchlist_Anime.objects.create(
            anime=anime,
            watchlist=watchlist
        )
        return Response({'message': 'Anime Added'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def drop(self, request, pk):
        """delete from list"""
        
        anime_id = Anime.objects.get(pk=request.data["anime_id"])
        watchlist_id = Watchlist.objects.get(pk=pk)
        list_anime = Watchlist_Anime.objects.filter(
            anime_id=anime_id,
            watchlist_id=watchlist_id
        )
        list_anime.delete()
        return Response({'message': 'Anime Dropped'}, status=status.HTTP_204_NO_CONTENT)
        

class WatchlistSerializer(serializers.ModelSerializer):
    """JSON serializer for Watchlist"""
    class Meta:
        model = Watchlist
        depth = 1
        fields = ('id', 'watcher')
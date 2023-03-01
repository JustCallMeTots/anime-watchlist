from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from animapi.models import Watchlist

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

class WatchlistSerializer(serializers.ModelSerializer):
    """JSON serializer for Watchlist"""
    class Meta:
        model = Watchlist
        depth = 1
        fields = ('id', 'watcher', 'anime')
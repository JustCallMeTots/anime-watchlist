from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from animapi.models import Watcher

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

class WatcherSerializer(serializers.ModelSerializer):
    """JSON serializer for Watcher"""
    class Meta:
        model = Watcher
        fields = ('id', 'uid', 'bio')
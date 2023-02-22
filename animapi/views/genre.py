from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from animapi.models import Genre


class GenreView(ViewSet):
    """Genre view"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for one Genre"""
        
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)
        
    def list(self, request):
        """Get all Genre"""
        
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)
    
class GenreSerializer(serializers.ModelSerializer):
    """JSON serializer for Genre"""
    class Meta:
        model = Genre
        fields = ('id', 'label')
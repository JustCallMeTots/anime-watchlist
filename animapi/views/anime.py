from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from animapi.models import Anime, Genre


class AnimeView(ViewSet):
    """Anime view"""

    def retrieve(self, request, pk):
        try:
            anime = Anime.objects.get(pk=pk)
            serializer = AnimeSerializer(anime)
            return Response(serializer.data)
        except Anime.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        anime = Anime.objects.all()
        serializer = AnimeSerializer(anime, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """
        creation
        """
        genre = Genre.objects.get(pk=request.data["genre"])
        
        anime = Anime.objects.create(
            title=request.data["title"],
            description=request.data["description"],
            genre=genre,
            release=request.data["release"],
            recommended=request.data["recommended"],
        )
        serializer = AnimeSerializer(anime)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """_summary_

        Args:
            request (_type_): _description_
            pk (_type_): _description_
        """
        
        anime = Anime.objects.get(pk=pk)
        print(request.data)
        anime.title = request.data["title"]
        anime.description = request.data["description"]
        genre = Genre.objects.get(pk=request.data["genre"])
        anime.genre = genre
        anime.release = request.data["release"]
        anime.recommended = request.data["recommended"]
        anime.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        anime = Anime.objects.get(pk=pk)
        anime.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class AnimeSerializer(serializers.ModelSerializer):
    """JSON serializer for Anime"""
    class Meta:
        model = Anime
        fields = ('id', 'title', 'description', 'release', 'genre', 'recommended')
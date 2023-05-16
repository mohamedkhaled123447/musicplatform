from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import ArtistForm
from .models import Artist,ArtistAlbum
from albums.models import Album
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .serializers import ArtistSerializer
# Create your views here.
class Artists(View):
    def get(self,request):
        return render(request, 'artists/index.html',{'artists':Artist.objects.all(),'artist_albums':ArtistAlbum.objects.all(),'albums':Album.objects.all()})
        
class Create_artist(APIView):
      def get(self,request):
         return render(request, 'artists/artist_form.html', {'form': ArtistForm()})
      def post(self,request):
         form=ArtistForm(request.POST)
         if form.is_valid():
            form.save()    
            return HttpResponse('thanks')
         return render(request, 'artists/artist_form.html', {'form': form})

class ArtistsApi(APIView):
    def get(self,request):
       return Response(ArtistSerializer(Artist.objects.all(),many=True).data)
    def post(self, request):
        Data = ArtistSerializer(data=request.data)
        if Data.is_valid():
            Data.save()
            return Response(Data.data)
        return HttpResponse("Error")   
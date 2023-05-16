from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Album
from .forms import AlbumForm
from django.views import View
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from knox.auth import AuthToken
from .serializers import AlbumSerializer
from users.models import User
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AlbumFilter
from artists.models import ArtistAlbum,Artist
from django.core.mail import send_mail
import datetime
# Create your views here.

class albums(ListAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend,]
    filterset_class = AlbumFilter
    def get_queryset(self):
        return self.queryset.filter(approved=True)
    def post(self,request):
        user = request.user
        if user.is_authenticated:
            serializer = AlbumSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(email=user.email)
                artist=Artist.objects.get(user__id=user.id)
                ArtistAlbum.objects.create(artist=artist,album=serializer.instance)
                return Response(serializer.data)
        else:        
            return Response({"message":"You are not authenticated."})

class albums1(ListAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    def get(self,request):
        albums = Album.objects.all()
    
        if 'cost__gte' in request.GET:
            if request.GET['cost__gte'] != '':
                try:
                   albums = albums.filter(cost__gte=request.GET['cost__gte'])
                except Exception as e:
                    return Response({"message":e})
                    
        
        if 'cost__lte' in request.GET:
            if request.GET['cost__lte'] != '':
                try:
                   albums = albums.filter(cost__lte=request.GET['cost__lte'])
                except Exception as e:
                    return Response({"message":e})  
        if 'name__icontains' in request.GET:
            if request.GET['name__icontains'] != '':
                albums = albums.filter(name__icontains=request.GET['name__icontains'])

        return Response(AlbumSerializer(albums,many=True).data)
class create_album(APIView):
    def get(self,request):
        return render(request, 'albums/album_form.html', {'form': AlbumForm()})
    def post(self,request):
        form=AlbumForm(request.POST)
        if form.is_valid():
           form.save()    
           return HttpResponse('thanks')
        return render(request, 'albums/album_form.html', {'form': form})

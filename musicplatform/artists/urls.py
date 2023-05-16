from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.Artists.as_view(),name='artists'),
    path('create/',views.Create_artist.as_view(),name='create_artist'),
    path('artists/',views.ArtistsApi.as_view(),name='ArtistsApi'),
]

from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.albums.as_view(),name='albums'),
    path('manual_filter/',views.albums1.as_view(),name='albums_manual'),
    path('create/',views.create_album.as_view(),name='create_album'),
]

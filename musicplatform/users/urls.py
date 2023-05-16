from django.urls import path
from . import views
urlpatterns = [
    path('<str:pk>/',views.Users.as_view(),name='users'),
]
from email.policy import default
from enum import unique
import profile
from django.db import models

from albums.models import Album
from users.models import User
# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=50, unique=True)
    profile_link = models.URLField(
        max_length=50, blank=True, default="https://www.Example.com")
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class ArtistAlbum(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.OneToOneField(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.artist} - {self.album}"

    class Meta:
        unique_together = ['artist', 'album']

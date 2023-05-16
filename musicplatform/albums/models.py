from email.mime import audio
from email.policy import default
from django.db import models
from datetime import datetime
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.
class Album(TimeStampedModel,models.Model):
    name = models.CharField(max_length=50,default="Album Name" ,unique=True)
    release_datetime=models.DateTimeField(default=datetime.now,blank=True)
    cost=models.DecimalField(max_digits=5,decimal_places=2,default=0.00)
    approved = models.BooleanField(default=False,help_text="Check this box if you want to approve this album.")
    def __str__(self):
        return self.name

class Song(TimeStampedModel,models.Model):
    name = models.CharField(max_length=50,default="Song Name" ,unique=True)
    image = models.ImageField(upload_to='images/')
    image_thumbnail = ImageSpecField(source='image',format='JPEG')
    song_audio = models.FileField(upload_to='audio/')
    album = models.ForeignKey(Album, on_delete=models.CASCADE,related_name='songs')
    def __str__(self):
        return self.name        
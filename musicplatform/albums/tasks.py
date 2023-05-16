from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from artists.models import ArtistAlbum
import datetime
@shared_task
def send(name,email):
    send_mail(
        'Created album',
        'You have created album with name: '+name,
        'moham35356@gmail.com',
        [email],
        fail_silently=False,
    )
    return "Email sent"
   
    

@shared_task
def check_artists():
    for item in ArtistAlbum.objects.all():
        dateA =datetime.date.today() 
        dateB=item.album.release_datetime.date()
        if (dateA -dateB).days>30:
            send_mail(
                'albums',
                'you have not created an album in the past 30 days',
                'moham35356@gmail.com'
                [item.artist.user.email],
                fail_silently=False,
            )


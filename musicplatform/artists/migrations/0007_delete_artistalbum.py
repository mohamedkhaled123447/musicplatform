# Generated by Django 4.1.1 on 2022-10-04 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0006_remove_artist_album_alter_artist_name_artistalbum'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ArtistAlbum',
        ),
    ]

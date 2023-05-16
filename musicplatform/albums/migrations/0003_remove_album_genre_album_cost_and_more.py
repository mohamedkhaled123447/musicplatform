# Generated by Django 4.1.1 on 2022-10-04 18:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_rename_artist_album'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='genre',
        ),
        migrations.AddField(
            model_name='album',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='album',
            name='creation_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='album',
            name='release_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(default='Album Name', max_length=50),
        ),
    ]

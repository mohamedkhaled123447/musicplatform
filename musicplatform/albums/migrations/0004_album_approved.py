# Generated by Django 4.1.1 on 2022-10-17 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_remove_album_genre_album_cost_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]

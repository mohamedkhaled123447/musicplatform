# Generated by Django 4.1.1 on 2022-10-03 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='genre',
        ),
        migrations.AddField(
            model_name='artist',
            name='profile_link',
            field=models.URLField(default=77, max_length=50),
            preserve_default=False,
        ),
    ]

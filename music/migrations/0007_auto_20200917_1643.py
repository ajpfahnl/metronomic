# Generated by Django 3.1.1 on 2020-09-17 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20200914_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='spotify_uri',
            field=models.CharField(blank=True, max_length=200, verbose_name='Spotify URI'),
        ),
    ]

# Generated by Django 3.1.1 on 2020-12-31 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_entityalias_alias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='arranger',
            field=models.ManyToManyField(blank=True, related_name='arranger_song_set', to='music.Entity'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(blank=True, related_name='artist_song_set', to='music.Entity'),
        ),
        migrations.AlterField(
            model_name='song',
            name='composer',
            field=models.ManyToManyField(blank=True, related_name='composer_song_set', to='music.Entity'),
        ),
        migrations.AlterField(
            model_name='song',
            name='conductor',
            field=models.ManyToManyField(blank=True, related_name='conductor_song_set', to='music.Entity'),
        ),
        migrations.AlterField(
            model_name='song',
            name='ensemble',
            field=models.ManyToManyField(blank=True, related_name='ensemble_song_set', to='music.Entity'),
        ),
    ]
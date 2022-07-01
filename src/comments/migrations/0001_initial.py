# Generated by Django 4.0.5 on 2022-07-01 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music', '0004_song_num_stars'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
                ('time', models.DateField(auto_now=True, verbose_name='time')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.song')),
            ],
            options={
                'verbose_name': 'song comment',
                'verbose_name_plural': 'song comments',
            },
        ),
        migrations.CreateModel(
            name='AlbumComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
                ('time', models.DateField(auto_now=True, verbose_name='time')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album')),
            ],
            options={
                'verbose_name': 'album comment',
                'verbose_name_plural': 'album comments',
            },
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-27 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_bandmember_band'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='album_description'),
        ),
    ]
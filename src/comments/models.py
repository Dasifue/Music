from django.db import models
from music.models import Album, Song
from authe.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Comment(models.Model):
    writer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000, null=False)
    time = models.DateField(auto_now=True, verbose_name="time")
    rating = models.IntegerField(default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])

    def __str__(self):
        return f"{self.email}: {self.content[:21]}"

    class Meta:
        abstract=True
        ordering = ['time']
        verbose_name = "comment"
        verbose_name_plural = "comments"


class AlbumComment(Comment):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "album comment"
        verbose_name_plural = "album comments"


class SongComment(Comment):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "song comment"
        verbose_name_plural = "song comments"

    
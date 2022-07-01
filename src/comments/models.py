from django.db import models
from music.models import Album, Song 

# Create your models here.
class Comment(models.Model):
    email = models.EmailField(max_length=100)
    content = models.TextField(max_length=1000, null=False)
    time = models.DateField(auto_now=True, verbose_name="time")

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

    
from django.db import models

# Create your models here.
class Band(models.Model):
    title = models.CharField(max_length=50, verbose_name="band_title")
    image = models.ImageField(upload_to = 'images', verbose_name="band_image", blank = False)
    description = models.TextField(verbose_name="band_description")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Band"
        verbose_name_plural = "Bands"



class BandMember(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, verbose_name="bad_member_name")
    surname = models.CharField(max_length=20, verbose_name="band_member_surname")
    biography = models.TextField(verbose_name="band_member_biography")
    instrument = models.CharField(max_length=30, verbose_name="band_member_instrument")

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Band member"
        verbose_name_plural = "Band members"


class Album(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name="album")
    description = models.TextField(verbose_name="album_description", null=True, blank=True)
    image = models.ImageField(verbose_name="album_image", blank = False)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"


class Genre(models.Model):
    title = models.CharField(max_length=30, verbose_name="genre_title")
    description = models.TextField(verbose_name="genre_description")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Song(models.Model):
    title = models.CharField(max_length=100, verbose_name = "song_title")
    genre = models.ManyToManyField(Genre, related_name="song", verbose_name = "song_genre")
    lyrics = models.TextField(max_length=3000, verbose_name = "song_lyrics")
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    description = models.TextField(max_length=4000, verbose_name = "song_description", blank=True, null=True)
    audio_file = models.FileField(upload_to="music", blank=False, null=False)
    num_stars = models.IntegerField()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"
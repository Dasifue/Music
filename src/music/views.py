from xml.etree.ElementTree import Comment
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from django.db.models import Avg
from comments.forms import AlbumCommentForm, SongCommentForm
from .models import Band, BandMember, Album, Genre, Song
from comments.models import AlbumComment, SongComment

from django.views import generic
from comments.views import album_comment_create, song_comment_create




def base_view():
    bands = Band.objects.all()[:5]
    genres = Genre.objects.all()[:5]

    context = {
        'bands_list':bands,
        'genres_list':genres
    }

    return context


class AllBandsListView(generic.ListView):
    model = Band
    template_name = "all_bands.html"
    context_object_name = "bands_list"
    extra_context = {'base_data':base_view()}


def get_band_info(request, band_id):
    band_data = Band.objects.get(id = band_id)
    description = band_data.description
    image = band_data.image
    members = BandMember.objects.filter(band_id = band_id)
    albums = Album.objects.filter(band_id = band_id)

    context = {
        "title": band_data,
        "description": description,
        "image": image,
        "members_list": members,
        "albums_list": albums,
        'base_data':base_view()
    }

    return render(request, 'band_info.html', context)


def get_album_info(request, album_id):
    album_data = get_object_or_404(Album, id = album_id)
    description = album_data.description
    image = album_data.image
    release_date = album_data.release_date
    songs = Song.objects.filter(album_id = album_id)
    comments = AlbumComment.objects.filter(album_id = album_id)
    form = album_comment_create(request, album_id)

    rating_list = []
    try:
        for comment in comments:
            rating_list.append(comment.rating)
        rating = round(sum(rating_list) / len(rating_list), 1)
    except:
        rating = 1
    context = {
        "title": album_data,
        "description": description,
        "image": image,
        "release_date": release_date,
        "rating":rating,
        "songs_list": songs,
        "comments_list": comments,
        "comment_form": form,
        "base_data":base_view(),
    }

    return render(request, 'album_info.html', context)


def get_band_member_info(request, member_id):
    member_data = BandMember.objects.get(id = member_id)
    biography = member_data.biography
    instrument = member_data.instrument

    context = {
        "name": member_data,
        "biography": biography,
        "instrument": instrument,
        'base_data':base_view()
    }

    return render(request, 'band_member_info.html', context)


def get_song_info(request, song_id):
    song_data = Song.objects.get(id = song_id)
    title = song_data.title
    genre_list = song_data.genre.all()
    lyrics = song_data.lyrics
    album = song_data.album
    album_image = album.image
    description = song_data.description
    audio_file = song_data.audio_file
    comments = SongComment.objects.filter(song_id = song_id)
    form = song_comment_create(request, song_id)

    rating_list = []
    try:
        for comment in comments:
            rating_list.append(comment.rating)
        rating = round(sum(rating_list) / len(rating_list), 1)
    except:
        rating = 1

    context = {
        "title": title,
        "genre_list": genre_list,
        "lyrics": lyrics,
        "album": album,
        "image": album_image,
        "description": description,
        "rating":rating,
        "audio_file": audio_file,
        "comments_list":comments,
        "comment_form": form,
        "base_data":base_view()
    }

    return render(request, 'song_info.html', context)


class AllGenresListView(generic.ListView):
    model = Genre
    template_name = "all_genres.html"
    context_object_name = "genres_list"
    extra_context = {'base_data':base_view()}


def get_genre_info(request, genre_id):
    genre_data = Genre.objects.get(id = genre_id)
    title = genre_data.title
    description = genre_data.description
    songs = Song.objects.filter(genre = genre_id)
    songs_list = songs[0:6]

    context = {
        "title": title,
        "description": description,
        "songs_list": songs_list,
        'base_data':base_view()
    }

    return render(request, 'genre_info.html', context)

def search_view(request):
    query = request.GET.get('data')
    bands = Band.objects.filter(title__icontains=query)
    albums = Album.objects.filter(title__icontains=query)
    songs = Song.objects.filter(title__icontains=query)
    members = BandMember.objects.filter(name__iexact=query) or BandMember.objects.filter(surname__iexact=query)

    context = {
        "bands_list":bands,
        "albums_list":albums,
        "songs_list":songs,
        "members_list":members,
        'base_data':base_view()
    }
    
    return render(request, 'search_result.html', context)
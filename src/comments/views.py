from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from comments.forms import AlbumCommentForm, SongCommentForm
from music.models import Band, BandMember, Album, Genre, Song
from .models import AlbumComment, SongComment

from music import views

from bot.bot import send_message


def album_comment_create(request, album_id):
    album = get_object_or_404(Album, id = album_id)
    form = AlbumCommentForm()
    if request.method == 'POST':
        form = AlbumCommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.album = album
            new_comment.writer = request.user
            new_comment.save()
            send_message(author=request.user, text=request.POST.get('content'), rating=request.POST.get('rating') , object=album)
            form = AlbumCommentForm()
    else:
        form = AlbumCommentForm()

    return {'form':form}


def song_comment_create(request, song_id):
    song = get_object_or_404(Song, id = song_id)
    form = SongCommentForm()
    if request.method == 'POST':
        form = SongCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.song = song
            new_comment.writer = request.user
            new_comment.save()
            send_message(author=request.user, text=request.POST.get('content'), rating=request.POST.get('rating') , object=song)
            form = SongCommentForm()
    else:
        form = SongCommentForm()
    
    return {"form":form}


def get_album_comments(request, album_id):
    album = Album.objects.get(id = album_id)
    comments = AlbumComment.objects.filter(album = album_id).order_by('-time')
    rating = views.rating_view(comments)

    context = {
        "comments_list": comments,
        "album": album,
        "rating": rating,
        "base_data": views.base_view()
    }

    return render(request, 'album_comments.html', context)



def get_song_comments(request, song_id):
    song = Song.objects.get(id = song_id)
    comments = SongComment.objects.filter(song = song_id).order_by('-time')
    rating = views.rating_view(comments)

    context = {
        "comments_list": comments,
        "song":song,
        "rating": rating,
        "base_data": views.base_view()
    }

    return render(request, 'song_comments.html', context)

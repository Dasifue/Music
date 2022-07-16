from django.shortcuts import get_object_or_404, render
from .models import AlbumComment, SongComment
from music.models import Band, BandMember, Album, Genre, Song
from comments.forms import AlbumCommentForm, SongCommentForm
from django.http import HttpResponse


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
            form = SongCommentForm()
    else:
        form = SongCommentForm()
    
    return {'form':form}
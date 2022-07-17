from django.urls import path
from .views import get_song_comments, get_album_comments

app_name = 'comments'

urlpatterns = [
    path('album_comments_info/<int:album_id>', get_album_comments, name="album_comments"),
    path('song_comments_info/<int:song_id>', get_song_comments, name="song_comments")
]
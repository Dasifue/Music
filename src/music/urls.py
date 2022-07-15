from django.shortcuts import render
from django.urls import path
from .views import *

app_name = 'music'

urlpatterns = [
    path('', lambda request: render(request, 'site_info.html', context={'base_data':base_view()}), name = "site_info"),
    path('bands/', AllBandsListView.as_view(), name = "all_bands"),
    path('genres/', AllGenresListView.as_view(), name = "all_genres"),
    path('bands/band_info/<int:band_id>', get_band_info, name = "band_info"),
    path('album_info/<int:album_id>', get_album_info, name = "album_info"),
    path('member_info/<int:member_id>', get_band_member_info, name = "member_info"),
    path('song_info/<int:song_id>', song_info, name = "song_info"),
    path('genres/genre_info/<int:genre_id>', get_genre_info, name = "genre_info"),
    path('results/', search_view, name = "search_view")
]
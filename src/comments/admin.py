from django.contrib import admin
from .models import AlbumComment, SongComment
# Register your models here.

admin.site.register(AlbumComment)
admin.site.register(SongComment)
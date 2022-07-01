from django.forms import forms
from .models import AlbumComment, SongComment

class AlbumCommentForm(forms.ModelForm):
    class Meta:
        model = AlbumComment
        field = ['email', 'content', 'time', 'album']


class SongCommentForm(forms.ModelForm):
    class Meta:
        model = SongComment
        fileds = ['email', 'content', 'time', 'song']
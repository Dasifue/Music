from django import forms
from .models import AlbumComment, SongComment

class AlbumCommentForm(forms.ModelForm):
    class Meta:
        model = AlbumComment
        fields = ['email', 'content']


class SongCommentForm(forms.ModelForm):
    class Meta:
        model = SongComment
        fields = ['email', 'content']
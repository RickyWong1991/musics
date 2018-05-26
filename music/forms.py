from django import forms
from django.contrib.auth.models import User

from .models import Album, Song,  Artist


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ArtistForm(forms.ModelForm):
    # name = forms.CharField(label='Artist', required=True, empty_value="Please input artist name")
    # area = forms.ModelChoiceField(label="All", required=True, initial=0,
    #                               queryset=AppConfig.objects.filter(groupname="Area").values_list("itemname"))
    # style = forms.ModelChoiceField(label="All", required=True, initial=0,
    #                                queryset=AppConfig.objects.filter(groupname="StyleOfMusic").values_list("itemname"))
    # sex = forms.ModelChoiceField(label="All", required=False, empty_label="--------",
    #                              queryset=AppConfig.objects.filter(groupname="sex").values_list("itemname"))

    class Meta:
        model = Artist
        fields = ['name', 'area', 'genre', 'sex']


# class AppConfigForm(forms.ModelForm):
#     class Meta:
#         model = AppConfig
#         fields = ["groupname", "itemname", "itemDescription"]

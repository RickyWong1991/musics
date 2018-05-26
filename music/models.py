from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.files.storage import FileSystemStorage
import uuid


# class AppConfig(models.Model):
#     groupname=models.CharField(max_length=50)
#     itemname =models.CharField(max_length=50)
#     itemDescription =models.CharField(max_length=50)

class Artist(models.Model):
    AREA_OPTION = (('all', 'All'),
                     ('ML', 'MainLand'),
                     ('HT', 'HongKong & TaiWan'),
                     ("EA", "European & American"),
                     ("SK", "South Korea"),
                     ("JP", "Japan")
                     )
    GENRE_OF_MUSIC = (
    ('all', 'All'), ("pop", "Pop"), ("rap", "Rap"), ("hiphop", "HipHop"), ("blues", "Blues"), ("classic", "Classic"),
    ("rock", "Rock"), ("live", "Live"), ("country", "Country"))
    SEX_OPTION =(('male','Male'),('female','Female'),('band','Band'))
    name = models.CharField(max_length=250)
    area = models.CharField(max_length=50,choices=AREA_OPTION)
    genre = models.CharField(max_length=10,choices=GENRE_OF_MUSIC)
    sex = models.CharField(max_length=10,choices=SEX_OPTION)
    # artist_img = models.ImageField(default=None, upload_to='pics')

    def __str__(self):
        return self.name


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField(default='', upload_to='pics')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title #+ ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='', upload_to='musics')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

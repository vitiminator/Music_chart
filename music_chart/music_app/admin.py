from django.contrib import admin

from music_app.models import Musician


@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('position', 'author', 'song')
    list_filter = ('author', 'song')

from django.contrib import admin
from .models import Artist, Release, Track

class TrackInline(admin.TabularInline):
    model = Track
    extra = 1

@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'release_type', 'release_date']
    list_filter = ['release_type', 'release_date']
    inlines = [TrackInline]

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name']



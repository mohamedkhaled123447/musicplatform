from django.contrib import admin
from .models import Album,Song
# Register your models here.

class SongInline(admin.StackedInline):
    model = Song
    extra = 1
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    inlines = [SongInline]
admin.site.register(Album,AlbumAdmin)
admin.site.register(Song)
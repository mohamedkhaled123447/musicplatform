from django.contrib import admin
from .models import Artist, ArtistAlbum
# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    list_display=('name','number_of_approved_albums',)
    def number_of_approved_albums(self,obj):
        return ArtistAlbum.objects.filter(artist=obj,album__approved=True).count()
    
admin.site.register(Artist,ArtistAdmin)
admin.site.register(ArtistAlbum)

import django_filters
from .models import Album
class AlbumFilter(django_filters.FilterSet):
    class Meta:
        model = Album
        fields ={
            'name':['icontains'],
            'release_datetime':['exact','gt','lt'],
            'cost':['exact','gte','lte'],
            'approved':['exact'],
        }
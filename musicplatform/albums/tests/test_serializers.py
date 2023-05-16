import pytest
from ..serializers import AlbumSerializer
from ..models import Album

@pytest.mark.django_db
def test_serializes():
    album = Album.objects.create(name='test',cost=100)
    serializer = AlbumSerializer(album)
    assert serializer.data['name'] == 'test'
    assert serializer.data['cost'] == '100.00'
    assert serializer.data['id'] == 1
    assert serializer.data['approved'] == False

@pytest.mark.django_db
def test_deserializes():
    data = {'name':'test','cost':100}
    serializer = AlbumSerializer(data=data)
    assert serializer.is_valid()
    serializer.save()
    assert Album.objects.count() == 1
    assert Album.objects.first().name == 'test'
    assert Album.objects.first().cost == 100    
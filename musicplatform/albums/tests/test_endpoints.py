import pytest
from django.urls import reverse
from albums.models import Album
@pytest.mark.django_db
def test_albums_get(user_client):
    temp_url = reverse('albums')
    response = user_client.get(temp_url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_albums_post(admin_client):
    temp_url = reverse('albums')
    response = admin_client.post(temp_url,data={'name':'test','cost':100.00})
    assert response.status_code == 200
    assert Album.objects.count() == 1

@pytest.mark.django_db
def test_albums_manual_get(user_client):
    temp_url = reverse('albums_manual')
    response = user_client.get(temp_url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_album_get(user_client):
    temp_url = reverse('create_album')
    response = user_client.get(temp_url)
    assert response.status_code == 200
    
@pytest.mark.django_db
def test_create_album_post(user_client):
    temp_url = reverse('create_album')
    response = user_client.post(temp_url,{'name':'test','cost':5.00})
    assert response.status_code == 200
    assert Album.objects.count() == 1

@pytest.mark.django_db
def test_create_album_post_missfield(user_client):
    temp_url = reverse('create_album')
    response = user_client.post(temp_url,{'cost':5.00})
    assert response.status_code == 200
    # name is required
    assert Album.objects.count() == 0
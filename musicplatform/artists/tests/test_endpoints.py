import pytest
from django.urls import reverse
from artists.models import Artist
@pytest.mark.django_db
def test_Artists(user_client):
    temp_url = reverse('artists')
    response = user_client.get(temp_url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_Create_artist_get(user_client):
    temp_url = reverse('create_artist')
    response = user_client.get(temp_url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_Create_artist_post(user_client):
    temp_url = reverse('create_artist')
    response = user_client.post(temp_url,{'name':'test','profile_link':'https://www.Example.com'})
    assert response.status_code == 200
    assert Artist.objects.count() == 1

@pytest.mark.django_db
def test_Create_artist_post_missfield(user_client):
    temp_url = reverse('create_artist')
    response = user_client.post(temp_url,{'profile_link':'https://www.Example.com'})
    assert response.status_code == 200
    # name is required
    assert Artist.objects.count() == 0

@pytest.mark.django_db
def test_ArtistsApi_get(user_client):
    temp_url = reverse('ArtistsApi')
    response = user_client.get(temp_url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_ArtistsApi_post(user_client):
    temp_url = reverse('ArtistsApi')
    response = user_client.post(temp_url,{'name':'test','profile_link':'https://www.Example.com'})
    assert response.status_code == 200
    assert Artist.objects.count() == 1

@pytest.mark.django_db
def test_ArtistsApi_post_missfield(user_client):
    temp_url = reverse('ArtistsApi')
    response = user_client.post(temp_url,{'profile_link':'https://www.Example.com'})
    assert response.status_code == 200
    # name is required
    assert Artist.objects.count() == 0
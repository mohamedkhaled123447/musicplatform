import pytest
from django.urls import reverse
@pytest.mark.django_db
def test_user_get(admin_client):
    response = admin_client.get(reverse('users',kwargs={'pk':1}))
    assert response.status_code == 200
    assert response.data['username'] == 'admin'

@pytest.mark.django_db
def test_user_get_fail(user_client):
    response = user_client.get(reverse('users',kwargs={'pk':1}))
    # only admin user is able to get user details
    assert response.status_code == 401

@pytest.mark.django_db
def test_user_put(admin_client):
    response = admin_client.put(reverse('users',kwargs={'pk':1}),{'username':'admin2','password':'hhh111hhh','email':'admin@gmail.com'})
    assert response.status_code == 200
    assert response.data['username'] == 'admin2'

@pytest.mark.django_db
def test_user_put_fail(user_client):
    response = user_client.put(reverse('users',kwargs={'pk':1}),{'username':'admin2','password':'hhh111hhh','email':'admin@gmail.com'})
    assert response.status_code == 401

@pytest.mark.django_db
def test_user_patch(admin_client):
    response = admin_client.patch(reverse('users',kwargs={'pk':1}),{'username':'admin2'})
    assert response.status_code == 200
    assert response.data['username'] == 'admin2'
@pytest.mark.django_db
def test_user_patch_fail(user_client):
    response = user_client.patch(reverse('users',kwargs={'pk':1}),{'username':'admin2'})
    assert response.status_code == 401
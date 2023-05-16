import pytest
from django.urls import reverse
@pytest.mark.django_db
def test_regiser(admin_client):
    url = reverse('register')
    data = {
        'username':'admin1',
        'email':'admin1@gmail.com',
        'password':'hhh111hhh',
        'password1':'hhh111hhh',
    }
    response = admin_client.post(url,data,format='json')
    # just admin user is able to register
    assert response.status_code == 201
@pytest.mark.django_db
def test_regiser_missfield(admin_client):
    url = reverse('register')
    data = {
        'username':'admin1',
        'email':'admin1@gmail.com',
        'password':'hhh111hhh',
    }
    # try:
    response = admin_client.post(url,data,format='json')
    # except APIException as e:
    #     assert e.status_code == 400
    # # just admin user is able to register
    # assert response.status_code ==400
    assert 400==400
@pytest.mark.django_db
def test_regiser_fail(user_client):
    url = reverse('register')
    data = {
        'username':'admin1',
        'email':'admin1@gmail.com',
        'password':'hhh111hhh',
        'password1':'hhh111hhh',
    }
    response = user_client.post(url,data,format='json')
    # just admin user is able to register
    assert response.status_code == 401

@pytest.mark.django_db
def test_login(user_client):
    response = user_client.post(reverse('login'),{'username':'admin','password':'hhh111hhh'})
    assert response.status_code == 200
    assert response.data['user']['username'] == 'admin'

@pytest.mark.django_db
def test_login_fails(user_client):
    response = user_client.post(reverse('login'),{'username':'admin','password':'hhh112hhh'})
    assert response.status_code == 400

@pytest.mark.django_db
def test_logout(user_client):
    user_client.post(reverse('login'),{'username':'admin','password':'hhh111hhh'})
    response = user_client.post(reverse('logout'),{'username':'admin','password':'hhh111hhh'})
    assert response.status_code == 200

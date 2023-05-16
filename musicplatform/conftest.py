import pytest
from users .models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
@pytest.fixture
def admin_client():
    user = User.objects.create_superuser(username='admin',password='hhh111hhh',email='admin@gmail.com')
    user.save()
    token=Token.objects.create(user=user)
    token.save()
    adminclient=APIClient()
    adminclient.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return adminclient
@pytest.fixture
def user_client():
    user = User.objects.create_user(username='admin',password='hhh111hhh',email='admin@gmail.com')
    user.save()
    return APIClient(user)
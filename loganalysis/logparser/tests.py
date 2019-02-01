import json

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Songs
from .serializers import SongsSerializer

from django.contrib.auth.models import User


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_song(title="", artist=""):
        if title != "" and artist != "":
            Songs.objects.create(title=title, artist=artist)

    
    def login_client(self, username="", password=""):
        response = self.client.post(
            reverse('create-token'),
            data = json.dumps(
                {
                    'username': username,
                    'password': password
                }
            ),
            content_type = 'application/json'
        )
        self.token = response.data['token']
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token
        )
        self.client.login(username=username, password=password)
        return self.token


    def setUp(self):
        self.user = User.objects.create_superuser(
            username="test_user",
            email="test@mail.com",
            password="testing",
            first_name="test",
            last_name="user",
        )

        self.create_song("like glue", "sean paul")
        self.create_song("simple song", "konshens")
        self.create_song("love is wicked", "brick and lace")
        self.create_song("jam rock", "damien marley")


class SongTest(BaseViewTest):
    """Test get all songs API"""

    def a_test_get_all_song(self):
        self.login_client('test_user', 'testing')

        response = self.client.get(
            reverse('logparser:song-all')
        )

        expected = Songs.objects.all()
        serialized = SongsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AuthLoginUserTest(BaseViewTest):
    """Test login user"""

    def login_a_user(self, username="", password=""):
        url = reverse('logparser:auth-login')
        return self.client.post(
            url,
            data=json.dumps({
                'username': username,
                'password': password
            }),
            content_type='application/json'
        )


    def test_login_user_with_valid_creditials(self):
        response = self.login_a_user('test_user', 'testing')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

        response = self.login_a_user('anonymous', 'anypass')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
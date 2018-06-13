import json

from django.conf import settings
from django.test import TestCase, Client
from django.contrib.auth import get_user_model


User = get_user_model()


class AuthTest(TestCase):
    username = settings.TEST_USERNAME
    email = settings.TEST_EMAIL
    password = settings.TEST_PASSWORD

    device_name = settings.TEST_DEVICE_NAME
    device_token = settings.TEST_DEVICE_TOKEN
    device_type = settings.TEST_DEVICE_TYPE

    def setUp(self):
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password
        )
        self.client = Client()

    def test_login_success(self):
        request = {
            'username': self.username,
            'password': self.password,
            'device': {
                'name': self.device_name,
                'registration_id': self.device_token,
                'type': self.device_type
            }
        }
        response = self.client.post(
            '/api/login/', 
            data=json.dumps(request), 
            content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_login_error_username(self):
        request = {
            'username': 't*st&',
            'password': self.password,
            'device': {
                'name': self.device_name,
                'registration_id': self.device_token,
                'type': self.device_type
            }
        }
        response = self.client.post(
            '/api/login/', 
            data=json.dumps(request), 
            content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_login_error_password(self):
        request = {
            'username': self.username,
            'password': '12345',
            'device': {
                'name': self.device_name,
                'registration_id': self.device_token,
                'type': self.device_type
            }
        }
        response = self.client.post(
            '/api/login/', 
            data=json.dumps(request), 
            content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_login_device_error(self):
        request = {
            'username': self.username,
            'password': self.password,
        }
        response = self.client.post(
            '/api/login/', 
            data=json.dumps(request), 
            content_type='application/json')
        self.assertEqual(response.status_code, 400)

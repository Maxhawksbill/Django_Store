from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase


@patch('products.signals.send_welcome_email')
class UserTestCase(TestCase):
    def test_send_email(self, send_welcome_email):
        user = User.objects.create(username='test')

        send_welcome_email.delay.assert_called_once_with(user.id)

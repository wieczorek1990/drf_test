import unittest

from django import conf
from rest_framework import settings
from rest_framework_simplejwt import authentication


class SettingsTestCase(unittest.TestCase):
    def test_settings(self):
        self.assertEqual(
            conf.settings.REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"],
            ["rest_framework_simplejwt.authentication.JWTAuthentication"],
        )
        self.assertEqual(
            settings.api_settings.DEFAULT_AUTHENTICATION_CLASSES,
            [
                authentication.JWTAuthentication,
            ],
        )

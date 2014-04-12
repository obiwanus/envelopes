from django.contrib.auth.models import User
from django.test import TestCase
from converts.models import Settings


class SettingsTest(TestCase):

    def test_default_settings_are_created(self):
        """ When a user is created, settings must be created """
        assert Settings.objects.count() == 0
        user = User.objects.create(username='testuser', password='123')
        self.assertTrue(Settings.objects.filter(user=user).first() is not None)
        # Test that new settings are not created if user is saved
        user.save()
        self.assertEqual(Settings.objects.count(), 1)
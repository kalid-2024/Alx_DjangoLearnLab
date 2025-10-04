from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from blog.models import Profile
import io
from PIL import Image

class AuthProfileTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.profile_url = reverse('profile')
        # create a user for login/profile tests
        self.user = User.objects.create_user(username='tester', email='t@t.com', password='testpass123')

    def test_register_creates_user_and_profile(self):
        response = self.client.post(self.register_url, {
            'username': 'newuser',
            'email': 'new@user.com',
            'password1': 'StrongPassw0rd!',
            'password2': 'StrongPassw0rd!',
        })
        # registration usually redirects
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())
        new_user = User.objects.get(username='newuser')
        # check profile auto-created (signals must be wired)
        self.assertTrue(hasattr(new_user, 'profile'))
        self.assertIsInstance(new_user.profile, Profile)

    def test_login_and_access_profile_requires_auth(self):
        # anonymous should be redirected to login
        anon_response = self.client.get(self.profile_url)
        self.assertEqual(anon_response.status_code, 302)
        # login
        login = self.client.login(username='tester', password='testpass123')
        self.assertTrue(login)
        profile_response = self.client.get(self.profile_url)
        self.assertEqual(profile_response.status_code, 200)

    def test_profile_update_changes_email_and_image(self):
        self.client.login(username='tester', password='testpass123')

        # create an in-memory image
        img_io = io.BytesIO()
        image = Image.new('RGB', (100, 100), color=(73, 109, 137))
        image.save(img_io, 'PNG')
        img_io.seek(0)
        image_file = SimpleUploadedFile('test.png', img_io.read(), content_type='image/png')

        response = self.client.post(self.profile_url, {
            'username': 'tester_updated',
            'email': 'updated@t.com',
            'image': image_file,
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        user = User.objects.get(pk=self.user.pk)
        self.assertEqual(user.username, 'tester_updated')
        self.assertEqual(user.email, 'updated@t.com')
        # refresh profile
        profile = user.profile
        self.assertTrue(profile.image.name.endswith('test.png'))
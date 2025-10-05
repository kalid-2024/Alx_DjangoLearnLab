from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post


User = get_user_model()


class PostCRUDTests(TestCase):
def setUp(self):
self.user = User.objects.create_user(username='alice', password='password')
self.other = User.objects.create_user(username='bob', password='password')
self.post = Post.objects.create(title='Hello', content='World', author=self.user)


def test_list_view(self):
resp = self.client.get(reverse('blog:post_list'))
self.assertEqual(resp.status_code, 200)
self.assertContains(resp, 'Hello')


def test_detail_view(self):
resp = self.client.get(reverse('blog:post_detail', kwargs={'pk': self.post.pk}))
self.assertEqual(resp.status_code, 200)
self.assertContains(resp, 'World')


def test_create_requires_login(self):
resp = self.client.get(reverse('blog:post_create'))
self.assertNotEqual(resp.status_code, 200) # should redirect to login


self.client.login(username='alice', password='password')
resp = self.client.post(reverse('blog:post_create'), {'title': 'New', 'content': 'content'})
self.assertEqual(resp.status_code, 302)
self.assertTrue(Post.objects.filter(title='New').exists())


def test_update_by_author(self):
self.client.login(username='alice', password='password')
resp = self.client.post(reverse('blog:post_update', kwargs={'pk': self.post.pk}), {'title': 'Updated', 'content': 'x'})
self.assertEqual(resp.status_code, 302)
self.post.refresh_from_db()
self.assertEqual(self.post.title, 'Updated')


def test_update_by_other_forbidden(self):
self.client.login(username='bob', password='password')
resp = self.client.get(reverse('blog:post_update', kwargs={'pk': self.post.pk}))
# UserPassesTestMixin redirects to login by default for failing test; assert 403 or redirect
self.assertNotEqual(resp.status_code, 200)


def test_delete_by_author(self):
self.client.login(username='alice', password='password')
resp = self.client.post(reverse('blog:post_delete', kwargs={'pk': self.post.pk}))
self.assertEqual(resp.status_code, 302)
self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())
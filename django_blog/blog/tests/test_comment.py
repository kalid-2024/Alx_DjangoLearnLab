rom django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


from .models import Post, Comment


User = get_user_model()


class CommentTests(TestCase):
def setUp(self):
self.user1 = User.objects.create_user(username='user1', password='pass')
self.user2 = User.objects.create_user(username='user2', password='pass')
self.post = Post.objects.create(title='P', body='B', author=self.user1)


def test_create_comment_authenticated(self):
self.client.login(username='user2', password='pass')
url = reverse('comment-create', kwargs={'post_pk': self.post.pk})
resp = self.client.post(url, {'content': 'Nice post'})
self.assertEqual(resp.status_code, 302)
self.assertEqual(self.post.comments.count(), 1)
comment = self.post.comments.first()
self.assertEqual(comment.author, self.user2)


def test_only_author_can_edit(self):
comment = Comment.objects.create(post=self.post, author=self.user2, content='orig')
self.client.login(username='user1', password='pass')
url = reverse('comment-edit', kwargs={'pk': comment.pk})
resp = self.client.post(url, {'content': 'attempted edit'})
self.assertEqual(resp.status_code, 403)


def test_author_can_delete(self):
comment = Comment.objects.create(post=self.post, author=self.user2, content='orig')
self.client.login(username='user2', password='pass')
url = reverse('comment-delete', kwargs={'pk': comment.pk})
resp = self.client.post(url)
self.assertEqual(resp.status_code, 302)
self.assertEqual(self.post.comments.count(), 0)
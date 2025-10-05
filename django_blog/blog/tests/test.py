from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

class TagSearchTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass')
        self.p1 = Post.objects.create(title='Django tips', slug='django-tips', author=self.user, content='Tips for Django')
        self.p2 = Post.objects.create(title='Flask tutorial', slug='flask-tutorial', author=self.user, content='Flask content')
        self.p1.tags.add('django', 'web')
        self.p2.tags.add('flask')

    def test_search_by_title(self):
        resp = self.client.get('/search/', {'q': 'Django'})
        self.assertContains(resp, 'Django tips')
        self.assertNotContains(resp, 'Flask tutorial')

    def test_search_by_content(self):
        resp = self.client.get('/search/', {'q': 'Flask content'})
        self.assertContains(resp, 'Flask tutorial')

    def test_search_by_tag(self):
        resp = self.client.get('/search/', {'q': 'web'})
        self.assertContains(resp, 'Django tips')

    def test_posts_by_tag_view(self):
        resp = self.client.get('/tags/django/')
        self.assertContains(resp, 'Django tips')
        self.assertNotContains(resp, 'Flask tutorial')


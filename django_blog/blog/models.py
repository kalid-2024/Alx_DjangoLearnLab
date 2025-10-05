from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=CASCADE, related_name="posts")
    # Add tags using django-taggit tags = TaggableManager(blank=True)
    tags = TaggableManager(blank=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return f"{self.title} ({self.author})"

    def get_absolute_url(self): 
        return reverse('post_detail', args=[self.slug])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True)
    def __str__(self):
        return f"{self.user.username} Profile"

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    post = models.ManyToManyField(Post, related_name='custom_tags', blank=True)

    def __str__(self):
        return self.name


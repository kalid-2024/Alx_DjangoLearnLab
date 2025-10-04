from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.
class Post(models.Model):
    tittle = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=CASCADE, related_name="posts")
    def __str__(self):
        return f"{self.title} ({self.author})"
   
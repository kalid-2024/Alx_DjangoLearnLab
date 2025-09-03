from django.db import models

# Create your models here.
class Book:
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.IntegerField()
   
    def __str__(self):
        return self.title

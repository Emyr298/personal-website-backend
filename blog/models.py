from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField()
    categories = models.ManyToManyField(Category)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField()
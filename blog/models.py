from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField()
    edited_at = models.DateTimeField()
    categories = models.ManyToManyField(Category)
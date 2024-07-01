from django.urls import path
from .views import *

app_name = 'blog_medium'

urlpatterns = [
    path('', index_articles, name='index_articles'),
    path('<str:id>', get_article, name='get_article'),
]

from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', func_articles, name='articles'),
    path('<int:id>/', func_article_by_id, name='article_by_id'),
    path('categories/', func_categories, name='categories'),
    path('categories/<int:id>/', func_category_by_id, name='category_by_id'),
]

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
def func_articles(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST' and request.user.is_superuser:
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    return HttpResponse(status=403)

@api_view(['GET', 'PUT', 'DELETE'])
def func_article_by_id(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT' and request.user.is_superuser:
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE' and request.user.is_superuser:
        article.delete()
        return HttpResponse(status=204)
    
    return HttpResponse(status=403)

@api_view(['GET', 'POST'])
def func_article_comments(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if request.method == 'GET':
        comments = Comment.objects.filter(article__id=article.id).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST' and request.user.is_authenticated:
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data, context={'user': request.user, 'article': article})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    return HttpResponse(status=403)

@api_view(['GET', 'PUT', 'DELETE'])
def func_article_comment_by_id(request, article_id, comment_id):
    article = get_object_or_404(Article, id=article_id)
    comment = get_object_or_404(Comment, id=comment_id, article__id=article.id)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT' and comment.user == request.user:
        data = JSONParser().parse(request)
        serializer = CommentSerializer(comment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE' and comment.user == request.user:
        comment.delete()
        return HttpResponse(status=204)
    
    return HttpResponse(status=403)

@api_view(['GET', 'POST'])
def func_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)
        
    elif request.method == 'POST' and request.user.is_superuser:
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def func_category_by_id(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT' and request.user.is_superuser:
        data = JSONParser().parse(request)
        serializer = CategorySerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE' and request.user.is_superuser:
        category.delete()
        return HttpResponse(status=204)
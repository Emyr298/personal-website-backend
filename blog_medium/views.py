from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from blog_medium.logic.medium import get_medium_posts
from blog_medium.serializers import ArticleIndexSerializer, ArticleSerializer

@api_view(['GET'])
def index_articles(request):
    articles = get_medium_posts().values()
    serializer = ArticleIndexSerializer(articles, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def get_article(request, id):
    articles = get_medium_posts()
    if id in articles:
        serializer = ArticleSerializer(articles[id])
        return JsonResponse(serializer.data)
    return HttpResponse(status=404)

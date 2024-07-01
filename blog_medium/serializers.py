from bs4 import BeautifulSoup
from rest_framework import serializers

class ArticleIndexSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    sneak_peek = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    url = serializers.URLField(read_only=True)
    
    def get_sneak_peek(self, obj):
        soup = BeautifulSoup(obj['content'], 'html.parser')
        for fig in soup.find_all('figure'):
            fig.extract()
        original_content = soup.get_text()
        sneak_peek = original_content[:253]
        if len(original_content) > 253:
            return sneak_peek + "..."
        else:
            return sneak_peek

class ArticleSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True)
    content = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    url = serializers.URLField(read_only=True)

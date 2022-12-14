from django.utils import timezone
from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    body = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    edited_at = serializers.DateTimeField(read_only=True)
    categories = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Category.objects.all())
    
    def create(self, validated_data):
        instance = Article()
        instance.title = validated_data.get('title')
        instance.body = validated_data.get('body')
        instance.created_at = timezone.now()
        instance.edited_at = instance.created_at
        instance.save()
        instance.categories.set(validated_data.get('categories'))
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.edited_at = timezone.now()
        instance.categories.set(validated_data.get('categories'))
        instance.save()
        return instance

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    article = serializers.PrimaryKeyRelatedField(read_only=True)
    body = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    edited_at = serializers.DateTimeField(read_only=True)
    
    def create(self, validated_data):
        instance = Comment()
        instance.user = self.context.get('user')
        instance.article = self.context.get('article')
        instance.body = validated_data.get('body')
        instance.created_at = timezone.now()
        instance.edited_at = instance.created_at
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        instance.body = validated_data.get('body')
        instance.edited_at = timezone.now()
        instance.save()
        return instance
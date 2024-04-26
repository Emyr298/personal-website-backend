from .models import *
from rest_framework import serializers

class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = ['name', 'description', 'image_url']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'platform_name', 'platform_image_url', 'url']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'level']

class SkillCategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(source='get_ordered_skills', many=True, read_only=True)
    
    class Meta:
        model = SkillCategory
        fields = ['name', 'skills']

class AffiliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affiliation
        fields = ['id', 'name', 'image_url']

class EducationSerializer(serializers.ModelSerializer):
    affiliation = AffiliationSerializer(read_only=True) 
    
    class Meta:
        model = Education
        fields = ['id', 'degree', 'field', 'start_date', 'end_date', 'affiliation']

class ExperienceSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    affiliation = AffiliationSerializer(read_only=True)
    
    class Meta:
        model = Experience
        fields = ['id', 'position', 'skills', 'affiliation', 'description', 'start_date', 'end_date']

class ExperienceLiteSerializer(serializers.ModelSerializer):
    skills = serializers.SlugRelatedField(source='get_ordered_skills', many=True, read_only=True, slug_field='name')
    
    class Meta:
        model = Experience
        fields = ['id', 'position', 'skills', 'description', 'start_date', 'end_date']

class AffiliationExperienceSerializer(serializers.ModelSerializer):
    positions = ExperienceLiteSerializer(source='get_ordered_positions', many=True, read_only=True)
    
    class Meta:
        model = Affiliation
        fields = ['id', 'name', 'image_url', 'positions']

class ProjectUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUrl
        fields = ['id', 'name', 'url', 'project']

class ProjectSerializer(serializers.ModelSerializer):
    project_urls = ProjectUrlSerializer(many=True, read_only=True)
    skills = serializers.SlugRelatedField(source='get_ordered_skills', many=True, read_only=True, slug_field='name')
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'image_url', 'project_urls', 'skills']

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = ['id', 'name', 'affiliation', 'start_date', 'end_date', 'credential_id']
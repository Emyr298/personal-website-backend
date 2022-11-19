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

class AffiliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affiliation
        fields = ['id', 'name', 'image_url']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'degree', 'field', 'start_date', 'end_date', 'affiliation']

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'position', 'skills', 'affiliation']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description']

class ProjectUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectUrl
        fields = ['id', 'name', 'url', 'project']

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = ['id', 'name', 'affiliation', 'start_date', 'end_date', 'credential_id']
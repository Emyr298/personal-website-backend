from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from django.db.models import F

from commons.permissions import IsAdminUserOrReadOnly, ReadOnly

from .models import *
from .serializers import *

@api_view(['GET', 'POST', 'PUT'])
def func_general(request):
    if request.method == 'GET':
        generalInstance = get_object_or_404(General)
        serializer = GeneralSerializer(generalInstance)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.user.is_superuser:
        if request.method == 'POST' and General.objects.count() == 0:
            data = JSONParser().parse(request)
            serializer = GeneralSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        
        elif request.method == 'PUT':
            generalInstance = get_object_or_404(General)
            data = JSONParser().parse(request)
            serializer = GeneralSerializer(generalInstance, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)
    
    return HttpResponse(status=403)

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class SkillList(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class SkillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class SkillWithCategoryList(generics.ListCreateAPIView):
    queryset = SkillCategory.objects.all().order_by("priority")
    serializer_class = SkillCategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]

class EducationList(generics.ListCreateAPIView):
    queryset = Education.objects.all().order_by(F("end_date").desc(nulls_last=False))
    serializer_class = EducationSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class EducationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ExperienceList(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ExperienceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class AffiliationExperienceList(generics.ListCreateAPIView):
    queryset = Affiliation.objects.filter(
            positions__isnull=False
        ).order_by("name").order_by(
            F('positions__end_date').desc(nulls_first=True),
            F('positions__start_date').desc(nulls_first=True)
        )
    serializer_class = AffiliationExperienceSerializer
    permission_classes = [ReadOnly]
    
    def list(self, request):
        query_set = self.get_queryset()
        affiliation_set = set()
        affiliation_list = []
        for affiliation in query_set:
            if not affiliation.id in affiliation_set:
                affiliation_set.add(affiliation.id)
                affiliation_list.append(affiliation)
        serializer = AffiliationExperienceSerializer(affiliation_list, many=True)
        return JsonResponse(serializer.data, safe=False)

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.order_by("-date").all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ProjectUrlList(generics.ListCreateAPIView):
    queryset = ProjectUrl.objects.all()
    serializer_class = ProjectUrlSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ProjectUrlDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectUrl.objects.all()
    serializer_class = ProjectUrlSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class CertificationList(generics.ListCreateAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class CertificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    permission_classes = [IsAdminUserOrReadOnly]
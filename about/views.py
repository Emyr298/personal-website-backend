from django.shortcuts import render
from django.core import serializers
from commons.utils import ResponseFormatter
from django.forms.models import model_to_dict

from about.models import *

# Create your views here.
def general(request):
    try:
        general = General.objects.get()
    except General.DoesNotExist:
        return ResponseFormatter.error('Instance not found', 404)
    
    response_dict = model_to_dict(general, exclude=('id'))
    return ResponseFormatter.success(response_dict, 200)

def contacts(request):
    contact_list = Contact.objects.all()
    dict_list = list()
    for contact in contact_list:
        cur_dict = model_to_dict(contact)
        dict_list.append(cur_dict)
    return ResponseFormatter.success(dict_list, 200)

def skills(request):
    skill_list = Skill.objects.all()
    dict_list = list()
    for skill in skill_list:
        cur_dict = model_to_dict(skill)
        dict_list.append(cur_dict)
    return ResponseFormatter.success(dict_list, 200)

def educations(request):
    education_list = Education.objects.all()
    dict_list = list()
    for education in education_list:
        cur_dict = model_to_dict(education)
        cur_dict['affiliation'] = model_to_dict(education.affiliation)
        dict_list.append(cur_dict)
    return ResponseFormatter.success(dict_list, 200)

def experience(request):
    experience_list = Experience.objects.all()
    dict_list = list()
    for cur_experience in experience_list:
        cur_dict = model_to_dict(cur_experience)
        cur_dict['affiliation'] = model_to_dict(cur_experience.affiliation)
        dict_list.append(cur_dict)
    return ResponseFormatter.success(dict_list, 200)

def projects(request):
    project_list = Project.objects.all()
    dict_list = list()
    for project in project_list:
        cur_dict = model_to_dict(project)
        
        url_set = project.projecturl_set.all()
        url_list = list()
        for url in url_set:
            url_list.append(model_to_dict(url))
        
        cur_dict['urls'] = url_list
        dict_list.append(cur_dict)
    return ResponseFormatter.success(dict_list, 200)

def certifications(request):
    certification_list = Certification.objects.all()
    dict_list = list()
    for certification in certification_list:
        cur_dict = model_to_dict(certification)
        cur_dict['affiliation'] = model_to_dict(certification.affiliation)
        dict_list.append(cur_dict)
    return ResponseFormatter.success(dict_list, 200)

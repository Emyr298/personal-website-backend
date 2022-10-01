from django.urls import path
from about.views import *

app_name = 'about'

urlpatterns = [
    path('', general, name='general'),
    path('contacts/', contacts, name='contacts'),
    path('skills/', skills, name='skills'),
    path('educations/', educations, name='educations'),
    path('experience/', experience, name='experience'),
    path('projects/', projects, name='projects'),
    path('certifications/', certifications, name='certifications'),
]

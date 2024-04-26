from django.urls import path
from about.views import *

app_name = 'about'

urlpatterns = [
    path('', func_general, name='func_general'),
    path('contacts/', ContactList.as_view(), name='contacts'),
    path('contacts/<int:pk>/', ContactDetail.as_view(), name='contact_by_id'),
    path('skills/', SkillList.as_view(), name='skills'),
    path('skills/<int:pk>/', SkillDetail.as_view(), name='skill_by_id'),
    path('skills/by-category/', SkillWithCategoryList.as_view(), name='skills_by_category'),
    path('educations/', EducationList.as_view(), name='educations'),
    path('educations/<int:pk>/', EducationDetail.as_view(), name='education_by_id'),
    path('experience/', ExperienceList.as_view(), name='experience'),
    path('experience/<int:pk>/', ExperienceDetail.as_view(), name='experience_by_id'),
    path('projects/', ProjectList.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project_by_id'),
    path('certifications/', CertificationList.as_view(), name='certifications'),
    path('certifications/<int:pk>/', CertificationDetail.as_view(), name='certification_by_id'),
    path('affiliations/experience/', AffiliationExperienceList.as_view(), name='affiliation_experience'),
]
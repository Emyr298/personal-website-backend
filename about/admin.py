from django.contrib import admin

from .models import *

class GeneralAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('platform_name', 'url')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')

class AffiliationAdmin(admin.ModelAdmin):
    list_display = ('name',)

class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'field', 'affiliation_name')
    
    @admin.display(ordering='affiliation__name', description='Affiliation')
    def affiliation_name(self, obj):
        return obj.affiliation.name

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'affiliation_name')
    
    @admin.display(ordering='affiliation__name', description='Affiliation')
    def affiliation_name(self, obj):
        return obj.affiliation.name

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class ProjectUrlAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'project_name')
    
    @admin.display(ordering='project__name', description='Project')
    def project_name(self, obj):
        return obj.project.name

class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'affiliation_name', 'start_date', 'end_date', 'credential_id')
    
    @admin.display(ordering='affiliation__name', description='Affiliation')
    def affiliation_name(self, obj):
        return obj.affiliation.name

# Register your models here.
admin.site.register(General, GeneralAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Affiliation, AffiliationAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectUrl, ProjectUrlAdmin)
admin.site.register(Certification, CertificationAdmin)
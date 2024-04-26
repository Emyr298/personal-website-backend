from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import F

# Create your models here.
class General(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.URLField()
    
    def clean(self):
        if General.objects.count() > 0 and self.pk != General.objects.get().pk:
            raise ValidationError('Only 1 instance is allowed')
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    platform_name = models.CharField(max_length=20)
    platform_image_url = models.URLField()
    url = models.URLField()
    
    def __str__(self):
        return self.platform_name

class SkillCategory(models.Model):
    name = models.CharField(max_length=32, primary_key=True)
    priority = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    def get_ordered_skills(self):
        return self.skills.order_by("-level")

class Skill(models.Model):
    MIN_LEVEL = 1
    MAX_LEVEL = 5
    
    name = models.CharField(max_length=20)
    level = models.IntegerField(validators=[MinValueValidator(MIN_LEVEL), MaxValueValidator(MAX_LEVEL)])
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Affiliation(models.Model):
    name = models.CharField(max_length=30)
    image_url = models.URLField()
    
    def __str__(self):
        return self.name
    
    def get_ordered_positions(self):
        return self.positions.order_by(F("end_date").desc(nulls_last=False))

class Education(models.Model):
    degree = models.CharField(max_length=20, null=True)
    field = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.field + " at " + self.affiliation.name

class Experience(models.Model):
    position = models.CharField(max_length=64)
    description = models.TextField(default='')
    skills = models.ManyToManyField(Skill)
    affiliation = models.ForeignKey(Affiliation, related_name='positions', on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.position + " at " + self.affiliation.name
    
    def get_ordered_skills(self):
        return self.skills.order_by("-level")

class Project(models.Model):
    name = models.CharField(max_length=20)
    image_url = models.URLField()
    description = models.TextField()
    skills = models.ManyToManyField(Skill)
    
    def __str__(self):
        return self.name
    
    def get_ordered_skills(self):
        return self.skills.order_by("-level")

class ProjectUrl(models.Model):
    REPOSITORY = "REPO"
    LINK = "LINK"
    URL_TYPE_CHOICES = [
        (REPOSITORY, 'Repository'),
        (LINK, 'Link'),
    ]
    
    name = models.CharField(max_length=20)
    url = models.URLField()
    url_type = models.CharField(max_length=4, choices=URL_TYPE_CHOICES, default=LINK)
    project = models.ForeignKey(Project, related_name='project_urls', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name + " for " + self.project.name

class Certification(models.Model):
    name = models.CharField(max_length=20)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    credential_id = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name + " on " + self.affiliation
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

# References
# https://stackoverflow.com/questions/2138408/limit-number-of-model-instances-to-be-created-django

# Create your models here.
class General(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.URLField()
    
    def clean(self):
        if General.objects.count() > 0 and self.pk != General.objects.get().pk:
            raise ValidationError('Only 1 instance is allowed')

class Contact(models.Model):
    platform_name = models.CharField(max_length=20)
    platform_image_url = models.URLField()
    url = models.URLField()

class Skill(models.Model):
    MIN_LEVEL = 1
    MAX_LEVEL = 5
    
    name = models.CharField(max_length=20)
    level = models.IntegerField(validators=[MinValueValidator(MIN_LEVEL), MaxValueValidator(MAX_LEVEL)])

class Affiliation(models.Model):
    name = models.CharField(max_length=30)
    image_url = models.URLField()

class Education(models.Model):
    degree = models.CharField(max_length=20, null=True)
    field = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.CASCADE)

class Experience(models.Model):
    position = models.CharField(max_length=20)
    skills = models.ManyToManyField(Skill)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.CASCADE)

class Project(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

class ProjectUrl(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Certification(models.Model):
    name = models.CharField(max_length=20)
    affiliation = models.ForeignKey(Affiliation, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    credential_id = models.CharField(max_length=30)
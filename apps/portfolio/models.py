from django.db import models
from ..common.models import TimeStampedModel
from tinymce.models import HTMLField

# Create your models here.
class Project(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = HTMLField()
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_url = models.URLField(blank=True, null=True, verbose_name="GitHub URL")
    live_url = models.URLField(blank=True, null=True, verbose_name="Live Demo URL")
    is_active = models.BooleanField(default=True)
    skills = models.ManyToManyField('Skill', related_name='projects')
    category = models.ForeignKey('ProjectCategory', on_delete=models.CASCADE, related_name='projects')
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

class ProjectCategory(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"

class Skill(TimeStampedModel):
    name = models.CharField(max_length=255)
    proficiency = models.PositiveIntegerField()  # Percentage (0-100)
    icon_class = models.CharField(max_length=255)  # For font-awesome or similar icons
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

class Image(TimeStampedModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project_images/')
    caption = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"
from django.contrib import admin
from .models import Project, ProjectCategory, Skill, Image
from django.contrib.admin import site

# Register your models here.
site.register(Project)
site.register(ProjectCategory)
site.register(Skill)
site.register(Image)
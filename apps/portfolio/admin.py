from django.contrib import admin, site
from .models import Project, ProjectCategory, Skill, Image

# Register your models here.
site.register(Project)
site.register(ProjectCategory)
site.register(Skill)
site.register(Image)
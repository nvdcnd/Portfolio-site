from django.contrib import admin
from .models import Post, PostCategory, Tag
from django.contrib.admin import site

# Register your models here.
site.register(Post)
site.register(PostCategory)
site.register(Tag)
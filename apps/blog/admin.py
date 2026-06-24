from django.contrib import admin, site
from .models import Post, PostCategory, Tag

# Register your models here.
site.register(Post)
site.register(PostCategory)
site.register(Tag)
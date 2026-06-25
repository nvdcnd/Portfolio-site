from django.contrib import admin
from .models import Post, PostCategory, Tag

@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'display_order')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active', 'display_order')
    search_fields = ('name', 'description')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'display_order')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active', 'display_order')
    search_fields = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'is_active', 'display_order', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_active', 'display_order')
    list_filter = ('category', 'tags', 'is_active')
    search_fields = ('title', 'content')
    filter_horizontal = ('tags',)
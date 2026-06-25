from django.contrib import admin
from .models import Project, ProjectCategory, Skill, Image

class ProjectImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('image', 'caption', 'is_active', 'display_order')

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'display_order')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active', 'display_order')
    search_fields = ('name', 'description')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'icon_class', 'is_active', 'display_order')
    list_editable = ('proficiency', 'is_active', 'display_order')
    search_fields = ('name', 'icon_class')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'is_active', 'display_order')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_active', 'display_order')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'short_description', 'description')
    filter_horizontal = ('skills',)
    inlines = [ProjectImageInline]

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('project', 'image', 'caption', 'is_active', 'display_order')
    list_editable = ('is_active', 'display_order')
    list_filter = ('project', 'is_active')
    search_fields = ('caption',)
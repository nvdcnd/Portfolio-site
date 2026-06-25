from django.contrib import admin
from .models import Services, ServiceCategory, Testimonial, FAQ

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'display_order')
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('is_active', 'display_order')
    search_fields = ('name', 'description')

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'featured', 'is_active', 'display_order')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('featured', 'is_active', 'display_order')
    list_filter = ('category', 'featured', 'is_active')
    search_fields = ('title', 'short_description', 'description')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'service', 'is_active', 'display_order')
    list_editable = ('is_active', 'display_order')
    list_filter = ('service', 'is_active')
    search_fields = ('question', 'answer')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'company', 'is_active', 'display_order')
    list_editable = ('is_active', 'display_order')
    list_filter = ('is_active',)
    search_fields = ('name', 'testimonial', 'company')

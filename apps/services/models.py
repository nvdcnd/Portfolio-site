from django.db import models
from ..common.models import TimeStampedModel
from tinymce.models import HTMLField

# Create your models here.
class Services(TimeStampedModel):
    title = models.CharField(max_length=255)
    description = HTMLField()
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    icon_class = models.CharField(max_length=255)  # For font-awesome or similar icons
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='ai_development/')
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey('ServiceCategory', on_delete=models.CASCADE, related_name='services')
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Services"

class ServiceCategory(TimeStampedModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"

class FAQ(TimeStampedModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='faqs')
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

class Testimonial(TimeStampedModel):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    testimonial = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
from django.db import models
from ..common.models import TimeStampedModel
from tinymce.models import HTMLField

# Create your models here.
class Hero(TimeStampedModel):
    avatar = models.ImageField(upload_to='avatars/')
    title = models.TextField()
    subtitle = models.TextField()
    description = HTMLField()
    resume_file = models.FileField(upload_to='resume/')
    background_image = models.ImageField(upload_to='background/')
    cta1_text = models.CharField(max_length=255)
    cta2_text = models.CharField(max_length=255)
    cta1_link = models.URLField()
    cta2_link = models.URLField()
    greeting = models.CharField(max_length=255)
    badge_text = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

class Statistic(TimeStampedModel):
    icon_class = models.CharField(max_length=255)  # For font-awesome or similar icons
    title = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    suffix = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

class Title(TimeStampedModel):
    text = models.CharField(max_length=255)
    organization = models.CharField(max_length=255, blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

class Timeline(TimeStampedModel):
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255, blank=True, null=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    location = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    type = models.CharField(max_length=50, choices=[('education', 'Education'), ('experience', 'Experience')])
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class PublishableModel(TimeStampedModel):
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True

class OrderableModel(TimeStampedModel):
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True

class Footer(TimeStampedModel):
    content = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footers"

class SEOSettings(TimeStampedModel):
    meta_title = models.CharField(max_length=255)
    meta_description = models.TextField()
    meta_keywords = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "SEO Setting"
        verbose_name_plural = "SEO Settings"

class SocialMediaLink(TimeStampedModel):
    platform_name = models.CharField(max_length=255)
    profile_url = models.URLField()
    icon_class = models.CharField(max_length=255)  # For font-awesome or similar icons
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Social Media Link"
        verbose_name_plural = "Social Media Links"

class ContactInfo(TimeStampedModel):
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Infos"

class GeneralSettings(TimeStampedModel):
    site_name = models.CharField(max_length=255)
    site_logo = models.ImageField(upload_to='site_logo/')
    favicon = models.ImageField(upload_to='favicon/')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "General Setting"
        verbose_name_plural = "General Settings"

class AnalyticsSettings(TimeStampedModel):
    google_analytics_id = models.CharField(max_length=255, blank=True, null=True)
    facebook_pixel_id = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Analytics Setting"
        verbose_name_plural = "Analytics Settings"
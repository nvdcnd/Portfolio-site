from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class PublishableModel(models.Model):
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True

class OrderableModel(models.Model):
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
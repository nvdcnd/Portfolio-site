from django.db import models
from ..common.models import TimeStampedModel

class ContactMessage(TimeStampedModel):
    """
    Client inquiries and leads submitted through the contact form.
    """
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"

from django.contrib import admin, site
from .models import Services, ServiceCategory, Testimonial, FAQ

# Register your models here.
site.register(Services)
site.register(ServiceCategory)
site.register(Testimonial)
site.register(FAQ)

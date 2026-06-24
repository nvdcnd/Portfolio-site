from django.contrib import admin
from .models import TimeStampedModel, Hero, Statistic, Title, Timeline
from django.contrib.admin import site

# Register your models here.
site.register(Hero)
site.register(Statistic)
site.register(Title)
site.register(Timeline)

#admin.site.site_header = "Portfolio Site Admin"
#admin.site.site_title = "Portfolio Site Admin Portal"
#admin.site.index_title = "Welcome to Portfolio Site Admin Portal"


from django.contrib import admin
from django.contrib.admin import site
from .models import TimeStampedModel, PublishableModel, OrderableModel, Footer, SEOSettings, SocialMediaLink, ContactInfo, GeneralSettings, AnalyticsSettings  

# Register your models here.
admin.site.site_header = "Portfolio Site Admin"
admin.site.site_title = "Portfolio Site Admin Portal"
admin.site.index_title = "Welcome to Portfolio Site Admin Portal"

#site.register(TimeStampedModel)
#site.register(PublishableModel)
#site.register(OrderableModel)
site.register(Footer)
site.register(SEOSettings)
site.register(SocialMediaLink)
site.register(ContactInfo)
site.register(GeneralSettings)
site.register(AnalyticsSettings)


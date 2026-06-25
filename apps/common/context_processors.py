from .models import GeneralSettings, SEOSettings, Footer, ContactInfo, SocialMediaLink

def global_site_context(request):
    """
    Globally inject site settings, seo data, footer message,
    contact info, and social media links.
    """
    settings = GeneralSettings.objects.filter(is_active=True).order_by('-updated_at').first()
    seo = SEOSettings.objects.filter(is_active=True).order_by('-updated_at').first()
    footer = Footer.objects.filter(is_active=True).order_by('-updated_at').first()
    contact_info = ContactInfo.objects.filter(is_active=True).order_by('-updated_at').first()
    socials = SocialMediaLink.objects.filter(is_active=True).order_by('platform_name')

    return {
        'settings': settings,
        'seo': seo,
        'footer': footer,
        'contact_info': contact_info,
        'socials': socials,
    }

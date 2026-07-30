from django.shortcuts import render

from apps.blog.models import Post
from apps.common.models import (
    ContactInfo,
    Footer,
    GeneralSettings,
    SEOSettings,
    SocialMediaLink,
)
from apps.portfolio.models import Project
from apps.services.models import Services, Testimonial

from .models import Hero, Statistic, Timeline


def home(request):
    hero = Hero.objects.filter(is_active=True).order_by("-updated_at").first()
    settings = GeneralSettings.objects.filter(is_active=True).order_by("-updated_at").first()
    seo = SEOSettings.objects.filter(is_active=True).order_by("-updated_at").first()
    footer = Footer.objects.filter(is_active=True).order_by("-updated_at").first()
    contact_info = ContactInfo.objects.filter(is_active=True).order_by("-updated_at").first()
    socials = SocialMediaLink.objects.filter(is_active=True).order_by("platform_name")

    stats = Statistic.objects.filter(is_active=True).order_by("display_order", "-created_at")
    services = (
        Services.objects.filter(is_active=True, featured=True)
        .select_related("category")
        .order_by("display_order", "-created_at")[:3]
    )
    projects = (
        Project.objects.filter(is_active=True)
        .select_related("category")
        .prefetch_related("skills")
        .order_by("display_order", "-created_at")[:3]
    )
    timeline_items = Timeline.objects.filter(is_active=True).order_by(
        "display_order",
        "-start_date",
        "-end_date",
        "-created_at",
    )
    testimonials = Testimonial.objects.filter(is_active=True).order_by(
        "display_order",
        "-created_at",
    )[:3]
    posts = (
        Post.objects.filter(is_active=True)
        .select_related("category")
        .prefetch_related("tags")
        .order_by("-created_at")[:3]
    )

    return render(
        request,
        "pages/home.html",
        {
            "settings": settings,
            "seo": seo,
            "footer": footer,
            "contact_info": contact_info,
            "socials": socials,
            "hero": hero,
            "stats": stats,
            "services": services,
            "projects": projects,
            "timeline_items": timeline_items,
            "testimonials": testimonials,
            "posts": posts,
        },
    )


index = home

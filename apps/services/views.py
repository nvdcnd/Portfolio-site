from django.shortcuts import render, get_object_or_404
from .models import Services, ServiceCategory, Testimonial, FAQ

def index(request):
    """
    List all active services grouped by category.
    """
    categories = ServiceCategory.objects.filter(is_active=True).order_by('display_order', 'name')
    services = Services.objects.filter(is_active=True).select_related('category').order_by(
        'category__display_order', 'display_order', '-created_at'
    )
    return render(request, 'pages/services.html', {
        'categories': categories,
        'services': services
    })

def detail(request, slug):
    """
    Detailed service page including related FAQs and testimonials.
    """
    service = get_object_or_404(Services, slug=slug, is_active=True)
    faqs = service.faqs.filter(is_active=True).order_by('display_order', '-created_at')
    # Filter testimonials matching service title in testimonial title / company / role
    testimonials = Testimonial.objects.filter(
        is_active=True,
        testimonial__icontains=service.title
    ).order_by('display_order', '-created_at')[:3]
    
    # Fallback to general testimonials if none matched
    if not testimonials.exists():
        testimonials = Testimonial.objects.filter(is_active=True).order_by('display_order', '-created_at')[:3]
        
    return render(request, 'pages/service_detail.html', {
        'service': service,
        'faqs': faqs,
        'testimonials': testimonials
    })

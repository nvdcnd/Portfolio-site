from django.shortcuts import render, get_object_or_404
from .models import Project, ProjectCategory, Image

def index(request):
    """
    List all active projects with pre-fetched skills and categories.
    """
    categories = ProjectCategory.objects.filter(is_active=True).order_by('display_order', 'name')
    projects = Project.objects.filter(is_active=True).select_related('category').prefetch_related('skills').order_by(
        'display_order', '-created_at'
    )
    return render(request, 'pages/portfolio.html', {
        'categories': categories,
        'projects': projects
    })

def detail(request, slug):
    """
    Case study details for a single project.
    """
    project = get_object_or_404(Project.objects.prefetch_related('skills'), slug=slug, is_active=True)
    images = project.images.filter(is_active=True).order_by('display_order', '-created_at')
    related_projects = Project.objects.filter(
        category=project.category, is_active=True
    ).exclude(id=project.id).prefetch_related('skills').order_by('display_order', '-created_at')[:2]
    
    return render(request, 'pages/project_detail.html', {
        'project': project,
        'images': images,
        'related_projects': related_projects
    })

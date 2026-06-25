from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post, PostCategory

def index(request):
    """
    List active blog posts with support for search query 'q',
    category filtration, and standard pagination.
    """
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    
    posts = Post.objects.filter(is_active=True).select_related('category').prefetch_related('tags')
    
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    if category_slug:
        posts = posts.filter(category__slug=category_slug)
        
    posts = posts.order_by('display_order', '-created_at')
    
    paginator = Paginator(posts, 9)
    page = request.GET.get('page')
    paginated_posts = paginator.get_page(page)
    
    categories = PostCategory.objects.filter(is_active=True).order_by('display_order', 'name')
    recent_posts = Post.objects.filter(is_active=True).order_by('-created_at')[:5]
    
    return render(request, 'pages/blog.html', {
        'posts': paginated_posts,
        'categories': categories,
        'recent_posts': recent_posts,
        'search_query': query,
        'category_slug': category_slug,
    })

def detail(request, slug):
    """
    Display a single article in detail and query related reading material.
    """
    post = get_object_or_404(Post.objects.prefetch_related('tags'), slug=slug, is_active=True)
    
    # Query 3 related posts based on matching category or tags
    related_posts = Post.objects.filter(is_active=True).filter(
        Q(category=post.category) | Q(tags__in=post.tags.all())
    ).exclude(id=post.id).distinct().order_by('-created_at')[:3]
    
    return render(request, 'pages/blog_detail.html', {
        'post': post,
        'related_posts': related_posts
    })

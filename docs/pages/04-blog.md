---
title: Blog Page Specification
version: 1.0.0
status: Stable
---

# Purpose

This document specifies the template structures, routing, and search queries for the Blog index and Article detail pages.

It guides developers and AI agents in rendering the blog feed, search functions, post tag lists, and related reading lists.

Following this spec ensures standard SEO readability and highly indexable text content for search and AI engine queries.



# Blog Index Page (`/blog/`)

The blog index page shows a feed of technical articles, supporting text search and category filtration.

Template

```
templates/pages/blog.html
```

Context Variables

- `categories` (queryset of active PostCategory records)

- `posts` (paginated queryset of active Post records, pre-fetching tags)

- `recent_posts` (queryset of 5 latest posts)

- `search_query` (String parameter captured from search input)

Layout & Structure

- Header: Breadcrumb (Home > Blog).

- Section Title: "Technical Blog" (introductory text emphasizing backend architecture, AI research, and mentoring).

- Search & Filter Row: Horizontal form containing text input search bar and category dropdown selector.

- Blog Feed Grid: Loop and render `templates/components/blog_card.html` within a 3-column layout.

- Sidebar (Optional / Desktop): Recent posts list and category cloud.

- Pagination: Standard pagination controls (`?page=2`).



# Article Detail Page (`/blog/<slug>/`)

The detail page displays the full rich-text content of a single blog post.

Template

```
templates/pages/blog_detail.html
```

Context Variables

- `post` (single active Post instance matching slug)

- `related_posts` (queryset of 3 related posts based on matching tags or category)

Layout & Structure

- Article Header:
  - Title (H1)
  - Meta info: Category badge, publish date (`created_at` formatted), reading time, and author.
- Article Content Wrapper:
  - Rich text content rendered with raw HTML filter: `{{ post.content|safe }}`.
  - Standard typography rules applied (clean margins, code highlighting).
- Article Footer:
  - Tags list (`#Python`, `#Django`).
  - Share buttons (LinkedIn, Facebook, copy link).
- Related Reading: Row of 3 blog cards at the very bottom.



# Database Views Query Logic

```python
# apps/blog/views.py

def blog_index(request):
    query = request.GET.get('q', '')
    category_slug = request.GET.get('category', '')
    
    posts = Post.objects.filter(is_active=True).select_related('category')
    
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    if category_slug:
        posts = posts.filter(category__slug=category_slug)
        
    paginator = Paginator(posts.order_by('-created_at'), 9)
    page = request.GET.get('page')
    paginated_posts = paginator.get_page(page)
    
    return render(request, 'pages/blog.html', {
        'posts': paginated_posts,
        'query': query
    })
```



# SEO & AI Optimization

- The title tag must map to: `[Article Title] | Blog | Hoàng Hùng Anh`.

- Inject a TechArticle JSON-LD schema containing author profile, dates, and keywords.

- Article content headings inside TinyMCE must use `<h2>` and `<h3>` tags (no `<h1>` inside content).

- Code blocks must use semantic `<pre><code>` tags with correct language classes for parser understanding.



# Definition of Done for Blog Page

✓ Text search filters the post feed accurately.

✓ Rich-text article content renders safely without escaping HTML tags.

✓ Metadata (date, category, read time) displays correctly.

✓ TechArticle schema validates without warnings.

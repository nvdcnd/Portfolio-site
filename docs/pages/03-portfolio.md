---
title: Portfolio Page Specification
version: 1.0.0
status: Stable
---

# Purpose

This document specifies the page layouts, context variables, and template structures for the Portfolio index and Project Detail (Case Study) pages.

It guides developers and AI agents in rendering the developer's work, tech stacks, and screenshots.

Following this spec ensures a high-performing showcase that proves engineering capability to technical recruiters and clients.



# Portfolio Index Page (`/portfolio/`)

The portfolio index page lists all past projects, supporting interactive filter controls.

Template

```
templates/pages/portfolio.html
```

Context Variables

- `categories` (queryset of active ProjectCategory records)

- `projects` (queryset of active Project records, pre-fetching tags/skills)

Layout & Structure

- Header: Breadcrumb (Home > Portfolio).

- Section Title: "Project Showcase" (brief copy summarizing the developer's scale of work).

- Filter Navigation: Category badge tabs (e.g. All, Web Apps, AI Tools).

- Project Grid: 3-column responsive layout rendering `templates/components/project_card.html`.

- Pagination: Bootstrap pagination controls (if projects count exceeds 9).



# Project Detail (Case Study) Page (`/portfolio/<slug>/`)

The case study page goes in-depth into a single project, highlighting the problem, solution, architecture, and results.

Template

```
templates/pages/project_detail.html
```

Context Variables

- `project` (single active Project instance matching slug)

- `images` (queryset of active Image records related to this project)

- `skills` (queryset of active Skill records used in the project)

Layout & Structure

- Page Hero: Banner containing Project title, category, links to live demo and source repository.

- Grid Split (Desktop):
  - Left Column (8 cols): Main case study description (rendered from HTMLField: Problem, Architecture, Outcome) + Project detailed Image Gallery.
  - Right Column (4 cols): Meta details sidebar (Client, Timeline, Role, Tech Stack badges).

- Image Gallery: CSS lightbox or responsive carousel showing additional project screenshots (with captions).

- Related Projects: Row of 2 project cards from the same category at the bottom.



# Database Views Query Logic

```python
# apps/portfolio/views.py

def project_detail(request, slug):
    project = get_object_or_404(Project.objects.prefetch_related('skills'), slug=slug, is_active=True)
    images = project.images.filter(is_active=True).order_by('display_order')
    related_projects = Project.objects.filter(category=project.category, is_active=True).exclude(id=project.id)[:2]
    return render(request, 'pages/project_detail.html', {
        'project': project,
        'images': images,
        'related_projects': related_projects
    })
```



# SEO & AI Optimization

- The title tag must map to: `[Project Title] | Portfolio | Hoàng Hùng Anh`.

- Project images must use descriptive alt texts (e.g. "[Project Name] architecture diagram").

- Inject JSON-LD CreativeWork schema to highlight coding projects and tech stacks.

- Use standard headers (`<h2>` for Problem, `<h2>` for Solution).



# Definition of Done for Portfolio Page

✓ Category tab filters project lists correctly.

✓ Project detail page maps live demo and repository links.

✓ Gallery images use lazy loading and expand in a lightbox.

✓ Responsive layouts are pixel-perfect on mobile and desktop.

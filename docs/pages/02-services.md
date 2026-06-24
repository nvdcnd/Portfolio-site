---
title: Services Page Specification
version: 1.0.0
status: Stable
---

# Purpose

This document specifies the page structures and parameters for the Services directory and Service detail pages.

It details how to represent individual offerings (Software Dev, Mentoring, Consulting) and how FAQs and Testimonials are bound to these offerings.

Following this guide ensures high conversion rates and clean structured data for service packages.



# Services Index Page (`/services/`)

The services index page lists all available services grouped by category.

Template

```
templates/pages/services.html
```

Context Variables

- `categories` (queryset of active ServiceCategory records)

- `services` (queryset of active Services records, sorted by category and display_order)

Layout & Structure

- Header: Breadcrumb navigation (Home > Services).

- Section Title: "My Services" (introductory copy explaining consulting, dev, and coaching).

- Categories Filter Tabs: Filter services dynamically using Bootstrap tab-panes.

- Services Grid: Loop and render `templates/components/service_card.html` within a 3-column grid.

- Bottom CTA: Banner driving conversion to Contact Page.



# Service Detail Page (`/services/<slug>/`)

The service detail page provides deep technical specs, target audiences, pricing details (if any), FAQs, and specific testimonials.

Template

```
templates/pages/service_detail.html
```

Context Variables

- `service` (single active Services instance matching slug)

- `faqs` (queryset of active FAQ records related to this service)

- `testimonials` (queryset of active Testimonial records associated with the service or company)

Layout & Structure

- Header Hero: Banner with title, category, and primary CTA ("Book Consultation" or "Inquire").

- Grid Split (Desktop):
  - Left Column (8 cols): Service description (rich text TinyMCE content) + FAQ Accordion.
  - Right Column (4 cols): Sidebar with key highlights, tools used, contact info, and pricing badge.

- FAQ Accordion: Bootstrap Accordion component rendering FAQs related specifically to the service.

- Testimonials Grid: Showcase 2-3 testimonials from clients who purchased this specific service category.



# Database Views Query Logic

```python
# apps/services/views.py

def service_detail(request, slug):
    service = get_object_or_400(Services, slug=slug, is_active=True)
    faqs = service.faqs.filter(is_active=True).order_by('display_order')
    testimonials = Testimonial.objects.filter(is_active=True, title__icontains=service.title)[:3]
    return render(request, 'pages/service_detail.html', {
        'service': service,
        'faqs': faqs,
        'testimonials': testimonials
    })
```



# SEO & AI Optimization

- The title tag must map to: `[Service Name] | Services | Hoàng Hùng Anh`.

- Inject a ProfessionalService Schema block containing pricing, service descriptions, and FAQs to capture rich Google snippets.

- Detail headers must use semantic structure (`<h2>` for Description, `<h2>` for FAQs).



# Definition of Done for Services Page

✓ Detailed service page matches standard responsive layout.

✓ Tab filters switch instantly without page reload.

✓ FAQ accordion expands and collapses cleanly.

✓ Schema markup passes validation checks.

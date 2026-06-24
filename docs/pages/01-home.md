---
title: Home Page Specification
version: 1.0.0
status: Stable
---

# Purpose

This document specifies the layout, data requirements, and component assembly of the website's Homepage.

It guides the backend developer and AI coding agent in writing the view query and assembling the templates.

It defines the exact ordering of elements to maintain brand trust and maximize user conversion.



# Page Context Variables

The homepage view (`apps.core.views.home`) must pass the following data context to the template:

- `settings` (apps.common.models.GeneralSettings, active instance)

- `socials` (apps.common.models.SocialMediaLink, queryset of active records)

- `hero` (apps.core.models.Hero, active instance)

- `stats` (apps.core.models.Statistic, queryset of active records, sorted by display_order)

- `services` (apps.services.models.Services, queryset of active featured records, sorted by display_order)

- `projects` (apps.portfolio.models.Project, queryset of active featured records, sorted by display_order)

- `timeline_items` (apps.core.models.Timeline, queryset of active records, sorted by display_order)

- `testimonials` (apps.services.models.Testimonial, queryset of active records, sorted by display_order)

- `posts` (apps.blog.models.Post, queryset of active records, sliced to latest 3, sorted by created_at desc)



# Section Assembly Order

The homepage template (`templates/pages/home.html`) must assemble components in this exact order:

Section 1: Global Navigation

- Render: `templates/components/navbar.html`

Section 2: Hero Section

- Render: `templates/components/hero.html`

Section 3: Statistics

- Render: `templates/components/stat_card.html` (inside a grid wrapper)

Section 4: Featured Services

- Render: `templates/components/section_title.html` (Badge: "What I Do", Title: "Services", Description: "Freelance dev...")

- Render: `templates/components/service_card.html` (inside grid)

Section 5: Featured Projects

- Render: `templates/components/section_title.html` (Badge: "My Work", Title: "Featured Projects", Description: "Case studies...")

- Render: `templates/components/project_card.html` (inside grid)

Section 6: Timeline (Career & Education)

- Render: `templates/components/section_title.html` (Badge: "My Journey", Title: "Education & Experience", Description: "Work history...")

- Render: `templates/components/timeline_item.html` (inside vertical container)

Section 7: Testimonials

- Render: `templates/components/section_title.html` (Badge: "Client Reviews", Title: "What People Say", Description: "Feedback...")

- Render: `templates/components/testimonial_card.html` (inside grid)

Section 8: Latest Articles

- Render: `templates/components/section_title.html` (Badge: "Writing", Title: "Latest Articles", Description: "Technical blogs...")

- Render: `templates/components/blog_card.html` (inside grid)

Section 9: Call to Action Banner

- Render: `templates/components/cta_banner.html`

Section 10: Global Footer

- Render: `templates/components/footer.html`



# SEO & AI Optimization

- The Homepage must contain exactly one `<h1>` tag (located inside the Hero title).

- All section titles must use `<h2>` tags.

- Meta tags must be populated from the `SEOSettings` model.

- Include JSON-LD Person schema in the head block.



# Definition of Done for Homepage

✓ All queries filter by `is_active=True`.

✓ Page loads in less than 1.5 seconds.

✓ Standard Bootstrap responsive breakpoints verified.

✓ Accessibility standards checked (WCAG AA).

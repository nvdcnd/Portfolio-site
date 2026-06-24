---
title: Project Card Component
component: ProjectCard
version: 1.0.0
status: Stable
---

# Purpose

The Project Card showcases a single portfolio project on the homepage or portfolio archive.

It displays the cover image, title, summary, technology stack badges, and action buttons.

It highlights technical expertise and results to build developer credibility.



# Business Goal

The Project Card should:

- Show potential clients or employers the quality and scale of past projects.

- Showcase specific toolsets and frameworks used (e.g. Django, React, PostgreSQL).

- Drive visitors to read the full case study or visit the live application.

- Build trust by providing transparent access to source code (GitHub) and live demos.



# User Goal

Users should easily:

- See a visual preview of the project.

- Filter projects by technology stack or category.

- Understand the developer's role and contribution to the project.

- Check the live demo or inspect the code repository.



# Database Mapping

Data Source

- apps.portfolio.models.Project

- apps.portfolio.models.Skill

- apps.portfolio.models.ProjectCategory

Fields Used

- Project: `title`, `short_description`, `image` (cover), `slug`, `skills` (ManyToMany to Skill), `category` (FK to ProjectCategory)

- Skill: `name`, `icon_class`

- ProjectCategory: `name`

Future / Custom Fields (to be added)

- `github_url` (Link to repository)

- `demo_url` (Link to live application)



# Template Mapping

Template

```
templates/components/project_card.html
```

CSS

```
static/css/components/cards.css
```

JavaScript

None.



# Component Structure

```
Project Card
├── Image Area
│   └── Cover Image (Lazy Loaded)
└── Content Area
    ├── Category & Meta
    ├── Title (H3)
    ├── Short Description
    ├── Tech Stack (Skills Badges)
    └── Button Group
        ├── Primary: View Details / Case Study
        ├── Icon Link: GitHub (Optional)
        └── Icon Link: Live Demo (Optional)
```



# Layout

Standard Layout

```
--------------------------------------------
 |                                        |
 |              Cover Image               |
 |________________________________________|
 
  [Category Badge]
  
  Project Title
  Short project description outlining the problem
  and solution in 2-3 sentences.
  
  [Python] [Django] [PostgreSQL] [Bootstrap]
  
  View Case Study      [GitHub]  [Live Demo]
--------------------------------------------
```



# Bootstrap Layout

Preferred Structure

```
<article class="card project-card h-100 border-0 shadow-sm overflow-hidden">

    <div class="project-img-wrapper position-relative overflow-hidden">

        <img src="{{ project.image.url }}" alt="{{ project.title }} preview" class="card-img-top img-fluid" loading="lazy">

        <span class="badge bg-primary text-white position-absolute top-3 start-3 rounded-pill px-3 py-2">

            {{ project.category.name }}

        </span>

    </div>

    <div class="card-body p-4 d-flex flex-column h-100">

        <h3 class="card-title h4 font-heading fw-semibold text-dark mb-2">

            {{ project.title }}

        </h3>

        <p class="card-text text-secondary mb-4 flex-grow-1">

            {{ project.short_description }}

        </p>

        <!-- Tech Stack Badges -->

        <div class="tech-stack-wrapper d-flex flex-wrap gap-2 mb-4">

            {% for skill in project.skills.all|dictsort:"display_order" %}

                <span class="badge bg-light text-secondary border border-light-subtle rounded-pill px-2 py-1 fs-8">

                    {% if skill.icon_class %}<i class="{{ skill.icon_class }} me-1"></i>{% endif %}

                    {{ skill.name }}

                </span>

            {% endfor %}

        </div>

        <!-- Button Group -->

        <div class="mt-auto d-flex align-items-center justify-content-between">

            <a href="{% url 'portfolio:detail' project.slug %}" class="btn btn-outline-primary btn-sm rounded-3 px-3 py-2">

                View Details

            </a>

            <div class="d-flex align-items-center gap-2">

                {% if project.github_url %}

                    <a href="{{ project.github_url }}" class="btn btn-link text-secondary p-2" target="_blank" rel="noopener noreferrer" aria-label="GitHub Repository for {{ project.title }}">

                        <i class="bi bi-github fs-5"></i>

                    </a>

                {% endif %}

                {% if project.demo_url %}

                    <a href="{{ project.demo_url }}" class="btn btn-link text-secondary p-2" target="_blank" rel="noopener noreferrer" aria-label="Live Demo of {{ project.title }}">

                        <i class="bi bi-box-arrow-up-right fs-5"></i>

                    </a>

                {% endif %}

            </div>

        </div>

    </div>

</article>
```



# Styling

Card Wrapper

- Background: White `#FFFFFF`

- Border: Slate Border `#E2E8F0` (1px, solid)

- Border Radius: 16px

- Elevation: Subtle shadow

- Hover State: Elevation shadow intensifies, image scales up slightly (`scale(1.05)`) within its container.

Image Container

- Ratio: 16:9 aspect-ratio

- Overflow: Hidden

- Hover Transition: `transition: transform 0.3s ease-in-out`

Tech Badges

- Background: Slate `#F1F5F9` (or Light `#F8FAFC`)

- Border: Subtle Gray `#E2E8F0`

- Text Color: Slate `#475569`

Buttons

- Primary Button: Secondary outline style (`btn btn-outline-primary`, 12px border radius)

- Icon buttons: Ghost link buttons (`btn-link`), changing color to Royal Blue on hover.



# Typography

Heading Font

- Plus Jakarta Sans (H3 / 20px)

Body Font

- Inter (15px)

Badges Font

- JetBrains Mono (12px / Monospace)

Line Height

- Heading: 1.3

- Body: 1.6



# Responsive Rules

Desktop Grid

- Grid layout matching standard 3-column (`col-lg-4`) or 2-column if featured (`col-lg-6`).

Tablet

- 2 columns (`col-md-6`).

Mobile

- 1 column (`col-12`).

- Cover image occupies full width, text content stacks directly below.

- Buttons expand or fill width if needed.



# Accessibility

Semantic HTML

- Enclosed in an `<article>` tag.

- Title should be H3.

Keyboard Navigation

- Focus order: Image area (if linked) -> Details Button -> GitHub icon -> Demo icon.

- Hover and active outline styling must be visible.

Aria Attributes

- Cover image must contain custom `alt` descriptions, not generic names.

- Icons must use `aria-hidden="true"`.

- Icon buttons must include descriptive `aria-label` defining target location.



# SEO

- Images must include SEO-friendly alt tags (e.g. "[Project Name] Dashboard Showcase").

- Anchor links must lead to crawlable paths.

- Text headings must include targeted keywords (e.g. "Django E-commerce Platform").



# AI Optimization

- The listing of tech stacks in individual badges represents a semantic semantic relationship (Software Project -> uses Technology).

- Descriptions should contain keyword statements describing the system architecture (e.g., REST API, microservices) to assist AI parsers.



# Performance

- Cover image must be compressed and formatted in WebP.

- Lazy loading (`loading="lazy"`) is mandatory.

- Do not use Javascript transitions. Use CSS variables and transitions.



# Do

✓ Crop project images to a consistent 16:9 ratio

✓ Show technology badges sorted by logical order

✓ Keep the short description focused on outcomes

✓ Ensure equal height grid cards (`h-100`)

✓ Use clean alt attributes for images



# Don't

✗ Link to broken repository links

✗ Load heavy raw images (keep images under 250KB)

✗ Include decorative text that adds zero value

✗ Add more than 6 tech badges in the card (overflow wrap is messy)

✗ Style each card with custom unique borders or background colors



# Definition of Done

✓ Database Driven (Project model)

✓ Responsive grid alignment

✓ Semantic HTML structure

✓ Bootstrap card based

✓ Accessible (aria-labels, contrast validation)

✓ SEO crawlable links

✓ AI optimized markup (keywords, technical stack tags)

✓ Performance optimized (lazy-loaded WebP images)

✓ Reusable template

✓ Production ready

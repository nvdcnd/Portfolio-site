---
title: Service Card Component
component: ServiceCard
version: 1.0.0
status: Stable
---

# Purpose

The Service Card displays a single service offering on the homepage grid or services directory.

It outlines what Hoàng Hùng Anh offers (Freelance Dev, Mentoring, Consulting) in a clean, legible format.

It acts as a gateway to the detailed service details page.



# Business Goal

The Service Card should:

- Educate prospective clients or students about specific services.

- Drive visitors to learn more or contact Hoàng Hùng Anh for inquiries.

- Build trust by showcasing specific technical capabilities.

- Highlight featured services to optimize conversion rates.



# User Goal

Users should easily:

- Skim through the list of services within seconds.

- Understand what each service entails from its short summary.

- Click through to see full descriptions, FAQs, and testimonials.



# Database Mapping

Data Source

- apps.services.models.Services

Fields Used

- `title` (service heading)

- `short_description` (concise 2-3 sentence overview)

- `icon_class` (Bootstrap Icon name, e.g. `bi-code-slash`)

- `slug` (url path for the service detail page)

- `featured` (Boolean to apply featured highlight style)

- `category` (ServiceCategory name)



# Template Mapping

Template

```
templates/components/service_card.html
```

CSS

```
static/css/components/cards.css
```

JavaScript

None.



# Component Structure

```
Service Card
├── Category Badge
├── Icon Container
│   └── Bootstrap Icon
├── Title (H3)
├── Short Description
└── Text Link ("Learn More" with Arrow)
```



# Layout

Standard Card (Default)

```
--------------------------------------------
 [Category Badge]
 [Icon: bi-code-slash]

 Service Title
 Short description of the service offering.
 
 Learn More ->
--------------------------------------------
```

Featured Card (Highlighted Accent Border)

- Card receives a subtle Royal Blue top border or background elevation to indicate importance.



# Bootstrap Layout

Preferred Structure

```
<div class="card service-card h-100 border-0 shadow-sm p-4 {% if service.featured %}border-top border-primary border-4{% endif %}">

    <div class="card-body p-0 d-flex flex-column h-100">

        <div class="d-flex justify-content-between align-items-center mb-3">

            <div class="icon-wrapper bg-light text-primary rounded-3 p-3 d-inline-flex">

                <i class="bi {{ service.icon_class }} fs-4"></i>

            </div>

            <span class="badge bg-secondary-subtle text-secondary fs-8 rounded-pill px-3 py-1">

                {{ service.category.name }}

            </span>

        </div>

        <h3 class="card-title h4 font-heading fw-semibold text-dark mb-2">

            {{ service.title }}

        </h3>

        <p class="card-text text-secondary mb-4 flex-grow-1">

            {{ service.short_description }}

        </p>

        <div class="mt-auto">

            <a href="{% url 'services:detail' service.slug %}" class="btn-text text-primary fw-semibold d-inline-flex align-items-center gap-2">

                Learn More

                <i class="bi bi-arrow-right"></i>

            </a>

        </div>

    </div>

</div>
```



# Styling

Card Wrapper

- Background: White `#FFFFFF`

- Border: Slate Border `#E2E8F0` (1px, solid)

- Border Radius: 16px

- Padding: 32px (p-4)

- Hover State: Subtle translation up (`translateY(-4px)`) and slightly deeper shadow.

Icon Wrapper

- Background: Very Light Surface `#F8FAFC`

- Icon Color: Royal Blue `#2563EB`

- Border Radius: 12px

Title

- Color: Navy `#0F172A`

- Font weight: 600

Description

- Color: Secondary Slate `#64748B`

- Font-size: 15px

Action Link

- Style: Text button (accent color, no underline by default)

- Underline appears on hover, arrow slides 4px to the right.



# Typography

Heading Font

- Plus Jakarta Sans (H3 / 20px)

Body Font

- Inter (15px / Regular)

Line Height

- Heading: 1.3

- Body: 1.6



# Responsive Rules

Grid Layout (Desktop)

- Services should align to a 3-column Bootstrap Grid (`col-lg-4`).

Tablet

- 2 columns (`col-md-6`).

Mobile

- 1 column (`col-12`).

- Cards stretch to match equal height (`h-100` class on the card wrapper).



# Accessibility

Semantic HTML

- Enclosed in an `<article>` tag.

- Title must be `<h3 class="h4">` or `<h4>` depending on layout level.

Keyboard Navigation

- Action link must be reachable via TAB key and show a visible outline.

Aria Attributes

- Icons are purely decorative and must have `aria-hidden="true"`.

- Link must use `aria-label` if the page contains multiple generic "Learn More" links.

Example: `aria-label="Learn more about {{ service.title }}"`.



# SEO

- Anchor links must contain actual URLs (never generic hashtags `#`).

- Link texts must include the service name for search engines to crawl details correctly.



# AI Optimization

- Schema.org markup is reinforced by simple fields.

- The short description clearly describes what the service delivers.

- The category badge helps categorize service entity types.



# Performance

- Cards must not load giant images.

- Icons must use vector SVGs (Bootstrap Icons) instead of pixel graphics.

- Card translations should use CSS hardware-accelerated transforms (`transform: translateY()`).



# Do

✓ Keep description lengths consistent

✓ Highlight one featured service to direct attention

✓ Provide unique aria-label values for links

✓ Use standard Bootstrap Icons

✓ Enable `h-100` on the card to ensure all cards in the row have equal height



# Don't

✗ Use multiple different icon sets in the same grid

✗ Put massive blocks of text in the description

✗ Use bright glowing neon borders for featured cards

✗ Hardcode links (always use Django `{% url %}`)

✗ Add separate download buttons or secondary CTAs inside the card



# Definition of Done

✓ Database Driven (Services model)

✓ Responsive grid alignment

✓ Semantic HTML structure

✓ Bootstrap card based

✓ Accessible (unique aria-labels, high contrast)

✓ SEO crawlable links

✓ AI optimized markup

✓ Performance optimized

✓ Reusable template

✓ Production ready

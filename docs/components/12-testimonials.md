---
title: Testimonial Card Component
component: TestimonialCard
version: 1.0.0
status: Stable
---

# Purpose

The Testimonial Card displays quotes and reviews from clients, colleagues, or students.

It provides powerful social proof that validates Hoàng Hùng Anh's skills and delivery quality.

It helps convert skeptical visitors into active leads.



# Business Goal

The Testimonial Card should:

- Establish trustworthiness and professional capability.

- Address objections regarding capability, communication, and speed.

- Showcase successful outcomes (scholarships won, systems successfully delivered).

- Promote mentoring and freelance services through direct recommendations.



# User Goal

Users should easily:

- Read opinions of real people who worked with Hoàng Hùng Anh.

- Assess the developer's soft skills, professionalism, and integrity.

- Verify credentials through the reviewer's professional title/company.



# Database Mapping

Data Source

- apps.services.models.Testimonial

Fields Used

- `name` (reviewer's name)

- `title` (reviewer's professional role, e.g. Co-founder, Mentee)

- `company` (reviewer's organization, optional)

- `testimonial` (review quote content text)

- `image` (avatar/headshot of reviewer)

- `display_order` (sorting order)



# Template Mapping

Template

```
templates/components/testimonial_card.html
```

CSS

```
static/css/components/cards.css
```

JavaScript

None (cards display in a clean grid instead of layout-shifting carousels).



# Component Structure

```
Testimonial Card
├── Quote Icon (Subtle)
├── Review Text / Quote (Paragraph)
└── Reviewer Details (Footer)
    ├── Avatar Image
    └── Text Metadata
        ├── Reviewer Name (SemiBold)
        └── Title & Company (Muted)
```



# Layout

Standard Card Grid Layout

- Renders inside equal-height columns.

```
--------------------------------------------
  "Hoàng Hùng Anh delivered the project on
  time and exceeded our expectations. Highly
  recommended for backend development."
  
  [Avatar]  Hoàng Hùng Anh
            Software Engineer at Google
--------------------------------------------
```



# Bootstrap Layout

Preferred Structure

```
<article class="card testimonial-card h-100 border-0 shadow-sm p-4">

    <div class="card-body p-0 d-flex flex-column h-100">

        <!-- Quote Icon (Subtle) -->

        <div class="quote-icon text-light-emphasis mb-3">

            <i class="bi bi-quote fs-2 text-primary opacity-25"></i>

        </div>

        <!-- Testimonial Text -->

        <blockquote class="blockquote flex-grow-1 mb-4">

            <p class="fs-6 text-secondary font-body fst-italic">

                "{{ testimonial.testimonial }}"

            </p>

        </blockquote>

        <!-- Reviewer Info -->

        <div class="reviewer-info d-flex align-items-center gap-3 mt-auto pt-3 border-top border-light-subtle">

            {% if testimonial.image %}

                <img src="{{ testimonial.image.url }}" alt="{{ testimonial.name }} headshot" class="rounded-circle img-fluid" style="width: 48px; height: 48px; object-fit: cover;" loading="lazy">

            {% else %}

                <div class="avatar-placeholder rounded-circle bg-light text-secondary d-flex align-items-center justify-content-center fw-bold" style="width: 48px; height: 48px;">

                    {{ testimonial.name|slice:":1" }}

                </div>

            {% endif %}

            <div>

                <h4 class="h6 font-heading fw-semibold text-dark mb-0">

                    {{ testimonial.name }}

                </h4>

                <span class="fs-8 text-secondary">

                    {{ testimonial.title }}{% if testimonial.company %}, {{ testimonial.company }}{% endif %}

                </span>

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

- Padding: 32px (p-4)

- Elevation: Light subtle shadow

Avatar

- Layout: Perfect circle, 48px width and height

- Border: Subtle white ring to separate from card bg

Quote Text

- Style: Italicized, muted text `#475569`

- Font size: 15px

Divider

- Border: Muted border `#E2E8F0` (1px, solid, separating quote text and reviewer details)



# Typography

Quote Font

- Inter (15px / fst-italic)

Reviewer Name

- Plus Jakarta Sans (14px / SemiBold)

Reviewer Title

- Inter (12px / Muted)

Line Height

- Quote: 1.6

- Name: 1.2

- Title: 1.3



# Responsive Rules

Desktop Grid

- Testimonials align to a 3-column Grid (`col-lg-4`) or 2-column if featured (`col-lg-6`).

Tablet

- 2 columns (`col-md-6`).

Mobile

- 1 column (`col-12`).

- Equal height columns (`h-100`) to keep grids aligned perfectly.



# Accessibility

Semantic HTML

- Enclosed in an `<article>` tag.

- Review text wrapped in `<blockquote>` and `<p>`.

- Reviewer name wrapped in a heading `<h4>` or `<h5>` dependent on structure.

Aria Attributes

- Avatar image must have `alt` naming (e.g. "[Name] profile photo").

- Decorative quote icon uses `aria-hidden="true"`.



# SEO

- Review structures can map to Schema.org Review markup.

- Real company names and client names add search engine verification value.



# AI Optimization

- Clear quote structure helps AI engines parse social credentials.

- Explicit connection between reviewer and company adds relational authority to the page.



# Performance

- Avatars must be compressed to under 50KB.

- Lazy loading (`loading="lazy"`) is mandatory.

- Avoid JS sliders or carousel scrolling wrappers to maximize page speed and prevent layout shifts (CLS).



# Do

✓ Keep testimonial quotes concise (truncate excessively long reviews in admin)

✓ Use placeholders if a reviewer avatar is missing

✓ Use equal heights (`h-100`) for card consistency

✓ Display the company name to add authority

✓ Ensure high contrast between text and background



# Don't

✗ Use distracting sliders or auto-rotating carousels

✗ Display giant headshots that distract from the quote text

✗ Mix multiple testimonials styles inside the same list

✗ Fake testimonial names or reviews (zero integrity)

✗ Put links or promotional buttons inside client quote text



# Definition of Done

✓ Database Driven (Testimonial model)

✓ Responsive grid alignment

✓ Semantic HTML structure (uses <blockquote>)

✓ Bootstrap based

✓ Accessible (proper image alt, WCAG AA contrast)

✓ SEO optimized structure

✓ AI readable entity relationships

✓ Performance friendly (lazy-loaded WebP avatars)

✓ Reusable template

✓ Production ready

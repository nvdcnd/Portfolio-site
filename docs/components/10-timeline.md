---
title: Timeline Component
component: Timeline
version: 1.0.0
status: Stable
---

# Purpose

The Timeline component displays Hoàng Hùng Anh's professional career and educational history.

It provides a vertical chronological view of experiences, achievements, and credentials.

It establishes academic and professional authority in a clean, easy-to-read format.



# Business Goal

The Timeline should:

- Build strong professional credibility for freelance clients and recruiters.

- Highlight notable organizations, roles, and academic institutions.

- Demonstrate continuous growth and technical consistency.

- Keep recruiters engaged by organizing a traditional resume into an interactive experience.



# User Goal

Users should easily:

- Trace professional history from past to present.

- Differentiate between work experience and academic milestones.

- Read key achievements and responsibilities in each role.

- Link to organization websites to verify credentials.



# Database Mapping

Data Source

- apps.core.models.Timeline

Fields Used

- `title` (role or degree name)

- `organization` (company or university name)

- `year` (year indicator, e.g. 2024)

- `start_date` (beginning date of work/study)

- `end_date` (conclusion date of work/study)

- `is_current` (Boolean indicating currently active role)

- `location` (city, country, or remote status)

- `url` (link to organization website)

- `type` (choices: 'education' or 'experience')

- `description` (details of achievements, bulleted or text)



# Template Mapping

Template

```
templates/components/timeline_item.html
```

CSS

```
static/css/components/timeline.css
```

JavaScript

None.



# Component Structure

```
Timeline (Wrapper)
└── Timeline Item
    ├── Timeline Marker
    │   ├── Type Icon (Education / Work)
    │   └── Chronological Line
    └── Content Card
        ├── Header
        │   ├── Title (H3/H4)
        │   ├── Organization / Link
        │   └── Location & Date range
        └── Description
```



# Layout

Vertical Layout (Default)

```
       [Marker] --- 2024 - Present
          |
          |         Software Engineer at Google DeepMind (Remote)
          |         Building agentic AI tools and running experiments...
          |
       [Marker] --- 2020 - 2024
          |
          |         B.S. in Computer Science at University
          |         Graduated with Honors. Specialized in Algorithms...
          |
```

- Markers represent nodes: briefcase icon for experience, graduation cap for education.

- Left column contains date range, right column contains role card (or standard vertical stacking on mobile).



# Bootstrap Layout

Preferred Structure

```
<div class="timeline-container position-relative py-3">

    {% for item in timeline_items %}

        <div class="timeline-item d-flex gap-4 mb-4">

            <!-- Marker & Line -->

            <div class="timeline-aside d-flex flex-column align-items-center">

                <div class="timeline-marker bg-white border border-primary border-3 rounded-circle d-flex align-items-center justify-content-center" style="width: 48px; height: 48px;">

                    {% if item.type == 'education' %}

                        <i class="bi bi-mortarboard-fill text-primary fs-5"></i>

                    {% else %}

                        <i class="bi bi-briefcase-fill text-primary fs-5"></i>

                    {% endif %}

                </div>

                <div class="timeline-line flex-grow-1 border-start border-2 border-light-subtle my-2"></div>

            </div>

            <!-- Content Card -->

            <div class="timeline-content card border-0 shadow-sm p-4 flex-grow-1">

                <div class="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-3">

                    <div>

                        <span class="badge bg-secondary-subtle text-secondary rounded-pill px-3 py-1 text-uppercase fs-8 mb-2 d-inline-block">

                            {{ item.get_type_display }}

                        </span>

                        <h3 class="h4 font-heading fw-semibold text-dark mb-1">

                            {{ item.title }}

                        </h3>

                        <div class="text-primary fw-medium">

                            {% if item.url %}

                                <a href="{{ item.url }}" target="_blank" rel="noopener noreferrer" class="text-decoration-none hover-underline text-primary">

                                    {{ item.organization }}

                                </a>

                            {% else %}

                                {{ item.organization }}

                            {% endif %}

                            <span class="text-secondary ms-2"><i class="bi bi-geo-alt"></i> {{ item.location }}</span>

                        </div>

                    </div>

                    <div class="text-md-end mt-2 mt-md-0">

                        <span class="text-secondary fw-semibold">

                            {% if item.is_current %}

                                {{ item.start_date|date:"M Y" }} - Present

                            {% else %}

                                {{ item.start_date|date:"M Y" }} - {{ item.end_date|date:"M Y" }}

                            {% endif %}

                        </span>

                    </div>

                </div>

                <div class="timeline-description text-secondary">

                    {{ item.description|linebreaks }}

                </div>

            </div>

        </div>

    {% endfor %}

</div>
```



# Styling

Markers

- Color: White background, Royal Blue border (`#2563EB`)

- Width/Height: 48px diameter

- Icons: Bootstrap Icons (`bi-briefcase-fill`, `bi-mortarboard-fill`)

Timeline Line

- Color: Light border grey `#E2E8F0`

- Alignment: Perfectly centered beneath markers

Content Card

- Background: White `#FFFFFF`

- Border Radius: 16px

- Border: None (shadow provides separation)

- Shadow: Subtle Elevation



# Typography

Heading Font

- Plus Jakarta Sans (H3 / 20px)

Body Font

- Inter (15px)

Date / Meta Font

- Inter (14px / SemiBold)

Line Height

- Heading: 1.3

- Body: 1.6



# Responsive Rules

Desktop

- Dual column spacing with offset timeline.

- Broad vertical spacing (`mb-5`).

Mobile

- Columns collapse to vertical stack.

- Marker is positioned to the left, content card occupies remaining width.

- Timeline line persists to link elements.

- Spacing: `mb-4`.



# Accessibility

Semantic HTML

- Timeline markers should be hidden from screen readers if decorative (`aria-hidden="true"`).

- Roles and degrees must be in heading elements.

Keyboard Navigation

- Links to organizations must be keyboard accessible and tab-navigable.

Aria Attributes

- `aria-label` applied to external credentials.

- Icons use `aria-hidden="true"`.



# SEO

- Structured content with company names and locations helps local SEO searches.

- Heading tags organize the CV section semantic outline.



# AI Optimization

- The timeline maps clear temporal relationships (Entity -> worked at Organization -> from Time1 to Time2).

- Helps AI systems synthesize Hoàng Hùng Anh's experience history and academic path correctly.



# Performance

- Pure CSS layouts.

- Text-only timeline loads instantly.

- Avoid JavaScript scroll effects or libraries. Use CSS transition.



# Do

✓ Group timeline elements by display order and start date

✓ Differentiate visually between academic and work records

✓ Keep descriptions structured with bullets or paragraphs

✓ Add correct rel attributes to external links

✓ Use standard time tags where dates appear



# Don't

✗ Use bright neon timeline lines

✗ Put huge paragraphs of unsorted text in descriptions

✗ Use multiple headers that break layout structure

✗ Add floating graphics or scroll-triggered slide-ins that lag on mobile

✗ Duplicate items from portfolio in detail



# Definition of Done

✓ Database Driven (Timeline model)

✓ Responsive vertical layout

✓ Semantic HTML structure

✓ Bootstrap flex layout

✓ Accessible (visible keyboard focus, AA contrast)

✓ SEO ready metadata dates

✓ AI optimized relationships

✓ Performance friendly

✓ Reusable template

✓ Production ready

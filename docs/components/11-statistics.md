---
title: Statistics Component
component: Statistics
version: 1.0.0
status: Stable
---

# Purpose

The Statistics component displays high-impact numbers and achievements (e.g., 5+ Years Coding, 20+ Projects, 100+ Students).

It provides immediate empirical proof of credibility and expertise.

It resides on the homepage to capture visitor trust within the first few seconds.



# Business Goal

The Statistics component should:

- Communicate professional scale and experience quickly.

- Increase landing page conversions through solid social proof.

- Highlight specific areas of strength (Development, Mentoring, Speaking).

- Assure recruiters and prospective clients of proven competence.



# User Goal

Users should easily:

- Scan and digest key experience milestones in under 3 seconds.

- See the absolute scale of work done (number of projects, students, experience).



# Database Mapping

Data Source

- apps.core.models.Statistic

Fields Used

- `value` (numerical or text quantity, e.g. '5', '20', '100')

- `suffix` (optional symbol appended, e.g. '+', '%')

- `title` (metric label, e.g. 'Projects Completed')

- `icon_class` (Bootstrap Icon class, e.g. 'bi-check-circle')

- `display_order` (display sort priority)



# Template Mapping

Template

```
templates/components/stat_card.html
```

CSS

```
static/css/components/statistics.css
```

JavaScript

None (or simple dynamic numeric count-up animation if needed, keep CSS transitions first).



# Component Structure

```
Statistics Grid
└── Stat Card
    ├── Icon (Optional)
    ├── Value (Value + Suffix)
    └── Title / Label
```



# Layout

Horizontal Grid Layout

- Standard layout is a row containing 3 or 4 equal-width columns.

```
-------------------------------------------------------------------------
   [Icon: bi-code]          [Icon: bi-mortarboard]     [Icon: bi-terminal]
         5+                          100+                       20+
    Years Coding              Students Mentored         Projects Completed
-------------------------------------------------------------------------
```



# Bootstrap Layout

Preferred Structure

```
<div class="row g-4 py-4">

    {% for stat in stats %}

        <div class="col-6 col-md-3">

            <div class="card stat-card border-0 bg-transparent text-center">

                <div class="card-body p-3">

                    {% if stat.icon_class %}

                        <div class="stat-icon-wrapper text-primary mb-3">

                            <i class="bi {{ stat.icon_class }} display-5"></i>

                        </div>

                    {% endif %}

                    <div class="stat-value display-4 font-heading fw-bold text-dark mb-1">

                        {{ stat.value }}{{ stat.suffix|default:"" }}

                    </div>

                    <h3 class="stat-title h6 font-body fw-medium text-secondary text-uppercase tracking-wider">

                        {{ stat.title }}

                    </h3>

                </div>

            </div>

        </div>

    {% endfor %}

</div>
```



# Styling

Grid Container

- Background: Clean White `#FFFFFF` or Light Surface `#F8FAFC`

- Spacing: Standard vertical grid gutters

Stat Cards

- Background: Transparent (to feel integrated into the background layout)

- Border: None

- Spacing: Centered content

Value Text

- Font Color: Primary Navy `#0F172A`

- Font Weight: 700 / Bold

- Highlight Accent: Optional subtle Royal Blue `#2563EB` color for numbers

Icon Style

- Muted primary accent color

- No heavy surrounding circles or background fill to keep it clean and minimal



# Typography

Value Font

- Plus Jakarta Sans (display-4 / 40px-48px)

Title Font

- Inter (14px / H6 / uppercase)

Line Height

- Value: 1.1

- Title: 1.3



# Responsive Rules

Desktop

- 4 columns (`col-md-3`).

Tablet

- 2 columns (`col-sm-6`).

Mobile

- 2 columns (`col-6`).

- Spacing and gutters shrink to prevent text wrapping on small screens.

- Font sizes drop automatically through Bootstrap responsive headers.



# Accessibility

Semantic HTML

- Values should be read correctly as quantities.

- Title should be H3 or H4 for semantic layout.

Keyboard Navigation

- Not applicable (non-interactive display).

Screen Readers

- Must read prefix/suffix and value as a single combined string (e.g. "5 plus" or "100 percent").

- Icons use `aria-hidden="true"`.



# SEO

- Structured stats increase authority signals.

- Text values are indexed as normal text elements.



# AI Optimization

- The key-value pairs (metric name -> quantity) help LLMs summarize candidate qualities quickly (e.g. "Hoàng Hùng Anh has 5+ years of experience and mentored 100+ students").



# Performance

- Loads instantly.

- Minimal DOM nodes.

- Avoid heavy Javascript count-up libraries. Simple CSS transition on load is sufficient.



# Do

✓ Keep titles short and descriptive (1-3 words)

✓ Sort statistics logically by import priority

✓ Use uniform icon styling across all cards

✓ Style value numbers with bold headings

✓ Fallback gracefully if suffix is blank



# Don't

✗ Use neon text shadows or glowing borders

✗ Use different styles or fonts for different cards

✗ Include long descriptions underneath the stat titles

✗ Hardcode values inside templates

✗ Use heavy animated graphics for numbers (causes layout lag)



# Definition of Done

✓ Database Driven (Statistic model)

✓ Responsive grid alignment

✓ Semantic HTML structure

✓ Bootstrap grid based

✓ Accessible (aria-hidden icons, AA color contrast)

✓ SEO search compliant

✓ AI friendly key-value pairing

✓ Performance optimized

✓ Reusable template

✓ Production ready

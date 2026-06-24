---
title: Section Title Component
component: SectionTitle
version: 1.0.0
status: Stable
---

# Purpose

The Section Title component is a reusable UI block used to introduce major content sections.

It establishes structure and visual hierarchy across the page.

It guides the reader's eye and signals transitions between different topics.



# Business Goal

The Section Title should:

- State the value proposition of the section immediately.

- Drive user focus toward primary conversion areas (e.g. Services, Projects).

- Standardize UI design to reduce development complexity.



# User Goal

Users should easily:

- Understand what each section is about when scanning.

- Read the high-level summary before committing to detailed cards/content.



# Database Mapping

Data Source

- None (purely presentation component)

Inputs / Parameters

- `badge` (String, optional)

- `title` (String, required)

- `description` (String, optional)

- `alignment` (String: 'center' or 'left', default: 'center')



# Template Mapping

Template

```
templates/components/section_title.html
```

CSS

```
static/css/components/section_title.css
```

JavaScript

None.



# Component Structure

```
Section Title
├── Badge / Tag (Optional)
├── Heading (H2)
└── Description (Optional)
```



# Layout

Centered (Default)

```
                       [ Badge ]
                   [ Section Title ]
         [ Short description explaining the section. ]
```

Left Aligned

```
[ Badge ]
[ Section Title ]
[ Short description explaining the section. ]
```



# Bootstrap Layout

Preferred Structure

```
<div class="section-header text-{{ alignment|default:'center' }} mb-5">

    {% if badge %}

        <span class="badge bg-light text-primary border border-primary px-3 py-2 rounded-pill text-uppercase fs-7 mb-2">

            {{ badge }}

        </span>

    {% endif %}

    <h2 class="display-6 font-heading fw-bold text-dark mb-3">

        {{ title }}

    </h2>

    {% if description %}

        <p class="lead text-secondary mx-auto max-width-600">

            {{ description }}

        </p>

    {% endif %}

</div>
```



# Styling

Badge

- Background: Light gray `#F8FAFC`

- Border: Accent Blue `#2563EB` (or Border Slate `#E2E8F0`)

- Text: Royal Blue `#2563EB` (font weight: 600, text-transform: uppercase)

Heading (H2)

- Color: Navy `#0F172A`

- Font weight: 700 / Bold

Description / Subtitle

- Color: Muted Slate `#64748B`

- Max-width: 600px (to prevent line lengths that are too wide to read easily)

- Margins: Auto margins when centered



# Typography

Heading Font

- Plus Jakarta Sans (H2 or display-6)

Body / Description Font

- Inter (font-size: 16px or 18px / lead)

Line Height

- Heading: 1.2

- Description: 1.6



# Responsive Rules

Desktop

- Spacing: `mb-5` (48px spacing below)

- Font sizes: standard H2 / display-6 size

Tablet / Mobile

- Spacing: `mb-4` (32px spacing below)

- Heading size shrinks to standard H3 on small screens (Bootstrap's responsive typography)

- Align text to center on mobile even if layout is left-aligned on desktop.



# Accessibility

Semantic HTML

- Heading MUST be an `<h2>`.

- Badge must have a clear text equivalent.

Keyboard Navigation

- Not applicable (non-interactive).

Screen Readers

- Structure must be logical.

- Hidden content must not be spoken.



# SEO

- Every major section MUST start with an `<h2>` for proper SEO structure.

- Do not use `<h1>` for section titles (only one `<h1>` per page, in Hero).

- Heading text should contain keywords relevant to the section.



# AI Optimization

- Descriptive titles and subtitles assist AI search engines and readers in parsing page layout and understanding user intents.

- Avoid ambiguous or overly creative section headings.



# Performance

- No scripts, very simple CSS.

- Rendered directly by Django template engine with zero client overhead.



# Do

✓ Keep description text brief (max 2 sentences)

✓ Use the H2 tag consistently for section headings

✓ Restrict max-width on description paragraphs for readable line lengths

✓ Keep naming clear: `badge`, `title`, `description`

✓ Support clean fallback if description or badge is missing



# Don't

✗ Skip H2 tags and use H3 or H4 for section headings

✗ Style section titles differently in each section

✗ Put interactive links inside the section description

✗ Overuse badges on every single section



# Definition of Done

✓ Fully responsive

✓ Matches heading scale and styling guide

✓ Semantic H2 markup

✓ Reusable parameterized Django template

✓ SEO compliant

✓ AI friendly

✓ High performance

✓ Production ready

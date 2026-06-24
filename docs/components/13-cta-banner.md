---
title: CTA Banner Component
component: CTABanner
version: 1.0.0
status: Stable
---

# Purpose

The CTA (Call to Action) Banner is a prominent full-width component positioned at the bottom of pages.

It serves as the final step in the homepage user experience, prompting conversion.

It gathers visitor focus and provides immediate access to action steps.



# Business Goal

The CTA Banner should:

- Direct users toward primary conversion actions (e.g., booking consultation, hiring).

- Streamline lead generation by reducing contact friction.

- Highlight availability for freelance development and mentoring services.

- Maximize page conversion rate.



# User Goal

Users should easily:

- Initiate contact with Hoàng Hùng Anh.

- Know exactly what actions to take next (email, fill form, book calendar).

- Get immediate direction without having to search for the contact page.



# Database Mapping

Data Source

- None (presentation component driven by template parameters)

Inputs / Parameters

- `title` (Heading text, e.g. "Ready to start your next project?")

- `description` (Supporting text, e.g. "Let's collaborate to build scalable software...")

- `primary_cta_text` (Button label, e.g. "Hire Me")

- `primary_cta_link` (Button URL, e.g. "/contact/")

- `secondary_cta_text` (Button label, e.g. "Book Mentoring")

- `secondary_cta_link` (Button URL, e.g. "/services/")



# Template Mapping

Template

```
templates/components/cta_banner.html
```

CSS

```
static/css/components/cta_banner.css
```

JavaScript

None.



# Component Structure

```
CTA Banner
├── Heading (H2)
├── Subheading / Description
└── Button Group
    ├── Primary CTA Button
    └── Secondary CTA Button (Optional)
```



# Layout

Centered Stacked Layout

```
--------------------------------------------------------------
                [ Ready to build something together? ]
       [ Let's collaborate to build high-performance Django apps ]
       
                    [ Hire Me ]    [ Book Call ]
--------------------------------------------------------------
```

- Content is centered vertically and horizontally inside a high-contrast container.



# Bootstrap Layout

Preferred Structure

```
<section class="cta-banner bg-dark text-white text-center py-5 my-0">

    <div class="container py-4">

        <div class="row justify-content-center">

            <div class="col-lg-8">

                <h2 class="display-5 font-heading fw-bold text-white mb-3">

                    {{ title|default:"Ready to work together?" }}

                </h2>

                <p class="lead text-light-emphasis mb-4">

                    {{ description|default:"Let's collaborate to build high-performance systems or train the next generation of engineers." }}

                </p>

                <div class="d-flex flex-column flex-sm-row justify-content-center align-items-center gap-3">

                    <a href="{{ primary_cta_link|default:'/contact/' }}" class="btn btn-primary btn-lg rounded-3 px-4 py-3">

                        {{ primary_cta_text|default:"Get In Touch" }}

                    </a>

                    {% if secondary_cta_text and secondary_cta_link %}

                        <a href="{{ secondary_cta_link }}" class="btn btn-outline-light btn-lg rounded-3 px-4 py-3">

                            {{ secondary_cta_text }}

                        </a>

                    {% endif %}

                </div>

            </div>

        </div>

    </div>

</section>
```



# Styling

Banner Container

- Background: Primary Dark Navy `#0F172A` (creates contrast from white page sections)

- Padding: Generous vertical padding (`py-5` / 80px)

- Border: None

Text Primary

- White: `#FFFFFF`

Text Secondary

- Muted Slate: `#94A3B8`

Primary Button

- Background: Royal Blue `#2563EB` (Solid)

- Text: White `#FFFFFF`

- Border Radius: 12px

Secondary Button

- Background: Transparent

- Border: White `#FFFFFF` (Outline, 1px)

- Text: White `#FFFFFF`

- Hover State: Solid White background, dark Navy text



# Typography

Heading Font

- Plus Jakarta Sans (display-5 / 36px-40px)

Body Font

- Inter (16px-18px / Lead)

Button Font

- Plus Jakarta Sans (16px / SemiBold)

Line Height

- Heading: 1.2

- Body: 1.6



# Responsive Rules

Desktop

- Padding: `py-5`.

- Two buttons aligned horizontally with gap-3.

Mobile

- Padding: `py-4`.

- Heading font size reduces.

- Buttons stack vertically, expanding to 100% container width.



# Accessibility

Semantic HTML

- Wrapped in `<section class="cta-banner">`.

- Title must be `<h2>`.

Keyboard Navigation

- Buttons must be reachable via standard tab controls with focus rings.

Aria Attributes

- Buttons must have clear, readable destination names (no vague "Click here").

- Background elements must use high-contrast color choices (Off-white on Navy).



# SEO

- Clean CTA anchors help search engine crawlers trace conversion paths.

- Keywords in heading text (e.g. "Work Together", "Hire Software Developer") boost SEO relevance.



# AI Optimization

- The CTA clearly defines the conversion intentions (Entity -> offers Services -> through Contact actions).

- Clearly labeled parameters allow AI parsers to discover contact entryways.



# Performance

- No static images or video backgrounds (solid color CSS background only).

- Instant DOM rendering.

- No client-side scripting.



# Do

✓ Keep call-to-action wording simple and active

✓ Limit button selection to maximum 2 choices

✓ Use high-contrast dark backgrounds for focus

✓ Use flexible default parameters in the Django template

✓ Keep spacing clean and generous



# Don't

✗ Use carousels or rotating text banners

✗ Put background videos or heavy graphics in the CTA section

✗ Place multiple competing links or paragraphs of copy in the card

✗ Style each CTA banner differently across pages (maintain consistency)

✗ Include social links inside the CTA group (belongs in footer/navbar)



# Definition of Done

✓ Parameterized Django template

✓ Responsive spacing and layout

✓ High contrast design

✓ Bootstrap based grid structure

✓ Accessible (visible focus, AA contrast minimum)

✓ SEO search friendly links

✓ AI discoverable paths

✓ High performance

✓ Reusable template

✓ Production ready

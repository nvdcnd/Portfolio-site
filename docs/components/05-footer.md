---
title: Footer Component
component: Footer
version: 1.0.0
status: Stable
---

# Purpose

The footer is the final anchor of the website's user journey.

It provides persistent global information, secondary navigation, social links, contact info, and legal requirements.

It ensures that visitors who scroll to the very bottom have a clear path to continue interacting with the personal brand.



# Business Goal

The footer should:

- Provide a final opportunity for visitor conversion.

- Direct users to contact channels (Email, Phone).

- Increase social media engagement and followers.

- Establish professional presence through copyright and branding.

- Enhance SEO indexing through logical site structure links.



# User Goal

Users should easily:

- Find email and contact information.

- Access secondary social media links.

- Navigate back to top-level sections (Services, Blog, Portfolio).

- Read legal and copyright notices.



# Database Mapping

Data Sources

- apps.common.models.Footer

- apps.common.models.ContactInfo

- apps.common.models.SocialMediaLink

- apps.common.models.GeneralSettings

Fields Used

- Footer: `content` (custom raw content/HTML block)

- ContactInfo: `email`, `phone_number`, `address`

- SocialMediaLink: `platform_name`, `profile_url`, `icon_class`

- GeneralSettings: `site_name`, `site_logo`



# Template Mapping

Template

```
templates/components/footer.html
```

CSS

```
static/css/components/footer.css
```

JavaScript

None (or minimal for scroll-to-top feature).



# Component Structure

```
Footer
├── Brand Area
│   ├── Logo / Wordmark
│   ├── Short Description
│   └── Social Links
├── Quick Links
│   ├── Home
│   ├── Services
│   ├── Portfolio
│   └── Blog
├── Contact Info
│   ├── Email
│   ├── Phone Number
│   └── Address
└── Bottom Bar
    ├── Copyright
    └── Back to Top
```



# Layout

Desktop

```
-----------------------------------------------------------------------------------
[Column 1: Brand]     [Column 2: Navigation]    [Column 3: Contact]
Logo / site_name      Quick Links Heading        Contact Info Heading
Short Description     Links (Home, Services...)  Email, Phone, Address
Social Media Icons
-----------------------------------------------------------------------------------
[Copyright Info]                                      [Back to Top Button]
-----------------------------------------------------------------------------------
```

Tablet

```
- Column 1: Brand (width 12)
- Column 2: Navigation (width 6)
- Column 3: Contact (width 6)
- Bottom: Copyright + Back to Top stacked
```

Mobile

```
- Single column layout (stacked vertically)
- Column order: Brand -> Navigation -> Contact -> Copyright -> Back to Top
- All elements centered
```



# Bootstrap Layout

Preferred Structure

```
<footer class="bg-dark text-light py-5">

    <div class="container">

        <div class="row gy-4">

            <div class="col-lg-4 col-md-12">

                <!-- Brand Area -->

            </div>

            <div class="col-lg-4 col-md-6">

                <!-- Quick Links -->

            </div>

            <div class="col-lg-4 col-md-6">

                <!-- Contact Info -->

            </div>

        </div>

        <hr class="my-4 border-secondary">

        <div class="row align-items-center justify-content-between">

            <div class="col-md-6 text-center text-md-start">

                <!-- Copyright -->

            </div>

            <div class="col-md-6 text-center text-md-end mt-3 mt-md-0">

                <!-- Back to Top -->

            </div>

        </div>

    </div>

</footer>
```



# Styling

Background

- Primary Dark: `#0F172A`

Text Primary

- Off-White: `#F8FAFC`

Text Secondary

- Muted Slate: `#94A3B8`

Borders

- Muted Border: `#334155`

Hover State

- Links change color to Royal Blue `#3B82F6` (Light mode variant `#2563EB`)

- Subtle under-line or color fade.



# Typography

Heading Font

- Plus Jakarta Sans (font-weight: 600, 18px / H6)

Body / Link Font

- Inter (font-weight: 400, 14px / Small)

Line Height

- Heading: 1.2

- Body: 1.5



# Responsive Rules

Desktop

- 3 columns layout.

- Spacing: `py-5`.

Tablet / Mobile

- Columns stack.

- Spacing: `py-4`.

- Links target area must maintain minimum size (44px height/width).



# Accessibility

Semantic HTML

- Enclosed in `<footer>`.

- Links use descriptive text.

Keyboard Navigation

- Logical tab ordering.

- Focus outline matches the system accent color.

Aria Attributes

- Icons must use `aria-hidden="true"`.

- Icon-only links (Social) must have `aria-label` defining the platform.



# SEO

- Links should be crawlable (`href` must be valid, no JavaScript-only links).

- The footer must NOT contain any H1 tags.

- Anchor titles must be descriptive (e.g. "Services" instead of "What I Do").



# AI Optimization

- The footer clearly maps the entity relationships (Hoàng Hùng Anh, services, contacts).

- Clear labels and structural headings help AI crawlers determine structure.



# Performance

- Use local SVG or Bootstrap Icons instead of loading giant external font packages.

- Images (such as logo) must contain `loading="lazy"`.

- Avoid CSS styling that requires layout recalculations.



# Do

✓ Keep footer tidy and organized

✓ Use Bootstrap's `gy-4` for mobile row spacing

✓ Keep contact information accurate and dynamic

✓ Use correct rel attributes for external links (`rel="noopener noreferrer"`)

✓ Ensure proper dark mode contrast compliance



# Don't

✗ Add large images or animations

✗ Insert newsletter forms if not supported by backend

✗ Create multiple navigation lists that duplicate main navbar

✗ Hardcode personal biography in template (use Footer content model)

✗ Mix up heading hierarchy (no H1 or H2 tags in footer)



# Definition of Done

✓ Database Driven (from common models)

✓ Responsive

✓ Semantic HTML (uses <footer>)

✓ Bootstrap Based

✓ Accessible (WCAG AA Contrast, aria-labels)

✓ SEO Friendly

✓ AI Optimized

✓ High Performance

✓ Reusable

✓ Production Ready

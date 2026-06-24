=== FILE: docs/components/02-navigation.md ===

---
title: Navigation Component
component: Navbar
version: 1.0.0
status: Stable
---

# Purpose

The navigation component is the primary orientation system of the website.

Users should understand who Hoàng Hùng Anh is and where they can go within 3 seconds.

The navigation should build trust and reduce friction.

Navigation is not a place for creativity.

Navigation is a place for clarity.



# Business Goal

The navigation should help users:

- Understand the brand
- Discover services
- Discover portfolio projects
- Read blog content
- Contact Hoàng Hùng Anh
- Convert into leads

The navigation should support business growth.

It should never become a distraction.



# User Goal

Users should immediately find

- About
- Services
- Portfolio
- Blog
- Contact

without thinking.

Navigation should feel obvious.



# Database Mapping

Data Source

SiteSetting

Social Links

Navigation Items (future)

Current Version

Static Navigation

Future Version

Database-driven Navigation



# Template Mapping

Template

templates/components/navbar.html

CSS

static/css/components/navbar.css

JavaScript

static/js/components/navbar.js



# Component Structure

```
Navbar

├── Logo

├── Navigation Links

├── Primary CTA

└── Mobile Toggle
```

Navigation should remain simple.

Do not add unnecessary elements.



# Navigation Items

Current

Home

Services

Portfolio

Blog

Contact

Future

Resources

Speaking

Mentorship

FAQ

Avoid adding too many menu items.



# Navigation Order

Desktop

```
Logo

↓

Navigation Links

↓

Primary CTA
```

Primary CTA should always appear on the far right.



# Primary CTA

Text

Hire Me

or

Book a Consultation

Only one primary CTA.

Do not create multiple competing actions.



# Secondary Actions

Not displayed in navbar.

Secondary actions belong inside page content.



# Logo

Logo should be text-based initially.

Example

```
Hoàng Hùng Anh
```

Future

Wordmark

Personal Logo

Avoid large logo graphics.



# Layout

Desktop

```
Logo

Navigation

CTA
```

Tablet

Same as desktop if space allows.

Mobile

```
Logo

Hamburger

↓

Drawer Menu
```



# Bootstrap Structure

Preferred

```
navbar

navbar-expand-lg

container

d-flex

align-items-center

justify-content-between
```

Avoid custom navigation systems.



# Positioning

Navbar should be

Sticky

Top

Always visible

Example

```
position: sticky
top: 0
```

Avoid fixed navigation unless necessary.



# Scroll Behavior

Top of Page

Transparent

After Scroll

Solid Background

Light Shadow

The transition should feel subtle.



# Height

Desktop

72px

Mobile

64px

Avoid oversized navigation bars.



# Typography

Font

Plus Jakarta Sans

Weight

500

Navigation should be readable.

Avoid excessive font weight.



# Active State

Active page should use

Accent Color

#2563EB

Users should always know their location.



# Hover State

Subtle

Color transition

No scaling

No bouncing

No underlines that move.



# Mobile Menu

Behavior

Slide Down

or

Slide From Right

Choose one.

Keep implementation simple.

Avoid fullscreen overlays.



# Mobile Navigation Rules

Links should be large enough to tap.

Minimum touch target

44px

Spacing should be generous.



# Accessibility

Must Support

Keyboard Navigation

Tab Navigation

Screen Readers

ARIA Labels

Examples

```
aria-label="Main Navigation"
```

```
aria-expanded="false"
```

Never rely solely on visual indicators.



# SEO

Navigation should use

Semantic HTML

Example

```
<nav>
```

Avoid generic wrappers.

Navigation links should use descriptive text.

Good

```
Portfolio
```

Bad

```
My Stuff
```



# AI Optimization

Navigation labels should clearly describe content.

Preferred

Services

Portfolio

Blog

Contact

Avoid vague labels.

Bad

```
Explore

Resources

Discover
```

Without context.



# Performance

Navigation should require minimal JavaScript.

Preferred

CSS + Bootstrap

JavaScript only when necessary.

Avoid animation libraries.



# Dark Mode Support

Future Support Required.

Current implementation must not block dark mode development.



# Security

All external links must use

```
rel="noopener noreferrer"
```

when opening in new tabs.



# Animation

Allowed

Fade

Background Transition

Slide

Duration

200ms–300ms

Avoid

Bounce

Rotate

Glow

Complex Motion



# Responsive Rules

Desktop

Full Navigation

Tablet

Full Navigation if space allows

Mobile

Collapsed Menu

Never allow horizontal scrolling.



# Content Rules

Navigation should remain concise.

Maximum visible menu items

7

Ideal

5

Current

5



# Do

✓ Keep navigation minimal

✓ Keep CTA visible

✓ Use semantic HTML

✓ Support keyboard navigation

✓ Keep labels clear

✓ Keep layout responsive



# Don't

✗ Add unnecessary dropdowns

✗ Add social links in main navigation

✗ Use flashy animations

✗ Add multiple primary CTAs

✗ Create mega menus

✗ Use vague labels



# Future Enhancements

Possible Future Features

- Language Switcher
- Search
- Resources Dropdown
- User Authentication

These features must not complicate the current version.



# Definition of Done

✓ Responsive

✓ Accessible

✓ Sticky

✓ Semantic HTML

✓ Bootstrap Based

✓ SEO Friendly

✓ AI Optimized

✓ Fast

✓ Reusable

✓ Production Ready
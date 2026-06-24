=== FILE: docs/components/01-layout-components.md ===

---
title: Layout Components
version: 1.0.0
status: Stable
---

# Purpose

This document defines the global page layout.

Every page in this project MUST follow the same layout structure.

Never create page-specific layouts unless absolutely necessary.



# Philosophy

A layout is responsible for structure.

A component is responsible for content.

Pages assemble components inside layouts.

Layouts should never contain business logic.



# Page Hierarchy

Every page must follow this structure.

```
<html>

    <head>

    <body>

        <header>

        <main>

            <section>

            <section>

            <section>

        </main>

        <footer>

    </body>

</html>
```

Never replace semantic elements with generic divs.



# Base Template

Every page MUST extend

```
templates/base.html
```

Never duplicate HTML document structure.



# Base Template Responsibilities

base.html is responsible for

- HTML document
- Metadata
- Global CSS
- Global JavaScript
- Navbar
- Footer
- Theme
- Messages
- Common scripts

Pages should only provide content.



# Template Structure

```
templates/

base.html

layouts/

components/

pages/
```

Pages should never import CSS directly.

Pages should never duplicate Navbar or Footer.



# Standard Layout

```
<header>

    Navbar

</header>

<main>

    Hero

    Page Content

    CTA

</main>

<footer>

    Footer

</footer>
```



# Main Container

Use Bootstrap

```
container

or

container-xl
```

Maximum width

1320px

Never use custom fixed widths.



# Bootstrap Grid

Always use Bootstrap Grid.

Preferred

```
row

col

col-lg-6

col-xl-4
```

Avoid manual flex layouts unless necessary.



# Section Structure

Every section follows

```
<section>

    Container

        Section Header

        Content

</section>
```

Do not skip the container.



# Section Header

Each section should include

Heading

↓

Short description

↓

Content

Example

```
Our Services

Professional software development,
technical mentoring and consulting.

[Cards]
```

Never begin a section directly with cards.



# Vertical Spacing

Desktop

120px

Tablet

96px

Mobile

64px

Never use random spacing values.



# Horizontal Spacing

Use Bootstrap utilities.

Examples

```
px-3

px-4

px-lg-5
```

Avoid custom padding classes.



# Component Order

Homepage

```
Navbar

↓

Hero

↓

Trusted By

↓

Statistics

↓

Services

↓

Featured Projects

↓

Achievements

↓

Timeline

↓

Testimonials

↓

Latest Articles

↓

Call To Action

↓

Footer
```

Maintain this order unless business requirements change.



# Background Rules

Default

White

Alternate

Light Surface

Alternate sections should help users distinguish content.

Avoid excessive color changes.



# Cards Layout

Cards should always align to Bootstrap Grid.

Example

Desktop

```
3 columns
```

Tablet

```
2 columns
```

Mobile

```
1 column
```

Never create uneven layouts.



# Images

Images should

Use Bootstrap responsive utilities

```
img-fluid
```

Include

```
loading="lazy"
```

Include

```
alt
```

Avoid oversized images.



# Responsive Behavior

Desktop

Content may use two-column layouts.

Tablet

Reduce spacing.

Stack secondary content when necessary.

Mobile

Everything should become a single-column experience.

Never require horizontal scrolling.



# Typography Hierarchy

Only one H1.

Each section begins with H2.

Cards use H3 or H4 depending on importance.

Never skip heading levels.



# Breadcrumb

Internal pages should support breadcrumbs.

Example

```
Home

>

Portfolio

>

Project
```

Homepage does not require breadcrumbs.



# Sidebar

Current version

No sidebar.

Future

Blog pages may include

Recent Articles

Categories

Tags

Newsletter



# Empty States

Every list should support an empty state.

Example

No blog posts available.

No projects found.

Never leave empty whitespace.



# Loading States

Future enhancement

Skeleton loading

Spinner only when absolutely necessary.



# Error States

Components should never collapse the page.

If data is missing

Hide component gracefully.

Show fallback only when necessary.



# Theme Support

Future

Dark Mode

Current implementation should not prevent future dark mode support.



# SEO

Layout must include

Language attribute

Meta tags

Canonical

Open Graph

Twitter Card

Structured Data block

Never forget viewport.



# Accessibility

Layout should support

Keyboard navigation

Logical tab order

Visible focus

Screen readers

Proper landmarks

<header>

<nav>

<main>

<footer>



# Performance

Load only required CSS.

Load JavaScript at the bottom.

Lazy load images.

Avoid render-blocking resources.



# AI Optimization

The page structure should clearly express

Who

What

Why

How

Every major section should answer one user intent.

Avoid decorative sections with no business value.



# Reusability

Layouts should never contain

Business content

Hardcoded titles

Specific projects

Specific services

Everything should come from Django context.



# Bootstrap Utilities

Preferred

```
container

row

col

d-flex

align-items-center

justify-content-between

gap-*

py-*

px-*

my-*

text-center

text-lg-start
```

Avoid custom layout CSS whenever Bootstrap already provides utilities.



# Definition of Done

The layout is complete only if

✓ Responsive

✓ Mobile First

✓ Accessible

✓ Semantic HTML

✓ Bootstrap-based

✓ SEO Ready

✓ AI Optimized

✓ Reusable

✓ Performance Friendly

✓ Future-proof
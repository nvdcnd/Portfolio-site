=== FILE: docs/01-design-system.md ===

---
title: Design System
version: 1.0.0
status: Stable
---

# Design System

## Purpose

This document defines every visual rule of the project.

Every page, component and layout MUST follow this document.

Never redesign the UI without updating this file.

This design system has higher priority than AI creativity.



# Design Philosophy

Theme

Modern Academic Luxury

The website should communicate

- Professional
- Premium
- Calm
- Trustworthy
- Intelligent
- Modern
- Elegant
- Timeless

The website should NEVER feel

- Playful
- Flashy
- Overdesigned
- Gaming
- Cyberpunk
- Neon
- Glass-heavy
- Startup hype



# Brand Personality

Imagine the intersection of

Apple

+

Stripe

+

Linear

+

Vercel

+

Notion

+

Harvard

+

MIT

The feeling should be

"I trust this engineer."

NOT

"This website has cool animations."



# Color System

## Primary

Navy

#0F172A

Main usage

- Logo
- Navigation
- Titles
- Buttons
- Footer



## Secondary

Slate

#334155

Main usage

- Secondary text
- Icons
- Borders



## Accent

Royal Blue

#2563EB

Main usage

- Primary CTA
- Active navigation
- Links
- Interactive elements



## Highlight

Gold

#D4AF37

Only for

- Awards
- Achievements
- Important badges

Never use Gold as the primary color.



## Background

White

#FFFFFF



## Surface

Light Gray

#F8FAFC



## Border

#E2E8F0



## Text Primary

#0F172A



## Text Secondary

#64748B



## Success

#16A34A



## Warning

#D97706



## Error

#DC2626



# Dark Mode

Background

#020617

Surface

#0F172A

Text

#E2E8F0

Accent

#3B82F6

Dark mode should feel premium instead of high contrast.



# Typography

## Heading Font

Plus Jakarta Sans

Fallback

Inter

sans-serif



## Body Font

Inter

sans-serif



## Monospace

JetBrains Mono



# Font Weight

Regular

400

Medium

500

SemiBold

600

Bold

700

Avoid using ExtraBold.



# Heading Scale

H1

48px

Desktop

40px Tablet

32px Mobile



H2

36px



H3

30px



H4

24px



H5

20px



H6

18px



Body

16px



Small

14px



Caption

13px



# Line Height

Heading

1.2

Body

1.7



# Spacing System

Use 8px spacing scale.

Allowed spacing

4

8

16

24

32

40

48

64

80

96

120

160

Avoid arbitrary values.



# Border Radius

Buttons

12px

Cards

16px

Images

16px

Badges

999px

Avoid sharp edges.



# Shadow System

Only subtle shadows.

Example

Small

0 2px 8px rgba(15,23,42,0.06)

Medium

0 8px 24px rgba(15,23,42,0.08)

Large

0 16px 48px rgba(15,23,42,0.10)

Never use heavy shadows.



# Buttons

Primary

Solid Navy

Hover

Royal Blue

Secondary

Outline

Ghost

Transparent

Rules

Only one Primary CTA per section.

Avoid multiple competing actions.



# Icons

Use Bootstrap Icons.

Never mix multiple icon libraries.

Icons should always match surrounding typography.



# Cards

Cards should

- Feel lightweight
- Have generous spacing
- Have subtle borders
- Have subtle shadows

Cards should NOT

- Have gradients
- Have glowing borders
- Have thick borders



# Images

Use rounded corners.

Use optimized images.

Always lazy load.

Always include alt text.

Prefer WebP whenever possible.



# Sections

Every section should follow

Section Title

↓

Short Description

↓

Content

↓

CTA (optional)

Never start a section directly with cards.



# Layout

Maximum container

1320px

Standard Bootstrap container.

Do not create custom widths unless necessary.



# Grid

Bootstrap Grid

12 Columns

Always use responsive breakpoints.



# Navigation

Sticky

Transparent at top

Solid background after scroll

Simple

Minimal

No mega menu

No excessive dropdowns



# Hero Section

Layout

Two Columns

Left

- Greeting
- Name
- Professional Titles
- Short Introduction
- Primary CTA
- Secondary CTA
- Social Links

Right

Professional Portrait

Floating Achievement Cards

The Hero must contain the only H1 of the page.



# Service Cards

Include

Icon

Title

Short Description

CTA

Avoid long paragraphs.



# Project Cards

Include

Cover Image

Title

Short Description

Technology Stack

GitHub Button

Live Demo Button



# Blog Cards

Include

Cover Image

Category

Publish Date

Reading Time

Title

Excerpt

Read More



# Timeline

Vertical layout

Chronological

Minimal

Readable

No unnecessary decorations.



# Statistics

Large Number

Small Description

Simple Icons

High contrast



# Footer

Minimal

Professional

Organized

Include

Navigation

Social Links

Contact

Copyright



# Animations

Allowed

Fade

Slide

Scale

Duration

200ms

250ms

300ms

Never exceed 400ms.

Avoid distracting animations.



# Responsive Strategy

Mobile First

Breakpoints

xs

sm

md

lg

xl

xxl

Avoid desktop-first layouts.



# Accessibility

Minimum contrast ratio

WCAG AA

Visible focus

Keyboard navigation

ARIA labels when needed



# UI Principles

Every page should feel

Simple

Elegant

Organized

Comfortable

Readable

Professional

Every component should have a clear purpose.

Nothing should exist only for decoration.



# Definition of Good Design

Good design is measured by

- Clarity
- Readability
- Accessibility
- Performance
- Maintainability

NOT by

- Fancy animations
- Bright colors
- Complex effects
- Visual noise
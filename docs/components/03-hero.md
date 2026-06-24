=== FILE: docs/components/03-hero.md ===

---
title: Hero Component
component: Hero
version: 1.0.0
status: Stable
priority: Highest
---

# Purpose

The Hero section is the most important component of the entire website.

Visitors should understand within the first 5 seconds

- Who Hoàng Hùng Anh is
- What he does
- Why they should trust him
- What action they should take next

The Hero is responsible for making a strong first impression and increasing conversion.



# Business Goal

The Hero should convert visitors into potential clients.

Primary objectives

- Build credibility
- Communicate expertise
- Showcase professionalism
- Encourage users to explore
- Generate freelance leads
- Generate mentoring leads



# User Goal

After reading the Hero, users should immediately know

✓ This person is a Software Engineer.

✓ This person provides freelance services.

✓ This person mentors students.

✓ This person has real achievements.

✓ This is someone worth contacting.



# Database Mapping

Model

Hero

Fields

avatar

title

subtitle

description

resume

background_image

cta1

cta2

Future Fields

typing_titles

years_of_experience

github_url

linkedin_url

email

status



# Template Mapping

```
templates/components/hero.html
```

CSS

```
static/css/components/hero.css
```

JavaScript

```
static/js/components/hero.js
```

No business logic should exist inside the template.



# Layout

Desktop

```
---------------------------------------------------

LEFT                     RIGHT

Greeting                 Portrait

H1                       Floating Cards

Subtitle

Description

CTA Buttons

Social Links

---------------------------------------------------
```

Desktop Ratio

```
6 / 6
```

Tablet

```
12

12
```

Mobile

Everything becomes

```
Single Column
```

Portrait moves below the CTA.



# Bootstrap Layout

Preferred Structure

```
container

↓

row align-items-center

↓

col-lg-6

↓

col-lg-6
```

Avoid custom flex layouts.



# Component Tree

```
Hero

├── Greeting

├── Main Heading

├── Subtitle

├── Description

├── CTA Group

├── Social Links

└── Portrait Area

        ├── Avatar

        ├── Achievement Card

        ├── Project Counter

        └── Experience Badge
```



# Greeting

Small text

Example

```
Hello, I'm
```

Purpose

Humanize the page.

Do not overuse animations.



# Main Heading

This is the ONLY H1 on the homepage.

Example

```
Hoàng Hùng Anh
```

Never split the H1 across multiple elements.

Never use multiple H1 tags.



# Professional Titles

Displayed directly below the H1.

Examples

Software Engineer

Backend Developer

AI Developer

Competitive Programming Mentor

STEM Educator

Do not list more than four titles.



# Subtitle

One concise sentence describing long-term value.

Example

```
Building scalable software, empowering future engineers and delivering impactful technical education.
```

Maximum

2 lines

Avoid buzzwords.



# Description

Should answer

Who

What

Why

Maximum

3–4 lines

Example

```
I build scalable web applications, mentor students for scholarships and competitive programming, and collaborate with organizations to deliver impactful STEM education.
```



# CTA Buttons

Exactly two buttons.

Primary

```
Hire Me
```

Secondary

```
View Portfolio
```

Avoid adding more buttons.

Primary button must use Accent Color.

Secondary button should be outline style.



# Resume Button

Resume download should NOT appear in Hero.

Place it inside

About Page

or

Navigation

Reason

Reduce decision fatigue.



# Social Links

Display

GitHub

LinkedIn

Facebook

Email

Future

YouTube

Medium

Icons only.

Do not use large buttons.



# Portrait

Professional headshot.

Requirements

Clean background

High resolution

Neutral expression

Business casual attire

Never use casual selfies.



# Portrait Style

Rounded corners

16px radius

Soft shadow

No border

No decorative frame.



# Floating Cards

Purpose

Increase credibility.

Maximum

3 cards.

Examples

```
5+

Years Coding
```

```
20+

Projects
```

```
100+

Students Mentored
```

Keep cards subtle.

Avoid visual clutter.



# Background

White

or

Very Light Surface

Avoid

Heavy gradients

Dark hero

Illustrations

Particles

Animated backgrounds



# Spacing

Desktop

Top Padding

120px

Bottom Padding

120px

Mobile

80px

Keep generous whitespace.



# Typography

Greeting

16px

Medium

H1

48px

Bold

Subtitle

24px

Medium

Description

18px

Regular



# Color Usage

Greeting

Secondary Text

H1

Primary Color

Subtitle

Slate

Description

Secondary Text

Primary CTA

Royal Blue

Secondary CTA

Outline Navy



# Animation

Allowed

Fade In

Slide Up

Duration

250ms

Portrait may animate slightly after text.

Avoid sequential animations longer than one second.



# Responsive Rules

Desktop

Two Columns

Tablet

Portrait below content

Mobile

Single Column

Centered

Buttons become full width.



# Accessibility

Avatar

Must include meaningful alt text.

Buttons

Must have descriptive labels.

Keyboard navigation

Required.

Decorative cards

Should be ignored by screen readers when appropriate.



# SEO

The Hero contains

One H1

Primary keywords

Clear introduction

Descriptive text

Never use images instead of text.

Search engines must understand the Hero without CSS.



# AI Optimization

The Hero should clearly answer

Who is Hoàng Hùng Anh?

What services does he provide?

Why is he qualified?

What should users do next?

Avoid vague marketing language.

Prefer factual, descriptive content.



# Performance

Portrait

Optimized

WebP preferred

Lazy loading

Disabled

Reason

Hero image is above the fold.

Avoid oversized assets.

Target image size

Less than 300KB.



# Future Enhancements

Possible additions

Typing Effect

Availability Badge

Current Location

Client Logos

Animated Statistics

These should remain optional.



# Do

✓ One H1

✓ Clear professional positioning

✓ Strong CTA

✓ Responsive

✓ Professional portrait

✓ Clean whitespace

✓ Semantic HTML

✓ Fast loading

✓ Database-driven content



# Don't

✗ Use sliders

✗ Use carousels

✗ Use background videos

✗ Use neon colors

✗ Use glassmorphism

✗ Add more than two CTA buttons

✗ Add unnecessary animations

✗ Overwrite Bootstrap layout



# Definition of Done

The Hero component is complete only if

✓ Database Driven

✓ Responsive

✓ Semantic HTML

✓ Bootstrap Based

✓ Accessible

✓ SEO Friendly

✓ AI Optimized

✓ High Performance

✓ Reusable

✓ Production Ready

✓ Matches Design System

✓ Consistent with Personal Brand
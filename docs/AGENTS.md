=== FILE: AGENTS.md ===

---
title: AI Development Rules
project: Personal Brand Platform
version: 1.0.0
status: Stable
last_updated: 2026-06
---

# AGENTS.md

## Purpose

This file is the single source of truth for every AI coding agent working on this project.

Every implementation MUST follow the rules defined in this file.

If any instruction from prompts conflicts with this file, this file has higher priority.

This project is intended to become a long-term production-ready personal branding platform.

It is NOT a tutorial project.

It is NOT a UI experiment.

It is NOT a playground.

Every decision should prioritize maintainability, scalability, SEO, AI optimization, accessibility and performance.



# Project Goal

The website represents the personal brand of Hoàng Hùng Anh.

Main objectives:

- Build a premium personal portfolio.
- Sell freelance software development services.
- Sell mentoring services.
- Publish technical blogs.
- Showcase achievements.
- Showcase portfolio projects.
- Build trust.
- Generate inbound leads.
- Become highly indexable by both search engines and AI search systems.



# Target Audience

Primary

- Companies looking for freelance developers
- Startup founders
- Technical recruiters
- Scholarship applicants
- Competitive programming students
- STEM organizations
- Universities

Secondary

- Developers
- Students
- Technical communities



# Core Philosophy

Everything should prioritize:

1. Clarity
2. Maintainability
3. Performance
4. Accessibility
5. Semantic HTML
6. SEO
7. AI Optimization
8. Reusability
9. Clean Architecture
10. Long-term scalability

Never sacrifice code quality for short-term convenience.



# Tech Stack

Backend

- Django
- PostgreSQL (Neon)
- Cloudinary
- TinyMCE

Frontend

- HTML5
- CSS3
- Bootstrap 5

Deployment

- Gunicorn
- WhiteNoise
- Nginx
- Docker (future)



# Architecture

The project follows modular Django architecture.

Apps

- common
- accounts
- core
- services
- portfolio
- blog
- contact

Business logic must stay inside its own application.

Avoid cross-app coupling whenever possible.



# Coding Principles

MUST

- Write clean and readable code.
- Keep functions small.
- Keep templates reusable.
- Prefer composition over duplication.
- Keep business logic inside Django.
- Use reusable components.
- Follow Django best practices.
- Write semantic HTML.
- Write accessible markup.

SHOULD

- Keep files organized.
- Use descriptive variable names.
- Keep CSS modular.
- Keep JavaScript minimal.

MUST NOT

- Duplicate code.
- Hardcode business content.
- Write inline CSS.
- Write inline JavaScript.
- Mix business logic inside templates.
- Create unnecessary abstractions.
- Create giant templates.



# Design Philosophy

The visual style is

Modern Academic Luxury

Inspired by

- Apple
- Stripe
- Linear
- Vercel
- Notion
- Harvard
- MIT

The interface should communicate

Professional

Elegant

Minimal

Premium

Trustworthy

Calm

Confident

The interface must NEVER feel

Flashy

Immature

Overdesigned

Gaming

Cyberpunk

Neon

Glass-heavy



# Frontend Rules

Always

- Responsive
- Mobile First
- Semantic HTML
- Bootstrap utilities first
- Component based
- Accessible
- Fast loading

Never

- Deep nesting
- Inline CSS
- Inline JavaScript
- Fixed pixel layouts
- Multiple H1 elements



# HTML Rules

Always use semantic elements whenever possible.

Prefer

<header>

<nav>

<main>

<section>

<article>

<aside>

<footer>

Avoid meaningless nested div structures.



# SEO Rules

Every page MUST contain

- One H1
- Proper heading hierarchy
- Meta title
- Meta description
- Canonical URL
- Open Graph tags
- Twitter Card tags

Every image MUST include

- alt attribute

Every page SHOULD include

Structured Data whenever applicable.



# AI Optimization Rules

The website should be easy for both humans and AI systems to understand.

Use

- clear headings
- semantic HTML
- descriptive links
- structured content
- meaningful section names

Avoid

generic titles

generic buttons

meaningless wrappers

ambiguous content



# Performance Rules

Always

- Compress images
- Lazy load images
- Optimize CSS
- Optimize JS
- Minimize HTTP requests

Avoid unnecessary animations.

Performance is more important than visual effects.



# Bootstrap Rules

Bootstrap is the primary UI framework.

Always

- Use Bootstrap Grid
- Use Bootstrap spacing utilities
- Use Bootstrap Flex utilities

Only create custom CSS when Bootstrap cannot solve the problem.



# Components

Every UI block should become an independent reusable component.

Examples

Navbar

Hero

Section Title

Buttons

Cards

Timeline

Statistics

Service Card

Project Card

Blog Card

Footer

CTA Banner

Components should never depend on page-specific code.



# Django Templates

Always

Extend base.html

Split reusable components into

templates/components/

Avoid duplicate HTML.



# Database Rules

The database schema has been finalized.

Do not redesign models unless a real business requirement appears.

Never create duplicate models.

Prefer extending existing models over creating new ones.



# Content Rules

Content should be

Professional

Educational

Helpful

Trustworthy

Evidence-based

Avoid marketing buzzwords.

Avoid exaggerated claims.

Never fake achievements.



# Accessibility

Always

Keyboard friendly

High contrast

Proper labels

Proper aria attributes when needed

Visible focus states

Readable typography



# Animations

Allowed

Fade

Slide

Scale

Duration

200–350ms

Never use

Bounce

Rotate

Heavy Parallax

Overly complex motion



# Git Rules

Commit messages should be meaningful.

Example

feat: add hero component

fix: improve navbar responsiveness

refactor: simplify service cards



# Before Creating New Code

Always ask

Can this be reused?

Can Bootstrap already solve this?

Can an existing component solve this?

Does this improve SEO?

Does this improve accessibility?

Does this improve maintainability?



# Definition of Done

A feature is considered complete only if

✓ Responsive

✓ Accessible

✓ SEO friendly

✓ AI optimized

✓ Uses semantic HTML

✓ Uses reusable components

✓ Clean Django implementation

✓ No duplicated code

✓ Production ready
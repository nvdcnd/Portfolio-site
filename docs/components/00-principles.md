=== FILE: docs/components/00-principles.md ===

---
title: Component Principles
version: 1.0.0
status: Stable
---

# Purpose

This document defines the universal rules that apply to every frontend component in this project.

Every component MUST follow these principles.

These rules have higher priority than individual component documentation.



# Philosophy

Components are building blocks.

A component should solve one problem.

A component should not know anything about the page that uses it.

Components should be reusable.

Components should be predictable.

Components should be composable.



# Single Responsibility

Every component should have only one responsibility.

Examples

Navbar

Navigation

Hero

Introduction

Service Card

Display one service

Project Card

Display one project

Blog Card

Display one article

Footer

Site information

Avoid components that try to solve multiple business problems.



# Reusability

Before creating a new component ask

Can an existing component solve this?

If yes

Reuse it.

Never duplicate HTML.



# Component Independence

A component should never depend on

A specific page

A specific route

A specific project

Hardcoded content

Business-specific values

Components receive data.

Components should not create data.



# Semantic HTML

Every component should use semantic HTML.

Prefer

<header>

<nav>

<section>

<article>

<footer>

<aside>

Avoid unnecessary div wrappers.



# Bootstrap First

Bootstrap is always the first choice.

Use Bootstrap utilities whenever possible.

Only write custom CSS when Bootstrap cannot achieve the desired design.



# CSS Rules

Each component owns its CSS.

Example

hero.css

navbar.css

cards.css

forms.css

Never place component-specific styles inside page CSS.



# JavaScript Rules

JavaScript is optional.

Use JavaScript only when necessary.

Examples

Navbar scroll state

Carousel

Theme switch

Dropdown

Avoid JavaScript-only interfaces.



# Naming

Templates

snake_case

hero.html

project_card.html

blog_card.html

CSS

kebab-case

.hero

.project-card

.blog-card

JavaScript

camelCase

toggleNavbar()

updateTheme()



# Responsive

Every component must support

Desktop

Tablet

Mobile

Mobile First

Never design desktop only.



# Accessibility

Every component must

Support keyboard navigation

Have proper focus state

Support screen readers

Use aria attributes where appropriate

Never rely only on color.



# SEO

Every component should contribute positively to SEO.

Examples

Meaningful headings

Descriptive links

Alt text

Semantic markup



# AI Optimization

Every component should expose clear meaning.

Avoid

Generic wrappers

Meaningless text

Vague labels

Prefer

Clear titles

Descriptive buttons

Logical hierarchy



# Performance

Every component should

Avoid unnecessary DOM nodes

Avoid large images

Lazy load media

Minimize CSS

Minimize JavaScript



# Animation

Animation is optional.

Allowed

Fade

Slide

Scale

200–300ms

Avoid

Bounce

Rotate

Infinite animation

Heavy parallax



# Content

Content should

Educate

Build trust

Communicate value

Avoid

Marketing hype

Buzzwords

Clickbait



# Visual Consistency

Every component must follow

The design system

Spacing system

Typography system

Color system

Border radius

Shadow system

Never invent new visual styles.



# Error Handling

Components should fail gracefully.

Missing image

↓

Placeholder

Missing description

↓

Hide section

Missing button

↓

Collapse layout

Never break the page.



# Maintainability

A developer should understand a component in less than five minutes.

If a component becomes too large

Split it.



# Definition of Done

A component is complete only if

✓ Responsive

✓ Accessible

✓ Semantic

✓ Bootstrap-based

✓ Reusable

✓ SEO friendly

✓ AI friendly

✓ Performance optimized

✓ Matches Design System

✓ No duplicated code
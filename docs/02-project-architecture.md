=== FILE: docs/02-project-architecture.md ===

---
title: Project Architecture
version: 1.0.0
status: Stable
---

# Project Architecture

## Purpose

This document defines the technical architecture of the project.

Every developer and AI agent MUST follow this architecture.

Do not introduce new structures unless a strong business reason exists.



# Architecture Philosophy

The project follows

- Django Best Practices
- Modular Architecture
- Reusable Components
- Thin Views
- Fat Models (when appropriate)
- Separation of Concerns
- Scalable Folder Structure

The goal is long-term maintainability rather than short-term convenience.



# Technology Stack

Backend

- Django
- PostgreSQL (Neon)
- Cloudinary
- TinyMCE

Frontend

- HTML5
- CSS3
- Bootstrap 5

Storage

- Cloudinary

Database

- PostgreSQL

Deployment

- WhiteNoise
- Gunicorn
- Nginx
- Docker (future)



# Root Structure

```
project_root/

│

├── apps/

├── config/

├── docs/

├── static/

├── templates/

├── media/

├── requirements/

├── manage.py

├── README.md

└── AGENTS.md
```

Never place application logic inside the project root.



# Apps

```
apps/

accounts/

blog/

common/

contact/

core/

portfolio/

services/
```

Each app is responsible for one business domain.

Never mix unrelated business logic.



# Responsibilities

## accounts

Responsible for

- Authentication
- User Profile
- Permissions

Must NOT contain

- Portfolio
- Blog
- Services



## core

Responsible for

Homepage

Hero

Statistics

Timeline

Awards

Testimonials

Site Settings



## services

Responsible for

Freelance Services

Mentoring

Consulting

Speaking

Teaching



## portfolio

Responsible for

Projects

Project Categories

Project Images

Technologies

Case Studies



## blog

Responsible for

Articles

Categories

Tags

Authors

SEO



## contact

Responsible for

Contact Form

Messages

Business Inquiries



## common

Reusable utilities

Mixins

Validators

Template Tags

Context Processors

Shared Models (if necessary)



# Internal App Structure

Each app should follow

```
app/

admin.py

apps.py

models.py

views.py

urls.py

forms.py

signals.py

tests.py

services.py

utils.py

migrations/

templates/

static/
```

Do not create unnecessary files.

Only add new modules when required.



# Template Structure

```
templates/

base.html

layouts/

components/

pages/

partials/
```

Never place all templates in one folder.



# Layouts

```
templates/layouts/

default.html

dashboard.html
```

Layouts define page skeletons.

Pages extend layouts.



# Components

```
templates/components/

navbar.html

footer.html

hero.html

section_title.html

service_card.html

project_card.html

blog_card.html

timeline_item.html

stat_card.html

testimonial_card.html

cta_banner.html
```

Components must be reusable.

Never duplicate component markup.



# Pages

```
templates/pages/

home.html

about.html

services.html

portfolio.html

blog.html

contact.html
```

Pages should assemble components.

Pages should not contain repeated HTML.



# Static Structure

```
static/

css/

js/

images/

fonts/

icons/
```



# CSS Structure

```
static/css/

base/

components/

layout/

pages/

utilities/
```

Example

```
base/

reset.css

variables.css

typography.css

base.css
```



Components

```
components/

buttons.css

cards.css

navbar.css

footer.css

forms.css

timeline.css

hero.css
```



Pages

```
pages/

home.css

blog.css

portfolio.css

services.css

contact.css
```



Utilities

```
utilities/

spacing.css

helpers.css

animations.css
```

Avoid creating one massive stylesheet.



# JavaScript Structure

```
static/js/

main.js

components/

pages/
```

Examples

```
components/

navbar.js

theme.js

carousel.js
```

Pages

```
pages/

home.js

blog.js
```

JavaScript should enhance the experience.

Never rely on JavaScript for essential content.



# Images

```
static/images/

icons/

logos/

illustrations/

placeholders/
```

User-uploaded images belong to Cloudinary.

Static images belong in static.



# Django Views

Views should remain thin.

Responsibilities

- Receive request
- Validate
- Query models
- Render template

Do not place business logic inside views.



# Models

Models are responsible for

Business rules

Validation

Relationships

Computed properties

Never place presentation logic inside models.



# Forms

Every form belongs to its application.

Examples

ContactForm

NewsletterForm

CommentForm

Never validate forms inside templates.



# URLs

Each app owns its own URLs.

Project URLs only include app URLs.

Example

```
config/urls.py

↓

apps/blog/urls.py

↓

views.py
```

Avoid large centralized URL files.



# Context Processors

Use only for truly global data.

Examples

- Site Settings
- Navigation
- Social Links

Never abuse context processors.



# Template Inheritance

Hierarchy

```
base.html

↓

layout.html

↓

page.html

↓

components
```

Avoid deep inheritance chains.



# Bootstrap Usage

Bootstrap is the default UI framework.

Use Bootstrap for

- Grid
- Flex
- Spacing
- Responsive Utilities

Avoid rewriting Bootstrap functionality.



# Custom CSS

Only create custom CSS when

Bootstrap cannot achieve the design.

Avoid unnecessary utility classes.



# Business Logic

Business logic belongs inside

- Models
- Services
- Utility modules

Never inside templates.



# Template Logic

Templates may

- Display data
- Loop
- Render conditions

Templates must NOT

- Execute business rules
- Query database
- Perform calculations



# Naming Convention

Templates

snake_case

Example

```
project_card.html
```

CSS

kebab-case

Example

```
project-card
```

Python

snake_case

Models

PascalCase

Example

ProjectCategory

Variables

snake_case



# Media

User uploaded files

Cloudinary

Never store uploaded media inside Git.



# Security

Never expose

Secret Keys

Database URLs

API Keys

Never commit .env files.



# Performance

Always

Reuse templates

Reuse components

Lazy load images

Compress assets

Minimize DOM complexity



# Reusability Rules

Before creating a new component ask

Can an existing component solve this?

If yes

Reuse it.

Do not duplicate markup.



# Future Scalability

The architecture should support

- Multiple services
- Hundreds of blog posts
- Hundreds of portfolio projects
- Multiple languages (future)
- Search (future)
- CMS expansion (future)



# Definition of Good Architecture

A good architecture

- Is understandable
- Is modular
- Is scalable
- Is reusable
- Is predictable

Every file should have one clear responsibility.

Every folder should have one clear purpose.
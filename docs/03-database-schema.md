---
title: Database Schema Specification
version: 1.0.0
status: Stable
---

# Purpose

This document defines the complete relational database schema of the Personal Brand website.

It acts as the single source of truth for the database layout, models, relationships, and business validations.

Every model definition and backend query MUST conform to this specification.



# Architecture Philosophy

The database is built on:

- PostgreSQL (hosted on Neon)

- Cloudinary (for ImageField storage)

- TinyMCE HTML fields (for rich text)

- Modular design using modular Django applications.



# Model Inheritance Patterns

All models inherit from common base helper models to enforce consistent tracking and audit metadata.

TimeStampedModel (Abstract)

- `created_at` (DateTimeField, auto_now_add=True)

- `updated_at` (DateTimeField, auto_now=True)

PublishableModel (Abstract)

- Inherits: TimeStampedModel

- `is_published` (BooleanField, default=True)

OrderableModel (Abstract)

- Inherits: TimeStampedModel

- `display_order` (PositiveIntegerField, default=0)



# Module: common (Global Site Settings)

This application stores global site settings, contact profiles, links, and SEO defaults.

Footer

- Inherits: TimeStampedModel

- `content` (TextField)

- `is_active` (BooleanField, default=True)

SEOSettings

- Inherits: TimeStampedModel

- `meta_title` (CharField, max_length=255)

- `meta_description` (TextField)

- `meta_keywords` (TextField)

- `is_active` (BooleanField, default=True)

SocialMediaLink

- Inherits: TimeStampedModel

- `platform_name` (CharField, max_length=255)

- `profile_url` (URLField)

- `icon_class` (CharField, max_length=255)

- `is_active` (BooleanField, default=True)

ContactInfo

- Inherits: TimeStampedModel

- `email` (EmailField)

- `phone_number` (CharField, max_length=20)

- `address` (TextField)

- `is_active` (BooleanField, default=True)

GeneralSettings

- Inherits: TimeStampedModel

- `site_name` (CharField, max_length=255)

- `site_logo` (ImageField, upload_to='site_logo/')

- `favicon` (ImageField, upload_to='favicon/')

- `is_active` (BooleanField, default=True)

AnalyticsSettings

- Inherits: TimeStampedModel

- `google_analytics_id` (CharField, max_length=255, blank=True, null=True)

- `facebook_pixel_id` (CharField, max_length=255, blank=True, null=True)

- `is_active` (BooleanField, default=True)



# Module: core (Homepage & Authority)

This application stores content blocks displayed primarily on the homepage.

Hero

- Inherits: TimeStampedModel

- `avatar` (ImageField, upload_to='avatars/')

- `title` (TextField)

- `subtitle` (TextField)

- `description` (tinymce.HTMLField)

- `resume_file` (FileField, upload_to='resume/')

- `background_image` (ImageField, upload_to='background/')

- `cta1_text` (CharField, max_length=255)

- `cta2_text` (CharField, max_length=255)

- `cta1_link` (URLField)

- `cta2_link` (URLField)

- `greeting` (CharField, max_length=255)

- `badge_text` (CharField, max_length=255)

- `is_active` (BooleanField, default=True)

Statistic

- Inherits: TimeStampedModel

- `icon_class` (CharField, max_length=255)

- `title` (CharField, max_length=255)

- `value` (CharField, max_length=255)

- `suffix` (CharField, max_length=50, blank=True, null=True)

- `is_active` (BooleanField, default=True)

- `display_order` (PositiveIntegerField, default=0)

Title (Professional Positions)

- Inherits: TimeStampedModel

- `text` (CharField, max_length=255)

- `organization` (CharField, max_length=255, blank=True, null=True)

- `year` (PositiveIntegerField, blank=True, null=True)

- `url` (URLField, blank=True, null=True)

- `description` (TextField, blank=True, null=True)

- `is_active` (BooleanField, default=True)

- `display_order` (PositiveIntegerField, default=0)

Timeline (Resume chronological records)

- Inherits: TimeStampedModel

- `title` (CharField, max_length=255)

- `organization` (CharField, max_length=255, blank=True, null=True)

- `year` (PositiveIntegerField, blank=True, null=True)

- `start_date` (DateField, blank=True, null=True)

- `end_date` (DateField, blank=True, null=True)

- `is_current` (BooleanField, default=False)

- `location` (CharField, max_length=255, blank=True, null=True)

- `url` (URLField, blank=True, null=True)

- `type` (CharField, choices=[('education', 'Education'), ('experience', 'Experience')], max_length=50)

- `description` (TextField, blank=True, null=True)

- `is_active` (BooleanField, default=True)

- `display_order` (PositiveIntegerField, default=0)



# Module: services (Offerings & Proof)

This application stores data relating to services (Freelance, Mentoring, Consulting) and validation proof.

ServiceCategory

- Inherits: TimeStampedModel

- `name` (CharField, max_length=255)

- `slug` (SlugField, unique=True)

- `description` (TextField)

- `is_active` (BooleanField, default=True)

- `display_order` (PositiveIntegerField, default=0)

Services

- Inherits: TimeStampedModel

- `title` (CharField, max_length=255)

- `description` (tinymce.HTMLField)

- `slug` (SlugField, unique=True)

- `short_description` (TextField)

- `icon_class` (CharField, max_length=255)

- `featured` (BooleanField, default=False)

- `image` (ImageField, upload_to='ai_development/')

- `is_active` (BooleanField, default=True)

- `category` (ForeignKey to ServiceCategory, related_name='services', on_delete=CASCADE)

- `display_order` (PositiveIntegerField, default=0)

FAQ

- Inherits: TimeStampedModel

- `question` (CharField, max_length=255)

- `answer` (TextField)

- `service` (ForeignKey to Services, related_name='faqs', on_delete=CASCADE)

- `is_active` (BooleanField, default=True)

- `display_order` (PositiveIntegerField, default=0)

Testimonial

- Inherits: TimeStampedModel

- `name` (CharField, max_length=255)

- `title` (CharField, max_length=255)

- `company` (CharField, max_length=255, blank=True, null=True)

- `testimonial` (TextField)

- `image` (ImageField, upload_to='testimonials/')

- `is_active` (BooleanField, default=True)

- `display_order` (PositiveIntegerField, default=0)



# Module: portfolio (Engineering Showcase)

This application stores information about software products, tools, and technical skills.

ProjectCategory

- Inherits: TimeStampedModel

- `name` (CharField, max_length=255)

- `slug` (SlugField, unique=True)

- `description` (TextField)

- `is_active` (BooleanField, default=True)

- `display_order` (PositiveIntegerField, default=0)

Skill (Tech Stack)

- Inherits: TimeStampedModel

- `name` (CharField, max_length=255)

- `proficiency` (PositiveIntegerField)

- `icon_class` (CharField, max_length=255)

- `is_active` (BooleanField, default=True)

- `display_order` (PositiveIntegerField, default=0)

Project

- Inherits: TimeStampedModel

- `title` (CharField, max_length=255)

- `description` (tinymce.HTMLField)

- `slug` (SlugField, unique=True)

- `short_description` (TextField)

- `image` (ImageField, upload_to='projects/')

- `is_active` (BooleanField, default=True)

- `category` (ForeignKey to ProjectCategory, related_name='projects', on_delete=CASCADE)

- `skills` (ManyToMany to Skill, related_name='projects')

- `display_order` (PositiveIntegerField, default=0)

Image (Project detailed gallery)

- Inherits: TimeStampedModel

- `project` (ForeignKey to Project, related_name='images', on_delete=CASCADE)

- `image` (ImageField, upload_to='project_images/')

- `caption` (CharField, max_length=255, blank=True, null=True)

- `is_active` (BooleanField, default=True)

- `display_order` (PositiveIntegerField, default=0)



# Module: blog (Technical Writing)

This application stores technical blog articles, categorizations, and tags.

PostCategory

- Inherits: TimeStampedModel

- `name` (CharField, max_length=255)

- `slug` (SlugField, unique=True)

- `description` (tinymce.HTMLField)

- `is_active` (BooleanField, default=True)

- `display_order` (PositiveIntegerField, default=0)

Tag

- Inherits: TimeStampedModel

- `name` (CharField, max_length=255)

- `slug` (SlugField, unique=True)

- `is_active` (BooleanField, default=True)

- `display_order` (PositiveIntegerField, default=0)

Post

- Inherits: TimeStampedModel

- `title` (CharField, max_length=255)

- `slug` (SlugField, unique=True)

- `content` (tinymce.HTMLField)

- `category` (ForeignKey to PostCategory, related_name='posts', on_delete=CASCADE)

- `tags` (ManyToMany to Tag, related_name='posts')

- `is_active` (BooleanField, default=True)

- `display_order` (PositiveIntegerField, default=0)



# Validation & Constraints

Slug Formats

- Slugs must contain only lowercase letters, numbers, and hyphens (`-`).

- Slugs must be generated automatically in the Django admin panel from the title/name.

Proficiency Levels

- Skill proficiency value must be restricted between 0 and 100 representing percentage.

Ordering

- Default model querying must always order records by `display_order` ascending, then `created_at` descending.

Status

- All views must filter records by `is_active=True` (or `is_published=True`) to ensure unreleased content remains invisible.



# Relational Database Constraints

On Delete Cascades

- Category deletion will cascade-delete dependent projects or blog posts (`on_delete=models.CASCADE`).

- Project deletion will cascade-delete dependent gallery images.

M2M Relationships

- Post tags and Project skills utilize standard join tables managed by Django ORM.



# Definition of Done for Schema Updates

- All model changes require the generation of migration files (`makemigrations`).

- All migration files must be committed to git.

- Seed scripts (fixtures) must be updated to align with the new model schema.

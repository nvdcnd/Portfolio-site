---
title: SEO & AI Optimization Standards
version: 1.0.0
status: Stable
---

# Purpose

This document defines the technical rules and metadata standards for SEO and AI Search Optimization.

It ensures that both traditional search engines (Google, Bing) and AI search engines (ChatGPT, Gemini, Claude, Perplexity) index and understand site content accurately.

Every page template and view context must align with these guidelines.



# Core SEO Objectives

- Page Indexability: Ensure all pages are fully crawlable without client-side JS rendering.

- Semantic Hierarchy: Enforce strict heading levels across all templates.

- Page Speed: Target Mobile Lighthouse performance scores above 90.

- Rich Snippets: Generate structured data schemas to display search rich results.



# Core AI Optimization Objectives

- LLM Readability: Format markup so text extractors easily summarize credentials.

- Entity Association: Explicitly link Hoàng Hùng Anh (Entity) to specific skills, services, and projects.

- Answer Engine Optimization (AEO): Provide clear, direct, and factual answers to probable user queries.



# Page Title & Meta Rules

Format for Titles

- `[Page Keyword/Title] | Hoàng Hùng Anh`

- Keep under 60 characters to prevent truncation in search result pages.

Meta Descriptions

- Write unique, active description text between 120 and 150 characters.

- Summarize the value proposition of the specific page.

Canonical URL

- Every page must contain a canonical link tag: `<link rel="canonical" href="{{ request.build_absolute_uri }}">`.



# Semantic Heading Structure

Only One H1 Tag

- The home page and internal detail pages must have exactly one `<h1>`.

- The `<h1>` must contain primary target keywords.

Section Headings

- Use `<h2>` for major page sections.

- Use `<h3>` for component card headings.

- Never skip heading levels (e.g. H2 directly to H5).



# Structured Data (JSON-LD)

Structured data must be injected into the `<head>` of templates via `<script type="application/ld+json">`.

Person Schema (Home / About)

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Hoàng Hùng Anh",
  "jobTitle": "Software Engineer",
  "url": "https://hoanghunganh.dev",
  "sameAs": [
    "https://github.com/hoanghunganh",
    "https://linkedin.com/in/hoanghunganh"
  ]
}
```

ProfessionalService Schema (Services)

- Details service locations, pricing, and specific offerings (Freelance development, Mentorship).

TechArticle Schema (Blog detail)

- Details publish dates, author, publisher, and keywords.



# OpenGraph & Twitter Cards

Metadata tags in `<head>` must support clean social media previews.

Required Tags

- `og:type` (website or article)

- `og:title` (page title)

- `og:description` (meta description)

- `og:image` (preview cover image url)

- `og:url` (absolute URL)

- `twitter:card` (summary_large_image)



# AI Crawling Directives (Robots.txt)

Configure `robots.txt` to explicitly permit friendly AI agents while preventing indexing of staging or administrative sections.

Example Directives

```
User-agent: *
Allow: /
Disallow: /admin/

User-agent: GPTBot
Allow: /

User-agent: ClaudeBot
Allow: /
```



# LLM Context Optimization

Key-Value Clarity

- Use clean, structured list elements for technical stacks to help LLMs parse credentials.

Descriptive Buttons

- Never use "Click Here" or "Read More" alone.

- Prefer "Read Full Article about [Topic]" or "View [Project Name] Case Study".

No Keyword Stuffing

- Write naturally and factually. AI engines recognize and downrank stuffed content.



# Definition of Done for Optimization

✓ Verified using Google Rich Results Test.

✓ Metatags validated using social share debuggers.

✓ Contrast ratios compliant with WCAG AA.

✓ Alt text present on all page images.

✓ HTML validator returns zero syntax errors.

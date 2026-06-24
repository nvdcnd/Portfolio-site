---
title: Blog Card Component
component: BlogCard
version: 1.0.0
status: Stable
---

# Purpose

The Blog Card displays an article excerpt on the homepage or blog index.

It highlights technical writing, ideas, and thought leadership.

It drives visitors to click through and read the full article.



# Business Goal

The Blog Card should:

- Showcase engineering knowledge and deep expertise.

- Improve organic search traffic (SEO) through regular text publication.

- Increase engagement and session duration on the site.

- Provide a funnel for conversion by linking articles to services.



# User Goal

Users should easily:

- Skim through recent technical topics.

- Read the metadata (category, date, read time) to assess relevance.

- Understand the core topic from the excerpt.

- Click to read the full article without friction.



# Database Mapping

Data Source

- apps.blog.models.Post

- apps.blog.models.PostCategory

- apps.blog.models.Tag

Fields Used

- Post: `title`, `slug`, `content` (excerpt generated from content), `created_at` (formatted publish date), `category` (FK to PostCategory), `tags` (ManyToMany to Tag)

- PostCategory: `name`

- Tag: `name`

Future / Calculated Fields

- `read_time` (estimated duration based on word count: words / 200)

- `cover_image` (ImageField for visual card option)



# Template Mapping

Template

```
templates/components/blog_card.html
```

CSS

```
static/css/components/cards.css
```

JavaScript

None.



# Component Structure

```
Blog Card
├── Meta Row
│   ├── Category Badge
│   ├── Publish Date
│   └── Reading Time
├── Title (H3)
├── Excerpt / Summary
├── Tags List (Optional)
└── Read More Link
```



# Layout

Minimalist Text-Only (Default)

- Elegant type-focused card matching Stripe/Vercel styling.

```
--------------------------------------------
  [Category]  •  June 24, 2026  •  5 min read
  
  Article Title: Scalable Django Architecture
  
  An excerpt from the article describing the core 
  architectural patterns used in production-ready 
  Django applications...
  
  [Django] [Backend] [Python]
  
  Read Article ->
--------------------------------------------
```



# Bootstrap Layout

Preferred Structure

```
<article class="card blog-card h-100 border-0 shadow-sm p-4">

    <div class="card-body p-0 d-flex flex-column h-100">

        <!-- Meta Row -->

        <div class="d-flex align-items-center gap-2 text-secondary fs-8 mb-3">

            <span class="badge bg-light text-primary border border-light-subtle rounded-pill px-3 py-1 text-uppercase fs-9">

                {{ post.category.name }}

            </span>

            <span class="meta-separator">•</span>

            <time datetime="{{ post.created_at|date:'Y-m-d' }}">

                {{ post.created_at|date:"M d, Y" }}

            </time>

            <span class="meta-separator">•</span>

            <span>

                {{ post.content|wordcount|divisibleby:200|default:"3" }} min read

            </span>

        </div>

        <!-- Title -->

        <h3 class="card-title h4 font-heading fw-semibold text-dark mb-2">

            <a href="{% url 'blog:detail' post.slug %}" class="text-decoration-none text-dark hover-primary">

                {{ post.title }}

            </a>

        </h3>

        <!-- Excerpt -->

        <p class="card-text text-secondary mb-4 flex-grow-1">

            {{ post.content|striptags|truncatechars:160 }}

        </p>

        <!-- Tags (Optional) -->

        <div class="blog-tags d-flex flex-wrap gap-2 mb-3">

            {% for tag in post.tags.all %}

                <span class="text-secondary fs-8">#{{ tag.name }}</span>

            {% endfor %}

        </div>

        <!-- Read Link -->

        <div class="mt-auto pt-2">

            <a href="{% url 'blog:detail' post.slug %}" class="btn-text text-primary fw-semibold d-inline-flex align-items-center gap-2">

                Read Article

                <i class="bi bi-arrow-right"></i>

            </a>

        </div>

    </div>

</article>
```



# Styling

Card Wrapper

- Background: White `#FFFFFF`

- Border: Slate Border `#E2E8F0` (1px, solid)

- Border Radius: 16px

- Padding: 32px (p-4)

- Hover State: Elevation shadow intensifies, card moves up slightly (`translateY(-4px)`).

Title Hover

- Title text color transitions from Navy `#0F172A` to Royal Blue `#2563EB` on hover.

Meta Spacing

- Separate category, date, and read time with a small dot (`•`) or separator.

- Muted Slate color: `#64748B`.



# Typography

Heading Font

- Plus Jakarta Sans (H3 / 20px)

Body Font

- Inter (15px)

Metadata Font

- Inter (13px / Caption)

Line Height

- Heading: 1.3

- Body: 1.6



# Responsive Rules

Grid Layout (Desktop)

- Blogs align to a 3-column Bootstrap Grid (`col-lg-4`).

Tablet

- 2 columns (`col-md-6`).

Mobile

- 1 column (`col-12`).

- Spacing and borders remain consistent.



# Accessibility

Semantic HTML

- Enclosed in an `<article>` tag.

- Title heading is H3.

- Publish date wrapped in `<time>` element.

Keyboard Navigation

- Focus order: Title Link -> Tag Link (if clickable) -> Read Article Link.

Aria Attributes

- Link should have `aria-label` defining the target.

Example: `aria-label="Read full article: {{ post.title }}"`.



# SEO

- Uses standard `<time>` tag with `datetime` attribute.

- Excerpt text provides valuable density of keywords.

- Article links are fully crawlable by indexers.



# AI Optimization

- The semantic structure clearly groups authors, publish dates, categories, and content keywords.

- Helps AI systems (ChatGPT, Gemini, Perplexity) parse and link technical articles to specific engineering skills.



# Performance

- Text-only design ensures immediate page loading speeds.

- Content length is truncated at database query level or by Django filter to minimize page DOM size.

- Avoid custom icon sets. Use SVG icons for navigation.



# Do

✓ Use Django filters to strip HTML tags from content excerpts

✓ Display readable relative or absolute publish dates

✓ Calculate reading times dynamically (e.g. based on word count)

✓ Ensure title links and read article links have matching hover states

✓ Keep tag lists minimal and focused



# Don't

✗ Leave HTML markup or tags inside excerpt text

✗ Put full article contents in the grid card

✗ Add unnecessary visual dividers inside metadata rows

✗ Use hardcoded links (always use Django `{% url %}`)

✗ Add animations to social sharing icons inside the card list



# Definition of Done

✓ Database Driven (Post model)

✓ Responsive grid layout

✓ Semantic HTML structure (uses <article>, <time>)

✓ Bootstrap card based

✓ Accessible (aria-labels, proper contrast)

✓ SEO optimized markup

✓ AI indexable schema properties

✓ Performance optimized

✓ Reusable template

✓ Production ready

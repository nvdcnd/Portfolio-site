=== FILE: docs/components/04-buttons.md ===

---
title: Buttons Component
component: Buttons
version: 1.0.0
status: Stable
priority: High
---

# Purpose

Buttons represent the primary interaction points throughout the website.

Every button should communicate a clear action.

Buttons should guide users toward meaningful business outcomes instead of creating visual noise.

The entire website should feel focused rather than overloaded with actions.



# Business Goal

Buttons exist to increase conversions.

Primary conversion goals

• Hire Me

• Book Mentoring

• View Portfolio

• Read Article

• Contact

Every button should have a measurable business purpose.



# Philosophy

Every button answers one question:

"What should the user do next?"

If a button does not answer this question,

it should not exist.



# Button Hierarchy

There are only four button types.

Primary

Highest priority.

Used only once inside a section.

Secondary

Supporting action.

Outline style.

Ghost

Low emphasis.

Mostly navigation.

Text Button

Minimal interaction.

Usually inside blog cards or inline links.



# Bootstrap Mapping

Primary

btn btn-primary

Secondary

btn btn-outline-primary

Ghost

btn btn-link

Danger

Never use on public pages.

Reserved for Django Admin.



# Primary Button

Color

Royal Blue

Background

Solid

Text

White

Border Radius

12px

Minimum Height

48px

Padding

px-4 py-2

Hover

Slightly darker blue.

Small shadow.

No scaling.



# Secondary Button

Transparent background.

Blue border.

Blue text.

Hover

Solid blue background.

White text.



# Ghost Button

Transparent

No border

Text only

Hover

Light background

Never underline on hover.



# Text Button

Looks like normal text.

Accent color.

Small arrow icon optional.

Used for

Read More

Learn More

View Details



# CTA Priority

Every section

Maximum

One Primary Button

One Secondary Button

Example

Hire Me

↓

View Portfolio

Never create three competing CTAs.



# Homepage CTA Rules

Hero

Primary

Hire Me

Secondary

View Portfolio

Services

Primary

Explore Services

Projects

Primary

View All Projects

Blog

Primary

Read More Articles

Footer

Primary

Contact Me



# Icons

Bootstrap Icons only.

Icons should appear

Left

or

Right

Never both.

Avoid icon-only buttons unless universally understood.

Example

GitHub

LinkedIn

Email



# Button Width

Desktop

Auto Width

Mobile

100%

Avoid tiny buttons.



# Typography

Font

Plus Jakarta Sans

Weight

600

Text Transform

None

Never use ALL CAPS.



# Accessibility

Minimum height

44px

Visible focus state

Required.

Buttons must be keyboard accessible.

Every icon button must include

aria-label



# SEO

Buttons should contain meaningful text.

Good

Hire Me

Book Mentoring

View Portfolio

Bad

Click Here

Learn

More

Go



# AI Optimization

Button labels should clearly describe intent.

Avoid vague wording.

Every button should improve content understanding for AI systems.



# Animation

Allowed

Background transition

Color transition

Shadow transition

Duration

200ms

Avoid

Bounce

Pulse

Rotate

Glow



# Disabled State

Lower opacity.

Cursor

not-allowed

Never hide disabled buttons unexpectedly.



# Loading State

Future Support

Spinner

Button disabled

Loading text

Example

Sending...

Saving...

Booking...



# Responsive

Desktop

Auto width

Mobile

Full width

Buttons stacked vertically when necessary.



# Reusability

Every button should be implemented using one reusable template.

Example

components/button.html

Do not duplicate button markup.



# Future Improvements

Loading Buttons

Icon Buttons

Split Buttons

Dropdown Buttons

These features should not change existing APIs.



# Do

✓ Keep labels clear

✓ Use consistent sizing

✓ Keep spacing generous

✓ Use Bootstrap

✓ Prioritize accessibility

✓ Optimize for conversion



# Don't

✗ Multiple primary buttons

✗ Flashy hover effects

✗ Animated gradients

✗ Tiny buttons

✗ Generic labels

✗ Inline CSS

✗ JavaScript-only interactions



# Definition of Done

✓ Responsive

✓ Accessible

✓ Bootstrap Based

✓ Semantic

✓ Reusable

✓ SEO Friendly

✓ AI Optimized

✓ Production Ready
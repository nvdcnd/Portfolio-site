---
title: Contact Page Specification
version: 1.0.0
status: Stable
---

# Purpose

This document specifies the layout, fields, form validation, and backend processing logic for the Contact Page.

It guides developers and AI agents in building a robust lead capture system.

Following this spec ensures secure data submission, robust validations, and reliable email notifications.



# Contact Page (`/contact/`)

The contact page houses the primary inquiry form alongside contact details.

Template

```
templates/pages/contact.html
```

Context Variables

- `form` (instance of Django ContactForm)

- `contact_info` (apps.common.models.ContactInfo active instance)

- `socials` (apps.common.models.SocialMediaLink queryset)

Layout & Structure

- Header: Breadcrumb (Home > Contact).

- Grid Split (Desktop):
  - Left Column (5 cols): Direct contact details (Email, Phone, Address with icons) + Social media profile links.
  - Right Column (7 cols): Lead inquiry form card.



# Form Specifications

The form must be implemented using a standard Django form (`forms.Form` or `forms.ModelForm`).

Required Fields

- `name` (CharField, required, placeholder: "Your Name")

- `email` (EmailField, required, placeholder: "your.email@example.com")

- `subject` (CharField, required, placeholder: "How can I help you?")

- `message` (CharField, Widget: Textarea, required, placeholder: "Write your message details here...")

Anti-Spam Field

- `honeypot` (CharField, optional, hidden from view using CSS `display:none`)

- If the honeypot field contains any value upon submission, the request is flagged as spam and rejected.



# Form Processing Logic

Submission Flow

1. User fills and submits form.

2. Backend validates CSRF token and honeypot field.

3. Form field validations are run.

4. If validation fails, reload form displaying specific field errors.

5. If validation passes:
   - Create a database record in ContactMessages app (or log transaction).
   - Trigger asynchronous email notification to admin via email.
   - Display a clean, successful confirmation alert.



# View Processing Code

```python
# apps/contact/views.py

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Check honeypot
            if form.cleaned_data.get('honeypot'):
                return HttpResponseBadRequest("Spam detected.")
                
            # Process message
            message = form.save()
            
            # Send Notification
            send_mail(
                subject=f"New Inquiry: {message.subject}",
                message=f"From: {message.name} ({message.email})\n\n{message.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=True
            )
            
            messages.success(request, "Thank you! Your message has been sent successfully.")
            return redirect('contact:contact')
    else:
        form = ContactForm()
        
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    return render(request, 'pages/contact.html', {
        'form': form,
        'contact_info': contact_info
    })
```



# Styling & UI Feedback

Error State

- Fields with invalid inputs receive a red border (using Bootstrap `.is-invalid` class).

- Display a clear error text summary beneath the field: `<div class="invalid-feedback">`.

Success State

- Page redirects and displays a clean Bootstrap dismissible success alert.

Loading / Sending State

- The submit button transitions to a disabled state with text "Sending..." to prevent double submission.



# Accessibility

Semantic HTML

- Form fields must use `<label>` tags linked to `<input>` elements via `for` attributes.

- Input fields should specify autocomplete hints (e.g. `autocomplete="name"`).

Aria Attributes

- Use `aria-required="true"` on mandatory inputs.

- Validation alerts must include `role="alert"` for screen reader announcements.



# SEO & AI Optimization

- The title tag must map to: `Contact | Hoàng Hùng Anh`.

- The page clearly indicates hours of operation and response timelines (e.g. "Response within 24 hours") to build trust with both users and search indexers.



# Definition of Done for Contact Page

✓ CSRF token validation included in post forms.

✓ Honeypot spam test verified.

✓ Autocomplete attributes mapped to inputs.

✓ Success alert displays cleanly on redirect.

✓ Mandatory fields trigger native HTML5 and Django validation messages.

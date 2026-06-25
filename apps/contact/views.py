from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from apps.common.models import ContactInfo
from .forms import ContactForm

def index(request):
    """
    Handle contact page displaying form and client details,
    validating input and spam triggers on POST.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Check honeypot field
            if form.cleaned_data.get('honeypot'):
                return HttpResponseBadRequest("Spam detected.")
            
            # Save the message record to the database
            msg = form.save()
            
            # Send email alert to admin
            email_subject = f"New Inquiry: {msg.subject}"
            email_message = f"From: {msg.name} ({msg.email})\n\nMessage:\n{msg.message}"
            send_mail(
                subject=email_subject,
                message=email_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=True
            )
            
            messages.success(request, "Thank you! Your message has been sent successfully.")
            return redirect('contact:index')
    else:
        form = ContactForm()
        
    contact_info = ContactInfo.objects.filter(is_active=True).order_by('-updated_at').first()
    return render(request, 'pages/contact.html', {
        'form': form,
        'contact_info': contact_info
    })

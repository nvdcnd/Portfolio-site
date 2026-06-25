from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    # Hidden field to trap spam bots
    honeypot = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'style': 'display:none !important;',
            'autocomplete': 'off',
            'tabindex': '-1'
        }),
        label=''
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control rounded-3',
                'placeholder': 'Your Name',
                'autocomplete': 'name',
                'aria-required': 'true'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control rounded-3',
                'placeholder': 'your.email@example.com',
                'autocomplete': 'email',
                'aria-required': 'true'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control rounded-3',
                'placeholder': 'How can I help you?',
                'aria-required': 'true'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control rounded-3',
                'placeholder': 'Write your message details here...',
                'rows': 5,
                'aria-required': 'true'
            }),
        }

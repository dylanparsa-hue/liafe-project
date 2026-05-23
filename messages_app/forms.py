from django import forms
from .models import ContactMessage, Inquiry


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name':    forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email':   forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'phone':   forms.TextInput(attrs={'placeholder': '+44 ...'}),
            'subject': forms.TextInput(attrs={'placeholder': 'How can we help?'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your message...', 'rows': 5}),
        }


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['inquiry_type', 'name', 'email', 'phone', 'company', 'subject', 'message']
        widgets = {
            'name':    forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email':   forms.EmailInput(attrs={'placeholder': 'your@email.com'}),
            'phone':   forms.TextInput(attrs={'placeholder': '+44 ...'}),
            'company': forms.TextInput(attrs={'placeholder': 'Company / Organisation'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Research area / topic'}),
            'message': forms.Textarea(attrs={'placeholder': 'Describe your research needs...', 'rows': 5}),
        }

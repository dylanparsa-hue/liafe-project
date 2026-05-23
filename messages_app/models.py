from django.db import models
from ckeditor.fields import RichTextField


class ContactMessage(models.Model):
    name       = models.CharField(max_length=200)
    email      = models.EmailField()
    phone      = models.CharField(max_length=64, blank=True)
    subject    = models.CharField(max_length=200, blank=True)
    message    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read    = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} — {self.subject or 'No subject'}"


class Inquiry(models.Model):
    TYPES = [
        ("research",      "Research"),
        ("collaboration", "Collaboration"),
        ("training",      "Training"),
        ("publication",   "Publication"),
        ("other",         "Other"),
    ]
    inquiry_type    = models.CharField(max_length=20, choices=TYPES, default="research")
    name            = models.CharField(max_length=200)
    email           = models.EmailField()
    phone           = models.CharField(max_length=64, blank=True)
    company         = models.CharField(max_length=200, blank=True)
    subject         = models.CharField(max_length=200, blank=True)
    message         = models.TextField()
    related_service = models.ForeignKey(
        "services.Service", on_delete=models.SET_NULL, null=True, blank=True
    )
    admin_notes     = models.TextField(blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    is_read         = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Inquiry"
        verbose_name_plural = "Inquiries"

    def __str__(self):
        return f"{self.name} — {self.get_inquiry_type_display()}"


class ContactPage(models.Model):
    hero_title         = models.CharField(max_length=200, default="Speak with our team.")
    hero_subtitle      = models.CharField(max_length=300, blank=True)
    description        = RichTextField(blank=True)
    image              = models.ImageField(upload_to="contact/", blank=True, help_text="Recommended: 800×600 px")
    map_embed          = models.TextField(blank=True, help_text="Google Maps iframe embed code")
    contact_form_intro = models.TextField(blank=True)
    success_message    = models.CharField(max_length=300, default="Message sent — thank you.")
    created_at         = models.DateTimeField(auto_now_add=True)
    updated_at         = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact Page"
        verbose_name_plural = "Contact Page"

    def __str__(self):
        return "Contact Page Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

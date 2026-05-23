from django.contrib import admin
from django.utils.html import mark_safe
from unfold.admin import ModelAdmin
from .models import ContactMessage, Inquiry, ContactPage


@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display  = ['name', 'email', 'subject', 'read_badge', 'created_at']
    list_filter   = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['name', 'email', 'phone', 'subject', 'message', 'created_at']
    ordering = ['-created_at']

    fieldsets = [
        (None, {"fields": ["name", "email", "phone", "subject", "message", "created_at", "is_read"]}),
    ]

    def read_badge(self, obj):
        if obj.is_read:
            return mark_safe('<span style="background:#ECFDF3;color:#067647;padding:2px 8px;border-radius:4px;font-size:11px;">Read</span>')
        return mark_safe('<span style="background:#FEF2F2;color:#991B1B;padding:2px 8px;border-radius:4px;font-size:11px;">Unread</span>')
    read_badge.short_description = "Status"

    def has_add_permission(self, request):
        return False


@admin.register(Inquiry)
class InquiryAdmin(ModelAdmin):
    list_display  = ['name', 'email', 'inquiry_type', 'company', 'read_badge', 'created_at']
    list_filter   = ['inquiry_type', 'is_read', 'created_at']
    search_fields = ['name', 'email', 'company', 'subject']
    readonly_fields = ['name', 'email', 'phone', 'company', 'inquiry_type', 'subject', 'message', 'related_service', 'created_at']
    ordering = ['-created_at']

    fieldsets = [
        (None, {"fields": ["name", "email", "phone", "company", "inquiry_type", "subject", "message", "related_service", "created_at", "is_read"]}),
        ("Admin Notes", {"fields": ["admin_notes"]}),
    ]

    def read_badge(self, obj):
        if obj.is_read:
            return mark_safe('<span style="background:#ECFDF3;color:#067647;padding:2px 8px;border-radius:4px;font-size:11px;">Read</span>')
        return mark_safe('<span style="background:#FEF2F2;color:#991B1B;padding:2px 8px;border-radius:4px;font-size:11px;">Unread</span>')
    read_badge.short_description = "Status"

    def has_add_permission(self, request):
        return False


@admin.register(ContactPage)
class ContactPageAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_form = True

    fieldsets = [
        ("Hero", {"fields": ["hero_title", "hero_subtitle"]}),
        ("Content", {"fields": ["description", "contact_form_intro", "success_message"]}),
        ("Media", {"fields": ["image", "image_preview"]}),
        ("Map", {"fields": ["map_embed"]}),
    ]
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height:80px;border-radius:6px;">')
        return "—"
    image_preview.short_description = "Preview"

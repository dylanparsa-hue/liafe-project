from django.contrib import admin
from django.utils.html import mark_safe
from unfold.admin import ModelAdmin
from .models import SiteSetting, HomepageSection, ValuePillar, HeroSlide
from publications.models import Publication
from messages_app.models import ContactMessage, Inquiry


def dashboard_callback(request, context):
    from services.models import Service, Course, ResearchProject
    unread_messages  = ContactMessage.objects.filter(is_read=False).count()
    unread_inquiries = Inquiry.objects.filter(is_read=False).count()
    context.update({
        'dashboard_stats': {
            'services':          Service.objects.filter(is_active=True).count(),
            'publications':      Publication.objects.filter(is_active=True).count(),
            'courses':           Course.objects.filter(is_active=True).count(),
            'research_projects': ResearchProject.objects.filter(is_active=True).count(),
            'hero_slides':       HeroSlide.objects.filter(is_active=True).count(),
            'total_messages':    ContactMessage.objects.count(),
            'total_inquiries':   Inquiry.objects.count(),
            'unread_messages':   unread_messages,
            'unread_inquiries':  unread_inquiries,
            'has_unread':        (unread_messages + unread_inquiries) > 0,
        },
        'recent_messages':      ContactMessage.objects.order_by('-created_at')[:5],
        'recent_inquiries':     Inquiry.objects.order_by('-created_at')[:5],
        'recent_publications':  Publication.objects.filter(is_active=True).order_by('-created_at')[:5],
    })
    return context


@admin.register(SiteSetting)
class SiteSettingAdmin(ModelAdmin):
    compressed_fields = True
    warn_unsaved_form = True

    fieldsets = [
        ("Brand", {"fields": ["company_name", "short_name", "tagline", "logo", "logo_preview", "favicon", "favicon_preview"]}),
        ("Hero & Banners", {"fields": ["hero_background_image", "hero_preview", "default_page_banner"]}),
        ("Contact", {"fields": ["phone", "email", "address", "working_hours"]}),
        ("Social Media", {"fields": ["facebook_url", "instagram_url", "linkedin_url", "youtube_url"]}),
        ("Footer", {"fields": ["footer_text", "copyright_text"]}),
    ]
    readonly_fields = ['logo_preview', 'favicon_preview', 'hero_preview']

    def logo_preview(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" style="max-height:60px;border-radius:4px;border:1px solid #E5E7EB;">')
        return mark_safe('<p style="color:#9CA3AF;font-size:13px;">No logo uploaded</p>')
    logo_preview.short_description = "Current Logo"

    def favicon_preview(self, obj):
        if obj.favicon:
            return mark_safe(f'<img src="{obj.favicon.url}" style="max-height:32px;">')
        return mark_safe('<p style="color:#9CA3AF;font-size:13px;">No favicon uploaded</p>')
    favicon_preview.short_description = "Current Favicon"

    def hero_preview(self, obj):
        if obj.hero_background_image:
            return mark_safe(f'<img src="{obj.hero_background_image.url}" style="max-height:120px;border-radius:6px;border:1px solid #E5E7EB;">')
        return mark_safe('<p style="color:#9CA3AF;font-size:13px;">No image — using gradient fallback. Upload here or use Hero Slides instead.</p>')
    hero_preview.short_description = "Current Hero Background"


@admin.register(HeroSlide)
class HeroSlideAdmin(ModelAdmin):
    list_display  = ['slide_preview', 'title', 'subtitle', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter   = ['is_active']
    search_fields = ['title', 'subtitle']

    fieldsets = [
        ("Content", {"fields": ["title", "subtitle", "description"]}),
        ("Background Image", {"fields": ["background_image", "slide_thumb"],
            "description": "Recommended size: 1920×1080 px. Upload a high-quality photo for the best result."}),
        ("Buttons", {"fields": ["button_1_text", "button_1_link", "button_2_text", "button_2_link"]}),
        ("Display", {"fields": ["is_active", "order"]}),
    ]
    readonly_fields = ['slide_thumb']

    def slide_preview(self, obj):
        if obj.background_image:
            return mark_safe(f'<img src="{obj.background_image.url}" style="width:80px;height:45px;object-fit:cover;border-radius:4px;border:1px solid #E5E7EB;">')
        return mark_safe('<div style="width:80px;height:45px;background:#F3F4F6;border-radius:4px;border:1px solid #E5E7EB;display:flex;align-items:center;justify-content:center;font-size:10px;color:#9CA3AF;">No image</div>')
    slide_preview.short_description = "Preview"

    def slide_thumb(self, obj):
        if obj.background_image:
            return mark_safe(f'<img src="{obj.background_image.url}" style="max-height:160px;border-radius:8px;border:1px solid #E5E7EB;">')
        return mark_safe('<p style="color:#9CA3AF;font-size:13px;">No background image uploaded yet.</p>')
    slide_thumb.short_description = "Current Image"


@admin.register(HomepageSection)
class HomepageSectionAdmin(ModelAdmin):
    list_display  = ['section_name', 'title', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter   = ['is_active', 'section_name']

    fieldsets = [
        (None, {"fields": ["section_name", "title", "subtitle", "description", "is_active", "order"]}),
        ("Media", {"fields": ["image", "image_preview", "background_image", "bg_preview"]}),
        ("Button", {"fields": ["button_text", "button_link"]}),
    ]
    readonly_fields = ['image_preview', 'bg_preview']

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height:120px;border-radius:6px;border:1px solid #E5E7EB;">')
        return mark_safe('<p style="color:#9CA3AF;font-size:13px;">No image uploaded</p>')
    image_preview.short_description = "Section Image Preview"

    def bg_preview(self, obj):
        if obj.background_image:
            return mark_safe(f'<img src="{obj.background_image.url}" style="max-height:120px;border-radius:6px;border:1px solid #E5E7EB;">')
        return mark_safe('<p style="color:#9CA3AF;font-size:13px;">No background image uploaded</p>')
    bg_preview.short_description = "Background Image Preview"


@admin.register(ValuePillar)
class ValuePillarAdmin(ModelAdmin):
    list_display  = ['title', 'icon_class', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter   = ['is_active']
    search_fields = ['title']

    fieldsets = [
        (None, {"fields": ["title", "description", "icon_class"]}),
        ("Media", {"fields": ["image", "image_preview"]}),
        ("Display", {"fields": ["is_active", "order"]}),
    ]
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height:80px;border-radius:6px;border:1px solid #E5E7EB;">')
        return "—"
    image_preview.short_description = "Preview"

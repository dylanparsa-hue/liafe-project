from django.contrib import admin
from django.utils.html import mark_safe
from unfold.admin import ModelAdmin
from .models import Publication


@admin.register(Publication)
class PublicationAdmin(ModelAdmin):
    list_display  = ['cover_thumb', 'title', 'publication_type', 'author', 'is_featured', 'is_active', 'order', 'updated_at']
    list_editable = ['is_featured', 'is_active', 'order']
    list_filter   = ['publication_type', 'is_featured', 'is_active']
    search_fields = ['title', 'author', 'tags']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'

    fieldsets = [
        ("Identity", {"fields": ["title", "slug", "publication_type", "author", "co_authors"]}),
        ("Content", {"fields": ["short_description", "full_description"]}),
        ("Media & Files", {"fields": ["cover_image", "cover_thumb_field", "pdf_file"]}),
        ("Metadata", {"fields": ["isbn", "doi", "published_date", "external_link", "tags"]}),
        ("Status", {"fields": ["is_featured", "is_active", "order"]}),
    ]
    readonly_fields = ['cover_thumb', 'cover_thumb_field']

    def cover_thumb(self, obj):
        if obj.cover_image:
            return mark_safe(f'<img src="{obj.cover_image.url}" style="width:36px;height:48px;object-fit:cover;border-radius:3px;">')
        return mark_safe('<div style="width:36px;height:48px;background:#E5E7EB;border-radius:3px;"></div>')
    cover_thumb.short_description = ""

    def cover_thumb_field(self, obj):
        if obj.cover_image:
            return mark_safe(f'<img src="{obj.cover_image.url}" style="max-height:120px;border-radius:6px;">')
        return "—"
    cover_thumb_field.short_description = "Preview"

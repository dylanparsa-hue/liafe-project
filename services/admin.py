from django.contrib import admin
from django.utils.html import mark_safe
from unfold.admin import ModelAdmin
from unfold.contrib.inlines.admin import TabularInline
from .models import Service, ServiceFeature, CourseCategory, Course, ResearchCategory, ResearchProject


class ServiceFeatureInline(TabularInline):
    model  = ServiceFeature
    extra  = 0
    fields = ['title', 'description', 'icon_class', 'item_type', 'is_active', 'order']


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display  = ['icon_col', 'title', 'slug', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter   = ['is_active']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceFeatureInline]

    fieldsets = [
        ("Identity", {"fields": ["title", "slug", "menu_title", "icon_class"]}),
        ("Content", {"fields": ["short_description", "full_description"]}),
        ("Hero", {"fields": ["hero_title", "hero_subtitle", "hero_description", "hero_image", "hero_image_preview"]}),
        ("Image", {"fields": ["image", "image_preview"]}),
        ("CTA", {"fields": ["cta_title", "cta_description", "cta_button_text", "cta_button_link"]}),
        ("SEO", {"fields": ["seo_title", "seo_description"]}),
        ("Status", {"fields": ["is_active", "order"]}),
    ]
    readonly_fields = ['image_preview', 'hero_image_preview']

    def icon_col(self, obj):
        return obj.icon_class or "—"
    icon_col.short_description = "Icon"

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height:60px;border-radius:4px;">')
        return "—"
    image_preview.short_description = "Preview"

    def hero_image_preview(self, obj):
        if obj.hero_image:
            return mark_safe(f'<img src="{obj.hero_image.url}" style="max-height:60px;border-radius:4px;">')
        return "—"
    hero_image_preview.short_description = "Preview"


@admin.register(ServiceFeature)
class ServiceFeatureAdmin(ModelAdmin):
    list_display  = ['title', 'service', 'item_type', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter   = ['service', 'item_type', 'is_active']
    search_fields = ['title', 'service__title']


@admin.register(CourseCategory)
class CourseCategoryAdmin(ModelAdmin):
    list_display  = ['title', 'delivery_method', 'duration', 'level', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter   = ['is_active']
    search_fields = ['title']

    fieldsets = [
        (None, {"fields": ["title", "description", "full_description", "icon_class"]}),
        ("Media", {"fields": ["image", "image_preview"]}),
        ("Details", {"fields": ["delivery_method", "duration", "level", "button_text", "button_link"]}),
        ("Status", {"fields": ["is_active", "order"]}),
    ]
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height:60px;border-radius:4px;">')
        return "—"
    image_preview.short_description = "Preview"


@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display  = ['title', 'category', 'delivery_method', 'level', 'is_featured', 'is_active', 'order']
    list_editable = ['is_featured', 'is_active', 'order']
    list_filter   = ['category', 'delivery_method', 'level', 'is_featured', 'is_active']
    search_fields = ['title', 'category__title']


@admin.register(ResearchCategory)
class ResearchCategoryAdmin(ModelAdmin):
    list_display  = ['title', 'is_active', 'order']
    list_editable = ['is_active', 'order']
    list_filter   = ['is_active']
    search_fields = ['title']


@admin.register(ResearchProject)
class ResearchProjectAdmin(ModelAdmin):
    list_display  = ['title', 'category', 'research_status', 'year', 'is_featured', 'is_active', 'order']
    list_editable = ['is_featured', 'is_active', 'order']
    list_filter   = ['category', 'research_status', 'is_featured', 'is_active']
    search_fields = ['title', 'category__title']

    fieldsets = [
        (None, {"fields": ["title", "category", "short_description", "full_description"]}),
        ("Media & Files", {"fields": ["image", "image_preview", "report_file"]}),
        ("Details", {"fields": ["research_status", "client_or_partner", "year", "external_link"]}),
        ("Status", {"fields": ["is_featured", "is_active", "order"]}),
    ]
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height:60px;border-radius:4px;">')
        return "—"
    image_preview.short_description = "Preview"

from django.db import models
from ckeditor.fields import RichTextField


class SiteSetting(models.Model):
    company_name          = models.CharField(max_length=200, default="London International Academy for Excellence")
    short_name            = models.CharField(max_length=64, default="LIAFE")
    tagline               = models.CharField(max_length=300, blank=True)
    logo                  = models.ImageField(upload_to="logos/", blank=True, help_text="Recommended: 300×100 px")
    favicon               = models.ImageField(upload_to="logos/", blank=True, help_text="Recommended: 32×32 px")
    hero_background_image = models.ImageField(upload_to="homepage/", blank=True, help_text="Recommended: 1920×1080 px")
    default_page_banner   = models.ImageField(upload_to="banners/", blank=True, help_text="Recommended: 1920×600 px")
    phone                 = models.CharField(max_length=64, default="+44 207 354 33 55")
    email                 = models.EmailField(default="info@ukliafe.com")
    address               = models.CharField(max_length=300, default="London, N4 2DN")
    working_hours         = models.CharField(max_length=120, default="9 AM – 5 PM")
    facebook_url          = models.URLField(blank=True)
    instagram_url         = models.URLField(blank=True)
    linkedin_url          = models.URLField(blank=True)
    youtube_url           = models.URLField(blank=True)
    footer_text           = models.TextField(blank=True)
    copyright_text        = models.CharField(max_length=300, blank=True)
    created_at            = models.DateTimeField(auto_now_add=True)
    updated_at            = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class HomepageSection(models.Model):
    SECTION_CHOICES = [
        ("hero",          "Hero"),
        ("about",         "About"),
        ("core_services", "Core Services"),
        ("why_choose_us", "Why Choose Us"),
        ("approach",      "Approach"),
        ("cta",           "CTA"),
    ]
    section_name     = models.CharField(max_length=64, choices=SECTION_CHOICES, unique=True)
    title            = models.CharField(max_length=300, blank=True)
    subtitle         = models.CharField(max_length=300, blank=True)
    description      = RichTextField(blank=True)
    image            = models.ImageField(upload_to="homepage/", blank=True, help_text="Recommended: 800×600 px")
    background_image = models.ImageField(upload_to="homepage/", blank=True, help_text="Recommended: 1920×1080 px")
    button_text      = models.CharField(max_length=100, blank=True)
    button_link      = models.CharField(max_length=300, blank=True)
    is_active        = models.BooleanField(default=True)
    order            = models.PositiveSmallIntegerField(default=0)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Homepage Section"
        verbose_name_plural = "Homepage Sections"

    def __str__(self):
        return self.get_section_name_display()


class HeroSlide(models.Model):
    title            = models.CharField(max_length=300)
    subtitle         = models.CharField(max_length=300, blank=True)
    description      = models.TextField(blank=True)
    background_image = models.ImageField(upload_to='hero/', blank=True, help_text='Recommended: 1920×1080 px')
    button_1_text    = models.CharField(max_length=100, blank=True, default='Consult Us')
    button_1_link    = models.CharField(max_length=300, blank=True, default='/contact/')
    button_2_text    = models.CharField(max_length=100, blank=True, default='Explore Services')
    button_2_link    = models.CharField(max_length=300, blank=True, default='#services')
    order            = models.PositiveSmallIntegerField(default=0)
    is_active        = models.BooleanField(default=True)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Hero Slide'
        verbose_name_plural = 'Hero Slides'

    def __str__(self):
        return self.title


class AboutStat(models.Model):
    value     = models.CharField(max_length=20, help_text="e.g. 12, 40, 25, £3.2")
    suffix    = models.CharField(max_length=10, blank=True, help_text="e.g. +, bn (leave blank if none)")
    label     = models.CharField(max_length=100, help_text="e.g. Markets Served")
    is_active = models.BooleanField(default=True)
    order     = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'About Stat'
        verbose_name_plural = 'About Stats'

    def __str__(self):
        return f"{self.value}{self.suffix} — {self.label}"


class ValuePillar(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField()
    icon_class  = models.CharField(max_length=64, help_text="e.g. 'Knowledge' (matches frontend icon set)")
    image       = models.ImageField(upload_to="general/", blank=True, help_text="Recommended: 800×500 px")
    is_active   = models.BooleanField(default=True)
    order       = models.PositiveSmallIntegerField(default=0)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Value Pillar"
        verbose_name_plural = "Value Pillars"

    def __str__(self):
        return self.title

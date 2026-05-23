from django.db import models


class CustomPage(models.Model):
    title           = models.CharField(max_length=200)
    slug            = models.SlugField(max_length=200, unique=True, help_text='URL-friendly name, e.g. about-us')
    subtitle        = models.CharField(max_length=300, blank=True)
    description     = models.TextField(blank=True)
    featured_image  = models.ImageField(upload_to='pages/', blank=True, help_text='Recommended: 1200×630 px')
    seo_title       = models.CharField(max_length=200, blank=True)
    seo_description = models.CharField(max_length=300, blank=True)
    is_active       = models.BooleanField(default=True)
    show_in_menu    = models.BooleanField(default=False, help_text='Add this page to the top navigation bar')
    menu_label      = models.CharField(max_length=100, blank=True, help_text='Short label in the nav (defaults to title)')
    menu_order      = models.PositiveSmallIntegerField(default=99)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['menu_order', 'title']
        verbose_name = 'Custom Page'
        verbose_name_plural = 'Custom Pages'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/pages/{self.slug}/'

    def get_menu_label(self):
        return self.menu_label or self.title


class PageSection(models.Model):
    SECTION_TYPES = [
        ('hero',       'Hero'),
        ('text',       'Text Block'),
        ('image_text', 'Image + Text'),
        ('cards',      'Cards'),
        ('gallery',    'Gallery / Pictures'),
        ('cta',        'Call to Action'),
        ('faq',        'FAQ'),
    ]
    IMAGE_POSITIONS = [('left', 'Left'), ('right', 'Right')]
    TEXT_ALIGNMENTS = [('left', 'Left'), ('center', 'Center')]

    page             = models.ForeignKey(CustomPage, on_delete=models.CASCADE, related_name='sections')
    section_type     = models.CharField(max_length=30, choices=SECTION_TYPES)
    title            = models.CharField(max_length=300, blank=True)
    subtitle         = models.CharField(max_length=300, blank=True)
    description      = models.TextField(blank=True)
    image            = models.ImageField(upload_to='pages/sections/', blank=True, help_text='Recommended: 800×600 px')
    background_image = models.ImageField(upload_to='pages/backgrounds/', blank=True, help_text='Recommended: 1920×1080 px')
    background_color = models.CharField(max_length=20, blank=True, help_text='e.g. #F8FAFC (leave blank for white)')
    image_position   = models.CharField(max_length=10, choices=IMAGE_POSITIONS, default='right')
    button_text      = models.CharField(max_length=100, blank=True)
    button_link      = models.CharField(max_length=300, blank=True)
    text_alignment   = models.CharField(max_length=10, choices=TEXT_ALIGNMENTS, default='left')
    order            = models.PositiveSmallIntegerField(default=0)
    is_active        = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Page Section'
        verbose_name_plural = 'Page Sections'

    def __str__(self):
        return f'{self.page.title} — {self.get_section_type_display()} (#{self.order})'


class SectionItem(models.Model):
    section     = models.ForeignKey(PageSection, on_delete=models.CASCADE, related_name='items')
    title       = models.CharField(max_length=200, blank=True)
    subtitle    = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    icon_class  = models.CharField(max_length=64, blank=True, help_text='e.g. Star, Globe, Shield')
    image       = models.ImageField(upload_to='pages/items/', blank=True, help_text='Recommended: 600×400 px')
    button_text = models.CharField(max_length=100, blank=True)
    button_link = models.CharField(max_length=300, blank=True)
    caption     = models.CharField(max_length=200, blank=True, help_text='Caption shown below gallery images')
    order       = models.PositiveSmallIntegerField(default=0)
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Section Item'
        verbose_name_plural = 'Section Items'

    def __str__(self):
        return self.title or f'Item #{self.pk}'


class NavigationMenuItem(models.Model):
    label           = models.CharField(max_length=100)
    page            = models.ForeignKey(CustomPage, on_delete=models.SET_NULL, null=True, blank=True,
                                        help_text='Link to a custom page (leave blank to use External URL)')
    external_url    = models.CharField(max_length=500, blank=True,
                                       help_text='Used when no page is selected — e.g. /contact/')
    order           = models.PositiveSmallIntegerField(default=0)
    is_active       = models.BooleanField(default=True)
    open_in_new_tab = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']
        verbose_name = 'Navigation Menu Item'
        verbose_name_plural = 'Navigation Menu Items'

    def __str__(self):
        return self.label

    def get_url(self):
        if self.page and self.page.is_active:
            return self.page.get_absolute_url()
        return self.external_url or '#'

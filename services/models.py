from django.db import models
from ckeditor.fields import RichTextField


class Service(models.Model):
    title             = models.CharField(max_length=200)
    slug              = models.SlugField(unique=True)
    menu_title        = models.CharField(max_length=120, blank=True)
    icon_class        = models.CharField(max_length=64, blank=True, help_text="e.g. 'Shariah', 'Academy'")
    short_description = models.CharField(max_length=400)
    full_description  = RichTextField(blank=True)
    image             = models.ImageField(upload_to="services/", blank=True, help_text="Recommended: 800×600 px")
    hero_image        = models.ImageField(upload_to="services/", blank=True, help_text="Recommended: 1920×1080 px")
    hero_title        = models.CharField(max_length=200, blank=True)
    hero_subtitle     = models.CharField(max_length=300, blank=True)
    hero_description  = models.TextField(blank=True)
    cta_title         = models.CharField(max_length=200, blank=True)
    cta_description   = models.TextField(blank=True)
    cta_button_text   = models.CharField(max_length=100, blank=True)
    cta_button_link   = models.CharField(max_length=300, blank=True)
    seo_title         = models.CharField(max_length=200, blank=True)
    seo_description   = models.CharField(max_length=300, blank=True)
    is_active         = models.BooleanField(default=True)
    order             = models.PositiveSmallIntegerField(default=0)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        slug_map = {
            'shariah-advisory': 'shariah',
            'academy':          'academy',
            'research-house':   'research',
            'publication':      'publication',
        }
        name = slug_map.get(self.slug, 'home')
        return reverse(name)


class ServiceFeature(models.Model):
    ITEM_TYPES = [
        ("process",  "Process Step"),
        ("card",     "Service Card"),
        ("delivery", "Delivery Mode"),
        ("value",    "Research Value"),
    ]
    service          = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="features")
    title            = models.CharField(max_length=200)
    description      = models.TextField()
    full_description = RichTextField(blank=True)
    icon_class       = models.CharField(max_length=64, blank=True)
    image            = models.ImageField(upload_to="services/", blank=True, help_text="Recommended: 800×500 px")
    item_type        = models.CharField(max_length=20, choices=ITEM_TYPES, default="card")
    is_active        = models.BooleanField(default=True)
    order            = models.PositiveSmallIntegerField(default=0)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Service Feature"
        verbose_name_plural = "Service Features"

    def __str__(self):
        return f"{self.service.title} — {self.title}"


class CourseCategory(models.Model):
    title            = models.CharField(max_length=200)
    description      = models.TextField()
    full_description = RichTextField(blank=True)
    icon_class       = models.CharField(max_length=64, blank=True)
    image            = models.ImageField(upload_to="academy/", blank=True, help_text="Recommended: 800×500 px")
    delivery_method  = models.CharField(max_length=64, blank=True)
    duration         = models.CharField(max_length=64, blank=True)
    level            = models.CharField(max_length=64, blank=True)
    button_text      = models.CharField(max_length=64, blank=True, default="Learn More")
    button_link      = models.CharField(max_length=300, blank=True)
    is_active        = models.BooleanField(default=True)
    order            = models.PositiveSmallIntegerField(default=0)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Course Category"
        verbose_name_plural = "Course Categories"

    def __str__(self):
        return self.title


class Course(models.Model):
    title             = models.CharField(max_length=200)
    category          = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, related_name="courses")
    short_description = models.CharField(max_length=400)
    full_description  = RichTextField(blank=True)
    image             = models.ImageField(upload_to="academy/", blank=True, help_text="Recommended: 800×500 px")
    duration          = models.CharField(max_length=64, blank=True)
    delivery_method   = models.CharField(max_length=64, blank=True)
    level             = models.CharField(max_length=64, blank=True)
    price             = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    registration_link = models.URLField(blank=True)
    start_date        = models.DateField(null=True, blank=True)
    is_featured       = models.BooleanField(default=False)
    is_active         = models.BooleanField(default=True)
    order             = models.PositiveSmallIntegerField(default=0)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title


class ResearchCategory(models.Model):
    title            = models.CharField(max_length=200)
    description      = models.TextField()
    full_description = RichTextField(blank=True)
    icon_class       = models.CharField(max_length=64, blank=True)
    image            = models.ImageField(upload_to="research/", blank=True, help_text="Recommended: 800×500 px")
    is_active        = models.BooleanField(default=True)
    order            = models.PositiveSmallIntegerField(default=0)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Research Category"
        verbose_name_plural = "Research Categories"

    def __str__(self):
        return self.title


class ResearchProject(models.Model):
    STATUS = [
        ("draft",       "Draft"),
        ("in_progress", "In Progress"),
        ("published",   "Published"),
    ]
    title             = models.CharField(max_length=300)
    category          = models.ForeignKey(ResearchCategory, on_delete=models.CASCADE, related_name="projects")
    short_description = models.CharField(max_length=400)
    full_description  = RichTextField(blank=True)
    image             = models.ImageField(upload_to="research/", blank=True, help_text="Recommended: 800×500 px")
    research_status   = models.CharField(max_length=20, choices=STATUS, default="published")
    client_or_partner = models.CharField(max_length=200, blank=True)
    year              = models.PositiveIntegerField(null=True, blank=True)
    report_file       = models.FileField(upload_to="research/reports/", blank=True)
    external_link     = models.URLField(blank=True)
    is_featured       = models.BooleanField(default=False)
    is_active         = models.BooleanField(default=True)
    order             = models.PositiveSmallIntegerField(default=0)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-year"]
        verbose_name = "Research Project"
        verbose_name_plural = "Research Projects"

    def __str__(self):
        return self.title

from django.db import models
from ckeditor.fields import RichTextField


class Publication(models.Model):
    TYPES = [
        ("book",      "Book"),
        ("article",   "Article"),
        ("report",    "Research Report"),
        ("journal",   "Journal Paper"),
        ("thought",   "Thought Leadership"),
        ("other",     "Other"),
    ]

    title             = models.CharField(max_length=300)
    slug              = models.SlugField(unique=True)
    publication_type  = models.CharField(max_length=20, choices=TYPES)
    author            = models.CharField(max_length=200)
    co_authors        = models.CharField(max_length=400, blank=True)
    short_description = models.CharField(max_length=400)
    full_description  = RichTextField(blank=True)
    cover_image       = models.ImageField(upload_to="publications/covers/", blank=True, help_text="Recommended: 600×900 px")
    pdf_file          = models.FileField(upload_to="publications/pdfs/", blank=True)
    external_link     = models.URLField(blank=True)
    isbn              = models.CharField(max_length=64, blank=True)
    doi               = models.CharField(max_length=128, blank=True)
    published_date    = models.DateField(null=True, blank=True)
    tags              = models.CharField(max_length=300, blank=True, help_text="Comma-separated tags")
    is_featured       = models.BooleanField(default=False)
    is_active         = models.BooleanField(default=True)
    order             = models.PositiveSmallIntegerField(default=0)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-published_date"]
        verbose_name = "Publication"
        verbose_name_plural = "Publications"

    def __str__(self):
        return self.title

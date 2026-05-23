from django.shortcuts import render, get_object_or_404
from .models import CustomPage


def custom_page(request, slug):
    page = get_object_or_404(CustomPage, slug=slug, is_active=True)
    sections = page.sections.filter(is_active=True).prefetch_related('items')
    return render(request, 'pages/custom_page.html', {
        'page':     page,
        'sections': sections,
    })

from django.shortcuts import render
from .models import HomepageSection, ValuePillar, HeroSlide, AboutStat
from services.models import Service
from publications.models import Publication


def home(request):
    sections      = {s.section_name: s for s in HomepageSection.objects.filter(is_active=True)}
    services      = Service.objects.filter(is_active=True)
    pillars       = ValuePillar.objects.filter(is_active=True)
    hero_slides   = HeroSlide.objects.filter(is_active=True)
    featured_pubs = Publication.objects.filter(is_active=True, is_featured=True)[:4]
    about_stats   = AboutStat.objects.filter(is_active=True)
    return render(request, 'pages/home.html', {
        'sections':     sections,
        'services':     services,
        'pillars':      pillars,
        'hero_slides':  hero_slides,
        'featured_pubs': featured_pubs,
        'about_stats':  about_stats,
    })

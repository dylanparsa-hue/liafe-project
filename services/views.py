from django.shortcuts import render, get_object_or_404
from .models import Service, ServiceFeature, CourseCategory, Course, ResearchCategory, ResearchProject
from messages_app.forms import InquiryForm
from publications.models import Publication


def shariah(request):
    service = get_object_or_404(Service, slug='shariah-advisory', is_active=True)
    process_items = service.features.filter(item_type='process', is_active=True)
    card_items    = service.features.filter(item_type='card', is_active=True)
    return render(request, 'pages/shariah.html', {
        'service': service,
        'process_items': process_items,
        'card_items': card_items,
    })


def academy(request):
    service        = get_object_or_404(Service, slug='academy', is_active=True)
    categories     = CourseCategory.objects.filter(is_active=True)
    courses        = Course.objects.filter(is_active=True)
    delivery_modes = service.features.filter(item_type='delivery', is_active=True)
    return render(request, 'pages/academy.html', {
        'service':        service,
        'categories':     categories,
        'courses':        courses,
        'delivery_modes': delivery_modes,
    })


def research(request):
    service      = get_object_or_404(Service, slug='research-house', is_active=True)
    categories   = ResearchCategory.objects.filter(is_active=True)
    projects     = ResearchProject.objects.filter(is_active=True)
    inquiry_form = InquiryForm(initial={'inquiry_type': 'research'})
    success = False

    if request.method == 'POST':
        inquiry_form = InquiryForm(request.POST)
        if inquiry_form.is_valid():
            inquiry_form.save()
            success = True
            inquiry_form = InquiryForm(initial={'inquiry_type': 'research'})

    research_values = service.features.filter(item_type='value', is_active=True)

    return render(request, 'pages/research.html', {
        'service':         service,
        'categories':      categories,
        'projects':        projects,
        'inquiry_form':    inquiry_form,
        'success':         success,
        'research_values': research_values,
    })


def publication(request):
    service   = get_object_or_404(Service, slug='publication', is_active=True)
    pub_type  = request.GET.get('type', '')
    pubs      = Publication.objects.filter(is_active=True)
    if pub_type:
        pubs = pubs.filter(publication_type=pub_type)

    return render(request, 'pages/publication.html', {
        'service':      service,
        'publications': pubs,
        'pub_types':    Publication.TYPES,
        'active_type':  pub_type,
    })

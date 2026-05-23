from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse

from core.models import SiteSetting, HomepageSection, HeroSlide, ValuePillar, AboutStat
from pages.models import CustomPage, PageSection, SectionItem, NavigationMenuItem
from services.models import Service, ServiceFeature, CourseCategory, Course, ResearchCategory, ResearchProject
from publications.models import Publication
from messages_app.models import ContactMessage, Inquiry, ContactPage
from .forms import (
    SiteSettingForm, HomepageSectionForm, HeroSlideForm, ValuePillarForm, AboutStatForm,
    CustomPageForm, PageSectionForm, SectionItemForm, NavigationMenuItemForm,
    ServiceForm, ServiceFeatureForm,
    CourseCategoryForm, CourseForm,
    ResearchCategoryForm, ResearchProjectForm,
    PublicationForm, ContactPageForm, InquiryNotesForm,
)

staff_required = user_passes_test(lambda u: u.is_active and u.is_staff)


def staff_login_required(view_func):
    return login_required(staff_required(view_func))


# ── Overview ─────────────────────────────────────────────────────────────────

@staff_login_required
def overview(request):
    context = {
        'services_count':     Service.objects.filter(is_active=True).count(),
        'publications_count': Publication.objects.filter(is_active=True).count(),
        'hero_slides_count':  HeroSlide.objects.filter(is_active=True).count(),
        'sections_count':     HomepageSection.objects.count(),
        'messages_count':     ContactMessage.objects.count(),
        'unread_messages':    ContactMessage.objects.filter(is_read=False).count(),
        'inquiries_count':    Inquiry.objects.count(),
        'unread_inquiries':   Inquiry.objects.filter(is_read=False).count(),
        'recent_messages':    ContactMessage.objects.order_by('-created_at')[:5],
        'recent_inquiries':   Inquiry.objects.order_by('-created_at')[:5],
        'page': 'overview',
    }
    return render(request, 'dashboard/overview.html', context)


# ── Site Settings ─────────────────────────────────────────────────────────────

@staff_login_required
def site_settings(request):
    obj  = SiteSetting.load()
    form = SiteSettingForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Site settings saved.')
        return redirect('dashboard:site_settings')
    return render(request, 'dashboard/site_settings.html', {'form': form, 'page': 'site_settings'})


# ── Hero Slides ───────────────────────────────────────────────────────────────

@staff_login_required
def hero_slides(request):
    slides = HeroSlide.objects.all()
    return render(request, 'dashboard/hero_slides.html', {'slides': slides, 'page': 'hero_slides'})


@staff_login_required
def hero_slide_form(request, pk=None):
    obj  = get_object_or_404(HeroSlide, pk=pk) if pk else None
    form = HeroSlideForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Hero slide saved.')
        return redirect('dashboard:hero_slides')
    return render(request, 'dashboard/hero_slide_form.html', {'form': form, 'obj': obj, 'page': 'hero_slides'})


@staff_login_required
def hero_slide_delete(request, pk):
    obj = get_object_or_404(HeroSlide, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Hero slide deleted.')
        return redirect('dashboard:hero_slides')
    return render(request, 'dashboard/confirm_delete.html', {
        'obj': obj, 'obj_name': obj.title,
        'cancel_url': reverse('dashboard:hero_slides'), 'page': 'hero_slides',
    })


# ── Homepage Sections ─────────────────────────────────────────────────────────

@staff_login_required
def homepage_sections(request):
    sections = HomepageSection.objects.all()
    return render(request, 'dashboard/homepage_sections.html', {'sections': sections, 'page': 'homepage_sections'})


@staff_login_required
def homepage_section_form(request, pk):
    obj  = get_object_or_404(HomepageSection, pk=pk)
    form = HomepageSectionForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Section saved.')
        return redirect('dashboard:homepage_sections')
    return render(request, 'dashboard/homepage_section_form.html', {
        'form': form, 'obj': obj, 'page': 'homepage_sections',
    })


# ── Value Pillars ─────────────────────────────────────────────────────────────

@staff_login_required
def value_pillars(request):
    pillars = ValuePillar.objects.all()
    return render(request, 'dashboard/value_pillars.html', {'pillars': pillars, 'page': 'homepage_sections'})


@staff_login_required
def value_pillar_form(request, pk=None):
    obj  = get_object_or_404(ValuePillar, pk=pk) if pk else None
    form = ValuePillarForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Value pillar saved.')
        return redirect('dashboard:value_pillars')
    return render(request, 'dashboard/value_pillar_form.html', {'form': form, 'obj': obj, 'page': 'homepage_sections'})


@staff_login_required
def value_pillar_delete(request, pk):
    obj = get_object_or_404(ValuePillar, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Value pillar deleted.')
        return redirect('dashboard:value_pillars')
    return render(request, 'dashboard/confirm_delete.html', {
        'obj': obj, 'obj_name': obj.title,
        'cancel_url': reverse('dashboard:value_pillars'), 'page': 'homepage_sections',
    })


# ── About Stats ───────────────────────────────────────────────────────────────

@staff_login_required
def about_stats(request):
    stats = AboutStat.objects.all()
    return render(request, 'dashboard/about_stats.html', {'stats': stats, 'page': 'homepage_sections'})


@staff_login_required
def about_stat_form(request, pk=None):
    obj  = get_object_or_404(AboutStat, pk=pk) if pk else None
    form = AboutStatForm(request.POST or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Stat saved.')
        return redirect('dashboard:about_stats')
    return render(request, 'dashboard/about_stat_form.html', {
        'form': form, 'obj': obj, 'page': 'homepage_sections',
    })


@staff_login_required
def about_stat_delete(request, pk):
    obj = get_object_or_404(AboutStat, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Stat deleted.')
        return redirect('dashboard:about_stats')
    return render(request, 'dashboard/confirm_delete.html', {
        'obj': obj, 'obj_name': str(obj),
        'cancel_url': reverse('dashboard:about_stats'), 'page': 'homepage_sections',
    })


# ── Services ──────────────────────────────────────────────────────────────────

@staff_login_required
def services(request):
    svcs = Service.objects.all()
    return render(request, 'dashboard/services.html', {'services': svcs, 'page': 'services'})


@staff_login_required
def service_form(request, pk=None):
    obj  = get_object_or_404(Service, pk=pk) if pk else None
    form = ServiceForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        saved = form.save()
        messages.success(request, 'Service saved.')
        return redirect('dashboard:service_detail', pk=saved.pk)
    return render(request, 'dashboard/service_form.html', {'form': form, 'obj': obj, 'page': 'services'})


@staff_login_required
def service_detail(request, pk):
    svc = get_object_or_404(Service, pk=pk)
    features_by_type = {
        'process':  svc.features.filter(item_type='process'),
        'card':     svc.features.filter(item_type='card'),
        'delivery': svc.features.filter(item_type='delivery'),
        'value':    svc.features.filter(item_type='value'),
    }
    return render(request, 'dashboard/service_detail.html', {
        'svc': svc, 'features_by_type': features_by_type, 'page': 'services',
    })


@staff_login_required
def service_delete(request, pk):
    obj = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Service deleted.')
        return redirect('dashboard:services')
    return render(request, 'dashboard/confirm_delete.html', {
        'obj': obj, 'obj_name': obj.title,
        'cancel_url': reverse('dashboard:services'), 'page': 'services',
    })


# ── Service Features ──────────────────────────────────────────────────────────

@staff_login_required
def service_feature_form(request, service_pk, pk=None):
    svc  = get_object_or_404(Service, pk=service_pk)
    obj  = get_object_or_404(ServiceFeature, pk=pk, service=svc) if pk else None
    form = ServiceFeatureForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        feat = form.save(commit=False)
        feat.service = svc
        feat.save()
        messages.success(request, 'Feature saved.')
        return redirect('dashboard:service_detail', pk=service_pk)
    return render(request, 'dashboard/service_feature_form.html', {
        'form': form, 'obj': obj, 'svc': svc, 'page': 'services',
    })


@staff_login_required
def service_feature_delete(request, service_pk, pk):
    svc = get_object_or_404(Service, pk=service_pk)
    obj = get_object_or_404(ServiceFeature, pk=pk, service=svc)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Feature deleted.')
        return redirect('dashboard:service_detail', pk=service_pk)
    return render(request, 'dashboard/confirm_delete.html', {
        'obj': obj, 'obj_name': obj.title,
        'cancel_url': reverse('dashboard:service_detail', args=[service_pk]),
        'page': 'services',
    })


# ── Academy ───────────────────────────────────────────────────────────────────

@staff_login_required
def academy(request):
    categories    = CourseCategory.objects.all()
    courses       = Course.objects.select_related('category').all()
    academy_svc   = Service.objects.filter(slug='academy').first()
    return render(request, 'dashboard/academy.html', {
        'categories': categories, 'courses': courses,
        'academy_svc': academy_svc, 'page': 'academy',
    })


@staff_login_required
def course_category_form(request, pk=None):
    obj  = get_object_or_404(CourseCategory, pk=pk) if pk else None
    form = CourseCategoryForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Course category saved.')
        return redirect('dashboard:academy')
    return render(request, 'dashboard/course_category_form.html', {'form': form, 'obj': obj, 'page': 'academy'})


@staff_login_required
def course_category_delete(request, pk):
    obj = get_object_or_404(CourseCategory, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Category deleted.')
        return redirect('dashboard:academy')
    return render(request, 'dashboard/confirm_delete.html', {
        'obj': obj, 'obj_name': obj.title,
        'cancel_url': reverse('dashboard:academy'), 'page': 'academy',
    })


@staff_login_required
def course_form(request, pk=None):
    obj  = get_object_or_404(Course, pk=pk) if pk else None
    form = CourseForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Course saved.')
        return redirect('dashboard:academy')
    return render(request, 'dashboard/course_form.html', {'form': form, 'obj': obj, 'page': 'academy'})


@staff_login_required
def course_delete(request, pk):
    obj = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Course deleted.')
        return redirect('dashboard:academy')
    return render(request, 'dashboard/confirm_delete.html', {
        'obj': obj, 'obj_name': obj.title,
        'cancel_url': reverse('dashboard:academy'), 'page': 'academy',
    })


# ── Research ──────────────────────────────────────────────────────────────────

@staff_login_required
def research(request):
    categories   = ResearchCategory.objects.all()
    projects     = ResearchProject.objects.select_related('category').all()
    research_svc = Service.objects.filter(slug='research-house').first()
    return render(request, 'dashboard/research.html', {
        'categories': categories, 'projects': projects,
        'research_svc': research_svc, 'page': 'research',
    })


@staff_login_required
def research_category_form(request, pk=None):
    obj  = get_object_or_404(ResearchCategory, pk=pk) if pk else None
    form = ResearchCategoryForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Research category saved.')
        return redirect('dashboard:research')
    return render(request, 'dashboard/research_category_form.html', {'form': form, 'obj': obj, 'page': 'research'})


@staff_login_required
def research_category_delete(request, pk):
    obj = get_object_or_404(ResearchCategory, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Category deleted.')
        return redirect('dashboard:research')
    return render(request, 'dashboard/confirm_delete.html', {
        'obj': obj, 'obj_name': obj.title,
        'cancel_url': reverse('dashboard:research'), 'page': 'research',
    })


@staff_login_required
def research_project_form(request, pk=None):
    obj  = get_object_or_404(ResearchProject, pk=pk) if pk else None
    form = ResearchProjectForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Research project saved.')
        return redirect('dashboard:research')
    return render(request, 'dashboard/research_project_form.html', {'form': form, 'obj': obj, 'page': 'research'})


@staff_login_required
def research_project_delete(request, pk):
    obj = get_object_or_404(ResearchProject, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Project deleted.')
        return redirect('dashboard:research')
    return render(request, 'dashboard/confirm_delete.html', {
        'obj': obj, 'obj_name': obj.title,
        'cancel_url': reverse('dashboard:research'), 'page': 'research',
    })


# ── Publications ──────────────────────────────────────────────────────────────

@staff_login_required
def publications(request):
    pubs = Publication.objects.all()
    return render(request, 'dashboard/publications.html', {'publications': pubs, 'page': 'publications'})


@staff_login_required
def publication_form(request, pk=None):
    obj  = get_object_or_404(Publication, pk=pk) if pk else None
    form = PublicationForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Publication saved.')
        return redirect('dashboard:publications')
    return render(request, 'dashboard/publication_form.html', {'form': form, 'obj': obj, 'page': 'publications'})


@staff_login_required
def publication_delete(request, pk):
    obj = get_object_or_404(Publication, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Publication deleted.')
        return redirect('dashboard:publications')
    return render(request, 'dashboard/confirm_delete.html', {
        'obj': obj, 'obj_name': obj.title,
        'cancel_url': reverse('dashboard:publications'), 'page': 'publications',
    })


# ── Contact Page ──────────────────────────────────────────────────────────────

@staff_login_required
def contact_settings(request):
    obj, _ = ContactPage.objects.get_or_create(pk=1)
    form   = ContactPageForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Contact page saved.')
        return redirect('dashboard:contact_settings')
    return render(request, 'dashboard/contact_settings.html', {'form': form, 'page': 'contact'})


# ── Contact Messages ──────────────────────────────────────────────────────────

@staff_login_required
def contact_messages(request):
    msgs = ContactMessage.objects.all()
    return render(request, 'dashboard/messages.html', {'messages_list': msgs, 'page': 'messages'})


@staff_login_required
def message_detail(request, pk):
    obj = get_object_or_404(ContactMessage, pk=pk)
    if not obj.is_read:
        obj.is_read = True
        obj.save(update_fields=['is_read'])
    return render(request, 'dashboard/message_detail.html', {'obj': obj, 'page': 'messages'})


@staff_login_required
def message_delete(request, pk):
    obj = get_object_or_404(ContactMessage, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Message deleted.')
        return redirect('dashboard:messages')
    return render(request, 'dashboard/confirm_delete.html', {
        'obj': obj, 'obj_name': str(obj),
        'cancel_url': reverse('dashboard:messages'), 'page': 'messages',
    })


# ── Inquiries ─────────────────────────────────────────────────────────────────

@staff_login_required
def inquiries(request):
    inqs = Inquiry.objects.all()
    return render(request, 'dashboard/inquiries.html', {'inquiries': inqs, 'page': 'inquiries'})


@staff_login_required
def inquiry_detail(request, pk):
    obj  = get_object_or_404(Inquiry, pk=pk)
    form = InquiryNotesForm(request.POST or None, instance=obj)
    if not obj.is_read:
        obj.is_read = True
        obj.save(update_fields=['is_read'])
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Notes saved.')
        return redirect('dashboard:inquiry_detail', pk=pk)
    return render(request, 'dashboard/inquiry_detail.html', {'obj': obj, 'form': form, 'page': 'inquiries'})


@staff_login_required
def inquiry_delete(request, pk):
    obj = get_object_or_404(Inquiry, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Inquiry deleted.')
        return redirect('dashboard:inquiries')
    return render(request, 'dashboard/confirm_delete.html', {
        'obj': obj, 'obj_name': str(obj),
        'cancel_url': reverse('dashboard:inquiries'), 'page': 'inquiries',
    })


# ── Media Library ─────────────────────────────────────────────────────────────

@staff_login_required
def media_library(request):
    import os
    from django.conf import settings as django_settings

    media_root = django_settings.MEDIA_ROOT
    files = []
    if os.path.exists(media_root):
        for dirpath, dirnames, filenames in os.walk(media_root):
            for fname in filenames:
                fpath = os.path.join(dirpath, fname)
                rel   = os.path.relpath(fpath, media_root)
                ext   = os.path.splitext(fname)[1].lower()
                is_image = ext in ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg')
                files.append({
                    'name': fname,
                    'rel':  rel,
                    'url':  django_settings.MEDIA_URL + rel.replace(os.sep, '/'),
                    'size': os.path.getsize(fpath),
                    'is_image': is_image,
                })
        files.sort(key=lambda f: f['name'].lower())

    return render(request, 'dashboard/media_library.html', {'files': files, 'page': 'media_library'})


# ── Custom Pages ──────────────────────────────────────────────────────────────

@staff_login_required
def pages_list(request):
    all_pages = CustomPage.objects.all()
    return render(request, 'dashboard/pages_list.html', {'all_pages': all_pages, 'page': 'pages'})


@staff_login_required
def page_form(request, pk=None):
    obj  = get_object_or_404(CustomPage, pk=pk) if pk else None
    form = CustomPageForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        saved = form.save()
        messages.success(request, f'Page "{saved.title}" saved.')
        return redirect('dashboard:page_detail', pk=saved.pk)
    return render(request, 'dashboard/page_form.html', {'form': form, 'obj': obj, 'page': 'pages'})


@staff_login_required
def page_detail(request, pk):
    obj      = get_object_or_404(CustomPage, pk=pk)
    sections = obj.sections.all().prefetch_related('items')
    return render(request, 'dashboard/page_detail.html', {
        'obj': obj, 'sections': sections, 'page': 'pages',
        'section_types': PageSection.SECTION_TYPES,
    })


@staff_login_required
def page_delete(request, pk):
    obj = get_object_or_404(CustomPage, pk=pk)
    if request.method == 'POST':
        title = obj.title
        obj.delete()
        messages.success(request, f'Page "{title}" deleted.')
        return redirect('dashboard:pages_list')
    return render(request, 'dashboard/confirm_delete.html', {
        'obj': obj, 'obj_name': obj.title,
        'cancel_url': reverse('dashboard:page_detail', args=[pk]), 'page': 'pages',
    })


# ── Page Sections ─────────────────────────────────────────────────────────────

@staff_login_required
def section_form(request, page_pk=None, pk=None):
    if pk and not page_pk:
        # Editing existing section — look up the page from the section
        existing = get_object_or_404(PageSection, pk=pk)
        page_pk  = existing.page_id
    page_obj = get_object_or_404(CustomPage, pk=page_pk)
    obj      = get_object_or_404(PageSection, pk=pk, page=page_obj) if pk else None
    # Pre-select section type via ?type= query param when adding
    initial  = {}
    if not pk and request.GET.get('type'):
        initial['section_type'] = request.GET.get('type')
    form = PageSectionForm(request.POST or None, request.FILES or None, instance=obj, initial=initial)
    if request.method == 'POST' and form.is_valid():
        sec = form.save(commit=False)
        sec.page = page_obj
        # Auto-assign order if new
        if not pk:
            max_order = page_obj.sections.aggregate(m=__import__('django.db.models', fromlist=['Max']).Max('order'))['m'] or -1
            sec.order = max_order + 1
        sec.save()
        messages.success(request, 'Section saved.')
        return redirect('dashboard:page_detail', pk=page_pk)
    return render(request, 'dashboard/section_form.html', {
        'form': form, 'obj': obj, 'page_obj': page_obj, 'page': 'pages',
    })


@staff_login_required
def section_delete(request, pk):
    obj = get_object_or_404(PageSection, pk=pk)
    page_pk = obj.page_id
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Section deleted.')
        return redirect('dashboard:page_detail', pk=page_pk)
    return render(request, 'dashboard/confirm_delete.html', {
        'obj': obj, 'obj_name': str(obj),
        'cancel_url': reverse('dashboard:page_detail', args=[page_pk]), 'page': 'pages',
    })


@staff_login_required
def section_toggle(request, pk):
    """Quick POST toggle for active/inactive."""
    if request.method == 'POST':
        obj = get_object_or_404(PageSection, pk=pk)
        obj.is_active = not obj.is_active
        obj.save(update_fields=['is_active'])
        messages.success(request, f'Section {"activated" if obj.is_active else "hidden"}.')
        return redirect('dashboard:page_detail', pk=obj.page_id)
    return redirect('dashboard:pages_list')


@staff_login_required
def section_move(request, pk, direction):
    """Swap order with adjacent section (up / down)."""
    if request.method == 'POST':
        obj      = get_object_or_404(PageSection, pk=pk)
        siblings = list(obj.page.sections.order_by('order'))
        idx      = next((i for i, s in enumerate(siblings) if s.pk == pk), None)
        swap_idx = idx - 1 if direction == 'up' else idx + 1
        if 0 <= swap_idx < len(siblings):
            other = siblings[swap_idx]
            obj.order, other.order = other.order, obj.order
            obj.save(update_fields=['order'])
            other.save(update_fields=['order'])
    return redirect('dashboard:page_detail', pk=obj.page_id)


# ── Section Items ─────────────────────────────────────────────────────────────

@staff_login_required
def item_form(request, section_pk=None, pk=None):
    if pk and not section_pk:
        existing   = get_object_or_404(SectionItem, pk=pk)
        section_pk = existing.section_id
    section = get_object_or_404(PageSection, pk=section_pk)
    obj     = get_object_or_404(SectionItem, pk=pk, section=section) if pk else None
    form    = SectionItemForm(request.POST or None, request.FILES or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        item = form.save(commit=False)
        item.section = section
        if not pk:
            from django.db.models import Max
            max_order = section.items.aggregate(m=Max('order'))['m'] or -1
            item.order = max_order + 1
        item.save()
        messages.success(request, 'Item saved.')
        return redirect('dashboard:page_detail', pk=section.page_id)
    return render(request, 'dashboard/item_form.html', {
        'form': form, 'obj': obj, 'section': section, 'page': 'pages',
    })


@staff_login_required
def item_delete(request, pk):
    obj = get_object_or_404(SectionItem, pk=pk)
    page_pk = obj.section.page_id
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Item deleted.')
        return redirect('dashboard:page_detail', pk=page_pk)
    return render(request, 'dashboard/confirm_delete.html', {
        'obj': obj, 'obj_name': str(obj),
        'cancel_url': reverse('dashboard:page_detail', args=[page_pk]), 'page': 'pages',
    })


@staff_login_required
def item_toggle(request, pk):
    if request.method == 'POST':
        obj = get_object_or_404(SectionItem, pk=pk)
        obj.is_active = not obj.is_active
        obj.save(update_fields=['is_active'])
        return redirect('dashboard:page_detail', pk=obj.section.page_id)
    return redirect('dashboard:pages_list')


@staff_login_required
def item_move(request, pk, direction):
    if request.method == 'POST':
        obj      = get_object_or_404(SectionItem, pk=pk)
        siblings = list(obj.section.items.order_by('order'))
        idx      = next((i for i, s in enumerate(siblings) if s.pk == pk), None)
        swap_idx = idx - 1 if direction == 'up' else idx + 1
        if 0 <= swap_idx < len(siblings):
            other = siblings[swap_idx]
            obj.order, other.order = other.order, obj.order
            obj.save(update_fields=['order'])
            other.save(update_fields=['order'])
    return redirect('dashboard:page_detail', pk=obj.section.page_id)


# ── Navigation Menu ───────────────────────────────────────────────────────────

@staff_login_required
def navigation_menu(request):
    items = NavigationMenuItem.objects.all()
    return render(request, 'dashboard/navigation_menu.html', {'items': items, 'page': 'navigation'})


@staff_login_required
def nav_item_form(request, pk=None):
    obj  = get_object_or_404(NavigationMenuItem, pk=pk) if pk else None
    form = NavigationMenuItemForm(request.POST or None, instance=obj)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Menu item saved.')
        return redirect('dashboard:navigation_menu')
    return render(request, 'dashboard/nav_item_form.html', {
        'form': form, 'obj': obj, 'page': 'navigation',
    })


@staff_login_required
def nav_item_delete(request, pk):
    obj = get_object_or_404(NavigationMenuItem, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Menu item deleted.')
        return redirect('dashboard:navigation_menu')
    return render(request, 'dashboard/confirm_delete.html', {
        'obj': obj, 'obj_name': obj.label,
        'cancel_url': reverse('dashboard:navigation_menu'), 'page': 'navigation',
    })

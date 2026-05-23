from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Overview
    path('',                                    views.overview,                  name='overview'),
    path('settings/',                           views.site_settings,             name='site_settings'),

    # Hero slides
    path('hero-slides/',                        views.hero_slides,               name='hero_slides'),
    path('hero-slides/add/',                    views.hero_slide_form,           name='hero_slide_add'),
    path('hero-slides/<int:pk>/edit/',          views.hero_slide_form,           name='hero_slide_edit'),
    path('hero-slides/<int:pk>/delete/',        views.hero_slide_delete,         name='hero_slide_delete'),

    # Homepage sections
    path('homepage-sections/',                  views.homepage_sections,         name='homepage_sections'),
    path('homepage-sections/<int:pk>/edit/',    views.homepage_section_form,     name='homepage_section_edit'),

    # Value pillars
    path('value-pillars/',                      views.value_pillars,             name='value_pillars'),
    path('value-pillars/add/',                  views.value_pillar_form,         name='value_pillar_add'),
    path('value-pillars/<int:pk>/edit/',        views.value_pillar_form,         name='value_pillar_edit'),
    path('value-pillars/<int:pk>/delete/',      views.value_pillar_delete,       name='value_pillar_delete'),

    # About stats
    path('about-stats/',                        views.about_stats,               name='about_stats'),
    path('about-stats/add/',                    views.about_stat_form,           name='about_stat_add'),
    path('about-stats/<int:pk>/edit/',          views.about_stat_form,           name='about_stat_edit'),
    path('about-stats/<int:pk>/delete/',        views.about_stat_delete,         name='about_stat_delete'),

    # Services
    path('services/',                           views.services,                  name='services'),
    path('services/add/',                       views.service_form,              name='service_add'),
    path('services/<int:pk>/',                  views.service_detail,            name='service_detail'),
    path('services/<int:pk>/edit/',             views.service_form,              name='service_edit'),
    path('services/<int:pk>/delete/',           views.service_delete,            name='service_delete'),

    # Service features (nested under service)
    path('services/<int:service_pk>/features/add/',              views.service_feature_form,   name='feature_add'),
    path('services/<int:service_pk>/features/<int:pk>/edit/',    views.service_feature_form,   name='feature_edit'),
    path('services/<int:service_pk>/features/<int:pk>/delete/',  views.service_feature_delete, name='feature_delete'),

    # Academy
    path('academy/',                            views.academy,                   name='academy'),
    path('academy/categories/add/',             views.course_category_form,      name='course_category_add'),
    path('academy/categories/<int:pk>/edit/',   views.course_category_form,      name='course_category_edit'),
    path('academy/categories/<int:pk>/delete/', views.course_category_delete,    name='course_category_delete'),
    path('academy/courses/add/',                views.course_form,               name='course_add'),
    path('academy/courses/<int:pk>/edit/',      views.course_form,               name='course_edit'),
    path('academy/courses/<int:pk>/delete/',    views.course_delete,             name='course_delete'),

    # Research
    path('research/',                           views.research,                  name='research'),
    path('research/categories/add/',            views.research_category_form,    name='research_category_add'),
    path('research/categories/<int:pk>/edit/',  views.research_category_form,    name='research_category_edit'),
    path('research/categories/<int:pk>/delete/',views.research_category_delete,  name='research_category_delete'),
    path('research/projects/add/',              views.research_project_form,     name='research_project_add'),
    path('research/projects/<int:pk>/edit/',    views.research_project_form,     name='research_project_edit'),
    path('research/projects/<int:pk>/delete/',  views.research_project_delete,   name='research_project_delete'),

    # Publications
    path('publications/',                       views.publications,              name='publications'),
    path('publications/add/',                   views.publication_form,          name='publication_add'),
    path('publications/<int:pk>/edit/',         views.publication_form,          name='publication_edit'),
    path('publications/<int:pk>/delete/',       views.publication_delete,        name='publication_delete'),

    # Contact
    path('contact/',                            views.contact_settings,          name='contact_settings'),
    path('messages/',                           views.contact_messages,          name='messages'),
    path('messages/<int:pk>/',                  views.message_detail,            name='message_detail'),
    path('messages/<int:pk>/delete/',           views.message_delete,            name='message_delete'),
    path('inquiries/',                          views.inquiries,                 name='inquiries'),
    path('inquiries/<int:pk>/',                 views.inquiry_detail,            name='inquiry_detail'),
    path('inquiries/<int:pk>/delete/',          views.inquiry_delete,            name='inquiry_delete'),

    # Media
    path('media/',                              views.media_library,             name='media_library'),

    # Custom Pages
    path('pages/',                              views.pages_list,                name='pages_list'),
    path('pages/add/',                          views.page_form,                 name='page_add'),
    path('pages/<int:pk>/',                     views.page_detail,               name='page_detail'),
    path('pages/<int:pk>/edit/',                views.page_form,                 name='page_edit'),
    path('pages/<int:pk>/delete/',              views.page_delete,               name='page_delete'),

    # Page Sections (nested under page)
    path('pages/<int:page_pk>/sections/add/',   views.section_form,              name='section_add'),
    path('sections/<int:pk>/edit/',             views.section_form,              name='section_edit'),
    path('sections/<int:pk>/delete/',           views.section_delete,            name='section_delete'),
    path('sections/<int:pk>/toggle/',           views.section_toggle,            name='section_toggle'),
    path('sections/<int:pk>/move/<str:direction>/', views.section_move,          name='section_move'),

    # Section Items (nested under section)
    path('sections/<int:section_pk>/items/add/', views.item_form,               name='item_add'),
    path('items/<int:pk>/edit/',                views.item_form,                 name='item_edit'),
    path('items/<int:pk>/delete/',              views.item_delete,               name='item_delete'),
    path('items/<int:pk>/toggle/',              views.item_toggle,               name='item_toggle'),
    path('items/<int:pk>/move/<str:direction>/', views.item_move,                name='item_move'),

    # Navigation Menu
    path('navigation/',                         views.navigation_menu,           name='navigation_menu'),
    path('navigation/add/',                     views.nav_item_form,             name='nav_item_add'),
    path('navigation/<int:pk>/edit/',           views.nav_item_form,             name='nav_item_edit'),
    path('navigation/<int:pk>/delete/',         views.nav_item_delete,           name='nav_item_delete'),
]

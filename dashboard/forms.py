from django import forms
from core.models import SiteSetting, HomepageSection, HeroSlide, ValuePillar, AboutStat
from services.models import Service, ServiceFeature, CourseCategory, Course, ResearchCategory, ResearchProject
from publications.models import Publication
from messages_app.models import Inquiry, ContactPage
from pages.models import CustomPage, PageSection, SectionItem, NavigationMenuItem


class SiteSettingForm(forms.ModelForm):
    class Meta:
        model = SiteSetting
        exclude = ['created_at', 'updated_at']
        widgets = {
            'footer_text': forms.Textarea(attrs={'rows': 3}),
            'copyright_text': forms.TextInput(),
        }


class HomepageSectionForm(forms.ModelForm):
    class Meta:
        model = HomepageSection
        # section_name is set at creation and must never change — excluding it
        # prevents a silent validation failure when the hidden field isn't in POST
        exclude = ['created_at', 'updated_at', 'section_name']


class HeroSlideForm(forms.ModelForm):
    class Meta:
        model = HeroSlide
        exclude = ['created_at', 'updated_at']
        widgets = {'description': forms.Textarea(attrs={'rows': 3})}


class ValuePillarForm(forms.ModelForm):
    class Meta:
        model = ValuePillar
        exclude = ['created_at', 'updated_at']
        widgets = {'description': forms.Textarea(attrs={'rows': 3})}


class AboutStatForm(forms.ModelForm):
    class Meta:
        model = AboutStat
        fields = ['value', 'suffix', 'label', 'order', 'is_active']
        widgets = {
            'value':  forms.TextInput(attrs={'placeholder': 'e.g. 12, 40, £3.2'}),
            'suffix': forms.TextInput(attrs={'placeholder': 'e.g. + or bn (leave blank if none)'}),
            'label':  forms.TextInput(attrs={'placeholder': 'e.g. Markets Served'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        # full_description uses CKEditor's RichTextField — excluding it here
        # prevents a silent validation failure when it's absent from POST data.
        # It can be edited directly in the Django admin if needed.
        exclude = ['created_at', 'updated_at', 'full_description']
        widgets = {
            'short_description': forms.Textarea(attrs={'rows': 2}),
            'hero_description':  forms.Textarea(attrs={'rows': 3}),
            'cta_description':   forms.Textarea(attrs={'rows': 2}),
        }


class ServiceFeatureForm(forms.ModelForm):
    class Meta:
        model = ServiceFeature
        exclude = ['service', 'created_at', 'updated_at', 'full_description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class CourseCategoryForm(forms.ModelForm):
    class Meta:
        model = CourseCategory
        exclude = ['created_at', 'updated_at', 'full_description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ['created_at', 'updated_at', 'full_description']
        widgets = {
            'short_description': forms.Textarea(attrs={'rows': 2}),
        }


class ResearchCategoryForm(forms.ModelForm):
    class Meta:
        model = ResearchCategory
        exclude = ['created_at', 'updated_at', 'full_description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class ResearchProjectForm(forms.ModelForm):
    class Meta:
        model = ResearchProject
        exclude = ['created_at', 'updated_at', 'full_description']
        widgets = {
            'short_description': forms.Textarea(attrs={'rows': 2}),
        }


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        exclude = ['created_at', 'updated_at']
        widgets = {'short_description': forms.Textarea(attrs={'rows': 2})}


class ContactPageForm(forms.ModelForm):
    class Meta:
        model = ContactPage
        exclude = ['created_at', 'updated_at']
        widgets = {
            'description':        forms.Textarea(attrs={'rows': 4}),
            'map_embed':          forms.Textarea(attrs={'rows': 4}),
            'contact_form_intro': forms.Textarea(attrs={'rows': 3}),
        }


class InquiryNotesForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['admin_notes', 'is_read']
        widgets = {'admin_notes': forms.Textarea(attrs={'rows': 4})}


# ── Pages ─────────────────────────────────────────────────────────────────────

class CustomPageForm(forms.ModelForm):
    class Meta:
        model = CustomPage
        exclude = ['created_at', 'updated_at']
        widgets = {
            'description':     forms.Textarea(attrs={'rows': 3}),
            'seo_description': forms.Textarea(attrs={'rows': 2}),
        }


class PageSectionForm(forms.ModelForm):
    class Meta:
        model = PageSection
        exclude = ['page']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class SectionItemForm(forms.ModelForm):
    class Meta:
        model = SectionItem
        exclude = ['section']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class NavigationMenuItemForm(forms.ModelForm):
    class Meta:
        model = NavigationMenuItem
        fields = '__all__'
        widgets = {
            'external_url': forms.TextInput(attrs={'placeholder': 'e.g. /contact/ or https://...'}),
        }

from .models import SiteSetting


def site_settings(request):
    from pages.models import NavigationMenuItem
    nav_items = NavigationMenuItem.objects.filter(is_active=True).select_related('page')
    return {
        'site':      SiteSetting.load(),
        'nav_items': nav_items,
    }

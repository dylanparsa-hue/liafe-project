from messages_app.models import ContactMessage, Inquiry


def dashboard_counts(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return {}
    return {
        'unread_messages':  ContactMessage.objects.filter(is_read=False).count(),
        'unread_inquiries': Inquiry.objects.filter(is_read=False).count(),
    }

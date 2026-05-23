from django.shortcuts import render
from .models import ContactPage
from .forms import ContactForm


def contact(request):
    page    = ContactPage.objects.filter(pk=1).first() or ContactPage()
    form    = ContactForm()
    success = False

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()

    return render(request, 'pages/contact.html', {
        'page': page,
        'form': form,
        'success': success,
    })

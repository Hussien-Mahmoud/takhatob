from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from django.core.paginator import Paginator


from .forms import ContactForm
from users.models import Center, Specialist

# Create your views here.


def home(request):
    specialists = Specialist.objects.all()
    specialists_paginator = Paginator(specialists, 3)

    return render(request, 'main/Home.html', {
        'specialists_paginator': specialists_paginator,
        'centers': Center.objects.all()[:4]
    })


def contact_us(request):
    if request.method == 'POST':
        return render(request, 'main/contact-us-success.html')

    return render(request, 'main/contact-us.html')

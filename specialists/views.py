from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed, HttpResponseForbidden, HttpResponseBadRequest
from django.urls import reverse

from django.db.models import Avg

from users.models import Specialist, Client
from .forms import SpecialistEditForm, SpecialistAddReviewForm
from .models import SpecialistReviews, SpecialistCertifications
from chat.models import Room


# Create your views here.


def specialists_list(request):
    specialists = Specialist.objects.all()
    return render(request, 'specialists/specialists-list.html', {'specialists': specialists})


def specialist_details(request, id):
    specialist = get_object_or_404(Specialist, id=id)
    form = SpecialistAddReviewForm()
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        print(request.user in Client.objects.all())
        try:
            client = Client.objects.get(id=request.user.id)
        except:
            return HttpResponseForbidden()

        form = SpecialistAddReviewForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.client = client
            instance.specialist = specialist
            try:
                instance.save()
            except:
                return HttpResponseBadRequest()

    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

    average = int(SpecialistReviews.objects.filter(specialist=specialist)
                  .aggregate(Avg('rate')).get('rate__avg') or 0)

    client = Client.objects.filter(id=request.user.id)
    try:
        opened_chat = Room.objects.get(specialist=specialist, client=client[0] if client else Client.objects.none())
    except:
        opened_chat = None

    certifications = SpecialistCertifications.objects.filter(specialist=specialist)
    return render(request, 'specialists/specialist-details.html', {
        'reviews': SpecialistReviews,
        'average_rating': average,
        'specialist': specialist,
        'certifications': certifications,
        'opened_chat': opened_chat,
        'form': form,
    })


def specialist_edit(request, id):
    specialist = Specialist.objects.get(id=id)

    if request.user.id != specialist.id:
        return HttpResponseForbidden()

    if request.method == 'GET':
        form = SpecialistEditForm(instance=specialist)

    elif request.method == 'POST':
        # Certifications upload form
        files = request.FILES.getlist('certification_image')
        if files:
            SpecialistCertifications.objects.filter(specialist=specialist).delete()
            for file in files:
                SpecialistCertifications.objects.create(certification_image=file, specialist=specialist)

        form = SpecialistEditForm(request.POST, request.FILES, instance=specialist)
        if form.is_valid():
            print(form.full_clean())
            print(form.cleaned_data)
            form.save()

            return redirect(reverse('specialist-details', args=[id]))
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

    return render(request, 'specialists/specialist-edit.html', {
        'specialist': specialist,
        'form': form,
    })

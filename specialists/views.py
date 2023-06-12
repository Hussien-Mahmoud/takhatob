from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed, HttpResponseForbidden, HttpResponseBadRequest
from django.urls import reverse

from django.db.models import Avg

from users.models import Specialist, Client
from .forms import SpecialistEditForm, SpecialistAddReviewForm
from .models import SpecialistReviews
from chat.models import Room


# Create your views here.


def specialists_list(request):
    specialists = Specialist.objects.all()
    return render(request, 'specialists/specialists-list.html', {'specialists': specialists})


def specialist_details(request, id):
    specialist = Specialist.objects.get(id=id)
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

    return render(request, 'specialists/specialist-details.html', {
        'reviews': SpecialistReviews,
        'average_rating': average,
        'specialist': specialist,
        'opened_chat': opened_chat,
        'form': form,
    })


def specialist_edit(request, id):
    specialist = Specialist.objects.get(id=id)
    if request.method == 'GET':
        form = SpecialistEditForm()

    elif request.method == 'POST':
        form = SpecialistEditForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = id
            instance.email = specialist.email
            # instance.username = form.cleaned_data['username']
            # instance.excerpt = form.cleaned_data['excerpt']
            # instance.description = form.cleaned_data['description']
            # instance.experience = form.cleaned_data['experience']
            # instance.image = form.cleaned_data['image']
            instance.save()

            return redirect(reverse('specialist-details', args=[id]))
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

    return render(request, 'specialists/specialist-edit.html', {
        'specialist': specialist,
        'form': form
    })

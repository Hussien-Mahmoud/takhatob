from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed, HttpResponseForbidden, HttpResponseBadRequest
from django.urls import reverse

from django.db.models import Avg

from users.models import Center, Client
from .forms import CenterEditForm, CenterAddReviewForm
from .models import CenterReviews


# Create your views here.


def centers_list(request):
    centers = Center.objects.all()
    return render(request, 'centers/centers-list.html', {'centers': centers})


def center_details(request, id):
    center = Center.objects.get(id=id)
    form = CenterAddReviewForm()
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        print(request.user in Client.objects.all())
        try:
            client = Client.objects.get(id=request.user.id)
        except:
            return HttpResponseForbidden()

        form = CenterAddReviewForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.client = client
            instance.center = center
            try:
                instance.save()
            except:
                return HttpResponseBadRequest()

    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

    average = int(CenterReviews.objects.filter(center=center)
                  .aggregate(Avg('rate')).get('rate__avg', 0))
    return render(request, 'centers/center-details.html', {
        'reviews': CenterReviews,
        'average_rating': average,
        'center': center,
        'form': form,
    })


def center_edit(request, id):
    center = Center.objects.get(id=id)
    if request.method == 'GET':
        form = CenterEditForm()

    elif request.method == 'POST':
        form = CenterEditForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.id = id
            instance.email = center.email
            # instance.username = form.cleaned_data['username']
            # instance.excerpt = form.cleaned_data['excerpt']
            # instance.description = form.cleaned_data['description']
            # instance.experience = form.cleaned_data['experience']
            # instance.image = form.cleaned_data['image']
            instance.save()

            return redirect(reverse('center-details', args=[id]))
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

    return render(request, 'centers/center-edit.html', {
        'center': center,
        'form': form
    })

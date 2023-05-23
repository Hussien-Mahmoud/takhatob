from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from django.urls import reverse_lazy
from django.contrib.auth import login


from .forms import ClientSignUpForm, CenterSignupForm
from .models import Center

# Create your views here.


def sign_up(request):
    if request.method == 'GET':
        form = ClientSignUpForm()

    elif request.method == 'POST':
        form = ClientSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy('home'))
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

    return render(request, 'registration/sign_up.html', {
        'form': form
    })


def center_sign_up(request):
    if request.method == 'GET':
        form = CenterSignupForm()

    elif request.method == 'POST':
        form = CenterSignupForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy('home'))
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

    return render(request, 'registration/sign_up.html', {
        'form': form
    })


def centers_list(request):
    centers = Center.objects.all()
    return render(request, 'centers/CenterPages.html', {'centers': centers})


def center_details(request, id):
    center = Center.objects.get(id=id)
    return render(request, 'centers/center-details.html', {'center': center})

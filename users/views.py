from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from django.urls import reverse_lazy
from django.contrib.auth import login


from .forms import ClientSignUpForm, CenterSignUpForm, SpecialistSignUpForm
from .models import Center

# Create your views here.


def sign_up_choice(request):
    return render(request, 'registration/sign_up_choice.html')


def client_sign_up(request):
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
        form = CenterSignUpForm()

    elif request.method == 'POST':
        form = CenterSignUpForm(request.POST)
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


def specialist_sign_up(request):
    if request.method == 'GET':
        form = SpecialistSignUpForm()

    elif request.method == 'POST':
        form = SpecialistSignUpForm(request.POST)
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

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Client, Center, Specialist


class ClientSignUpForm(UserCreationForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email address'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Create password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})


class CenterSignUpForm(UserCreationForm):
    class Meta:
        model = Center
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email address'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Create password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})


class SpecialistSignUpForm(UserCreationForm):
    class Meta:
        model = Specialist
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last name'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email address'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Create password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm password'})

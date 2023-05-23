from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign-up'),
    path('center/sign-up/', views.center_sign_up, name='center-sign-up'),
]

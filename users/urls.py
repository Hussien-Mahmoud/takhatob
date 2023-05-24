from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up_choice, name='sign-up'),
    path('client/sign-up/', views.client_sign_up, name='client-sign-up'),
    path('center/sign-up/', views.center_sign_up, name='center-sign-up'),
    path('specialist/sign-up/', views.specialist_sign_up, name='specialist-sign-up'),
]

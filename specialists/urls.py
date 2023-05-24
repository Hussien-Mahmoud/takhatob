from django.urls import path
from . import views

urlpatterns = [
    path('', views.specialists_list, name='specialists-list'),
    path('<int:id>', views.specialist_details, name='specialist-details'),
    path('<int:id>/edit/', views.specialist_edit, name='specialist-edit'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.centers_list, name='centers-list'),
    path('<int:id>', views.center_details, name='center-details'),
    path('<int:id>/edit/', views.center_edit, name='center-edit'),
]

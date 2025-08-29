from django.urls import path
from . import views

urlpatterns = [
    path('', views.presentation_list, name='presentation_list'),
]
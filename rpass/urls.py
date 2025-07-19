from django.urls import path
from . import views

urlpatterns = [
    path('reset/', views.edit_pass, name='edit_pass'),
    path('reset/code/', views.tekshir, name='tekshir'),
    path('reset/new/', views.yparol, name='yparol'),
]

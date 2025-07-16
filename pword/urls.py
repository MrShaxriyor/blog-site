from django.urls import path
from . import views

urlpatterns = [
    path('reset-password/', views.edit_password, name='reset_password'),
    path('verify-code/', views.verify_code, name='check_code'),
    path('set-new-password/', views.set_new_password, name='set_new_password'),
]

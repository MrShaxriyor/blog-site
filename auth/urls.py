from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.user_login, name='get-login'),
    path('logout/', views.logout_view, name='get-log'),
    path('home/', views.home_view, name='home'),
]

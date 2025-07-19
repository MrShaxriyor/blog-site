from django.urls import path
from .views import *

urlpatterns = [
    path('', get_home, name='get-home'),
    # path('about/', get_about, name='about'),
    # path('contact/', get_contact, name='contact'),
    # path('blog/', get_blog, name='blog'),
     
]

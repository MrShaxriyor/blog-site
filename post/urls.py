from django.urls import path
from .views import *

urlpatterns = [
    # path('', category_list, name='home'), 
    path('news/<int:pk>/',post_detail, name='get-detail'),

]
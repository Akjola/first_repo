from django.urls import path
from .views import index, my_list

urlpatterns = [
    path('', index),
    path('list/', my_list),
]
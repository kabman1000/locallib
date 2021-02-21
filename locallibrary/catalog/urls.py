from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #specifies path to its view 
]
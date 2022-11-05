from django.urls import path
from . import views

urlpatterns = [
    path('', views.hngUser, name='task'),
    path('calculate', views.calculate, name="calculate"),
]
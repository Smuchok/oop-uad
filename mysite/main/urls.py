from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_page),
    path('about', views.about, name='about'),
]

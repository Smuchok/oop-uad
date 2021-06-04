from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_blog', views.add_blog, name='add_blog'),
    path('<int:pk>', views.blogInDetales.as_view(), name='blogInDetails'),
]

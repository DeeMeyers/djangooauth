from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.userpage, name='home'),
    path('home/pretty/', views.userpage2, name='althome'),
    
]
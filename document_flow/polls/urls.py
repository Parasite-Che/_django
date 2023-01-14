from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='polls-base'),
    path('', views.home, name='polls-home'),
    path('about/', views.about, name='about-club'),
]
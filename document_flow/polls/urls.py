from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='polls-base'),
    path('documents/', views.documents, name='polls-doc'),
    path('my_documents/', views.my_documents, name='polls-myDoc'),
    path('settings/', views.settings, name='polls-settings'),
]
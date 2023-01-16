from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name='polls-base'),
    path('documents/', views.documents.as_view(), name='polls-doc'),
    path(r'^documents/docs_creating/&', views.DataCreate.as_view(), name='polls-doc-cr'),
    path(r'^documents/(?P<pk>\d+)/docs_updating/&', views.DataUpdate.as_view(), name='polls-doc-up'),
    path(r'^documents/(?P<pk>\d+)/docs_deleting/&', views.DataDelete.as_view(), name='polls-doc-de'),
    path('my_documents/', views.my_documents, name='polls-myDoc'),
    path('settings/', views.settings, name='polls-settings'),
]
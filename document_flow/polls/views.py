from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django_tables2 import SingleTableView
from users.models import Profile
from users.tables import ProfileTable


@login_required(login_url='login')
def base(request):
    return render(request, 'polls/base.html', {
        'foo': 'bar',
    })


class PersonListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    model = Profile
    table_class = ProfileTable
    template_name = 'polls/documents.html'


def documents(request):
    table = ProfileTable(Profile.objects.all())

    return render(request, "polls/documents.html", {
        "table": table
    })


@login_required(login_url='login')
def my_documents(request):

    return render(request, 'polls/my_documents.html', {
        'foo': 'bar',
    })


@login_required(login_url='login')
def settings(request):
    return render(request, 'polls/settings.html', {
        'foo': 'bar',
    })






# Create your views here.

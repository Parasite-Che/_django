from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def base(request):
    return render(request, 'polls/base.html', {
        'foo': 'bar',
    })


@login_required(login_url='login')
def documents(request):
    return render(request, 'polls/documents.html', {
        'foo': 'bar',
    })


@login_required(login_url='login')
def my_documents(request):
    return render(request, 'polls/my_documents.html', {
        'foo': 'bar',
    })


def settings(request):
    return render(request, 'polls/settings.html', {
        'foo': 'bar',
    })


# Create your views here.

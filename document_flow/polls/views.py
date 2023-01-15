from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def base(request):
    return render(request, 'polls/base.html', {
        'foo': 'bar',
    })


def home(request):
    return render(request, 'polls/home.html', {
        'foo': 'bar',
    })


def about(request):
    return render(request, 'polls/about.html', {
        'foo': 'bar',
    })


# Create your views here.

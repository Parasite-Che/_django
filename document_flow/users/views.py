from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
	return render(request, 'polls/base.html')


# Create your views here.

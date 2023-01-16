from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import SingleTableView
from main_datas.models import Data
from main_datas.models import UploadFileForm
from main_datas.tables import DataTable

import datetime

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


@login_required(login_url='login')
def base(request):
    return render(request, 'polls/base.html', {
        'foo': 'bar',
    })


class documents(LoginRequiredMixin, SingleTableView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    model = Data
    table_class = DataTable
    template_name = 'polls/documents.html'


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


@login_required(login_url='login')
def documents_creating(request):

    # Если данный запрос типа POST, тогда
    if request.method == 'POST':

        # Создаём экземпляр формы и заполняем данными из запроса (связывание, binding):
        form = UploadFileForm(request.POST)

        # Проверка валидности данных формы:
        if form.is_valid():
            # Обработка данных из form.cleaned_data
            #(здесь мы просто присваиваем их полю due_back)


            # Переход по адресу 'all-borrowed':
            return HttpResponseRedirect(reverse('polls-doc'))

    # Если это GET (или какой-либо ещё), создать форму по умолчанию.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = UploadFileForm(initial={'date_of_manufacture': proposed_renewal_date,})

    return render(request, 'polls/data_form.html', {'form': form})


class DataCreate(CreateView):
    model = Data
    fields = '__all__'

    def get_success_url(self):
        return reverse('polls-doc')


class DataUpdate(UpdateView):
    model = Data
    fields = ['signed_by', 'message']


class DataDelete(DeleteView):
    model = Data
    success_url = reverse_lazy('Datas')


# Create your views here.

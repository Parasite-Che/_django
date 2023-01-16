from django.db import models
from django.contrib.auth.models import User
from django import forms
import datetime
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.utils.translation import ngettext_lazy as _
from django.forms import ModelForm




class Data(models.Model):
    header = models.CharField(max_length=100)
    document_type = models.CharField(max_length=20)
    theme = models.CharField(max_length=50)
    made_by = models.CharField(max_length=50)
    signed_by = models.CharField(max_length=50)
    date_of_manufacture = models.DateField()
    message = models.CharField(max_length=300)


class UploadFileForm(forms.Form):
    header = forms.CharField(max_length=100)
    document_type = forms.CharField(max_length=20)
    theme = forms.CharField(max_length=50)
    made_by = forms.CharField(max_length=50)
    signed_by = forms.CharField(max_length=50)
    date_of_manufacture = forms.DateField()
    message = forms.CharField(max_length=300)

    def clean_renewal_date(self):
        data = self.cleaned_data['date_of_manufacture']

        if data > datetime.date.today():
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        return data


class RenewBookModelForm(ModelForm):
    pk_url_kwarg = 'id'

    class Meta:
        model = Data
        fields = '__all__'

    def clean_due_back(self):
        data = self.cleaned_data['date_of_manufacture']

        #Check date is in range librarian allowed to change (+4 weeks)
        if data > datetime.date.today():
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))

        # Не забывайте всегда возвращать очищенные данные
        return data



# Create your models here.

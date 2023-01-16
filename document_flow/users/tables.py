import django_tables2 as tables
from .models import Profile


class ProfileTable(tables.Table):
    class Meta:
        model = Profile
        template_name = "polls/documents.html"
        fields = ("name", )
        sequence = ()
        exclude = ("ID",)

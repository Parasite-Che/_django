# Generated by Django 4.1.5 on 2023-01-16 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_datas", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="data",
            name="message",
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(default="default.jpg", upload_to="media"),
        ),
    ]

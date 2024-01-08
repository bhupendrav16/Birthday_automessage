# Generated by Django 5.0.1 on 2024-01-06 08:41

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("address", models.TextField()),
                ("dob", models.DateField()),
                ("date_of_joining", models.DateField()),
                ("email", models.EmailField(max_length=254)),
                (
                    "phone_no",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
            ],
        ),
    ]
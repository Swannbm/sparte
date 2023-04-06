# Generated by Django 3.2.15 on 2022-08-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0006_contactform"),
    ]

    operations = [
        migrations.CreateModel(
            name="Newsletter",
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
                (
                    "email",
                    models.EmailField(max_length=254, verbose_name="Votre courriel"),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("confirm_token", models.CharField(max_length=25)),
                ("confirmation_date", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]

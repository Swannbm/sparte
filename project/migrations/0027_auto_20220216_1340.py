# Generated by Django 3.2.11 on 2022-02-16 13:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0026_request"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="first_year_ocsge",
            field=models.IntegerField(
                default=2015,
                validators=[django.core.validators.MinValueValidator(2000)],
                verbose_name="Premier millésime OCSGE",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="last_year_ocsge",
            field=models.IntegerField(
                default=2018,
                validators=[django.core.validators.MinValueValidator(2000)],
                verbose_name="Dernier millésime OCSGE",
            ),
            preserve_default=False,
        ),
    ]

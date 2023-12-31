# Generated by Django 3.2.5 on 2022-01-06 21:35

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("public_data", "0037_refplan_naf11art20"),
    ]

    operations = [
        migrations.CreateModel(
            name="Commune",
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
                ("insee", models.CharField(max_length=5, verbose_name="Code INSEE")),
                ("name", models.CharField(max_length=45, verbose_name="Nom")),
                (
                    "mpoly",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
                (
                    "departement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="public_data.departement",
                    ),
                ),
                (
                    "epci",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="public_data.epci",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 3.2.16 on 2022-12-15 10:48

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.db import migrations, models

import public_data.models.administration


class Migration(migrations.Migration):
    dependencies = [
        ("public_data", "0080_auto_20220826_1635"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commune",
            name="departement",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="public_data.departement",
            ),
        ),
        migrations.AlterField(
            model_name="commune",
            name="epci",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="public_data.epci"),
        ),
        migrations.CreateModel(
            name="Scot",
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
                ("name", models.CharField(max_length=50, verbose_name="Nom")),
                (
                    "mpoly",
                    django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326),
                ),
                ("is_inter_departement", models.BooleanField(default=False)),
                ("state_statut", models.CharField(max_length=250)),
                ("detailed_state_statut", models.CharField(max_length=250)),
                (
                    "date_published_perimeter",
                    models.DateField(blank=True, null=True, verbose_name="Publication du périmètre"),
                ),
                (
                    "date_acting",
                    models.DateField(blank=True, null=True, verbose_name="Engagement"),
                ),
                (
                    "date_stop",
                    models.DateField(blank=True, null=True, verbose_name="Arrêt du projet"),
                ),
                (
                    "date_validation",
                    models.DateField(blank=True, null=True, verbose_name="Approbation"),
                ),
                (
                    "date_end",
                    models.DateField(blank=True, null=True, verbose_name="Fin échéance"),
                ),
                ("is_ene_law", models.BooleanField(default=False)),
                ("scot_type", models.CharField(max_length=250)),
                ("siren", models.CharField(max_length=12)),
                (
                    "departement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="public_data.departement",
                    ),
                ),
                (
                    "region",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="public_data.region",
                    ),
                ),
            ],
            bases=(
                public_data.models.administration.LandMixin,
                public_data.models.administration.GetDataFromCeremaMixin,
                models.Model,
            ),
        ),
        migrations.AddField(
            model_name="commune",
            name="scot",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="public_data.scot",
            ),
        ),
    ]

# Generated by Django 3.2.5 on 2021-09-20 20:15

import django.contrib.gis.db.models.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import project.models
import public_data.models.mixins


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("project", "0011_alter_emprise_project"),
    ]

    operations = [
        migrations.CreateModel(
            name="Plan",
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
                ("name", models.CharField(max_length=100, verbose_name="Nom")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Description"),
                ),
                (
                    "shape_file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=project.models.user_directory_path,
                        verbose_name="Fichier .shp",
                    ),
                ),
                (
                    "import_error",
                    models.TextField(
                        blank=True,
                        null=True,
                        verbose_name="Message d'erreur traitement emprise",
                    ),
                ),
                (
                    "import_date",
                    models.DateTimeField(blank=True, null=True, verbose_name="Date et heure d'import"),
                ),
                (
                    "import_status",
                    models.CharField(
                        choices=[
                            ("MISSING", "Emprise à renseigner"),
                            ("PENDING", "Traitement du fichier Shape en cours"),
                            ("SUCCESS", "Emprise renseignée"),
                            ("FAILED", "Création de l'emprise échouée"),
                        ],
                        default="MISSING",
                        max_length=10,
                        verbose_name="Statut import",
                    ),
                ),
                (
                    "supplier_email",
                    models.EmailField(blank=True, max_length=254, verbose_name="Email du prestataire"),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="project.project",
                        verbose_name="Projet",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="propriétaire",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="emprise",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="project.project",
                verbose_name="Projet",
            ),
        ),
        migrations.CreateModel(
            name="PlanEmprise",
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
                    "mpoly",
                    django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Nom")),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="Description"),
                ),
                (
                    "lot",
                    models.CharField(blank=True, max_length=100, verbose_name="Lot"),
                ),
                (
                    "surface",
                    models.IntegerField(blank=True, null=True, verbose_name="Surface (ha)"),
                ),
                (
                    "us_code",
                    models.CharField(blank=True, max_length=10, verbose_name="Code usage du sol"),
                ),
                (
                    "cs_code",
                    models.CharField(blank=True, max_length=10, verbose_name="Code couverture du sol"),
                ),
                (
                    "prev_surface_artificial",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name="Surface artificielle avant (ha)",
                    ),
                ),
                (
                    "prev_surface_natural",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name="Surface naturelle avant (ha)",
                    ),
                ),
                (
                    "new_surface_artificial",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name="Nouvelle surface artificielle (ha)",
                    ),
                ),
                (
                    "new_surface_natural",
                    models.IntegerField(
                        blank=True,
                        null=True,
                        verbose_name="Nouvelle surface naturelle (ha)",
                    ),
                ),
                (
                    "plan",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="project.plan"),
                ),
            ],
            options={
                "ordering": ["plan", "name"],
            },
            bases=(public_data.models.mixins.DataColorationMixin, models.Model),
        ),
    ]

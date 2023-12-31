# Generated by Django 3.2.16 on 2022-12-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0048_auto_20221201_1149"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="land_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("COMM", "Commune"),
                    ("EPCI", "EPCI"),
                    ("DEPART", "Département"),
                    ("SCOT", "Scot"),
                    ("REGION", "Région"),
                    ("COMP", "Composite"),
                ],
                default="EPCI",
                help_text="Indique le niveau administratif des territoires sélectionnés par l'utilisateur lors de la création du diagnostic. Cela va de la commune à la région.",
                max_length=7,
                null=True,
                verbose_name="Type de territoire",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="level",
            field=models.CharField(
                choices=[
                    ("COMM", "Commune"),
                    ("EPCI", "EPCI"),
                    ("DEPART", "Département"),
                    ("SCOT", "Scot"),
                    ("REGION", "Région"),
                    ("COMP", "Composite"),
                ],
                default="COMMUNE",
                help_text="Utilisé dans les rapports afin de déterminer le niveau d'aggrégation des données à afficher. Si EPCI est sélectionné, alors les rapports montre des données EPCI par EPCI.",
                max_length=7,
                verbose_name="Niveau d'analyse",
            ),
        ),
    ]

# Generated by Django 3.2.13 on 2022-05-10 12:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("public_data", "0053_rename_is_new_naf_ocsgediff_is_new_natural"),
    ]

    operations = [
        migrations.AddField(
            model_name="commune",
            name="last_millesime",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(2000),
                    django.core.validators.MaxValueValidator(2050),
                ],
                verbose_name="Dernier millésime disponible",
            ),
        ),
        migrations.AddField(
            model_name="commune",
            name="surface_artif",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=15,
                null=True,
                verbose_name="Surface artificielle",
            ),
        ),
        migrations.AlterField(
            model_name="commune",
            name="map_color",
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name="Couleur d'affichage"),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-02 15:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("public_data", "0091_zoneurba_typezone"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArtifAreaZoneUrba",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "year",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(2000),
                            django.core.validators.MaxValueValidator(2050),
                        ],
                        verbose_name="Millésime",
                    ),
                ),
                ("area", models.DecimalField(decimal_places=4, max_digits=15, verbose_name="Surface artificielle")),
            ],
        ),
        migrations.RemoveField(
            model_name="zoneurba",
            name="artificial_area",
        ),
        migrations.AddIndex(
            model_name="zoneurba",
            index=models.Index(fields=["insee"], name="public_data_insee_3f872f_idx"),
        ),
        migrations.AddIndex(
            model_name="zoneurba",
            index=models.Index(fields=["typezone"], name="public_data_typezon_32785a_idx"),
        ),
        migrations.AddField(
            model_name="artifareazoneurba",
            name="zone_urba",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="public_data.zoneurba"),
        ),
        migrations.AddIndex(
            model_name="artifareazoneurba",
            index=models.Index(fields=["zone_urba"], name="public_data_zone_ur_cb8473_idx"),
        ),
        migrations.AddIndex(
            model_name="artifareazoneurba",
            index=models.Index(fields=["year"], name="public_data_year_71d4f9_idx"),
        ),
        migrations.AddIndex(
            model_name="artifareazoneurba",
            index=models.Index(fields=["zone_urba", "year"], name="public_data_zone_ur_57615b_idx"),
        ),
        migrations.AddConstraint(
            model_name="artifareazoneurba",
            constraint=models.UniqueConstraint(fields=("zone_urba", "year"), name="unique_zone_year"),
        ),
    ]
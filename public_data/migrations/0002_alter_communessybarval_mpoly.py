# Generated by Django 3.2.5 on 2021-08-13 22:22

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("public_data", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="communessybarval",
            name="mpoly",
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]

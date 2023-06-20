# Generated by Django 4.2.1 on 2023-05-24 08:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("public_data", "0088_ocsge_public_data_is_arti_05643d_idx"),
    ]

    operations = [
        migrations.RenameField(
            model_name="zoneurba",
            old_name="insee",
            new_name="origin_insee",
        ),
        migrations.AddField(
            model_name="zoneurba",
            name="area",
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name="area"),
        ),
        migrations.AddField(
            model_name="zoneurba",
            name="artificial_area",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=15, null=True, verbose_name="artificial_area"
            ),
        ),
        migrations.AddField(
            model_name="zoneurba",
            name="insee",
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name="insee"),
        ),
    ]
# Generated by Django 4.2.1 on 2023-05-17 08:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0053_rename_async_city_and_combined_emprise_done_historicalproject_async_add_city_done_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalproject",
            name="available_millesimes",
            field=models.CharField(
                blank=True,
                help_text="Millésimes disponibles sur la période d'analyse du diagnostic.",
                max_length=255,
                null=True,
                verbose_name="OCS GE disponibles",
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="available_millesimes",
            field=models.CharField(
                blank=True,
                help_text="Millésimes disponibles sur la période d'analyse du diagnostic.",
                max_length=255,
                null=True,
                verbose_name="OCS GE disponibles",
            ),
        ),
    ]
# Generated by Django 4.2 on 2023-05-02 07:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0051_historicalrequest_historicalproject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalproject",
            name="target_2031",
            field=models.IntegerField(
                default=50,
                help_text="A date, l'objectif national est de réduire de 50% la consommation d'espace d'ici à 2031. Cet objectif doit être personnalisé localement par les SRADDET. Vous pouvez changer l'objectif pour tester différents scénarios.",
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
                verbose_name="Objectif 2031 (en %)",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="target_2031",
            field=models.IntegerField(
                default=50,
                help_text="A date, l'objectif national est de réduire de 50% la consommation d'espace d'ici à 2031. Cet objectif doit être personnalisé localement par les SRADDET. Vous pouvez changer l'objectif pour tester différents scénarios.",
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
                verbose_name="Objectif 2031 (en %)",
            ),
        ),
    ]

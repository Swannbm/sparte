# Generated by Django 3.2.5 on 2021-11-02 11:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("project", "0015_auto_20211025_2134"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plan",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="propriétaire",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="propriétaire",
            ),
        ),
    ]

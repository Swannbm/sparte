# Generated by Django 3.2.5 on 2021-09-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0013_alter_planemprise_plan"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="couverture_usage",
            field=models.JSONField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.16 on 2023-01-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("public_data", "0083_auto_20230113_1752"),
    ]

    operations = [
        migrations.AddField(
            model_name="couverturesol",
            name="is_key",
            field=models.BooleanField(default=False, verbose_name="Est déterminant"),
        ),
        migrations.AddField(
            model_name="usagesol",
            name="is_key",
            field=models.BooleanField(default=False, verbose_name="Est déterminant"),
        ),
    ]

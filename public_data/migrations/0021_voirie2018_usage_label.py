# Generated by Django 3.2.5 on 2021-09-29 20:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("public_data", "0020_auto_20210928_1210"),
    ]

    operations = [
        migrations.AddField(
            model_name="voirie2018",
            name="usage_label",
            field=models.CharField(
                blank=True,
                max_length=254,
                null=True,
                verbose_name="Libellé usage du sol",
            ),
        ),
    ]

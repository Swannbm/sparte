# Generated by Django 3.2.14 on 2022-07-26 16:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("public_data", "0072_auto_20220726_1621"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cerema",
            name="cateaav202",
        ),
        migrations.AddField(
            model_name="cerema",
            name="aav2020_ty",
            field=models.CharField(max_length=39, null=True),
        ),
        migrations.AddField(
            model_name="cerema",
            name="scot",
            field=models.CharField(max_length=254, null=True),
        ),
    ]

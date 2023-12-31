# Generated by Django 3.2.14 on 2022-07-26 19:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("public_data", "0073_auto_20220726_1625"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cerema",
            name="aav2020",
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name="cerema",
            name="aav2020_ty",
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name="cerema",
            name="city_insee",
            field=models.CharField(db_index=True, max_length=7),
        ),
        migrations.AlterField(
            model_name="cerema",
            name="city_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="cerema",
            name="dept_id",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="cerema",
            name="dept_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="cerema",
            name="epci_id",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="cerema",
            name="epci_name",
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name="cerema",
            name="libaav2020",
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name="cerema",
            name="region_id",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="cerema",
            name="region_name",
            field=models.CharField(max_length=50),
        ),
    ]

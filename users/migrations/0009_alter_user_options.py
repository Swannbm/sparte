# Generated by Django 3.2.15 on 2022-09-22 15:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0008_auto_20210929_2029"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "Utilisateur"},
        ),
    ]

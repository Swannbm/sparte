# Generated by Django 3.2.13 on 2022-05-12 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("public_data", "0056_auto_20220511_0718"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ocsge",
            name="id_origine",
        ),
        migrations.RemoveField(
            model_name="ocsge",
            name="millesime",
        ),
        migrations.RemoveField(
            model_name="ocsge",
            name="millesime_source",
        ),
    ]
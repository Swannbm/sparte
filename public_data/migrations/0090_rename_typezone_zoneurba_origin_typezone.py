# Generated by Django 4.2.1 on 2023-06-02 15:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("public_data", "0089_zoneurba_area_zoneurba_artificial_area_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="zoneurba",
            old_name="typezone",
            new_name="origin_typezone",
        ),
    ]

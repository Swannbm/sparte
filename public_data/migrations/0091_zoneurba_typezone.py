# Generated by Django 4.2.1 on 2023-06-02 15:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("public_data", "0090_rename_typezone_zoneurba_origin_typezone"),
    ]

    operations = [
        migrations.AddField(
            model_name="zoneurba",
            name="typezone",
            field=models.CharField(blank=True, max_length=3, null=True, verbose_name="typezone"),
        ),
    ]

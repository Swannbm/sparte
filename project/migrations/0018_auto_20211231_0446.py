# Generated by Django 3.2.5 on 2021-12-31 04:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0017_auto_20211216_2053"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="is_public",
            field=models.BooleanField(default=False, verbose_name="Public"),
        ),
        migrations.AddField(
            model_name="project",
            name="public_key",
            field=models.SlugField(
                help_text="We need a way to find Project related to Region, Departement or EPCI\nthis is the purpose of below field which has a very specific rule of\nconstruction, it's like a slug\nepci : EPCI_[ID]\ndepartement : DEPART_[ID]\nregion : REGION_[ID]",
                null=True,
                unique=True,
            ),
        ),
    ]

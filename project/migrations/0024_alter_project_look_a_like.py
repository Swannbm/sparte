# Generated by Django 3.2.5 on 2022-01-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0023_auto_20220114_1613"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="look_a_like",
            field=models.CharField(
                help_text="We need a way to find Project related within Cerema's data. this is the purpose of this field which has a very specific rule of construction, it's like a slug: EPCI_[ID], DEPART_[ID] (département), REGION_[ID], COMMUNE_[ID]. field can contain several public key separate by ;",
                max_length=250,
                null=True,
                verbose_name="Territoire pour se comparer",
            ),
        ),
    ]
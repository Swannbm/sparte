# Generated by Django 3.2.15 on 2022-08-26 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("public_data", "0077_communepop"),
    ]

    operations = [
        migrations.AddField(
            model_name="communepop",
            name="menage",
            field=models.IntegerField(blank=True, null=True, verbose_name="Nb ménages"),
        ),
        migrations.AlterField(
            model_name="communepop",
            name="pop",
            field=models.IntegerField(blank=True, null=True, verbose_name="Population"),
        ),
    ]

# Generated by Django 3.2.16 on 2022-12-15 10:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0009_alter_contactform_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsletter",
            name="email",
            field=models.EmailField(max_length=254, verbose_name="Courriel"),
        ),
    ]

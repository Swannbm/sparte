# Generated by Django 3.2.15 on 2022-08-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0007_newsletter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsletter",
            name="confirm_token",
            field=models.CharField(max_length=25, unique=True),
        ),
    ]

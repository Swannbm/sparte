# Generated by Django 3.2.18 on 2023-02-27 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostic_word', '0002_auto_20230224_1314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wordtemplate',
            options={'ordering': ['slug'], 'verbose_name': 'Modèle Word', 'verbose_name_plural': 'Modèles Word'},
        ),
    ]

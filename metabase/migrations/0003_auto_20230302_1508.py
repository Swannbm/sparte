# Generated by Django 3.2.18 on 2023-03-02 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0050_auto_20230224_1306'),
        ('metabase', '0002_auto_20230302_1443'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OnlineDiagnostic',
            new_name='StatDiagnostic',
        ),
        migrations.AlterModelOptions(
            name='statdiagnostic',
            options={'ordering': ['-created_date'], 'verbose_name': 'Statistique'},
        ),
    ]
# Generated by Django 3.2.14 on 2022-07-29 10:46

from django.db import migrations, models
import project.models.project_base


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0036_auto_20220728_1543"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="cover_image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=project.models.project_base.upload_in_project_folder,
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="folder_name",
            field=models.CharField(
                blank=True, max_length=15, null=True, verbose_name="Dossier"
            ),
        ),
    ]

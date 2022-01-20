# Generated by Django 3.2.5 on 2022-01-20 12:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("project", "0024_alter_project_look_a_like"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="created_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="updated_date",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="analyse_end_date",
            field=models.CharField(
                choices=[
                    ("2009", "2009"),
                    ("2010", "2010"),
                    ("2011", "2011"),
                    ("2012", "2012"),
                    ("2013", "2013"),
                    ("2014", "2014"),
                    ("2015", "2015"),
                    ("2016", "2016"),
                    ("2017", "2017"),
                    ("2018", "2018"),
                    ("2019", "2019"),
                ],
                default="2018",
                max_length=4,
                verbose_name="Date de fin de période d'analyse",
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="analyse_start_date",
            field=models.CharField(
                choices=[
                    ("2009", "2009"),
                    ("2010", "2010"),
                    ("2011", "2011"),
                    ("2012", "2012"),
                    ("2013", "2013"),
                    ("2014", "2014"),
                    ("2015", "2015"),
                    ("2016", "2016"),
                    ("2017", "2017"),
                    ("2018", "2018"),
                    ("2019", "2019"),
                ],
                default="2015",
                max_length=4,
                verbose_name="Date de début de période d'analyse",
            ),
        ),
    ]
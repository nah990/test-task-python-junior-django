# Generated by Django 4.1.1 on 2022-11-30 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stations", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pointing",
            name="axis",
            field=models.CharField(
                choices=[("x", "x"), ("y", "y"), ("z", "z")], max_length=1
            ),
        ),
    ]

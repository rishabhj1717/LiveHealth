# Generated by Django 2.1 on 2018-09-19 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0034_studentmarks_doexam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmarks',
            name='isPresent',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentmarks',
            name='isUpdated',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 2.1 on 2018-09-18 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0027_auto_20180918_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='marks',
        ),
    ]

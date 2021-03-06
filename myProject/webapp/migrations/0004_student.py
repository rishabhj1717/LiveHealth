# Generated by Django 2.1 on 2018-09-14 05:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20180914_0509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Phone number')),
                ('emailP', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('dept', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('doj', models.DateField()),
            ],
        ),
    ]

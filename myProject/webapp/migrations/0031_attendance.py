# Generated by Django 2.1 on 2018-09-18 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0030_delete_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecId', models.CharField(default='0', max_length=50)),
                ('roll', models.CharField(max_length=10)),
                ('curratt', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
    ]

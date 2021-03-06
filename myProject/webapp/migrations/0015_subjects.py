# Generated by Django 2.1 on 2018-09-16 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem1', models.CharField(max_length=100)),
                ('sem2', models.CharField(max_length=100)),
                ('sem3', models.CharField(max_length=100)),
                ('sem4', models.CharField(max_length=100)),
                ('courseName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Courses')),
                ('deptName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Department')),
            ],
        ),
    ]

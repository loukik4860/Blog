# Generated by Django 4.2.6 on 2023-11-18 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApp', '0003_notificationmodel_remove_subjectmodel_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamSectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
            ],
        ),
    ]

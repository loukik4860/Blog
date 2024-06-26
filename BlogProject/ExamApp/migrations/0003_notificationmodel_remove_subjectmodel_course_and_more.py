# Generated by Django 4.2.6 on 2023-11-18 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApp', '0002_commissionmodel_exammodel_syllabus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('Year', models.CharField(max_length=10, unique=True)),
                ('date', models.DateTimeField()),
                ('description', models.TextField(blank=True, null=True)),
                ('credits', models.PositiveIntegerField(blank=True, default=3, null=True)),
                ('official_notification', models.FileField(upload_to='Files/Notification')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('exam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='ExamApp.exammodel')),
            ],
        ),
        migrations.RemoveField(
            model_name='subjectmodel',
            name='course',
        ),
        migrations.AddField(
            model_name='subjectmodel',
            name='exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='ExamApp.exammodel'),
        ),
        migrations.DeleteModel(
            name='CourseModel',
        ),
    ]

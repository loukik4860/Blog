# Generated by Django 4.2.6 on 2023-12-01 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApp', '0018_rename_blogtitleimage_titleimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='notesmodel',
            name='title_image',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ExamApp.titleimage'),
        ),
    ]

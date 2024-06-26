# Generated by Django 4.2.6 on 2023-11-24 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApp', '0012_remove_notesmodel_tags_notesmodel_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorisationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='ExamApp.subjectmodel')),
            ],
        ),
        migrations.CreateModel(
            name='ChapterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapterName', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ExamApp.categorisationmodel')),
            ],
        ),
        migrations.AddField(
            model_name='notesmodel',
            name='chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='note', to='ExamApp.chaptermodel'),
        ),
    ]

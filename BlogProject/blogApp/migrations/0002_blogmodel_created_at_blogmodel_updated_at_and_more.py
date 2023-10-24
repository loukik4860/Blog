# Generated by Django 4.2.6 on 2023-10-24 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='is_published',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='blogs', to='blogApp.tag'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
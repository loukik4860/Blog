# Generated by Django 4.2.6 on 2023-11-30 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_remove_blogmodel_blogimage_blogmodel_blogimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='tag',
            field=models.ManyToManyField(related_name='tag', to='blogApp.tag'),
        ),
    ]

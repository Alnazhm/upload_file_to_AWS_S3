# Generated by Django 4.2.6 on 2023-10-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='file',
        ),
        migrations.AddField(
            model_name='document',
            name='file_extension',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='document',
            name='file_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]

# Generated by Django 3.2 on 2021-10-23 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='en_slug',
            new_name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='fr_slug',
        ),
    ]
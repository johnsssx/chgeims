# Generated by Django 4.0 on 2022-01-17 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_post_copiri_post_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entries',
            name='funds',
        ),
    ]
# Generated by Django 4.0.1 on 2022-03-20 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_aside'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aside',
            old_name='bot',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='aside',
            old_name='img',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='aside',
            old_name='top',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='aside',
            old_name='urll',
            new_name='url',
        ),
    ]
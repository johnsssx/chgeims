# Generated by Django 4.0.1 on 2022-03-20 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_rename_bot_aside_description_rename_img_aside_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aside',
            old_name='title',
            new_name='header',
        ),
        migrations.RenameField(
            model_name='aside',
            old_name='url',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='aside',
            old_name='description',
            new_name='note',
        ),
        migrations.RenameField(
            model_name='aside',
            old_name='image',
            new_name='photo',
        ),
    ]
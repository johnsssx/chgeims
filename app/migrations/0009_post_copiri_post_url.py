# Generated by Django 4.0 on 2022-01-10 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_download_entries_article_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='copiri',
            field=models.CharField(max_length=75, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

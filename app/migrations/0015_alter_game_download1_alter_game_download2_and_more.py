# Generated by Django 4.0 on 2022-03-20 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_remove_game_download_game_download1_game_download2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='download1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='download2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='download3',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='screen1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='screen2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='screen3',
            field=models.URLField(blank=True, null=True),
        ),
    ]
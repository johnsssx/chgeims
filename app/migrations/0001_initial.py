# Generated by Django 4.0 on 2021-12-17 23:23

import app.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, upload_to=app.models.custom_upload_to)),
                ('bio', models.TextField(blank=True)),
                ('link', models.URLField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            options={
                'ordering': ['user__username'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('number', models.IntegerField(unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=75, unique=True)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='app.images')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='auth.user')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('gb', models.IntegerField(null=True)),
                ('content', models.TextField(unique=True)),
                ('date', models.DateField(verbose_name=datetime.date.today)),
                ('url', models.URLField(blank=True)),
                ('image', models.ImageField(upload_to='app.images')),
                ('miniature', models.ImageField(upload_to='app.miniature')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.genders')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.review')),
            ],
        ),
        migrations.CreateModel(
            name='Entries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('funds', models.IntegerField()),
                ('description', models.CharField(max_length=75, unique=True)),
                ('content', models.TextField(unique=True)),
                ('url', models.URLField(blank=True)),
                ('date', models.DateField(verbose_name=datetime.date.today)),
                ('image', models.ImageField(upload_to='app.images')),
                ('miniature', models.ImageField(upload_to='app.images_miniature')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.genders')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.review')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.post')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
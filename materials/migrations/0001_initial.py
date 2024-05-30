# Generated by Django 5.0.6 on 2024-05-29 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='materials/', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='materials/', verbose_name='Изображение')),
                ('slug', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='materials.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]

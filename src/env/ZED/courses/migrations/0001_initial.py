# Generated by Django 5.1.4 on 2024-12-30 12:39

import datetime
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
                ('course_name', models.CharField(max_length=100)),
                ('course_description', models.TextField()),
                ('course_duration', models.IntegerField()),
                ('course_image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('price', models.IntegerField()),
                ('course_type', models.CharField(choices=[('user_created', 'User Created'), ('apply', 'Apply')], default='apply', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CourseDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_title', models.CharField(max_length=100)),
                ('day_description', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=100)),
                ('video_description', models.TextField()),
                ('video_duration', models.IntegerField()),
                ('video', models.FileField(blank=True, upload_to='videos/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('course_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='courses.courseday')),
            ],
        ),
    ]

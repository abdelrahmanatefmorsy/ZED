# Generated by Django 5.1.4 on 2025-01-07 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_alter_course_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
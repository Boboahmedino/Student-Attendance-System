# Generated by Django 4.1.7 on 2023-04-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_attendance_options_remove_attendance_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='course',
            field=models.CharField(default=0, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='level',
            field=models.CharField(default=10, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.CharField(default=2222, max_length=300),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.13 on 2021-03-20 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0007_auto_20210320_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='mobile',
        ),
    ]

# Generated by Django 3.0.13 on 2021-03-22 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0011_auto_20210322_0911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='employees',
        ),
    ]

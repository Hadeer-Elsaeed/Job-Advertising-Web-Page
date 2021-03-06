# Generated by Django 3.0.13 on 2021-03-20 08:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody')], max_length=128)),
                ('mobile', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Mobile number should be strictly of 11 digits.', regex='^\\w{11}$')])),
                ('cv', models.FileField(upload_to='../static/uploads')),
            ],
        ),
    ]

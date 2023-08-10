# Generated by Django 4.2.4 on 2023-08-10 13:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='surname',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
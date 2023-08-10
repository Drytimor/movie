# Generated by Django 4.2.4 on 2023-08-10 13:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_feedback_name_alter_feedback_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='name',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='surname',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]

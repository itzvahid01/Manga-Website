# Generated by Django 5.1.2 on 2024-12-09 15:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taglist',
            name='rating',
            field=models.IntegerField(default=0, help_text='value 1 to 100', validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]

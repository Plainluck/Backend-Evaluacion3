# Generated by Django 4.1 on 2024-10-29 21:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PokeTCG', '0002_alter_card_hp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='HP',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(500)]),
        ),
    ]

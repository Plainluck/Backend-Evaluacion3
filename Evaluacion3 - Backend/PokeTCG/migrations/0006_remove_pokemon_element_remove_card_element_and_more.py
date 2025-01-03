# Generated by Django 4.1 on 2024-11-19 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PokeTCG', '0005_alter_card_hp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='element',
        ),
        migrations.RemoveField(
            model_name='card',
            name='element',
        ),
        migrations.AlterField(
            model_name='card',
            name='expansion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PokeTCG.expansion'),
        ),
        migrations.AlterField(
            model_name='card',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PokeTCG.pokemon'),
        ),
        migrations.AddField(
            model_name='card',
            name='element',
            field=models.ManyToManyField(related_name='card_elements', to='PokeTCG.element'),
        ),
    ]

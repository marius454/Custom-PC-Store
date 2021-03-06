# Generated by Django 3.0.2 on 2020-04-28 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_configuration_date_saved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='psu',
            old_name='Dimmension',
            new_name='Dimmensions',
        ),
        migrations.AddField(
            model_name='cpu',
            name='Generation',
            field=models.CharField(default='field not yet filled', max_length=50),
        ),
        migrations.AddField(
            model_name='cpu',
            name='Supported_ram_speeds',
            field=models.CharField(default='field not yet filled', max_length=200),
        ),
        migrations.AddField(
            model_name='gpu',
            name='Length',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='Supported_CPU_generations',
            field=models.CharField(default='field not yet filled', max_length=300),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='Supported_ram_types',
            field=models.CharField(default='field not yet filled', max_length=100),
        ),
    ]

# Generated by Django 3.0.2 on 2020-04-13 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200413_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='Recomendations',
            new_name='Recommendations',
        ),
        migrations.RenameField(
            model_name='cpu',
            old_name='Recomendations',
            new_name='Recommendations',
        ),
        migrations.RenameField(
            model_name='cpu_cooler',
            old_name='Recomendations',
            new_name='Recommendations',
        ),
        migrations.RenameField(
            model_name='gpu',
            old_name='Recomendations',
            new_name='Recommendations',
        ),
        migrations.RenameField(
            model_name='motherboard',
            old_name='Recomendations',
            new_name='Recommendations',
        ),
        migrations.RenameField(
            model_name='psu',
            old_name='Recomendations',
            new_name='Recommendations',
        ),
        migrations.RenameField(
            model_name='ram_set',
            old_name='Recomendations',
            new_name='Recommendations',
        ),
        migrations.RenameField(
            model_name='storage',
            old_name='Recomendations',
            new_name='Recommendations',
        ),
    ]

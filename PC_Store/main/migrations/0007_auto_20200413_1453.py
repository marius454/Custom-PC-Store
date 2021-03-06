# Generated by Django 3.0.2 on 2020-04-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200412_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='Description',
            field=models.TextField(default='not yet available'),
        ),
        migrations.AddField(
            model_name='case',
            name='Recomendations',
            field=models.TextField(default='not yet available'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='Description',
            field=models.TextField(default='not yet available'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='Recomendations',
            field=models.TextField(default='not yet available'),
        ),
        migrations.AddField(
            model_name='cpu_cooler',
            name='Description',
            field=models.TextField(default='not yet available'),
        ),
        migrations.AddField(
            model_name='cpu_cooler',
            name='Recomendations',
            field=models.TextField(default='not yet available'),
        ),
        migrations.AddField(
            model_name='gpu',
            name='Description',
            field=models.TextField(default='not yet available'),
        ),
        migrations.AddField(
            model_name='gpu',
            name='Recomendations',
            field=models.TextField(default='not yet available'),
        ),
        migrations.AddField(
            model_name='psu',
            name='Description',
            field=models.TextField(default='not yet available'),
        ),
        migrations.AddField(
            model_name='psu',
            name='Recomendations',
            field=models.TextField(default='not yet available'),
        ),
        migrations.AddField(
            model_name='ram_set',
            name='Description',
            field=models.TextField(default='not yet available'),
        ),
        migrations.AddField(
            model_name='ram_set',
            name='Recomendations',
            field=models.TextField(default='not yet available'),
        ),
        migrations.AddField(
            model_name='storage',
            name='Description',
            field=models.TextField(default='not yet available'),
        ),
        migrations.AddField(
            model_name='storage',
            name='Recomendations',
            field=models.TextField(default='not yet available'),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='Description',
            field=models.TextField(default='not yet available'),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='Recomendations',
            field=models.TextField(default='not yet available'),
        ),
    ]

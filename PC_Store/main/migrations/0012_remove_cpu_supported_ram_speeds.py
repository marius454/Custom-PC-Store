# Generated by Django 3.0.2 on 2020-04-28 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20200428_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpu',
            name='Supported_ram_speeds',
        ),
    ]

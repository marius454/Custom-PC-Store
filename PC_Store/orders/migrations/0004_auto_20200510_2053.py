# Generated by Django 3.0.2 on 2020-05-10 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_delete_orders'),
        ('orders', '0003_auto_20200510_1938'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]

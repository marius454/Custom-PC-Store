# Generated by Django 3.0.2 on 2020-05-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200511_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Phone',
            field=models.CharField(max_length=15),
        ),
    ]

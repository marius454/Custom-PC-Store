# Generated by Django 3.0.2 on 2020-05-12 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0017_delete_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saved_build',
            name='Belongs_to_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
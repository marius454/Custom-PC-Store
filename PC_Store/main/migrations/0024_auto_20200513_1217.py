# Generated by Django 3.0.2 on 2020-05-13 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_operating_system_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='Monitor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Monitor'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='Operating_System',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Operating_System'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='Optical_Drive',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Optical_Drive'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='Sound_Card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Sound_Card'),
        ),
        migrations.AlterField(
            model_name='optical_drive',
            name='Mounting_Orientation',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='optical_drive',
            name='Read_Speed',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='optical_drive',
            name='Write_Speed',
            field=models.TextField(max_length=500),
        ),
    ]

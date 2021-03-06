# Generated by Django 3.0.2 on 2020-03-31 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='Image',
            field=models.ImageField(default='default.jpg', upload_to='Part_Pics/Cases'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='Image',
            field=models.ImageField(default='default.jpg', upload_to='Part_Pics/CPUs'),
        ),
        migrations.AddField(
            model_name='cpu_cooler',
            name='Image',
            field=models.ImageField(default='default.jpg', upload_to='Part_Pics/CPU_Coolers'),
        ),
        migrations.AddField(
            model_name='gpu',
            name='Image',
            field=models.ImageField(default='default.jpg', upload_to='Part_Pics/GPUs'),
        ),
        migrations.AddField(
            model_name='motherboard',
            name='Image',
            field=models.ImageField(default='default.jpg', upload_to='Part_Pics/Motherboards'),
        ),
        migrations.AddField(
            model_name='psu',
            name='Image',
            field=models.ImageField(default='default.jpg', upload_to='Part_Pics/PSUs'),
        ),
        migrations.AddField(
            model_name='ram_set',
            name='Image',
            field=models.ImageField(default='default.jpg', upload_to='Part_Pics/Ram_sets'),
        ),
        migrations.AddField(
            model_name='storage',
            name='Image',
            field=models.ImageField(default='default.jpg', upload_to='Part_Pics/Storage'),
        ),
    ]

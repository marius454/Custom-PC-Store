# Generated by Django 3.0.2 on 2020-05-10 20:06

import creditcards.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200510_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total',
            new_name='sub_total',
        ),
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='card_expiration_date',
            field=creditcards.models.CardExpiryField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='card_number',
            field=creditcards.models.CardNumberField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='card_security_code',
            field=creditcards.models.SecurityCodeField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='email@email.email', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='final_total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='order',
            name='name_on_card',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='123456789', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='recipient_first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='recipient_last_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
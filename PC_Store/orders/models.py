from django.db import models
from main.models import Configuration as conf
from django.contrib.auth.models import User
from django.utils import timezone
from main.models import Configuration
from creditcards.models import CardNumberField, CardExpiryField, SecurityCodeField
from django_countries.fields import CountryField
from django.core.validators import RegexValidator

STATUS_CHOICES = (
    ("Started", "Started"),
    ("Cancelled","Cancelled"),
    ("Finished", "Finished"),
)
# alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
# alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only letters are allowed.')
# numeric = RegexValidator(r'^[0-9]*$', 'Only numeric characters are allowed.')
# num_and_slash = RegexValidator(r'^[0-9/]*$', 'Only numeric characters and a slash are allowed.')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    sub_total = models.DecimalField(default=0.00, max_digits=6, decimal_places=2)
    shipping_cost = models.DecimalField(default=0.00, max_digits=6, decimal_places=2)
    final_total = models.DecimalField(default=0.00, max_digits=6, decimal_places=2)
    recipient_first_name = models.CharField(max_length = 50, default="")
    recipient_last_name = models.CharField(max_length = 50, default="")
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    country = CountryField()
    delivery_address = models.CharField(max_length = 50, default="")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Started")
    timestamp = models.DateTimeField(default = timezone.now)
    configuration = models.ForeignKey(Configuration, on_delete=models.PROTECT)

    def __str__(self):
        return f'Order for configuration{self.configuration.id}, saved at {self.timestamp}'

class Payment_Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    billing_address = models.CharField(max_length = 50, default="")
    card_holder_name = models.CharField(max_length = 26)
    card_number = models.CharField(max_length = 19)
    card_expiration_date = models.CharField(max_length=5)

    def __str__(self):
        return f'Saved payment card of user - {self.user}'

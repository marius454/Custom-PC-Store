from django.db import models
from main.models import Configuration as conf
from django.contrib.auth.models import User
from django.utils import timezone
from main.models import Configuration

# class Cart(models.Model):
#     configuration = models.ForeignKey(conf, models.PROTECT)
#     total = models.DecimalField(max_digits=6, decimal_places=2, default = 0.00)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return f'Cart of user {self.configuration.UserID}'

STATUS_CHOICES = (
    ("Started", "Started"),
    ("Cancelled","Cancelled"),
    ("Finished", "Finished"),
)

class Order(models.Model):
    userID = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    shipping_total = models.DecimalField(default=0.00, max_digits=6, decimal_places=2)
    final_total = models.DecimalField(default=0.00, max_digits=6, decimal_places=2)
    Recipient_First_Name = models.CharField(max_length = 50, default="")
    Recipient_Last_Name = models.CharField(max_length = 50, default="")
    Billing_address = models.CharField(max_length = 50, default="")
    Delivery_address = models.CharField(max_length = 50, default="")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Started")
    timestamp = models.DateTimeField(default = timezone.now)
    configuration = models.ForeignKey(Configuration, on_delete=models.PROTECT)

    def __str__(self):
        return f'Order for {self.configuration}'

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Phone = models.CharField(max_length=15)
    Country = models.CharField(max_length=50)
    Delivery_Address = models.CharField(max_length=100)
    Post_Code = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.user.username} Profile'


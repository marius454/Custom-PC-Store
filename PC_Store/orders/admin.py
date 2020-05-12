from django.contrib import admin
from . import models as m
# Register your models here.

admin.site.register(m.Order)
admin.site.register(m.Payment_Info)
from django.urls import path
from . import views

urlpatterns = [
    path(r'cart/<confID>/', views.CartView, name='shopping-cart'),
    path(r'checkout/<confID>', views.Checkout, name='checkout'),
]
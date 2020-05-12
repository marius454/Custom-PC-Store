from django import forms
from .models import Order, Payment_Info
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['recipient_first_name', 'recipient_last_name', 'email',
        'phone', 'country', 'delivery_address']

class PaymentForm(forms.ModelForm):
    security_code = SecurityCodeField(max_length = 4, label = 'CVV/CVC')
    card_expiration_date = forms.CharField(max_length=5, min_length=5, widget=forms.TextInput(attrs={
        'placeholder': "MM YY",
        'id': "expDate",
        }))
    card_number = forms.CharField(max_length=19, widget=forms.TextInput(attrs={
        'id': "cardNR",
        }))
    card_holder_name = forms.CharField(max_length=26, widget=forms.TextInput(attrs={
        'id': "holderName",
        'onkeydown': "return /[A-Za-z ]/i.test(event.key)",
        }))
    class Meta:
        model = Payment_Info
        fields = ['billing_address', 'card_number', 'card_holder_name',
        'card_expiration_date']
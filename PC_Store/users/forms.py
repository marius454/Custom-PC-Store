from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Country', 'Delivery_Address', 'Post_Code', 'Phone']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Country', 'Delivery_Address', 'Post_Code', 'Phone']

class EmailUpdateForm(forms.ModelForm):
    password = forms.CharField(label='Please re-enter password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email']

    def clean(self):
        cleaned_data = super(EmailUpdateForm, self).clean()
        password = cleaned_data.get("password")
        if not self.instance.check_password(password):
            raise forms.ValidationError('Invalid password')

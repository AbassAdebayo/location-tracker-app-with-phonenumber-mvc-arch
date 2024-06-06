from django import forms
from django.contrib.auth.forms import UserCreationForm
from USERS.MODELS import CustomUser

class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=True)
    
    
    class Meta:
        model = CustomUser
        fields = ('username', 'phone_number', 'password1', 'password2')
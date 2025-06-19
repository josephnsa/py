from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models.user import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'first_name', 'last_name', 'dni', 'email',
            'phone', 'address', 'region', 'district', 'password1', 'password2', 'accepted_terms'
        ]
        widgets = {
            'accepted_terms': forms.CheckboxInput(),
        }

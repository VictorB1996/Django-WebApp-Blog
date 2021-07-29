from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # Specify the model that we want this form to interact with
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

# register/create a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
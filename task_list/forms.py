from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'password1' ,'password2' )

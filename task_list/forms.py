from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        # fields = ("__all__" )
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )

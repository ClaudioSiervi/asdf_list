from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
    fields = ('email', 'name', 'username', 'password1' ,'password2' )


class CreateUserForm(UserCreationForm):
    name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('email', 'name', 'username', 'password1' ,'password2' )


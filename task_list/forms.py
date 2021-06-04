from django import forms
from .models import User, Task
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('name', 'username', 'email', 'password1' ,'password2' )


class CreateTaskForm(forms.ModelForm):
    name = forms.CharField()
    class Meta:
        model = Task
        fields = ("name", "owner")


class DetailTaskForm(forms.ModelForm):
    name = forms.CharField()
    class Meta:
        model = Task
        fields = ("name", "owner")


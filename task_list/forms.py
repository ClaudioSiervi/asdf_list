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
    rating = forms.IntegerField(min_value=0, max_value=10)
    class Meta:
        model = Task
        fields = ("name", "description", "status", "owner", "rating", "comments", "task_date_time") 

class DetailTaskForm(forms.ModelForm):
    name = forms.CharField()
    class Meta:
        model = Task
        fields = ("name", "owner")

class UpdateTaskForm(forms.ModelForm):
    name = forms.CharField()
    rating = forms.IntegerField(min_value=0, max_value=10)
    class Meta:
        model = Task
        fields = ("name", "description", "status", "owner", "rating", "comments", "task_date_time") 


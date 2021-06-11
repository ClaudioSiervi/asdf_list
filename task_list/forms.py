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
        fields = ("name", "description", "is_concluded", "owner", "rating", "comments", "task_date_time") 
        widgets = {
            'name': forms.Textarea(attrs={'cols': 50, 'rows': 2}), 
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }


class UpdateTaskForm(forms.ModelForm):
    name = forms.CharField()
    rating = forms.IntegerField(min_value=0, max_value=10)
    class Meta:
        model = Task
        fields = ("name", "description","is_concluded",  "status", "owner", "rating", "comments", "task_date_time") 


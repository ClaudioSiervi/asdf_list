from django import forms
from .models import Task



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


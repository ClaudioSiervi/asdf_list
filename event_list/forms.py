from django import forms
from .models import Event


class CreateEventForm(forms.ModelForm):
    name = forms.CharField()
    rating = forms.IntegerField(min_value=0, max_value=10)

    class Meta:
        model = Event
        fields = ("name", "description", "rating", "start", "finish", "tasks", "family")


class UpdateEventForm(forms.ModelForm):
    name = forms.CharField()
    rating = forms.IntegerField(min_value=0, max_value=10)

    class Meta:
        model = Event
        fields = ("name", "description", "rating", "start", "finish", "tasks", "family")


from django import forms

from families.models import Family

class CreateFamilyForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Family
        fields = ("name", "members")

from users.models import User
from django import forms

from families.models import Family

class CreateFamilyForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Family
        fields = ("name", "members")


class UpdateFamilyForm(forms.ModelForm):
    name = forms.CharField()
    # members = forms.ModelMultipleChoiceField(
    #     queryset=User.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )
    class Meta:
        model = Family
        fields = ("name",)

from django.forms.widgets import DateInput, CheckboxInput,RadioSelect
from django import forms
from .models import ToDo_List

class NameForm(forms.ModelForm):
    class Meta:
        model = ToDo_List
        fields = ["action", "due"]
        labels = {"action": 'Activity', "due":'Due on:'}
        widgets = {
            'due': DateInput(attrs={'type': 'date'}),
        }

class CheckForm(forms.ModelForm):
    class Meta:
        model = ToDo_List
        fields = ["status"]
        widgets  ={'status':CheckboxInput(attrs={'type':'checkbox', 'name':'form2','onclick':"check(this)"})}

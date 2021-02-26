from django import forms
from django.core import validators
from django.forms.widgets import TextInput

class LinkForm(forms.Form):
    url = forms.CharField(label='url', max_length=400, validators=[validators.URLValidator()], widget=forms.TextInput(attrs={'placeholder':'http://www.google.com'}))

    class Meta:
        attrs = {'class':"table"}
from django import forms
from django.core import validators

class LinkForm(forms.Form):
    url = forms.CharField(label='url', max_length=400, validators=[validators.URLValidator()])
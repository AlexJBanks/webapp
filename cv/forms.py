from django import forms

from .models import Basic

class BasicForm(forms.ModelForm):

    class Meta:
        model = Basic
        fields = ('type', 'data',)

from django import forms

from .models import Basic, Education, Work


class BasicForm(forms.ModelForm):

    class Meta:
        model = Basic
        fields = '__all__'


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = '__all__'


class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = '__all__'


from django import forms

from .models import Basic, Education, Work, Grade


class BasicForm(forms.ModelForm):

    class Meta:
        model = Basic
        fields = '__all__'


class GradeForm(forms.ModelForm):

    class Meta:
        model = Grade
        fields = '__all__'
        exclude = ['education']


class EducationForm(forms.ModelForm):

    class Meta:
        model = Education
        fields = '__all__'


class WorkForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = '__all__'


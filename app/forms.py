from django import forms
from django.forms import ModelForm
from .models import People, Skill, Score, File

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ('sub_category','role_level','question')
        widgets = {
            'sub_category': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.TextInput(attrs={'class': 'form-control'}),
            'question': forms.Textarea(attrs={'class': 'form-control'}),
        }

class PeopleForm(ModelForm):
    class Meta:
        model = People
        fields = ('name','manager','role','role_level')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'manager': forms.Select(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'role_level': forms.Select(attrs={'class': 'form-control'}),
        }

class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ('name','document')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'document': forms.FileInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }
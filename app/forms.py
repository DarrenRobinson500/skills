from django import forms
from django.forms import ModelForm
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'



WIDGETS = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'actions': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'parent': forms.Select(attrs={'class': 'form-control'}),
            "date": forms.DateInput(attrs={"class": "form-control", 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
}

class BaseForm(ModelForm):
    class Meta:
        model = Note
        fields = ('name','description','type')
        widgets = WIDGETS

class PersonForm(ModelForm):
    class Meta:
        model = Note
        fields = ('name','date')
        labels = {'date': 'Birthday',}

        widgets = WIDGETS

class ObjectiveForm(ModelForm):
    class Meta:
        model = Note
        fields = ('name','description',)
        widgets = WIDGETS

class StoryForm(ModelForm):
    class Meta:
        model = Note
        fields = ('name','description',)
        labels = {'description': 'Story',}
        widgets = WIDGETS

class IssueForm(ModelForm):
    class Meta:
        model = Note
        fields = ('name','description',)
        widgets = WIDGETS

class ToDoForm(ModelForm):
    class Meta:
        model = Note
        fields = ('date', 'name','description','status',)
        widgets = WIDGETS

class ParentForm(ModelForm):
    parent = forms.ModelChoiceField(
        queryset=Note.objects.all().order_by('name'),
        required=False,
        label="Parent", widget=forms.Select(attrs={"class": "form-control"}),
    )
    class Meta:
        model = Note
        fields = ('parent',)
        widgets = WIDGETS

class GroupForm(ModelForm):
    class Meta:
        model = Note
        fields = ('name','description',)
        widgets = WIDGETS

class ReminderForm(ModelForm):
    class Meta:
        model = Note
        fields = ('date', 'name','description','status')
        widgets = WIDGETS

class MeetingForm(ModelForm):
    class Meta:
        model = Note
        fields = ('date', 'name','description', 'actions')
        labels = {'description': 'Notes',}
        widgets = WIDGETS


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
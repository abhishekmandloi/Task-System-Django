from django import forms
from django.forms import (formset_factory, modelformset_factory)

from .models import Task, Comments

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name','title','description','link_id','datecreated','datelastmodified',)
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Name of Person to whom this task is assigned'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the Title of the Task'
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description of this task'
            }),
            'datecreated': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the Date when this Task created',
                'type':'date'
            }),
            'datelastmodified': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Last Modified date of the task',
                'type':'date'
            })
            
        }

class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('task','comment',)
        task_list = Task.objects.all()
        widgets = {
            'task': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the comments'
                },
                choices = task_list
            ),
            'comment': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the comments'
            })
        }

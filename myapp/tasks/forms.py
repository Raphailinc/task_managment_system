from django import forms
from .models import Task, TaskFile

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'assigned_to', 'status']
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'assigned_to': 'Исполнитель',
            'status': 'Статус',
        }


class TaskFileForm(forms.ModelForm):
    class Meta:
        model = TaskFile
        fields = ['file']
from statistics import mode
from django.forms import ModelForm
from .models import Tasklist, Task

class TasklistForm(ModelForm):
    class Meta:
        model = Tasklist
        fields = ['title']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority']
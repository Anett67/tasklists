from django.forms import ModelForm
from .models import Tasklist, Task, Profil

class TasklistForm(ModelForm):
    class Meta:
        model = Tasklist
        fields = ['title']

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority']

class ProfileForm(ModelForm):
    class Meta:
        model = Profil
        fields = ['theme']
from django.forms import ModelForm
from .models import Tasklist, Task, Profil

class TasklistForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(TasklistForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
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
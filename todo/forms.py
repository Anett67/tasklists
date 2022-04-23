from django.forms import ModelForm
from .models import Tasklist, Task, Profil
from crispy_forms.helper import FormHelper

class TasklistForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(TasklistForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Tasklist
        fields = ['title']

class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority']
        

class ProfileForm(ModelForm):
    class Meta:
        model = Profil
        fields = ['theme']
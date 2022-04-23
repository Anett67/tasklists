from django.forms import ModelForm
from .models import Tasklist, Task, Profil
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class TasklistForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Enregistrer', css_class='btn-primary mt-3'))
        self.helper.form_method = 'POST'

    class Meta:
        model = Tasklist
        fields = ['title']

class TaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Enregistrer', css_class='btn-primary mt-3'))
        self.helper.form_method = 'POST'


    class Meta:
        model = Task
        fields = ['title', 'description', 'priority']
        

class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Enregistrer', css_class='btn-primary mt-3'))
        self.helper.form_method = 'POST'
        
    class Meta:
        model = Profil
        fields = ['theme']
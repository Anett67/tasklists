from django.db import models
from django.contrib.auth.models import User

class Theme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.user.username

    def theme_url(self):
        if not self.theme:
            return 'css/bootstrap.min.css'

        return 'css/%s/bootstrap.min.css' % self.theme.name

class Tasklist(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    archived = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title

    def tasks_count(self):
        return self.task_set.count()

    def completed_tasks_count(self):
        return self.task_set.filter(datecompleted__isnull=False).count()

    def tasks_to_do(self):
        return self.task_set.filter(datecompleted__isnull=True)

    def completed_tasks(self):
        return self.task_set.filter(datecompleted__isnull=False)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    priority = models.BooleanField(default=False)
    tasklist = models.ForeignKey(Tasklist, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title



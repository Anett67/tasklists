from django.db import models
from django.contrib.auth.models import User

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

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    priority = models.BooleanField(default=False)
    tasklist = models.ForeignKey(Tasklist, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
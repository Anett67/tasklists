from django.contrib import admin
from .models import Task, Tasklist, Profil, Theme

admin.site.register(Tasklist)
admin.site.register(Task)
admin.site.register(Profil)
admin.site.register(Theme)
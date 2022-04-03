from django.utils import timezone
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from todo.models import Tasklist, Task
from .forms import TasklistForm, TaskForm

def signupuser(request):
    if request.method == "GET":
        return render(request, 'todo/signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttasks')
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {
                    'form':UserCreationForm(), 
                    'error':'Un compte avec ce nom existe déjà.'
                })
        else: 
            return render(request, 'todo/signupuser.html', {
                'form':UserCreationForm(), 
                'error':'Les mots de passe ne sont pas identiques.'
            })

@login_required
def currenttasks(request):
    tasklists = Tasklist.objects.filter(user=request.user, archived__isnull=True)
    return render(request, 'todo/currenttasks.html', {'tasklists': tasklists})

@login_required
def archivedtasks(request):
    tasklists = Tasklist.objects.filter(user=request.user, archived__isnull=False).order_by('-archived')
    return render(request, 'todo/archivedtasks.html', {'tasklists': tasklists})

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('signupuser')

def loginuser(request):
        if request.method == "GET":
            return render(request, 'todo/login.html', {'form':AuthenticationForm()})
        else:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is None:
                return render(request, 'todo/login.html', {'form':AuthenticationForm(), 'error':'Identifiants invalides.'})
            else:
                login(request, user)
                return redirect('currenttasks')

@login_required
def createtasklist(request):
    if request.method == "GET":
        return render(request, 'todo/createtasklist.html', {'form':TasklistForm()})
    else:
        try:
            form = TasklistForm(request.POST)
            newtasklist = form.save(commit=False)
            newtasklist.user = request.user
            newtasklist.save()
            return redirect('currenttasks')
        except ValueError:
            return render(request, 'todo/createtasklist.html', {'form':TasklistForm(), 'error':'Titre invalide'}) 

@login_required
def createtask(request):
    if request.method == "GET":
        return render(request, 'todo/createtask.html', {'form':TaskForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/createtask.html', {'form':TaskForm(), 'error':'Identifiants invalides.'})
        else:
            login(request, user)
            return redirect('currenttasks')

@login_required
def viewtasklist(request, tasklist_pk):
    tasklist = get_object_or_404(Tasklist, pk=tasklist_pk)
    return render(request, 'todo/viewtasklist.html', {'tasklist':tasklist})

@login_required
def updatetasklist(request, tasklist_pk):
    tasklist = get_object_or_404(Tasklist, pk=tasklist_pk, user=request.user)
    if request.method == "GET":
        form = TasklistForm(instance=tasklist)
        return render(request, 'todo/updatetasklist.html', {'tasklist':tasklist, 'form':form})
    else:
        try:
            form = TasklistForm(request.POST, instance=tasklist)
            form.save()
            return redirect('viewtasklist', tasklist_pk=tasklist.pk)
        except ValueError:
            return render(request, 'todo/updatetasklist.html', {'tasklist':tasklist, 'form':form, 'error':'Titre invalide'})

@login_required
def archivetasklist(request, tasklist_pk):
    tasklist = get_object_or_404(Tasklist, pk=tasklist_pk, user=request.user)
    if request.method == 'POST':
        tasklist.archived = timezone.now()
        tasklist.save()
        return redirect('currenttasks')

@login_required
def activatetasklist(request, tasklist_pk):
    tasklist = get_object_or_404(Tasklist, pk=tasklist_pk, user=request.user)
    if request.method == 'POST':
        tasklist.archived = None
        tasklist.save()
        return redirect('currenttasks')

@login_required
def deletetasklist(request, tasklist_pk):
    tasklist = get_object_or_404(Tasklist, pk=tasklist_pk, user=request.user)
    if request.method == 'POST':
        tasklist.delete()
        return redirect('currenttasks')
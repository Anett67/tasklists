from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
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

def currenttasks(request):
    return render(request, 'todo/currenttasks.html')

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
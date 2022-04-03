"""todowoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth
    path('inscription/', views.signupuser, name="signupuser"),
    path('connexion/', views.loginuser, name="loginuser"),
    path('déconnexion', views.logoutuser, name="logoutuser"),

    # Tasklists
    path('listes/', views.currenttasks, name="currenttasks"),
    path('listes/archives', views.archivedtasks, name="archivedtasks"),
    path('listes/nouveau/', views.createtasklist, name="createtasklist"),
    path('listes/<int:tasklist_pk>/', views.viewtasklist, name="viewtasklist"),
    path('listes/<int:tasklist_pk>/edition', views.updatetasklist, name="updatetasklist"),
    path('listes/<int:tasklist_pk>/archive', views.archivetasklist, name="archivetasklist"),
    path('listes/<int:tasklist_pk>/activer', views.activatetasklist, name="activatetasklist"),
    path('listes/<int:tasklist_pk>/delete', views.deletetasklist, name="deletetasklist"),


    # Task
    path('taches/nouveau/', views.createtask, name="createTask")
]

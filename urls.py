"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from djangoProject import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('addTeacher/', views.addTeacher, name='addTeacher'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
    path('ourTeam/', views.ourTeam, name='ourTeam'),
    path('teacherList/', views.teacherList, name='teacherList'),
    path('teacherIndex/', views.teacherIndex, name='teacherIndex'),
    path('studentList/', views.studentList, name='studentList'),
    path('resultUpload/', views.resultUpload, name='resultUpload'),
    path('predictedResult/', views.predictedResult, name='predictedResult'),
    path('finalResult/', views.finalResult, name='finalResult'),
    path('changeProfile/', views.changeProfile, name='changeProfile'),
    path('changePassword/', views.changePassword, name='changePassword'),
    path('advisoryList/', views.advisoryList, name='advisoryList'),
    path('advisoryForm/', views.advisoryForm, name='advisoryForm'),
    path('addStudentMarks/', views.addStudentMarks, name='addStudentMarks'),
    path('addStudent/', views.addStudent, name='addStudent'),
    path('accuracy/', views.accuracy, name='accuracy'),
    path('updateTeacher/<str:id>', views.updateTeacher, name='updateTeacher'),
    path('add/', views.add, name='add'),
    path('feedback/', views.feedback, name='feedback'),
    path('feedbackUpdate/', views.feedbackUpdate, name='feedbackUpdate'),
    path('successView/', views.successView, name='successView'),
    path('loginProcessing/', views.loginProcessing, name='loginProcessing'),
    path('addStudentMarks/predict/', views.predict, name='predict'),
    path('editStudent/<str:pk>', views.editStudent, name="editStudent"),
    path('deleteStudent/<str:pk>', views.deleteStudent, name="deleteStudent"),
    path('editTeacher/<str:pk>', views.editTeacher, name="editTeacher"),
    path('deleteTeacher/<str:pk>', views.deleteTeacher, name="deleteTeacher"),


]

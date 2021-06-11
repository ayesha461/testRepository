from django.db import models


class Teacher(models.Model):
    TId = models.CharField(max_length=20)
    TName = models.CharField(max_length=20)
    TEmail = models.EmailField(unique=True)
    Department = models.CharField(max_length=20)
    Designation = models.CharField(max_length=20)
    Gender = models.CharField(max_length=20)
    Password = models.CharField(max_length=10)

    def is_valid(self):
        pass


class Student(models.Model):
    sid = models.CharField(max_length=20)
    semail = models.EmailField()
    sname = models.CharField(max_length=50)
    sdepartment = models.CharField(max_length=50)
    ssemester = models.CharField(max_length=10)
    sgender = models.CharField(max_length=10)
    spassword = models.CharField(max_length=10)
    sbatch = models.CharField(max_length=10)

    def is_valid(self):
        pass


class Feedback(models.Model):
    fName = models.CharField(max_length=20)
    fEmail = models.EmailField()
    fSubject = models.CharField(max_length=80)
    fMessage = models.TextField(max_length=200)

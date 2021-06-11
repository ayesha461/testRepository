from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .models import Teacher
from .models import Student
from .forms import TeacherForm, StudentForm
from .models import Feedback
from .forms import FeedbackForm
from django.shortcuts import render
import pandas as pd
from django.contrib import messages
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
import numpy as np

global flag


def home(request):
    return render(request, 'index.html')


def addTeacher(request):
    if request.method == 'POST':
        if request.POST.get('reg') and request.POST.get('name') and request.POST.get('gender') and request.POST.get(
                'desig') and request.POST.get('dep') and request.POST.get('email') and request.POST.get('password'):
            teacher = Teacher()
            teacher.TId = request.POST.get('reg')
            teacher.TName = request.POST.get('name')
            teacher.Gender = request.POST.get('gender')
            teacher.Designation = request.POST.get('desig')
            teacher.Department = request.POST.get('dep')
            teacher.TEmail = request.POST.get('email')
            teacher.Password = request.POST.get('password')
            teacher.save()
            return redirect('/teacherList')
        else:
            return render(request, 'teacher/teacherIndex')


def updateTeacher(request, id):
    teacher = Teacher.objects.get(id=id)
    form = TeacherForm(request.POST, instance=teacher)
    form.save()
    return redirect('/teacherList')


def login(request):
    return render(request, 'login.html')


def loginProcessing(request):
    if request.method == 'POST':
        if request.POST.get('loginName') and request.POST.get('loginPass'):
            email = request.POST.get('loginName')
            password = request.POST.get('loginPass')
            user = Teacher
            user1 = Student
            teacher = Teacher.objects.filter(TEmail=email, Password=password)
            student = Student.objects.filter(semail=email, spassword=password)
            if teacher:
                flag = 1
                return redirect('/teacherList')
            else:
                if student:
                    flag = 2
                    return redirect('/studentList')
                elif email == 'admin@gmail.com' and password == 'admin':
                    flag = 3
                    # if email == 'admin@gmail.com' and password == 'admin':
                    return redirect('/teacherList')
                else:
                    messages.error(request, 'Invalid Credentials...!')
                    return render(request, 'login.html')
        else:
            # return redirect('/login')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def aboutUs(request):
    return render(request, 'about_us.html')


def contact(request):
    return render(request, 'contact_us.html')


def ourTeam(request):
    return render(request, 'our_team.html')


def feedback(request):
    return render(request, 'Feedback.html')


def feedbackUpdate(request):
    if request.method == 'POST':
        form = FeedbackForm()
    else:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, subject, message, from_email, ['sgps6@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/successView')
    return render(request, "Feedback.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')


def teacherList(request):
    teacher = Teacher.objects.all
    return render(request, 'teachers_list.html', {'teacher': teacher})


def teacherIndex(request):
    return render(request, 'teacher_index.html')


def studentList(request):
    student = Student.objects.all()
    return render(request, 'student_list.html', {'student': student})


def resultUpload(request):
    return render(request, 'result_upload.html')


def predictedResult(request):
    return render(request, 'predicted_result.html')


def finalResult(request):
    return render(request, 'final_result.html')


def changeProfile(request):
    return render(request, 'change_profile.html')


def changePassword(request):
    return render(request, 'change_password.html')


def advisoryList(request):
    return render(request, 'advisory_list.html')


def advisoryForm(request):
    return render(request, 'advisory_form.html')


def addStudentMarks(request):
    return render(request, 'add_student_marks.html')


def addStudent(request):
    return render(request, 'add_student.html')


def add(request):
    if request.method == 'POST':
        if request.POST.get('sname') and request.POST.get('semail') and request.POST.get('sid') and request.POST.get(
                'sdepartment') and request.POST.get('ssemester') and request.POST.get('sgender') and request.POST.get(
            'sbatch') and request.POST.get('spassword'):
            saverecord = Student()
            saverecord.sname = request.POST.get('sname')
            saverecord.semail = request.POST.get('semail')
            saverecord.sid = request.POST.get('sid')
            saverecord.sdepartment = request.POST.get('sdepartment')
            saverecord.sbatch = request.POST.get('sbatch')
            saverecord.ssemester = request.POST.get('ssemester')
            saverecord.sgender = request.POST.get('sgender')
            saverecord.spassword = request.POST.get('spassword')
            saverecord.save()
            return redirect('/studentList')
        else:
            return render(request, 'saverecord/studentList')


def editStudent(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(pk=pk)
        saverecord = StudentForm(request.POST or None, instance=student)
        if saverecord.is_valid():
            saverecord.save()
            return redirect('/studentList')
        return render(request, 'editStudent.html', {'student': student})
    else:
        student = Student.objects.get(pk=pk)
        return render(request, 'editStudent.html', {'student': student})


def deleteStudent(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()

    return redirect('/studentList')


def editTeacher(request, pk):
    if request.method == 'POST':
        teacher = Teacher.objects.get(pk=pk)
        saverecord = TeacherForm(request.POST or None, instance=teacher)
        if saverecord.is_valid():
            saverecord.save()
            return redirect('/teacherList')
        return render(request, 'edit_teacher.html', {'teacher': teacher})
    else:
        teacher = Teacher.objects.get(pk=pk)
        return render(request, 'edit_teacher.html', {'teacher': teacher})


def deleteTeacher(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    teacher.delete()

    return redirect('/teacherList')


def accuracy(request):
    return render(request, 'accuracy_comp_result.html')


def define_grade(df):
    # Create a list to store the data
    grades = []

    # For each row in the column,
    for row in df['GAvg']:
        # if more than a value,
        if row >= (0.9 * df['GAvg'].max()):
            # Append a letter grade
            grades.append('A')
        # else, if more than a value,
        elif row >= (0.7 * df['GAvg'].max()):
            # Append a letter grade
            grades.append('B')
        # else, if more than a value,
        elif row < (0.7 * df['GAvg'].max()):
            # Append a letter grade
            grades.append('C')
    # Create a column from the list
    df['grades'] = grades
    return df


def predict(request):
    data = pd.read_csv(r"C:\Users\MALIK MUNEEB\OneDrive\Desktop\student-data.csv")
    data['GAvg'] = (data['G1'] + data['G2'] + data['G3']) / 3
    data = define_grade(data)

    data.drop(["school", "age", "Dalc", "Walc"], axis=1, inplace=True)

    d = {'yes': 1, 'no': 0}
    data['schoolsup'] = data['schoolsup'].map(d)
    data['famsup'] = data['famsup'].map(d)
    data['paid'] = data['paid'].map(d)
    data['activities'] = data['activities'].map(d)
    data['nursery'] = data['nursery'].map(d)
    data['higher'] = data['higher'].map(d)
    data['internet'] = data['internet'].map(d)
    data['romantic'] = data['romantic'].map(d)

    # map the sex data
    d = {'F': 1, 'M': 0}
    data['sex'] = data['sex'].map(d)

    # map the address data
    d = {'U': 1, 'R': 0}
    data['address'] = data['address'].map(d)

    # map the famili size data
    d = {'LE3': 1, 'GT3': 0}
    data['famsize'] = data['famsize'].map(d)

    # map the parent's status
    d = {'T': 1, 'A': 0}
    data['Pstatus'] = data['Pstatus'].map(d)

    # map the parent's job
    d = {'teacher': 0, 'health': 1, 'services': 2, 'at_home': 3, 'other': 4}
    data['Mjob'] = data['Mjob'].map(d)
    data['Fjob'] = data['Fjob'].map(d)

    # map the reason data
    d = {'home': 0, 'reputation': 1, 'course': 2, 'other': 3}
    data['reason'] = data['reason'].map(d)

    # map the guardian data
    d = {'mother': 0, 'father': 1, 'other': 2}
    data['guardian'] = data['guardian'].map(d)

    # map the grades data
    d = {'C': 0, 'B': 1, 'A': 2}
    data['grades'] = data['grades'].map(d)

    student_features = data.columns.tolist()
    student_features.remove('grades')
    student_features.remove('GAvg')
    student_features.remove('G1')
    student_features.remove('G2')
    student_features.remove('G3')
    # print(student_features)

    X = data[student_features].copy()

    y = data[['grades']].copy()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=100)

    grade_classifier = tree.DecisionTreeClassifier(max_leaf_nodes=len(X.columns), random_state=0)
    grade_classifier.fit(X_train, y_train)

    var1 = int(request.GET['n1'])
    var2 = int(request.GET['n2'])
    var3 = int(request.GET['n3'])
    var4 = int(request.GET['n4'])
    var5 = int(request.GET['n5'])
    var6 = int(request.GET['n6'])
    var7 = int(request.GET['n7'])
    var8 = int(request.GET['n8'])
    var9 = int(request.GET['n9'])
    var10 = int(request.GET['n10'])
    var11 = int(request.GET['n11'])
    var12 = int(request.GET['n12'])
    var13 = int(request.GET['n13'])
    var14 = int(request.GET['n14'])
    var15 = int(request.GET['n15'])
    var16 = int(request.GET['n16'])
    var17 = int(request.GET['n17'])
    var18 = int(request.GET['n18'])
    var19 = int(request.GET['n19'])
    var20 = int(request.GET['n20'])
    var21 = int(request.GET['n21'])
    var22 = int(request.GET['n22'])
    var23 = int(request.GET['n23'])
    var24 = int(request.GET['n24'])
    var25 = int(request.GET['n25'])
    var26 = int(request.GET['n26'])

    # predictions = grade_classifier.predict(X_test)

    predictions = grade_classifier.predict(
        np.array([var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12,
                  var13, var14, var15, var16, var17, var18, var19, var20, var21, var22, var23,
                  var24, var25, var26]).reshape(1, -1))

    if predictions == 2:
        output = "your Grade can be: A"
    elif predictions == 1:
        output = "Your Grades can be: B"
    else:
        output = "Your Grade can be: C"

    # score = accuracy_score(y_true=y_test, y_pred=predictions)

    return render(request, "add_student_marks.html", {"result2": output})


def accuracy(request):
    data = pd.read_csv('E:\Desktop\Desktop\student-data.csv')

    data['GAvg'] = (data['G1'] + data['G2'] + data['G3']) / 3

    data = define_grade(data)

    data.drop(["school", "age", "Dalc", "Walc"], axis=1, inplace=True)

    d = {'yes': 1, 'no': 0}
    data['schoolsup'] = data['schoolsup'].map(d)
    data['famsup'] = data['famsup'].map(d)
    data['paid'] = data['paid'].map(d)
    data['activities'] = data['activities'].map(d)
    data['nursery'] = data['nursery'].map(d)
    data['higher'] = data['higher'].map(d)
    data['internet'] = data['internet'].map(d)
    data['romantic'] = data['romantic'].map(d)

    # map the sex data
    d = {'F': 1, 'M': 0}
    data['sex'] = data['sex'].map(d)

    # map the address data
    d = {'U': 1, 'R': 0}
    data['address'] = data['address'].map(d)

    # map the famili size data
    d = {'LE3': 1, 'GT3': 0}
    data['famsize'] = data['famsize'].map(d)

    # map the parent's status
    d = {'T': 1, 'A': 0}
    data['Pstatus'] = data['Pstatus'].map(d)

    # map the parent's job
    d = {'teacher': 0, 'health': 1, 'services': 2, 'at_home': 3, 'other': 4}
    data['Mjob'] = data['Mjob'].map(d)
    data['Fjob'] = data['Fjob'].map(d)

    # map the reason data
    d = {'home': 0, 'reputation': 1, 'course': 2, 'other': 3}
    data['reason'] = data['reason'].map(d)

    # map the guardian data
    d = {'mother': 0, 'father': 1, 'other': 2}
    data['guardian'] = data['guardian'].map(d)

    # map the grades data
    d = {'C': 0, 'B': 1, 'A': 2}
    data['grades'] = data['grades'].map(d)

    student_features = data.columns.tolist()
    student_features.remove('grades')
    student_features.remove('GAvg')
    student_features.remove('G1')
    student_features.remove('G2')
    student_features.remove('G3')
    # print(student_features)

    X = data[student_features].copy()

    y = data[['grades']].copy()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=100)

    grade_classifier = tree.DecisionTreeClassifier(max_leaf_nodes=len(X.columns), random_state=0)
    grade_classifier.fit(X_train, y_train)

    predictions = grade_classifier.predict(X_test)

    score = accuracy_score(y_true=y_test, y_pred=predictions)

    return render(request, "accuracy.html", {"result3": score})

from django.shortcuts import render
from student.forms import Registration, Login
# Create your views here.

def register(req):
    context = {
        'form': Registration
    }
    return render(req, 'student/registration.html', context)

def login(req):
    fm = Login(auto_id=True, label_suffix=' -', initial={'email': 'example@gmail.com','password': '******'})
    return render(req, 'student/login.html', {'login':fm} )
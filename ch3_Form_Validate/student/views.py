from django.shortcuts import render, redirect
from student.forms import StudentRegistration

# Create your views here.

def register(req):
    if req.method == 'POST':
        fm = StudentRegistration(req.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']

            print('Name : ', name)
            print('email : ', email)
            print('Password : ', password)

          
        return redirect('/student/register/')
    else:
        fm = StudentRegistration()
    return render (req, 'student/registration.html', {'form':fm})
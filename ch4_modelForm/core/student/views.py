from django.shortcuts import render, redirect
from student.forms import Registration

def home(req):
    if req.method == 'POST':
        fm = Registration(req.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']

            print('Name : ', name)
            print('email : ', email)
            print('Password : ', password)
        return redirect('/student/register/')
    
    else:
        fm = Registration()
    return render (req, 'register.html', {'form':fm})

from django.shortcuts import render
from student.forms import StudentForm

# Create your views here.

def register(req):
    if req.method == 'POST':
        fm = StudentForm(req.POST)
        # print(fm)

        if fm.is_valid():
            # print(fm.cleaned_data)
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            address = fm.cleaned_data['address']

            print('name:', name)
            print('email:', email)
            print('address :', address)

        # print(req.POST)  #to see the data we entered in the form
        # print(req.POST['email']) to see data individually
        # print(req.POST['first_name'])


    else:                                              
        fm = StudentForm()
    return render(req, 'student/registration.html', {'form': fm})
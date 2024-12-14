from django.shortcuts import render
from student.forms import Registration
# Create your views here.

def register(req):
    context = {
        'form': Registration
    }
    return render(req, 'student/registration.html', context)


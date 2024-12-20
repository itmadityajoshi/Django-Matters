from django import forms 
from student.models import Profile

#create forms here

class Registration(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ("name","email", "password")
           
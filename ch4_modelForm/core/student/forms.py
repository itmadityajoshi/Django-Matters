from django import forms 
from student.models import Profile

#create forms here

class Registration(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name","email", "password"]
        labels = {
            'name': 'Enter the Name', 
            'email':'Enter your email',
            }
        error_messages = {
            'email':{'required': 'Email is required'},
        }
        widgets = {
            'password': forms.PasswordInput(attrs={
                'class': 'pwdclass',
                'placeholder': 'Type ypur pasword here'}),
                'name': forms.TextInput(attrs={'class': 'myclass',
                                               'placeholder':'Type your name here'})
            
        }
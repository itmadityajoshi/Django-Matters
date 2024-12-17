from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()


    def clean_name(self):
        name_value = self.cleaned_data['name']
        if len(name_value)  < 4:
            raise forms.ValidationError('Enter more than or equal to value')
        return name_value



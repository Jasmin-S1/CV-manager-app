from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'jobTitle',
            'companyName',
            'description',
            'cvFile',
            'coverLetterFile',
            ]
        

class JobSearchForm(forms.Form):
    jobTitle = forms.CharField(max_length=200, required=False)


class CreateUserForm(UserCreationForm): 
    class Meta:                         
        model = User                    
        fields = [                     
            'username',
            'email',
            'password1',
            'password2'
        ]

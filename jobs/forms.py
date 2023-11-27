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


class CreateUserForm(UserCreationForm): # CreateUserForm je nasa forma za kreiranje Usera
    class Meta:                         # ona nasljedjuje sve iz built-in djangove forme,
        model = User                    # za krerianje usera, ali mi zelimo na tu formu dodati,
        fields = [                      # nova pola npr. email
            'username',
            'email',
            'password1',
            'password2'
        ]
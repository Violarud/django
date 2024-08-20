from django.db import models
from .models import WebsiteUsers
from django.forms import ModelForm, PasswordInput, TextInput, ValidationError
from django.contrib.auth.models import User

class WebsiteUsersForm(ModelForm):
    class Meta:
        model = WebsiteUsers
        fields = ['username', 'password']

        widgets = { 
            "username": TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'label'
            }),

            "password": TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Password'
            }),

           }  

 #        



    

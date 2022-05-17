
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Students

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = Students
        fields = ['username','full_name', 'email','gender','password1','password2','category']

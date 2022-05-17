from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Students(User):
    full_name = models.CharField(max_length=100)
    gender_choice = [
        ('F','Female'),
        ('M','Male'),
        ('O','Unsure')
    ]

    category_choice = [
        ('S' , 'Student'),
        ('T' , 'Teacher')
    ]

    gender = models.CharField(max_length=1, choices=gender_choice)
    category = models.CharField(max_length=1 , choices=category_choice , default='S')

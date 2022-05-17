from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from accounts.models import Students

# Create your models here.

leave_choices = [
    ('Sick Leave' , 'Sick'),
    ('Casual Leave' , 'Casual Leave'),
    ('Emergency Leave' , 'Emergency'),
    ('Maternity Leave' , 'Maternity'),
    ('Earned Leave' , 'Earned Leave')
]
action_choices =[
    ('Accepted','Accepted'),
    ('Rejected','Rejected'),
    ('Pending','Pending')

]

class Leaves(models.Model):
    referring_user = models.ForeignKey(to =User,on_delete=models.CASCADE,default=1)
    start_date = models.DateField(verbose_name='Start Date',help_text='leave start date is on ..')
    end_date = models.DateField(verbose_name='End Date',help_text='Leave Ends on')
    leave_type = models.CharField(choices=leave_choices,max_length=30)
    reason = models.TextField(verbose_name='Detailed Reason for Leave',max_length= 300, help_text='Brief Reason for leave')
    days_count = models.IntegerField()
    status = models.BooleanField(max_length=25 , default=False)
    action_taken = models.CharField(choices=action_choices,max_length=20,default='Pending')
    created = models.DateTimeField(auto_now=False, auto_now_add=True)


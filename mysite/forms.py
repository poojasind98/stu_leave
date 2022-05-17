from dataclasses import field
from django import forms
from .models import Leaves
from django.forms import widgets
from .widgets import DatePickerInput

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leaves
        fields = ['start_date','end_date','leave_type','reason']
        widgets = {
            'start_date': DatePickerInput(),
            'end_date' : DatePickerInput(),
            'reason': forms.Textarea(attrs={'rows':4, 'cols':50}),
        }
        help_texts = {
            'reason': 'Explain your reason in brief'
        }

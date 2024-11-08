from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Dateinput(forms.DateInput):
        input_type = 'date '

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
        widgets = {
                'booking_date': Dateinput(),
            }
        labels = {
            'P_name': "Patient Name: ",
            'P_phone' : "Patient Phone:",
            'P_email' : "Patient Email:",
            # 'doc_name' : "Doctor Name:
            'booking_date': 'Booking Date:',
        }
class doctorsform(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = '__all__'
        
        
        labels = {
            'doc_name': "Doctors Name: ",
            'doc_spec' : "Doctors Specification:",
            'dep_name' : "Department Name",
            
        }
class CustomUserCreationForms(UserCreationForm):
     class Meta:
          model = User
          fields = ('username','password1','password2','email','first_name','last_name')
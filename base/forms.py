from django import forms
from django.forms import ModelForm
from .models import Member
from  phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class MemeberRegistrationForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'first_name_field','placeholder':'Enter your first name'}), required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'last_name_field','placeholder':'Enter your last name'}), required=False)
    phone_no = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='NG', attrs={'placeholder':'Enter your phone number'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'email_field','placeholder':'Enter your email'}))
    
   
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'phone_no', 'email']
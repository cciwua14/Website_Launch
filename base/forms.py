from xml.dom import ValidationErr
from django import forms
from django.forms import ModelForm
from .models import Member
from  phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class MemeberRegistrationForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your name'}), required=False)
    phone_no = PhoneNumberField(widget=PhoneNumberPrefixWidget(initial='NG', attrs={'placeholder':'Enter your phone number'}))
    phone_no.error_messages['invalid'] = 'Incorrect International Calling Code or Mobile Number!'
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'email_field','placeholder':'Enter your email'}))
   
    class Meta:
        model = Member
        fields = ['name','phone_no', 'email']

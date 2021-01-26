from bootstrap_datepicker_plus import DatePickerInput
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_age = forms.CharField(label='Your age')
    your_email = forms.EmailField(label='Email')
    your_birthday = forms.DateField(widget=DatePickerInput(format='%m%d%Y'))
    test_question = forms.BooleanField(label='Test Question')
from django import forms

from allauth.account.forms import LoginForm


class ContactForm(forms.Form):
    '''The contact form in the index.html file'''

    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)

from django import forms
from allauth.account.forms import SignupForm


class ContactForm(forms.Form):
    '''The contact form in the index.html file'''

    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)


class CustomSignUpForm(SignupForm):
    '''Add first name and last name fields to the allauth signup form '''
    first_name = forms.CharField(
        max_length=30, label='First Name', widget=forms.TextInput(
            attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(
        max_length=30, label='Last Name', widget=forms.TextInput(
            attrs={'placeholder': 'Last Name'}))

    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

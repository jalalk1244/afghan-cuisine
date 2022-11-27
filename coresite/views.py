from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from afghancuisine import settings

# Create your views here.


def index(request):
    '''View for the home page '''
    contact_form = ContactForm(request.POST or None)
    if request.method == 'POST' and contact_form.is_valid:
        # When the contact form is submitted
        name = f"{request.POST['first_name']} {request.POST['last_name']}"
        from_email = request.POST['email']
        subject = f'You have got an email from {name}'
        message = request.POST['message']
        recipient_list = [settings.EMAIL_HOST_USER]

        # Send the details in an emaiil
        send_mail(subject, message, from_email, recipient_list)

        return render(request, 'index.html', {'name': name, 'contact_form': ContactForm()})
    else:
        # return the 'index.html' template
        return render(request, 'index.html', {'contact_form': ContactForm()})

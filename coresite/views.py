from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from afghancuisine import settings
# Create your views here.


def index(request):
    '''View for the home page '''
    if request.method == 'POST':
        # When the contact form is submitted
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid:
            name = f"{request.POST['first_name']} {request.POST['last_name']}"
            from_email = request.POST['email']
            subject = f'You have got an email from {from_email}'
            message = request.POST['message']
            recipient_list = [settings.EMAIL_HOST_USER]

            # Send the details in an email
            send_mail(subject, message, from_email, recipient_list)
            # Success message
            success_message = f"Thank you {name}.\
                                We'll get back to you ass soon as possible!"
            messages.success(request, success_message)
            return render(
                request, 'index.html', {'name': name,
                                        'contact_form': ContactForm()})
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        # return the 'index.html' template
        return render(request, 'index.html', {'contact_form': ContactForm()})

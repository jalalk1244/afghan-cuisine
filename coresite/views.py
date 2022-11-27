from django.shortcuts import render
from .forms import ContactForm

# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST['fname'] + ' ' + request.POST['lname']
        email = request.POST['email']
        message = request.POST['message']

        return render(request, 'index.html', {'name': name})
    else:
        # return the 'index.html' template
        return render(request, 'index.html', {'contact_form': ContactForm()})

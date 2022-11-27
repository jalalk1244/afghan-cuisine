from django.shortcuts import render

# Create your views here.


def index(request):
    # return the 'index.html' template
    return render(request, 'index.html')


def contact(request):
    # Get the submited contact form details
    return render(request, 'contact.html')

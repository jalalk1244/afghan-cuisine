from django.shortcuts import render

# Create your views here.


def index(request):
    # return the 'index.html' template
    return render(request, 'index.html')

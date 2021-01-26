from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm

# Create your views here.
def index(request):
    #2 dct = {'name':'Tim'}
    #3 dct = {'name': request.GET.get('name','')} # get the value from the url
    #1 return HttpResponse("Hello world")
    form = NameForm() # bring in an instance of the NameForm class
    dct = {"form": form} # provide the instance in a dictionary
    return render(request, 'hello.html', dct)

def hello(request, name):
    dct = {'name': name} 
    return render(request, 'hello2.html', dct)
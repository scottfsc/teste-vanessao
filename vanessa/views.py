from django.shortcuts import render
from vanessa. models import *
from vanessa.forms import *
# Create your views here.


def home(request):
    
    form = UserForm()
    print(form)
    return render(request, "home.html", {'form': form})
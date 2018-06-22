from django import forms 
from vanessa.models import * 


class UserForm(forms.Form): 
    
    nome = forms.CharField(label = 'Nome', max_length=50)
    email = forms.EmailField()
    idade = forms.IntegerField()
    genero = forms.CharField()

    

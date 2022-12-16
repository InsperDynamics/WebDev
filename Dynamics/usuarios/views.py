
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.


def index(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        curso = request.POST.get('curso')
        semestre = request.POST.get('semestre')
        telefone = request.POST.get('telefone')

        PS = ProcessoSeletivo(nome = nome, email=email, curso=curso, semestre=semestre, telefone=telefone)
        PS.save()
    return render(request, 'index.html')
        

from tokenize import Token
from unicodedata import name
from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError
from .models import *
from django.contrib.auth import login
from .forms import *
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.core.paginator import Paginator
import requests
from rest_framework.response import Response
import json
import datetime
from django.contrib.auth.hashers import make_password
from django.http import FileResponse, HttpResponse, HttpResponseNotFound, JsonResponse
from django.conf import settings

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
        

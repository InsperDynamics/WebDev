from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    image = models.ImageField(default='default.jpg')

    def __str__(self):
        return self.username

class Register_token(models.Model):
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.token

class ProcessoSeletivo(models.Model):
    nome = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    semestre = models.IntegerField(max_length=50)
    telefone = models.CharField(max_length=50)
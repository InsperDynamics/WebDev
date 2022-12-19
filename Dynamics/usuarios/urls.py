from django.urls import path

from . import views

urlpatterns = [
    path("ProcessoSeletivo", views.processoSeletivoPage, name='ProcessoSeletivo'),
    path("", views.landingPage, name='LandingPage'),
]
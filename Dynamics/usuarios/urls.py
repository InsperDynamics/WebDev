from django.urls import path

from . import views

urlpatterns = [
    path("ProcessoSeletivo", views.processoSeletivoPage, name='ProcessoSeletivo'),
    path("SobreNos", views.sobreNosPage, name='SobreNos'),
    path("", views.landingPage, name='LandingPage'),
]
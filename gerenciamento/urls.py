from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastramento/', views.cadastramento, name='cadastramento'),
    path('participantes/', views.listar_participantes, name='listar_participantes'),
    path('entrada/', views.registrar_entrada, name='registrar_entrada'),
    path('saída/', views.registrar_saida, name='registrar_saida')

]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('cadastramento/', views.cadastramento, name='cadastramento'),
    path('confirmar_entrada/<pk>/', views.confirmar_entrada, name='confirmar_entrada'),
    path('participantes/', views.listar_participantes, name='listar_participantes'),
    path('participantes_presentes/', views.listar_participantes_presentes, name='listar_participantes_presentes'),
    path('entrada/', views.registrar_presenca, name='registrar_entrada'),
]


from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    #rota para pagina inicial 
    path('', views.home, name='home'),
    #rota para outras 
    #path('/cadastro')
    path('usuarios/', views.usuarios, name='listagem_usuarios')
]

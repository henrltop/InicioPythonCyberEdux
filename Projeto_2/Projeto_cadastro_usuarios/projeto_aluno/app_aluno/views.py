from django.shortcuts import render
from .models import Usuario

# Create your views here.
def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    Novo_usuario = Usuario()
    Novo_usuario.Nome = request.POST.get('Nome')
    Novo_usuario.Idade = request.POST.get('Idade')
    Novo_usuario.save()

    #exibir todos os usuarios ja cadastrados em uma nova página
    usuarios = {
        'usuarios':Usuario.objects.all()
    }
    #retornar os dados para a página de listagem de usuarios
    return render(request,'usuarios/usuarios.html',usuarios)
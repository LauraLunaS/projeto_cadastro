from django.shortcuts import render
from .models import Usuario

def home(request): 
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        # Verificar se o campo "nome" está preenchido
        if nome:
            novo_usuario = Usuario(nome=nome, idade=idade)
            novo_usuario.save()
        else:
            # Se o campo "nome" não estiver preenchido, você pode fornecer um feedback ao usuário
            # e talvez redirecioná-lo de volta ao formulário
            return render(request, 'usuarios/usuarios.html', {'error_message': 'O campo nome é obrigatório'})

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request, 'usuarios/usuarios.html', usuarios)
from django.shortcuts import render, redirect
from .models import Grupo, Usuario


def listar_grupos(request):
    grupos = Grupo.objects.all()
    return render(request, 'listar_grupos.html', {'grupos': grupos})


def cadastrar_grupo(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        status = request.POST['status']
        grupo = Grupo(titulo=titulo, descricao=descricao, status=status)
        grupo.save()
        return redirect('listar_grupos')
    return render(request, 'cadastrar_grupo.html')


def editar_grupo(request, grupo_id):
    grupo = Grupo.objects.get(id=grupo_id)
    if request.method == 'POST':
        grupo.titulo = request.POST['titulo']
        grupo.descricao = request.POST['descricao']
        grupo.status = request.POST['status']
        grupo.save()
        return redirect('listar_grupos')
    return render(request, 'editar_grupo.html', {'grupo': grupo})


def excluir_grupo(request, grupo_id):
    grupo = Grupo.objects.get(id=grupo_id)
    grupo.delete()
    return redirect('listar_grupos')


def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})


def cadastrar_usuario(request):
    grupos = Grupo.objects.all()
    if request.method == 'POST':
        nome = request.POST['nome']
        idade = request.POST['idade']
        sexo = request.POST['sexo']
        email = request.POST['email']
        telefone = request.POST['telefone']
        pais = request.POST['pais']
        estado = request.POST['estado']
        cidade = request.POST['cidade']
        bairro = request.POST['bairro']
        logradouro = request.POST['logradouro']
        status = request.POST['status']
        grupo_id = request.POST['grupo']
        grupo = Grupo.objects.get(id=grupo_id)
        usuario = Usuario(nome=nome, idade=idade, sexo=sexo, email=email, telefone=telefone,
                          pais=pais, estado=estado, cidade=cidade, bairro=bairro, logradouro=logradouro,
                          status=status, grupo=grupo)
        usuario.save()
        return redirect('listar_usuarios')
    return render(request, 'cadastrar_usuario.html', {'grupos': grupos})


def editar_usuario(request, usuario_id):
    grupos = Grupo.objects.all()
    usuario = Usuario.objects.get(id=usuario_id)
    if request.method == 'POST':
        usuario.nome = request.POST['nome']
        usuario.idade = request.POST['idade']
        usuario.sexo = request.POST['sexo']
        usuario.email = request.POST['email']
        usuario.telefone = request.POST['telefone']
        usuario.pais = request.POST['pais']
        usuario.estado = request.POST['estado']
        usuario.cidade = request.POST['cidade']
        usuario.bairro = request.POST['bairro']
        usuario.logradouro = request.POST['logradouro']
        usuario.status = request.POST['status']
        usuario.grupo_id = request.POST['grupo']
        usuario.save()
        return redirect('listar_usuarios')
    return render(request, 'editar_usuario.html', {'usuario': usuario, 'grupos': grupos})


def excluir_usuario(request, usuario_id):
    usuario = Usuario.objects.get(id=usuario_id)
    usuario.delete()
    return redirect('listar_usuarios')
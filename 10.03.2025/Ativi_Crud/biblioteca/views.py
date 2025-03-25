from django.shortcuts import render, redirect, get_object_or_404
from .models import Biblioteca
from .forms import Bibliotecaforms

# Está é a views do nosso projeto de biblioteca na onde treinamos o django 


# função para vermos todos os livros que temos
def listar_livros(request):
    livros = Biblioteca.objects.all()
    return render(request, 'listar_livros.html',{'livros' : livros})

# Cadastrar livros no nosso SQlite
def cadastrar_livro(request):
    if request.method == 'POST':
        form = Bibliotecaforms(request.POST)
        if form .is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = Bibliotecaforms()
    return render(request,'cadastrar_livro.html',{'form': form})

# Fazer alguma mudança em um id já existente
def atualizar_livros(request,pk):
    livro = get_object_or_404(Biblioteca, pk=pk)
    if request.method == 'POST':
        form = Bibliotecaforms(request.POST, instance = livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = Bibliotecaforms(instance=livro)
    return render(request, 'atualizar_livro.html', {'form':form, 'livro':livro})


# Deletar um id de uma base de dados 
def excluir_livro(request,pk):
    # pk usado para referenciar primary key
    livro = get_object_or_404(Biblioteca, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request,'excluir_livro.html', {'livro':livro})
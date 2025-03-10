from django.shortcuts import render, redirect, get_object_or_404
from .models import Biblioteca
from .forms import Bibliotecaforms

def listar_livros(request):
    livro = Biblioteca.objects.all()
    return render(request, 'biblioteca/listar_livros.html',{'biblioteca': biblioteca})

def cadastrar_livro(request):
    if request.method == 'POST':
        form = Bibliotecaforms(request.POST)
        if form .is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = Bibliotecaforms()
    return render(request,'biblioteca/cadastrar.html',{'form': form})

def atualizar_livros(request,pk):
    livro = get_object_or_404(Biblioteca, pk = pk)
    if request.method == 'POST':
        form = Bibliotecaforms(request.POST, instance = livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = Bibliotecaforms(instance=livro)
    return render(request, 'biblioteca/atualizar_livro.html', {'form':form, 'livro':livro})

def excluir_livro(request,pk):
    livro = get_object_or_404(Biblioteca, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request,'biblioteca/excluir_livro.html', {'livro':livro})

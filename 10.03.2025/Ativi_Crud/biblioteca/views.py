from django.shortcuts import render, redirect, get_object_or_404
from .models import Biblioteca
from .forms import Bibliotecaforms

def listar_livros(request):
    livros = Biblioteca.objects.all()
    return render(request, 'listar_livros.html',{'livros' : livros})

def cadastrar_livro(request):
    if request.method == 'POST':
        form = Bibliotecaforms(request.POST)
        if form .is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = Bibliotecaforms()
    return render(request,'cadastrar_livro.html',{'form': form})

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

def excluir_livro(request,pk):
    livro = get_object_or_404(Biblioteca, pk=pk)
    if request.method == 'POST':
        livro.delete()
        return redirect('listar_livros')
    return render(request,'excluir_livro.html', {'livro':livro})



def lista_livro(request):
    titulo = request.GET.get('titulo', None)
    ano = request.GET.get('ano_pubi', None)
    autor = request.GET.get('autor', None)

    # Inicia o queryset com todos os livro
    livro = Biblioteca.objects.all()

    # Aplica o filtro para cada campo, se o valor for fornecido
    if titulo:
        livro = livro.filter(titulo__icontains=titulo) | livro.filter(ano=ano) | livro.filter(autor__icontains=autor) # 'icontains' para pesquisa insensível a maiúsculas/minúsculas


    # Retorna os livro filtrados para a página
    return render(request, 'listar_livro.html', {'livro': livro})
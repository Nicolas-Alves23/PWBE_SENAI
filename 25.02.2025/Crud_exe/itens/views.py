from django.shortcuts import render , redirect , get_object_or_404
from .models import Item
from .forms import ItemForm 

# Primeira vez fazendo um crud


# READ
#Para Lermos o nossso banco de dados
def item_read(request):
    itens = Item.objects.all()
    return render(request, 'item_read.html', {'itens':itens})

# CREATE
#Criar novos itens no banco de dados 
def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_read')
    else:
        form = ItemForm()
    return render(request, 'itens_form.html', {'form' : form})

# UPDATE
# Modificar um item referenciado na pk
def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_read')
    else:
        form = ItemForm(instance= item)    
    return render(request, 'itens_form.html', {'form':form})

# DELETE
#Deletar o item 'pk'
def item_delete(request, pk):
    item = get_object_or_404(Item, pk = pk)
    if request.method == 'POST':
        item.delete()
        redirect('item_read')
    return render(request, 'confirmar_delete.html',{'item': item})
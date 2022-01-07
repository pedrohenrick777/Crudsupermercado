from django.shortcuts import redirect, render
from .forms import *
from .models import *

# Create your views here.

def marcas_create(request, template_name='marcas/marcas_form.html'):
    form = MarcaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_marcas')
    return render(request, template_name, {'form': form})

def marcas_edit(request, pk, template_name='marcas/marcas_form.html'):
    marca = Marca.objects.get(pk=pk)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('lista_marcas')
    else:
        form = MarcaForm(instance=marca)
    return render(request, template_name, {'form': form})

def marcas_delete(request, pk, template_name='marcas/marcas_deletar.html'):
    marca = Marca.objects.get(pk=pk)
    if request.method == 'POST':
        marca.delete()
        return redirect('lista_marcas')
    return render(request, template_name, {'marca': marca})

def marcas_list(request, template_name='marcas/marcas_list.html'):
    query = request.GET.get('busca')
    if query:
        marcas = Marca.objects.filter(nome__icontains=query)
    else:
        marcas = Marca.objects.all()
    return render(request, template_name, {'marcas': marcas})

def marcas_produtos_list(request, pk, template_name='marcas/marca_produto_list.html'):
    produtos = Produto.objects.filter(marca=pk)
    return render(request, template_name, {'produtos': produtos})

def produtos_create(request, template_name='produtos/produtos_form.html'):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, template_name, {'form': form})

def produtos_edit(request, pk, template_name='produtos/produtos_form.html'):
    produto = Produto.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, template_name, {'form': form })

def produtos_delete(request, pk, template_name='produtos/produtos_deletar.html'):
    produto = Produto.objects.get(pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, template_name, {'produto': produto})

def produtos_list(request, template_name='produtos/produtos_list.html'):
    query = request.GET.get('busca')
    if query:
        produtos = Produto.objects.filter(descricao__icontains=query)
    else:
        produtos = Produto.objects.all()
    return render(request, template_name, {'produtos': produtos})
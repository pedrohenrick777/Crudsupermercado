from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
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
    marca = get_object_or_404(Marca, pk=pk)
    if request.method == 'POST':
        form = MarcaForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            return redirect('lista_marcas')
    else:
        form = MarcaForm(instance=marca)
    return render(request, template_name, {'form': form})

def marcas_delete(request, pk, template_name='marcas/marcas_deletar.html'):
    marca = get_object_or_404(Marca, pk=pk)
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
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, template_name, {'form': form })

def produtos_delete(request, pk, template_name='produtos/produtos_deletar.html'):
    produto = get_object_or_404(Produto, pk=pk)
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

def produtos_show(request, pk, template_name='produtos/produtos_show.html'):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, template_name, {"produto": produto})

def categorias_create(request, template_name='categorias/categorias_form.html'):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_categorias')
    return render(request, template_name, {"form": form})

def categorias_edit(request, pk, template_name='categorias/categorias_form.html'):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, template_name, {"form": form})

def categorias_delete(request, pk, template_name='categorias/categorias_deletar.html'):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, template_name, {"categoria": categoria})

def categorias_list(request, template_name='categorias/categorias_list.html'):
    query = request.GET.get('busca')
    if query:
        categorias = Categoria.objects.filter(nome__icontains=query)
    else:
        categorias = Categoria.objects.all()
    return render(request, template_name, {"categorias":categorias})

def catetegoria_produtos_list(request, pk, template_name='categorias/categorias_produtos_list.html'):
    produtos = Produto.objects.filter(categoria=pk)
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, template_name, {"produtos":produtos, "categoria":categoria})
        
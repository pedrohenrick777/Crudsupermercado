from django.forms import ModelForm, fields
from .models import *

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ['nome']


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'preco', 'marca', 'categoria']

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
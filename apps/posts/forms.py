from django import forms

from .models import Categoria, Postagem

# bottom up

# DRY - Don't Repeat Youself

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__' # dunder | two underscore


class PostagemForm(forms.ModelForm):

    class Meta:
        model = Postagem
        exclude = ['criada_em', 'atualizada_em']


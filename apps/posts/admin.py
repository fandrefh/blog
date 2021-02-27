from django.contrib import admin

from .models import Categoria, Postagem

# Register your models here.


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']


@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'categoria', 'criada_em']

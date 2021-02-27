from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import CategoriaForm, PostagemForm
from .models import Categoria

# Create your views here.


def adicionar_categoria(request):
    template_name = 'posts/adicionar_categoria.html'
    context = {}
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    form = CategoriaForm()
    context['form'] = form
    return render(request, template_name, context)


def lista_categorias(request):
    template_name = 'posts/lista_categorias.html'
    categorias = Categoria.objects.all() # SELECT * FROM categorias;
    context = {
        'categorias': categorias,
    }
    return render(request, template_name, context)


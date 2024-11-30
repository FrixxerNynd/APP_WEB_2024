from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from articulos.models import Category, Article
# Create your views here.

@login_required(login_url='inicio')
def list_art(request):

    #Sacar articulos de la BD
    articulos = Article.objects.all()
    return render(request,'articulos/listado_art.html',{
        'title':'Articulos',
        'content':'Listado de Articulos',
        'articulos': articulos
    })


@login_required(login_url='inicio')
def list_cat(request):
    
    #Sacar categorias de la BD
    categorias = Category.objects.all()
    return render(request,'categoria/listado_cat.html',{
        'title':'Categorias',
        'content':'Listado de Categorias',
        'categorias': categorias
    })
    


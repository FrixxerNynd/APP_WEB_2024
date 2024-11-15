from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'mainapps/index.html',{
        'title':'Inicio',
        'content':'..:Hola:..'
    })

def about(request):
    return render(request,'mainapp/about.html',{
        'title':'Acerca de nosotros...',
        'content':'Soy un desarrollador'
    })

def mision(request):
    return render(request,'mainapp/mision.html',{
        'title':'Mision',
        'content':'Sin mision'
    })

def vision(request):
    return render(request,'mainapp/vision.html',{
        'title':'Vision',
        'content':'Sin vision'
   })
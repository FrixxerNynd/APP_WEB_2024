from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html',{
        'title':'Inicio',
        'content':'..:Bienvenido a la pagina principal:..',
    })

def about(request):
    return render(request, 'mainapp/about.html',{
        'title':'Acerca de nosotros...',
        'content':'Somos un equipo de desarrollo de software'
    })

def mision(request):
    return render(request,'mainapp/mision.html',{
        'title':'Mision',
        'content':'La mision de la empresa'
    })

def vision(request):
    return render(request,'mainapp/vision.html',{
        'title':'Vision',
        'content':'La vision de la empresa'
    })

def error_404(request, exception):
    return render(request,'mainapp/404.html', status=404)
from django.shortcuts import render

# Create your views here.
def index(request):
    mensaje='Hola soy un mensaje'
    return render(request, 'mainapps/index.html',{
        'title':'Inicio',
        'content':'..:Bienvenido a la pagina principal:..',
        'mensaje':mensaje
    })

def about(request):
    return render(request, 'mainapps/about.html',{
        'title':'Acerca de nosotros...',
        'content':'Somos un equipo de desarrollo de software'
    })

def mision(request):
    return render(request,'mainapps/mision.html',{
        'title':'Mision',
        'content':'La mision de la empresa'
    })

def vision(request):
    return render(request,'mainapps/vision.html',{
        'title':'Vision',
        'content':'La vision de la empresa'
    })
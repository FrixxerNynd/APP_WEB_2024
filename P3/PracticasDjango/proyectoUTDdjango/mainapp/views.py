from django.shortcuts import render, HttpResponse, redirect
# from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html',{
        'title':'Inicio',
        'content':'..:Bienvenido a la pagina principal:..',
    })

@login_required(login_url='inicio')
def about(request):
    return render(request, 'mainapp/about.html',{
        'title':'Acerca de nosotros...',
        'content':'Somos un equipo de desarrollo de software'
    })

@login_required(login_url='inicio')
def mision(request):
    return render(request,'mainapp/mision.html',{
        'title':'Mision',
        'content':'La mision de la empresa'
    })

@login_required(login_url='inicio')
def vision(request):
    return render(request,'mainapp/vision.html',{
        'title':'Vision',
        'content':'La vision de la empresa'
    })

def inicio_sesion(request):
    
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "¡Bienvenido al Inicio de sesion!")
                return redirect('inicio')
            else:
                messages.warning(request, "No es posible el acceso, use las credenciales correctas")

        return render(request, 'users/inicio_sesion.html', {
            'title': 'Iniciar Sesión',
            
            }
)

def registro(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        register_form=RegisterForm()
        
        if request.method == "POST":
            register_form=RegisterForm(request.POST)
            
            if register_form.is_valid():
                register_form.save()
                messages.success(request, "Registro con exito!")
                return redirect('inicio')
    
        return render(request,"users/registro.html",{
            'title':'Registro de usuarios',
            'register_form':register_form
            }
)
def logout_user(request):
    logout(request)
    return redirect('inicio') 


def error_404(request, exception):
    return render(request,'mainapp/404.html', status=404)

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='inicio'),
    path('inicio/', views.index, name='inicio'),
    path('acerca de/', views.about, name="Acerca de"),
    path('mision/', views.mision, name='Mision'),
    path('vision/', views.vision, name='Vision'),
    path('registro/', views.registro, name='Registro'),
    path('Inicio_sesion/', views.inicio_sesion, name='Inicio_sesion'),
    path('logout/', views.logout_user, name='logout')
]
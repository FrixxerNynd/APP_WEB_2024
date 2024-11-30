from django.urls import path
from . import views
urlpatterns = [
    path('listado_articulos/', views.list_art, name="Listadoarticulos"),
    path('listado_categorias/', views.list_cat, name="Listadocategorias"),
]
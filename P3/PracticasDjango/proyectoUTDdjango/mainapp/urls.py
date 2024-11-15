from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='inicio'),
    path('inicio/', views.index, name='inicio'),
    path('acerca de/', views.about, name="Acerca de"),
    path('mision/', views.mision, name='Mision'),
    path('vision/', views.vision, name='Vision'),
]
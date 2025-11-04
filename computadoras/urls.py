from django.urls import path
from . import views

urlpatterns = [
    # Computadoras
    path('computadoras/', views.lista_computadoras, name='lista_computadoras'),
    path('computadoras/nuevo/', views.nueva_computadora, name='nueva_computadora'),
    path('computadoras/editar/<int:id>/', views.editar_computadora, name='editar_computadora'),
    path('computadoras/eliminar/<int:id>/', views.eliminar_computadora, name='eliminar_computadora'),

    # Proveedores
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('proveedores/nuevo/', views.nuevo_proveedor, name='nuevo_proveedor'),
    path('proveedores/eliminar/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
]

from django.shortcuts import render, redirect, get_object_or_404
from .models import Computadora, Proveedor
from .forms import ComputadoraForm, ProveedorForm

# ==========================
# CRUD Computadoras
# ==========================
def lista_computadoras(request):
    computadoras = Computadora.objects.all()
    return render(request, 'computadoras/lista.html', {'computadoras': computadoras})

def nueva_computadora(request):
    if request.method == 'POST':
        form = ComputadoraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_computadoras')
    else:
        form = ComputadoraForm()
    return render(request, 'computadoras/form.html', {'form': form, 'titulo': 'Nueva Computadora'})

def editar_computadora(request, id):
    computadora = get_object_or_404(Computadora, id=id)
    if request.method == 'POST':
        form = ComputadoraForm(request.POST, request.FILES, instance=computadora)
        if form.is_valid():
            form.save()
            return redirect('lista_computadoras')
    else:
        form = ComputadoraForm(instance=computadora)
    return render(request, 'computadoras/form.html', {'form': form, 'titulo': 'Editar Computadora'})

def eliminar_computadora(request, id):
    computadora = get_object_or_404(Computadora, id=id)
    computadora.delete()
    return redirect('lista_computadoras')


# ==========================
# CRUD Proveedores
# ==========================
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'computadoras/proveedores.html', {'proveedores': proveedores})

def nuevo_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm()
    return render(request, 'computadoras/proveedores_form.html', {'form': form})

def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    return redirect('lista_proveedores')
